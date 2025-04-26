# message_formatter.py

def star_border(func):
    def wrapper(message):
        decorated = "*" * (len(message) + 4)
        return f"{decorated}\n* {func(message)} *\n{decorated}"
    return wrapper

def emoji_wrapper(func):
    def wrapper(message):
        return f"🎉 {func(message)} 🎉"
    return wrapper
