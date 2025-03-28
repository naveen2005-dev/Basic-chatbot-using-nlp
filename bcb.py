from datetime import datetime
from nltk.chat.util import Chat, reflections

# Define patterns for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hi there!']),
    (r'how are you', ['I am good, thank you!']),
    (r'How you doing', ['Good!!']),
    (r'i love you',['Thanks for loving me!']),
    (r'what is your name', ['You can call me Sakha.']),
    (r'bye|goodbye', ['Goodbye!', 'Caught you later!', 'See you later.']),
    (r'my name is (.*)', ['Nice to meet you, %1!']),
    (r'i am (.*)', ['Nice to meet you, %1!']),
    (r'myself (.*)', ['Nice to meet you, %1!']),
    (r'this is (.*)', ['Nice to meet you, %1!']),
    (r'time', ['The current time is %s.' % datetime.now().strftime('%H:%M:%S')]),
    (r'interview', ['For interview tips, make sure to research the company, practice common questions, and showcase your relevant skills and experiences.']),
    (r'resume|CV', ['When preparing your resume, highlight your achievements, use action verbs, and tailor it to the job description.']),
]

# Dictionary to store user prompts and responses
user_responses = {}

# Function to add a new prompt and response to the dictionary
def add_prompt(prompt, response):
    user_responses[prompt.lower()] = response

# Create a chatbot instance
chatbot = Chat(patterns, reflections)

# Function to start the chat
def start_chat():
    print("Hello! I'm a Sakha.")
    while True:
        user_input = input()
        if user_input.lower() == 'bye':
            print("Sakha: Goodbye!")
            break
        elif user_input.lower() == 'add':
            new_prompt = input("Sakha: Enter a new prompt: ")
            new_response = input("Sakha: Enter a response for the prompt: ")
            add_prompt(new_prompt, new_response)
            print("Sakha: New prompt added successfully.")
        else:
            # Check if the user input matches any prompt in the dictionary
            matched_response = user_responses.get(user_input.lower(), None)
            if matched_response:
                print("Sakha:", matched_response)
            else:
                response = chatbot.respond(user_input)
                print("Sakha:", response)

# Start the chat
start_chat()
