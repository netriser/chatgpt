import openai
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from colorama import just_fix_windows_console
just_fix_windows_console()

# Definir OpenAI API key 
openai.api_key = "API_KEY"

history = []
while True:
    user_input = input("Q: " + Style.BRIGHT + Fore.RED)
    print(Style.RESET_ALL)
    if user_input.upper() == "QUIT":
        break
        
    messages = []
    for input_text, completion_text in history:
        messages.append({"role": "user", "content": input_text})
        messages.append({"role": "assistant", "content": completion_text})

    messages.append({"role": "user", "content": user_input})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    completion_text = completion.choices[0].message.content
    print(Style.BRIGHT + Fore.GREEN + completion_text + Style.RESET_ALL)

    history.append((user_input, completion_text))
