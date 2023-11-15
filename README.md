# Snap Simulator 3000

👋 Hey.

Here is my submission. I've used `Poetry`, `Pytest`, `Black` and `iSort` in development but the package itself should run in a standard environment.

I used Python 3.12.0 to build this but I haven't used any features specific to that version so the code should be compatible with at least py3.10 and up.

I'm looking forward to your feedback.

## How to run

### Option 1

Install the wheel into your python environment using pip.

```shell
pip install pip install dist/snapsim3000-0.1.0-py3-none-any.whl
python -m snapsim3000 
```

### Option 2

Run directly from src.

```shell
cd src/
python -m snapsim3000
```

### Option 3

Use Poetry.

```shell
poetry install
poetry shell
python -m snapsim3000
```

Poetry will also allow you to run the test suite.

 ```shell
 poetry run pytest
 ```
