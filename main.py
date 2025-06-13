import json
import random
import difflib
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter
import os

with open("code.json", "r") as f:
    prompts = json.load(f)

def generate_code(user_input):
    matched_prompt = difflib.get_close_matches(user_input.lower(), prompts.keys())
    if matched_prompt:
        code = prompts[matched_prompt[0]]
        success = True
    else:
        code = ""
        success = False
    return code, success

def create_and_run_file(code):
    filename = f"generated_{random.randint(1000, 9999)}.py"
    with open(filename, "w") as f:
        f.write(code)
    os.system(f"python {filename}")

print("Hello! I'm Ghostwriter. You can ask me to code and I will do my best to provide the requested code.")
last_code_output = ""
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "run" and last_code_output:
        create_and_run_file(last_code_output)
    elif user_input.lower() == "clear":
      os.system("clear")
    else:
        code, success = generate_code(user_input)
        if success:
            highlighted_code = highlight(code, PythonLexer(), TerminalFormatter())
            code_output = f"\n{'=' * 50}\n{highlighted_code}{'=' * 50}\n"
            print(f"Ghostwriter: Here's the code you requested:{code_output}", "There will be indentation errors and I apologize. Type 'run' to test the code!")
            last_code_output = code
        else:
            print("Ghostwriter: I'm sorry, I couldn't understand your request. Please try again.")