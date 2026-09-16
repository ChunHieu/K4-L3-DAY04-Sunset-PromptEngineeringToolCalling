import uuid

def book_appointment(patient_name: str, phone: str, doctor_id: str, date: str, time: str, confirmed: bool = False) -> dict:
    if not confirmed:
        return {
            "tool": "book_appointment",
            "status": "pending_confirmation",
            "message": f"Bạn có chắc chắn muốn đặt lịch khám cho {patient_name} với bác sĩ {doctor_id} vào lúc {time} ngày {date} không?"
        }
    
    appointment_id = "APT-" + str(uuid.uuid4())[:8].upper()
    return {
        "tool": "book_appointment",
        "status": "success",
        "appointment_id": appointment_id,
        "message": f"Đã đặt lịch khám thành công. Mã lịch hẹn của bạn là {appointment_id}."
    }
