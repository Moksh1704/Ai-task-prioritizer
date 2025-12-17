#import 
from ai_utils import ask_ai_for_priority
#input to the ai
tasks = [
    "Finish DBMS assignment",
    "Buy groceries",
    "Prepare for coding test"
]

for task in tasks:
    priority = ask_ai_for_priority(task)
    print(task, "->", priority)
