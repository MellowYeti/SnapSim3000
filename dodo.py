def task_lint():
    return {
        "actions": [
            "isort ./src/ ./tests/ ./dodo.py",
            "black ./src/ ./tests/ ./dodo.py",
            "ruff check --fix ./src/ ./tests/ ./dodo.py",
        ]
    }


def task_test():
    return {"actions": ["pytest"]}


def task_build():
    return {
        "actions": [
            "poetry export -f requirements.txt --output requirements.txt",
            "poetry export -f requirements.txt --output requirements-dev.txt --with dev",
            "poetry build",
        ]
    }
