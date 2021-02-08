task=[]
task_redo=[]
task_undo=[]

def undo(task, task_des):
    if not task:
        print("Nothing to undo!")
    else:
        aux = task.pop()
        task_redo.append(aux)

def redo(task, task_re):
    if not task_redo:
        print("Nothing to redo!")
    else:
        aux = task_redo.pop()
        task.append(aux)

while True:
    answ = input("\nType if you want to Add, List, Undo, Redo or Exit [A/L/U/R/E]: ")
    answ = answ.upper()

    if answ == 'A':
        aux = input("Task: ")
        task.append(aux)
        continue

    elif answ == 'L':
        print(f"Taks: {task}")
        continue

    elif answ == 'U':
        undo(task, task_undo)
        continue

    elif answ == 'R':
        redo(task, task_undo)
        continue

    elif answ == 'E':
        print("\nEND!")
        break