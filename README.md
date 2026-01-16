# Todo CLI

A simple command-line todo manager for Linux and other Unix-like systems.

## Installation

### Install from source

1. Clone or download this repository
2. Navigate to the project directory
3. Install using pip:

```bash
pip install .
```

For development mode (changes to code take effect immediately):

```bash
pip install -e .
```

After installation, the `todo` command will be available in your terminal.

## Usage

### Add a todo

```bash
todo add "Buy groceries"
todo add "Finish project report"
```

### List all todos

```bash
todo list
```

### Complete a todo

```bash
todo do 1
```

This will complete and remove the first todo from your list.

### Clear all todos

```bash
todo clear
```

### Show help

```bash
todo help
```

## Data Storage

Todos are stored in `~/.todo/todos` as a plain text file, one todo per line.

## Uninstallation

To uninstall:

```bash
pip uninstall todo-cli
```

To also remove your todo data:

```bash
rm -rf ~/.todo
```

## Requirements

- Python 3.7 or higher
- pip

## License

MIT
