import random
import time

bot_template = "Bot:{0}"
user_template = "User:{0}"

responses = {
    "statement": ['tell me more!',
                  'why do you think that?',
                  'how long have you felt this way?',
                  'I find that extremely interesting',
                  'can you back that up?',
                  'oh wow!',
                  ':)'],
    "question": ["I don't know :(", 'you tell me!'],
    "Default": ["Sorry"],
}


def respond(message):

    if message.endswith("?"):

        return random.choice(responses["question"])
    else:
        return random.choice(responses["statement"])


def send_message(message):

    response = respond(message)
    print(bot_template.format(response))


if __name__ == '__main__':
    print(user_template.format("I love building chatbots"))
    time.sleep(5.0)
    send_message("I love building chatbots")


# send_message("what's today's weather?")
# send_message("what's today's weather?")
#
#
# send_message("I love building chatbots")
# send_message("I love building chatbots")
