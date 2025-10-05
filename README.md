# AlgoVaultPy

A collection of my algorithm challenges (LeetCode, Codewars, etc.), each backed by **pytest** unit tests.

TDD workflow: Red → Green → Refactor.

![tests](https://github.com/tonyruizo/AlgoVaultPy/actions/workflows/python.yml/badge.svg)

- *Code inside src/algo_vault/..*
- *Tests inside tests/..*

## Prerequisites
- Python 3.13+
- pip (latest recommended: python -m pip install --upgrade pip)
- (Optional but recommended) a virtual environment

### Quick Start (local)

```bash
git clone https://github.com/tonyruizo/AlgoVaultPy.git

cd AlgoVaultPy

# create & activate a venv
python -m venv .venv

# mac/linux:
source .venv/bin/activate
# windows (PowerShell):
# .venv\Scripts\Activate.ps1

# Install project + dev tools from pyproject.toml
pip install -e ".[dev]"    # Windows PowerShell: pip install -e '.[dev]'

# Run all tests
pytest 

# Run one test (replace test_file_name.py)         
pytest tests/test_leetcode/test_file_name.py 
