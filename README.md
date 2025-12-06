
---

# 🎯 **MiniMatrix**

*A lightweight educational Python package for basic matrix operations.*

MiniMatrix is a simple Python library that recreates core matrix and array functionality using pure Python.
It is designed for learning and demonstration purposes—showing how matrix operations such as addition, multiplication, scalar multiplication, and transposition work under the hood without relying on external numerical libraries like NumPy.

---

## 📦 **Features**

* Object-oriented `Matrix` class for representing dense matrices
* Core matrix operations:

  * Addition
  * Multiplication
  * Scalar multiplication
  * Transposition
* Dictionary-based `SparseMatrix` class for efficient storage of sparse data
* Convenience utilities for generating:

  * Zero matrices
  * Identity matrices
  * Random matrices
* Lightweight and fully implemented using only Python built-ins
* Includes unit tests via `pytest`

---

## 📁 **Project Structure**

```
minimatrix/
│
├── pyproject.toml
├── README.md
│
├── src/
│   └── minimatrix/
│       ├── __init__.py
│       ├── matrix.py
│       ├── operations.py
│       ├── sparse.py
│       └── utils.py
│
└── tests/
    └── test_matrix.py
```

---

## 🚀 **Installation**

Clone the repository and install MiniMatrix in editable mode:

```
pip install -e .
```

Run tests:

```
pytest tests/
```

---

## 🧠 **Usage Overview**

MiniMatrix can be used to:

* Create matrix objects
* Perform matrix addition and multiplication
* Multiply matrices by scalars
* Transpose matrices
* Work with sparse matrix representations
* Generate simple matrices for testing (zero, identity, random)

All operations rely on nested loops and Python primitives, making the package ideal for learning and demonstrating fundamental algorithmic concepts.

---

## 🛠 **Development & Testing**

To work on the package:

* Install it locally in editable mode
* Develop modules in the `src/minimatrix/` directory
* Add or modify tests under `tests/`
* Use `pytest` to validate correctness

---

## 📚 **Motivation**

MiniMatrix is a project that demonstrates:

* Object-oriented design
* Fundamental matrix operations
* Sparse data structures
* Packaging and distribution using `pyproject.toml`
* Unit testing and version control workflows

The package prioritizes clarity and educational value over performance.

---

## 📝 **License**

This project is licensed under the **MIT License**.

---

## 👤 **Author**

**Nishad Mansoor**
