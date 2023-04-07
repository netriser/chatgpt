import openai
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from colorama import just_fix_windows_console
just_fix_windows_console()

# Define OpenAI API key 
openai.api_key = "API_KEY"

f = open("jailbreak.txt", "r")
dan_var = f.read()

history = []
while True:
    
    if dan_var != "":
        user_input = dan_var
        dan_var = ""
    else:
        user_input = input("Q: " + Style.BRIGHT + Fore.RED)
        if user_input == "readex":
            f = open("readex.txt", "r")
            readex_var = f.read()
            if readex_var != "":
                user_input = readex_var
        print(Style.RESET_ALL)
    
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

    if user_input.upper() == "QUIT":
        break
