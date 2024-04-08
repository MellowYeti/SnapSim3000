# Snap Simulator 3000

👋 Hey.

This repository was created as a submission for another tech test. The brief is included in [docs/BRIEF.md](docs/BRIEF.md). I'm particulalry proud of this because I was able to use the Asyncio library to create a deliberate race condition. I wanted to have an indeterminate outcome from the simulation so that it would be a realistic representation of the game.

I've used `Poetry`, `Pytest`, `Black`, `Mypy`, `Ruff` and `iSort` in development but the package itself should run in a standard environment.

I used Python 3.12.0 to build this but I haven't used any features specific to that version so the code should be compatible with at least py3.10 and up.

I'm looking forward to discussing it with you.

## How to run

### Option 1

Install the wheel into your python environment using pip.

```shell
pip install dist/snapsim3000-0.1.0-py3-none-any.whl
python -m snapsim3000 
```

### Option 2

Use Poetry.

```shell
poetry install
poetry shell
python -m snapsim3000
```

Poetry will also allow you to run the test suite.

 ```shell
 poetry run doit test
 ```
