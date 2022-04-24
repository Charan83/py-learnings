from pyfiglet import figlet_format
from termcolor import colored
from helper import get_jokes

msg = "Dad Joke 3000"
figlet_text = figlet_format(msg)
colored_text = colored(figlet_text, color='cyan')
print(colored_text)
topic = input("Let me tell you a joke! Give me a topic: ")
jokes = get_jokes(topic).get("results")
num_jokes = len(jokes)
if num_jokes:
    print(f"I've got {num_jokes} jokes about {topic}. Here's one:")
    print(jokes[0].get('joke'))
else:
    print(f"Sorry, I don't have any jokes about {topic}! Please try again.")
