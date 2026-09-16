# TEAM — Day04, K4-L3B

**Làm nhóm.** Mỗi người tự viết và commit phần INDIVIDUAL của mình.

## Thông tin bài nộp

- Tên nhóm: Sunset
- Người đại diện / MSSV:Cao Đức Hiếu  / 2A202602701
- Tên repo: `K4-L3-DAY04-Sunset-PromptEngineeringToolCalling`
- URL repo, nhánh nộp, commit chốt: (Chờ nộp bài)
- Deadline áp dụng và link thông báo đổi hạn nếu có: Không có

## Thành viên

| Họ và tên | MSSV | GitHub | Vai trò và công việc | File/commit/PR |
|---|---|---|---|---|
| Trần Thanh Thái | 2A202602454 | tranthai239 | Cấu hình evaluation, viết test cases | `data/eval_clinic.json`, `run_eval.py` |
| Cao Đức Hiếu | 2A202602701 | ChunHieu | Thiết kế system prompt, xử lý luồng đặt/hủy lịch | `system_prompt.md`, `version_log.csv` |
| Dương Hữu Đạt | 2A202602544 | duonghuudat-aithucchien | Triển khai UI Chatbot, tích hợp Streamlit | `streamlit_app.py`, `chat.py` |
| Trần Công Thiện | 2A202602579 | trancongthienai-ship-it | Trưởng nhóm, định nghĩa Tool Schema, xử lý luồng tra cứu | `tools.yaml`, `agent.py`, `REPORT.md` |

## Nhận xét chung

- Kết quả và bằng chứng: Agent vượt qua 10/10 test cases (`case_accuracy` = 1.0) sau khi tối ưu hóa system prompt (được ghi nhận tại `version_log.csv` version v4).
- Thay đổi hiệu quả nhất: Chia nhóm các rules trong `system_prompt.md` theo từng luồng nghiệp vụ riêng biệt giúp giảm thiểu hiện tượng pha loãng chỉ thị (dilution) và tăng độ chính xác của mô hình khi phải làm theo đúng nguyên văn.
- Giới hạn còn lại: Kích thước system prompt hơi dài. Ở các phiên bản sau, cần thử nghiệm nghiệm việc đưa logic kiểm tra điều kiện vào code backend thay vì ép LLM bằng các luật lệ trong prompt.
- Cách phân công và tích hợp: Chia nhóm theo từng tính năng chuyên biệt, phát triển và chạy test cục bộ, sau đó hợp nhất qua Git.

## INDIVIDUAL

### Trần Thanh Thái — 2A202602454

- Phần việc và file/commit/PR: Tạo bộ dữ liệu đánh giá 30 câu cơ bản và tích hợp logic chạy đánh giá tự động.
- Quyết định, khó khăn và cách xử lý: Khó khăn trong việc cover mọi kịch bản lỗi, xử lý bằng cách tập trung vào những trường hợp thường xuyên bị sai ở version đầu để tạo test cases đánh thẳng vào đó.
- Điều đã học: Cách xây dựng test suite bài bản giúp tiết kiệm thời gian phát hiện lỗi hồi quy.
- AI/công cụ đã dùng và cách kiểm tra: Dùng LLM sinh ra các biến thể của câu hỏi, sau đó chọn lọc lại thủ công để đưa vào `eval_clinic.json`.
- Thời điểm đã tự nộp URL repo chung trên VLearn: (Chờ nộp bài)

### Cao Đức Hiếu — 2A202602701

- Phần việc và file/commit/PR: Tối ưu `system_prompt.md` cho luồng đặt lịch/hủy lịch, yêu cầu chatbot hỏi đủ thông tin nguyên văn.
- Quyết định, khó khăn và cách xử lý: Agent ban đầu thường tự ý đặt lịch khi chưa đủ thông tin hoặc tự bịa ra thông tin. Cách giải quyết là đưa ra rule cấm và ép LLM trả lời lại đúng nguyên văn câu hỏi.
- Điều đã học: Lời nhắc cần phải chia nhỏ (bullet point) thay vì viết liền mạch, đồng thời sử dụng format cấu trúc rõ ràng.
- AI/công cụ đã dùng và cách kiểm tra: Prompt tuning trực tiếp, quan sát kết quả trả về trong các file JSON log.
- Thời điểm đã tự nộp URL repo chung trên VLearn: (Chờ nộp bài)

### Dương Hữu Đạt — 2A202602544

- Phần việc và file/commit/PR: Cài đặt logic giao diện hiển thị lịch sử chat trên Streamlit và định tuyến function.
- Quyết định, khó khăn và cách xử lý: Streamlit re-render lại trang khiến state bị mất. Xử lý bằng cách dùng `st.session_state` để lưu lịch sử cuộc trò chuyện.
- Điều đã học: Quản lý trạng thái (state management) trong các ứng dụng web dạng server-side rendering đơn giản.
- AI/công cụ đã dùng và cách kiểm tra: Tham khảo tài liệu của Streamlit, hỏi AI về cách quản lý session.
- Thời điểm đã tự nộp URL repo chung trên VLearn: (Chờ nộp bài)

### Trần Công Thiện — 2A202602579

- Phần việc và file/commit/PR: Quản lý dự án, thiết kế bộ Tool Calling JSON schema tại `tools.yaml`, quản lý luồng tìm kiếm dịch vụ và bác sĩ.
- Quyết định, khó khăn và cách xử lý: Việc sử dụng tham số `category` ban đầu hay bị mô hình bỏ quên. Khắc phục bằng cách quy định giá trị default, và dùng system prompt để nhắc lại với một số tham số quan trọng.
- Điều đã học: Tool schema càng mô tả rõ (description tốt) thì LLM chọn tham số càng chính xác, giảm thiểu việc phải dùng system prompt.
- AI/công cụ đã dùng và cách kiểm tra: Sử dụng LLM để sinh ra JSON Schema mẫu, sau đó tự điều chỉnh lại, kiểm tra qua JSON validation script.
- Thời điểm đã tự nộp URL repo chung trên VLearn: (Chờ nộp bài)
