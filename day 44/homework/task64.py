def assignment(value, operator):
    if operator == "=":
        x = value
    elif operator == "+=":
        x += value
    elif operator == "-=":
        x -= value
    elif operator == "*=":
        x *= value
    elif operator == "/=":
        x /= value
    elif operator == "%=":
        x %= value
    elif operator == "**=":
        x **= value
    elif operator == "//=":
        x //= value
    return x