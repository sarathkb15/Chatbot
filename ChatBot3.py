import random
import time

bot_template = "Bot:{0}"
user_template = "User:{0}"

name = "Greg"
weather = "Cloudy"

responses = {
    "What's your Name ?": ["My Name Is {0}".format(name), "They Call Me{0}".format(name), "I go By {0}".format(name)],
    "What's today's Weather ?": ["Weather is {0}".format(weather), "its {0} today".format(weather)],
    "Default": ["Sorry"]
}


def respond(message):
    if message in responses:
        bot_message = random.choice(responses[message])
    else:
        bot_message = responses["default"]
    return bot_message


def send_message(message):
    # print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))


if __name__ == '__main__':
    print(user_template.format("What your Name ?"))
    time.sleep(5.0)
    send_message("What's your Name ?")
