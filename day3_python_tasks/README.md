# 🐍 Day 3 – Python Structured Project

## 📌 Project Overview

This repository contains structured Python practice tasks organized using a modular project architecture.

The project demonstrates:

- Clean folder structure
- Separation of concerns
- Validation logic
- Custom exception handling
- JSON file handling
- Unit testing using pytest
- Proper Python package organization

This structure follows professional backend development practices.

---

# 📂 Project Structure

```
day3_python_tasks/
│
├── basics/
│   ├── __init__.py
│   ├── list_operations.py
│   ├── dict_operations.py
│   ├── set_operations.py
│   └── tuple_operations.py
│
├── validations/
│   ├── __init__.py
│   ├── task_b_1_emailval.py
│   └── task_b_2_password.py
│
├── mini_project/
│   ├── __init__.py
│   ├── mark_processor.py
│   ├── cart_system.py
│   └── student_marks.json
│
├── tests/
│   ├── __init__.py
│   ├── test_task_b_1_emailval.py
│   └── test_task_b_2_password.py
│
├── manual_test/
│   └── test_task_b_2_password.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🧱 Folder & File Description

---

## 🔹 basics/

Contains fundamental Python data structure practice.

### Files:

- `list_operations.py` →  List Manipulation -
Add, remove, sort, reverse items,
Remove duplicates without using set()
- `dict_operations.py` → Dictionary operations - Count occurrences of each character in a string
- `set_operations.py` → Set operations & uniqueness logic - Find common items between two lists using sets
- `tuple_operations.py` → Immutable data structure usage - Convert tuple → list → tuple after modification

Purpose:
Strengthen core Python fundamentals before building applications.

---

## 🔹 validations/

Contains reusable validation logic.

### Files:

### `task_b_1_emailval.py`

Implements basic email validation logic.

Validation rules:
- Must contain exactly one '@'
- Must contain '.' in domain


Returns:
- True / False

---

### `task_b_2_password.py`

Implements password strength validation using:

- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit

Uses:
- Custom exception `WeakPasswordError`

Returns:
- Success message if valid
- Raises exception if invalid

Demonstrates:
- Exception handling
- Clean validation logic
- Professional error reporting

---

## 🔹 mini_project/

Contains small applied mini-projects.

### `mark_processor.py`
- Accepts student 5 subjects marks
- Calculates total
- Calculates average
- Assigns grade
- Store result in a dictionary
- Save the dictionary to a `JSON file`

Read the file again and print results

Demonstrates:
- Functions
- Conditional logic
- Data processing
- File handling
- JSON serialization/deserialization

---

### `cart_system.py`
Simple cart system logic for adding items and calculating totals.

Demonstrates:
- List/dictionary usage
- Basic business logic simulation

---

## 🔹 tests/

Contains unit tests written using pytest.

### Files:

- `test_task_b_1_emailval.py`

Purpose:
- Validate correctness of validation logic
- Ensure reliability
- Follow Test-Driven Development principles

Run tests using:

```
pytest
```

---

## 🔹 manual_test/

Used for manual execution testing outside pytest.

Note:
Recommended to run using:

```
python -m manual_test.test_task_b_2_password
```

Instead of directly running the file.

---

## 🔹 main.py

Entry point of the project.

Used to manually execute validation logic.

Run using:

```
python main.py
```

Professional Practice:
Always maintain a single execution entry point.

---

## 🔹 requirements.txt

Contains external dependencies.

Current dependency:

```
pytest
```

Used for unit testing.

Install using:

```
pip install -r requirements.txt
```

---

## 🔹 .gitignore

Prevents committing:

- venv/
- __pycache__/
- .env


Maintains clean repository hygiene.

---

---

## 📦 Understanding `__init__.py`

Each major folder in this project contains an `__init__.py` file.

Example:

```
basics/
validations/
mini_project/
tests/
```

### 🔹 What is `__init__.py`?

`__init__.py` marks a directory as a **Python package**.

# 🏗 Architectural Design

This project follows:

- Modular structure
- Separation of concerns
- Validation layer isolation
- Test layer separation
- Clean entry point design

Flow Example:

```
User Input → Validation Layer → Business Logic → Output
```

---

# 🧠 Concepts Demonstrated

- Python packages (`__init__.py`)
- Custom exceptions
- Exception handling
- Modular imports
- Unit testing with pytest
- JSON file handling
- Clean folder organization
- Import resolution handling
- Professional execution patterns (`python -m`)

---

# 🚀 How To Run The Project


## Run Tests

```
pytest
```

---

## Run Manual Test File Properly

```
python -m manual_test.test_task_b_2_password
```

---

## Run other .py files File

```
python <filename>.py
```

---

# 🎯 Learning Outcome

This project demonstrates the transition from:

Beginner script-based coding  
➡  
Modular, testable, professional Python project structure  

This architecture improves:

- Scalability
- Maintainability
- Testability
- Readability
- Professional coding standards

---


