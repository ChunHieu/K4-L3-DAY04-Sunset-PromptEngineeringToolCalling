import streamlit as st
import json
from pathlib import Path

from env_loader import load_lab_env
from providers import make_provider
from tools import load_tool_declarations, to_openai_tools
from chat import run_model_tool_loop

ROOT = Path(__file__).parent
ARTIFACTS_DIR = ROOT / "artifacts"
load_lab_env(ROOT)

st.set_page_config(page_title="Clinic AI Assistant", page_icon="🏥", layout="wide")
st.title("🏥 Clinic AI Assistant")

with st.sidebar:
    st.header("📜 Lịch sử Phiên bản")
    try:
        import csv
        with open(ARTIFACTS_DIR / "version_log.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)
        if data:
            st.dataframe(data)
        else:
            st.write("Chưa có log.")
    except Exception as e:
        st.error("Không thể đọc version_log.csv")

@st.cache_resource
def setup_agent():
    system_prompt = (ARTIFACTS_DIR / "system_prompt.md").read_text(encoding="utf-8")
    tool_declarations = load_tool_declarations(ARTIFACTS_DIR / "tools.yaml")
    openai_tools = to_openai_tools(tool_declarations)
    provider = make_provider("openai")
    model = getattr(provider, "default_model", None)
    return system_prompt, openai_tools, provider, model

system_prompt, openai_tools, provider, model = setup_agent()

if "history" not in st.session_state:
    st.session_state.history = []

def trim_history(history, window=5):
    flat_history = []
    for turn in history:
        flat_history.append({"role": "user", "content": turn["user"]})
        if turn.get("assistant"):
            flat_history.append({"role": "assistant", "content": turn["assistant"]})
    
    if window <= 0:
        return []
    return flat_history[-window * 2:]

# Render history
for turn in st.session_state.history:
    with st.chat_message("user"):
        st.markdown(turn["user"])
    
    with st.chat_message("assistant"):
        for event in turn.get("tool_events", []):
            with st.expander(f"🛠️ Đã dùng Tool: `{event['tool']}`"):
                st.write("**Tham số truyền vào:**")
                st.json(event["args"])
                st.write("**Kết quả trả về:**")
                st.json(event["result"])
        if turn.get("assistant"):
            st.markdown(turn["assistant"])

user_input = st.chat_input("Hỏi tôi về dịch vụ, bác sĩ, hoặc đặt lịch...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    
    messages = [
        {"role": "system", "content": system_prompt},
        *trim_history(st.session_state.history, 5),
        {"role": "user", "content": user_input},
    ]

    with st.spinner("Đang suy nghĩ..."):
        try:
            result = run_model_tool_loop(
                provider=provider,
                messages=messages,
                tools=openai_tools,
                model=model,
                max_tool_rounds=4,
            )
            
            assistant_text = result.get("assistant_text", "")
            tool_events = result.get("tool_events", [])
            
            with st.chat_message("assistant"):
                for event in tool_events:
                    with st.expander(f"🛠️ Đã dùng Tool: `{event['tool']}`"):
                        st.write("**Tham số truyền vào:**")
                        st.json(event["args"])
                        st.write("**Kết quả trả về:**")
                        st.json(event["result"])
                if assistant_text:
                    st.markdown(assistant_text)
            
            st.session_state.history.append({
                "user": user_input,
                "assistant": assistant_text,
                "tool_events": tool_events
            })
            
        except Exception as e:
            st.error(f"Lỗi: {str(e)}")
