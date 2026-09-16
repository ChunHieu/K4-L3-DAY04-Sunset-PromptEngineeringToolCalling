def search_doctors(specialty: str = "all") -> dict:
    doctors = [
        {"id": "DOC01", "name": "Dr. Tran Van A", "specialty": "general"},
        {"id": "DOC02", "name": "Dr. Nguyen Thi B", "specialty": "dentistry"},
        {"id": "DOC03", "name": "Dr. Le Van C", "specialty": "cardiology"},
        {"id": "DOC04", "name": "Dr. Pham Thi D", "specialty": "pediatrics"},
        {"id": "DOC05", "name": "Dr. Hoang Van E", "specialty": "dermatology"}
    ]
    results = [d for d in doctors if specialty == "all" or d["specialty"] == specialty]
    return {"tool": "search_doctors", "results": results}
