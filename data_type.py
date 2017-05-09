def data_type(arg):
    if isinstance(arg, str):
        return len(arg)
    elif arg is None:
        return "no value"
    elif isinstance(arg, bool):
        return bool(arg)
    elif isinstance(arg, int):
        return "less than 100" if arg < 100 else "equal to 100" if arg == 100 else "more than 100"
    elif isinstance(arg, list):
        return arg[2] if len(arg) > 2 else None


# print data_type(None)
# print data_type("None")
