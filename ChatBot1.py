bot_template = "Bot:{0}"
user_template = "User:{0}"


def respond(message):
    bot_message = "I can Hear You!You Said:" + message
    return bot_message


def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))


if __name__ == '__main__':

    send_message(message="Hello")
