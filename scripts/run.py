"""Turn task records into a realistic daily agenda."""
from runtime import *

def process(data):
    today = day(data["date"])
    budget = integer(data["available_minutes"], "available_minutes")
    tasks = records(data, "tasks")
    unique(tasks)
    result = []
    for item in tasks:
        title = text(item.get("title"), "title")
        state = choice(item.get("status"), ("ready","blocked","done"), "status")
        priority = integer(item.get("priority"), "priority", 1)
        if priority > 5:
            raise ValueError("priority must be 1..5")
        minutes = integer(item.get("minutes"), "minutes", 1)
        due = day(item["due"]) if item.get("due") else None
        group = "overdue" if due and due < today else "today" if due == today else "upcoming" if due else "undated"
        if state != "done":
            result.append(dict(item, deadline_class=group))
    rank = {"overdue":0,"today":1,"upcoming":2,"undated":3}
    result.sort(key=lambda x:(rank[x["deadline_class"]],x["priority"],x.get("due") or "9999-12-31",x["id"]))
    agenda, blocked, deferred = [], [], []
    for row in result:
        if row["status"] == "blocked":
            blocked.append(row)
        elif row["minutes"] <= budget:
            agenda.append(row)
            budget -= row["minutes"]
        else:
            deferred.append(row)
    return {"date":str(today),"agenda":agenda,"blocked":blocked,"deferred":deferred,"remaining_minutes":budget}

if __name__ == "__main__":
    sys.exit(main(process, "Turn task records into a realistic daily agenda."))
