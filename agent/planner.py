def plan(memory):
    if memory["age"] is None:
        return "ASK_AGE"
    if memory["income"] is None:
        return "ASK_INCOME"
    if memory["children"] is None:
        return "ASK_CHILDREN"
    return "FIND_SCHEME"
