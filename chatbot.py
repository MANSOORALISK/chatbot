# Importing necessary libraries
import nltk
# Downloading required NLTK datasets
nltk.download('punkt')
nltk.download('wordnet')

from nltk.chat.util import Chat, reflections

# Defineing pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",  # Pattern to match "my name is [name]"
        ["Hello %1, How are you today ?",]  # Response with the captured name
    ],
    [
        r"hi|hey|hello",  # Pattern to match greetings
        ["Hello", "Hey there",]  # Possible responses to greetings
    ],
    [
        r"what is your name ?",  # Pattern to ask the bot's name
        ["I am a chatbot created using NLTK.",]  # Response with bot's name
    ],
    [
        r"how are you ?",  # Pattern to ask how the bot is
        ["I'm doing good. How about you?",]  # Response to the query
    ],
    [
        r"sorry (.*)",  # Pattern to detect apologies
        ["It's alright, no problem.",]  # Response to apologies
    ],
    [
        r"I am fine",  # Pattern to indicate the user is fine
        ["Great to hear that. How can I help you?",]  # Response to user's well-being
    ],
    [
        r"quit",  # Pattern to end the conversation
        ["Bye, take care. It was nice talking to you. See you soon :)"]  # Response when quitting
    ],
]

# Defining a simple chatbot using NLTK's Chat utility
def chatbot():
    print("Hi, I'm the NLTK chatbot. Type 'quit' to exit.")  # Greeting message
    chat = Chat(pairs, reflections)  # Initialize the Chat object with patterns and reflections
    chat.converse()  # Start the conversation

# Run the chatbot
if __name__ == "__main__":
    chatbot()  # Call the chatbot function if the script is executed directly

'''
output:
[nltk_data] Downloading package punkt to
[nltk_data]     C:\Users\chari\AppData\Roaming\nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package wordnet to
[nltk_data]     C:\Users\chari\AppData\Roaming\nltk_data...


[nltk_data]   Package wordnet is already up-to-date!
Hi, I'm the NLTK chatbot. Type 'quit' to exit.
>my name is charitha
Hello charitha, How are you today ?
>i am fine
Great to hear that. How can I help you?
>how are you
I'm doing good. How about you?
>what is your name
I am a chatbot created using NLTK.
>hello 
Hey there
>sorry bot
It's alright, no problem.
>quit
Bye, take care.It was nice talking to you. See you soon :)'''
