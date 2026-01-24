#!/usr/bin/env python3
# todo.py

# This is a command line todo manager.
# We can make, complete and view todos.

# we will store a global list of todos in ~/.todo/todos

from pathlib import Path
import sys
TODO_FILE = Path.home() / ".todo" / "todos"

def load_todos():
    if not TODO_FILE.exists():
        return []
    with open(TODO_FILE, "r") as f:
        todos = [line.strip() for line in f.readlines() if line.strip()]
    return todos

def save_todos(todos):
    TODO_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(TODO_FILE, "w") as f:
        for todo in todos:
            f.write(todo + "\n")

def add_todo(todo):
    todos = load_todos()
    todos.append(todo)
    save_todos(todos)
    print(f"Added todo: {todo}")

def list_todos():
    todos = load_todos()
    if not todos:
        print("No todos found.")
        return
    for idx, todo in enumerate(todos, 1):
        print(f"{idx}. {todo}")

def complete_todo(index):
    todos = load_todos()
    if index < 1 or index > len(todos):
        print("Invalid todo index.")
        return
    completed = todos.pop(index - 1)
    save_todos(todos)
    print(f"Completed todo: {completed}")

def clear_todos():
    # Ask for confirmation
    confirm = input("Are you sure you want to clear all todos? (y/n): ")
    if confirm.lower() != 'y':
        print("Clear operation cancelled.")
        return

    todos = []
    save_todos(todos)
    print("Cleared all todos.")

def edit_todo(index, new_todo):
    todos = load_todos()
    if index < 1 or index > len(todos):
        print("Invalid todo index.")
        return
    todos[index - 1] = new_todo
    save_todos(todos)
    print(f"Edited todo {index}: {new_todo}")

def swap_todos(x, y):
        x -= 1
        y -= 1

        todos = load_todos()

        temp = todos[x]
        todos[x] = todos[y]
        todos[y] = temp

        save_todos(todos)

def top_todo(index):
    index -= 1

    todos = load_todos()

    todo = todos.pop(index)
    todos.insert(0, todo)

    save_todos(todos)

def bottom_todo(index):
    index -= 1

    todos = load_todos()

    todo = todos.pop(index)
    todos.append(todo)

    save_todos(todos)

def move_todo(index, position):
    index -= 1
    position -= 1

    todos = load_todos()

    todo = todos.pop(index)
    todos.insert(position, todo)

    save_todos(todos)

def print_help():
    help_text = """
Usage:
    todo add "description"            - Add a new todo
    todo list                         - List all todos
    todo do INDEX                     - Complete a todo by its index
    todo help                         - Show this help message
    todo clear                        - Clear all todos
    todo swap X Y                     - Swap todos at index X and Y
    todo top INDEX                    - Move todo at INDEX to the top
    todo bot INDEX                    - Move todo at INDEX to the bottom
    todo move INDEX POSITION          - Move todo at INDEX to POSITION
    todo edit INDEX "new description" - Edit the todo at INDEX
"""
    print(help_text)

def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide a description.")
            sys.exit(1)
        todo_description = " ".join(sys.argv[2:])
        add_todo(todo_description)
    elif command == "list":
        list_todos()
    elif command == "do":
        if len(sys.argv) < 3:
            print("Please provide the index of the todo to complete.")
            sys.exit(1)
        try:
            index = int(sys.argv[2])
            complete_todo(index)
        except ValueError:
            print("Index must be a number.")
            sys.exit(1)
    elif command == "help":
        print_help()
    elif command == "clear":
        clear_todos()
    elif command == "swap":
        if len(sys.argv) < 4:
            print("Please provide two indexes to swap")
            sys.exit(1)
        try:
            x = int(sys.argv[2])
            y = int(sys.argv[3])
            swap_todos(x, y)
        except ValueError:
            print("Indexes must be numbers.")
            sys.exit(1)
    elif command == "top":
        if len(sys.argv) < 3:
            print("Please provide the index of the todo to move to the top")
            sys.exit(1)
        try:
            index = int(sys.argv[2])
            top_todo(index)
        except ValueError:
            print("Index must be a number.")
            sys.exit(1)
    elif command == "bot":
        if len(sys.argv) < 3:
            print("Please provide the index of the todo to move to the bottom")
            sys.exit(1)
        try:
            index = int(sys.argv[2])
            bottom_todo(index)
        except ValueError:
            print("Index must be a number.")
            sys.exit(1)
    elif command == "move":
        if len(sys.argv) < 4:
            print("Please provide the index of the todo and the new position")
            sys.exit(1)
        try:
            index = int(sys.argv[2])
            position = int(sys.argv[3])
            move_todo(index, position)
        except ValueError:
            print("Indexes must be numbers.")
            sys.exit(1)
    else:
        print("Unknown command.")
        print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()

