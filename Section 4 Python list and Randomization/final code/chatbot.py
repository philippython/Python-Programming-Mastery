import random


conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "Hey",
    "How is your day",
    "Hello, Talk to you later",
    "wassup",
    "Be right back"
]



# step1 : print welcome to my first python chatbot
print("Welcome to my first python chatbot program!")
# step2 : greet the user/visitor
print("Hello I'm a chatbot..")
# step3 : prompt the user for response
user_response = input()
# step4 : respond to the user
bot_response = random.choice(conversation)

# comparing user response to bot response
if user_response.lower() == bot_response.lower() : 
    alternative_bot_response = random.choice(conversation)
    print(alternative_bot_response)
else :
    print(bot_response)

# step5 : exit program



