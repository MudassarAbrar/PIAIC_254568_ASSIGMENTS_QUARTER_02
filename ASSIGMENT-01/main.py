
# -*- coding: utf-8 -*-

from message_formatter import star_border, emoji_wrapper

@star_border
@emoji_wrapper
def greet(msg):
    return msg

if __name__ == "__main__":
    print(greet("Hello, Mudassir!"))
