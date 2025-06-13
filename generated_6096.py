    import random
    
    responses = {
     'hi': ['Hello!', 'Hi there!', 'Hi, how can I help you today?'],
     'how are you': ['I am doing well, thank you for asking.', 'I am fine, thanks for asking.'],
     'what is your name': ['My name is ChatBot.', 'I go by the name ChatBot.'],
     'bye': ['Goodbye!', 'See you later!', 'Have a nice day!']
    }
    
    def chatbot():
     print('Hello, I am ChatBot. How can I assist you today?')
     while True:
     message = input().lower()
     if message in responses:
     print(random.choice(responses[message]))
     elif 'joke' in message:
     print('Why don't scientists trust atoms? Because they make up everything!')
     elif 'meaning of life' in message:
     print('The answer to the ultimate question of life, the universe, and everything is 42.')
     elif 'exit' in message or 'bye' in message:
     print('Goodbye!')
     break
     else:
     print('I'm sorry, I don't understand. Can you please try again or ask me something else?')