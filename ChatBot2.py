import time

bot_template = "Bot:{0}"
user_template = "User:{0}"

name = "Greg"
weather = "Cloudy"

responses = {"What's Your Name?": "My Name is {0}".format(name),
             "What's Today Weather?": "The Weather is {0}".format(weather),
             "default": "Sorry"
             }


def respond(message):
    if message in responses:
        bot_message = responses[message]
    else:
        bot_message = responses["default"]

    return bot_message


def send_message(message):
    # print(user_template.format(message))

    response = respond(message)
    print(bot_template.format(response))


if __name__ == '__main__':
    print(user_template.format("What's Today Weather?"))
    time.sleep(5.0)
    send_message(message="What's Today Weather?")


