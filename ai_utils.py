def ask_ai_for_priority(task):
    task = task.lower()

    if "test" in task or "exam" in task or "assignment" in task or "deadline" in task:
        return "High"
    elif "buy" in task or "groceries" in task:
        return "Low"
    else:
        return "Medium"
