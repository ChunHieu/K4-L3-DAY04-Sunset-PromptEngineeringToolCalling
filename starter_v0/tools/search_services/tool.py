def search_services(query: str = "", category: str = "all") -> dict:
    services = [
        {"id": "S01", "name": "Khám tổng quát", "category": "general", "price": "500,000 VND"},
        {"id": "S02", "name": "Nhổ răng khôn", "category": "dental", "price": "1,500,000 VND"},
        {"id": "S03", "name": "Siêu âm thai", "category": "imaging", "price": "300,000 VND"},
        {"id": "S04", "name": "Xét nghiệm máu", "category": "lab", "price": "200,000 VND"},
        {"id": "S05", "name": "Khám chuyên khoa tim mạch", "category": "specialist", "price": "600,000 VND"}
    ]
    results = [s for s in services if (category == "all" or s["category"] == category) and (query.lower() in s["name"].lower())]
    return {"tool": "search_services", "results": results}
