def task_validation(attrs):
    if "name" in attrs and len(attrs.get("name")) < 1:
        return "name field is required"
    elif "category" is attrs and len(attrs.get("category")):
        return "Category field is required"
    else:
        pass


def add_task_validation(attrs):
    pass
