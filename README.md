# AlgoVaultPy

A collection of my algorithm challenges (LeetCode, Codewars, etc.), each backed by **pytest** unit tests.

TDD workflow: Red → Green → Refactor.

![tests](https://github.com/tonyruizo/AlgoVaultPy/actions/workflows/python.yml/badge.svg)
![type-check](https://github.com/tonyruizo/AlgoVaultPy/actions/workflows/type-check.yml/badge.svg)


- *Challenges are inside src/algo_vault/..*
- *Tests are inside tests/..*

<br>

## Prerequisites
- Python 3.10+
- pip (latest recommended: python -m pip install --upgrade pip)


<br>

## Quick Start 

```bash
git clone https://github.com/tonyruizo/AlgoVaultPy.git

$ cd AlgoVaultPy

# Create a virtual environment before installing depedencies (recommended)
$ python3 -m venv .venv     # Windows: python -m venv .venv     

# Activate the virtual environment:
$ source .venv/bin/activate # windows: .venv\Scripts\Activate

# Install dependencies from pyproject.toml
$ pip install -e ".[dev]"   # Windows: pip install -e '.[dev]'

# Run all tests
$ pytest 

# Run test on a specific file (replace test_file_name.py)         
$ pytest tests/test_leetcode/test_file_name.py 
