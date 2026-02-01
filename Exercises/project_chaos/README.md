# Project Chaos - Reorganization Exercise

This project is intentionally disorganized. All files are in the root directory without proper structure.

## Current State

- ❌ All source code in root
- ❌ Test files mixed with source code
- ❌ No package structure
- ❌ No proper separation of concerns

## Your Task

Reorganize this project into a professional Python src/ layout:

```
project_chaos/
├── src/
│   └── project_chaos/
│       ├── __init__.py
│       ├── main.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── database.py
│       │   └── analytics.py
│       └── utils/
│           ├── __init__.py
│           └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── test_database.py
│   └── test_analytics.py
├── README.md
├── requirements.txt
├── pyproject.toml
└── .gitignore
```

## Requirements

1. Create proper directory structure
2. Move files to appropriate locations
3. Fix all imports
4. Ensure tests run from root: `pytest`
5. Ensure main runs: `python -m project_chaos.main`

## Running Tests

After reorganization:
```bash
pytest tests/
```

## Running Application

After reorganization:
```bash
python -m src.project_chaos.main
```
