def clinic_policy(query: str = "", category: str = "all") -> dict:
    policies = [
        {"category": "insurance", "title": "Chính sách bảo hiểm y tế", "content": "Phòng khám chấp nhận BHYT nhà nước và một số bảo hiểm tư nhân như PVI, Bảo Việt."},
        {"category": "refund", "title": "Hoàn tiền", "content": "Khách hàng được hoàn tiền 100% nếu hủy lịch trước 24h."},
        {"category": "rules", "title": "Nội quy phòng khám", "content": "Bệnh nhân cần đến trước 15 phút so với giờ hẹn để làm thủ tục."}
    ]
    results = [p for p in policies if (category == "all" or p["category"] == category) and (query.lower() in p["content"].lower() or query.lower() in p["title"].lower())]
    return {"tool": "clinic_policy", "results": results}
