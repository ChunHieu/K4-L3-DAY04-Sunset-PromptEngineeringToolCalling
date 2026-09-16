def check_availability(doctor_id: str, date: str) -> dict:
    # Dummy logic for availability
    available_slots = ["08:00", "09:30", "14:00", "15:30"]
    return {
        "tool": "check_availability",
        "doctor_id": doctor_id,
        "date": date,
        "available_slots": available_slots,
        "message": f"Bác sĩ {doctor_id} có lịch trống vào {date}: {', '.join(available_slots)}"
    }
