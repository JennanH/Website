# Logik

# Mehrere To-Do-Listen
todo_lists = [] # erste Lösung mit Arrays | alle todo_lists. mit Datenbank Funktionen austauschen

def add_list(list_name):
    todo_lists.append({"name": list_name, "tasks": []})

def delete_list(list_number):
    if 0 < list_number <= len(todo_lists):
        del todo_lists[list_number - 1]
    else:
        print("Ungültige Listennummer.")

def add_task(list_number, task):
    if 0 < list_number <= len(todo_lists):
        todo_lists[list_number - 1]["tasks"].append({"task": task, "completed": False})
    else:
        print("Ungültige Listennummer.")

def show_tasks(list_number):
    if 0 < list_number <= len(todo_lists):
        tasks = todo_lists[list_number - 1]["tasks"]
        if not tasks:
            print("Keine Aufgaben vorhanden.")
        else:
            for idx, task in enumerate(tasks, start=1):
                status = "Erledigt" if task["completed"] else "Offen"
                print(f"{idx}. {task['task']} - {status}")
    else:
        print("Ungültige Listennummer.")

def delete_task(list_number, task_number):
    if 0 < list_number <= len(todo_lists):
        tasks = todo_lists[list_number - 1]["tasks"]
        if 0 < task_number <= len(tasks):
            del tasks[task_number - 1]
        else:
            print("Ungültige Aufgabennummer.")
    else:
        print("Ungültige Listennummer.")

def complete_task(list_number, task_number):
    if 0 < list_number <= len(todo_lists):
        tasks = todo_lists[list_number - 1]["tasks"]
        if 0 < task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
        else:
            print("Ungültige Aufgabennummer.")
    else:
        print("Ungültige Listennummer.")

def show_lists():
    if not todo_lists:
        print("Keine To-Do-Listen vorhanden.")
    else:
        for idx, todo_list in enumerate(todo_lists, start=1):
            print(f"Liste {idx}: {todo_list['name']}")
            tasks = todo_list["tasks"]
            if not tasks:
                print("  Keine Aufgaben vorhanden.")
            else:
                for task_idx, task in enumerate(tasks, start=1):
                    status = "Erledigt" if task["completed"] else "Offen"
                    print(f"  {task_idx}. {task['task']} - {status}")

# Logik Testung in CLI

while True:
    print("\n1. To-Do-Liste hinzufügen")
    print("2. Alle To-Do-Listen anzeigen")
    print("3. Aufgabe zu einer Liste hinzufügen")
    print("4. Aufgaben einer Liste anzeigen")
    print("5. Aufgabe aus einer Liste löschen")
    print("6. Aufgabe aus einer Liste als erledigt markieren")
    print("7. Liste löschen")
    print("8. Beenden")
    
    choice = input("Wähle eine Option: ")
    
    if choice == "1":
        list_name = input("Gib den Namen der Liste ein: ")
        add_list(list_name)
    elif choice == "2":
        show_lists()
    elif choice == "3":
        list_number = int(input("Gib die Listennummer ein: "))
        task = input("Gib die Aufgabe ein: ")
        add_task(list_number, task)
    elif choice == "4":
        list_number = int(input("Gib die Listennummer ein: "))
        show_tasks(list_number)
    elif choice == "5":
        list_number = int(input("Gib die Listennummer ein: "))
        task_number = int(input("Gib die Aufgabennummer zum Löschen ein: "))
        delete_task(list_number, task_number)
    elif choice == "6":
        list_number = int(input("Gib die Listennummer ein: "))
        task_number = int(input("Gib die Aufgabennummer zum Erledigen ein: "))
        complete_task(list_number, task_number)
    elif choice == "7":
        list_number = int(input("Gib die Listennummer zum Löschen ein: "))
        delete_list(list_number)
    elif choice == "8":
        break
    else:
        print("Ungültige Auswahl. Bitte versuche es erneut.")

