# AlgoVaultPy

A collection of my algorithm challenges (LeetCode, Codewars, etc.), each backed by **pytest** unit tests.

![tests](https://github.com/tonyruizo/AlgoVaultPy/actions/workflows/test.yml/badge.svg)
![type-check](https://github.com/tonyruizo/AlgoVaultPy/actions/workflows/type-check.yml/badge.svg)


- *Challenges are inside src/algo_vault/..*
- *Tests are inside tests/..*

<br>

## Prerequisites
- Python 3.10+
- **uv** (fast Python package manager, written in Rust.)
  - Install via `curl -LsSf https://astral.sh/uv/install.sh | sh` or `pip install uv`.
  - See the installing uv guide <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_target">docs</a>.


<br>

## Quick Start 

```bash
git clone https://github.com/tonyruizo/AlgoVaultPy.git

$ cd AlgoVaultPy

# Install dependencies from pyproject.toml (creates/uses .venv automatically)
$ uv sync
```
### Testing

```Bash
# Run all tests
$ uv run pytest

# Run tests on a specific file (e.g., leetcode directory)
$ uv run pytest tests/test_leetcode/test_file_name.py  # replace file_name

# Run a specific function within a file (e.g., leetcode directory)
$ uv run pytest tests/test_leetcode/test_file_name.py -k "function_name"  # replace file_name and function_name
```