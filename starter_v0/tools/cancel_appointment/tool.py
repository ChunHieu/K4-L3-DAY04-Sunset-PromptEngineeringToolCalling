def cancel_appointment(appointment_id: str, phone: str, confirmed: bool = False) -> dict:
    if not confirmed:
        return {
            "tool": "cancel_appointment",
            "status": "pending_confirmation",
            "message": f"Bạn có chắc chắn muốn hủy lịch hẹn mã {appointment_id} không?"
        }
    
    return {
        "tool": "cancel_appointment",
        "status": "success",
        "message": f"Đã hủy lịch hẹn {appointment_id} thành công."
    }
