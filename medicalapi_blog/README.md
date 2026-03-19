# MedicalAPI Blog

A FastAPI-based project for medical blogging and experimentation.

---

## 📁 Project Structure

```
Medicalapi_blog/
│
├── .venv/                      # Python virtual environment (ignored by Git)
├── main.py                     # Entry point for FastAPI app
├── notebooks/                  # Jupyter notebooks
│   └── example_notebook.ipynb
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── .gitignore                  # Git ignore rules
```

---

## ⚙️ Prerequisites

- Python 3.9+
- `pip` or [`uv`](https://github.com/astral-sh/uv) package manager

---

## 🐍 Virtual Environment Setup

This project uses a Python virtual environment for dependency isolation.

**1. Create the virtual environment:**
```bash
python -m venv .venv
```

**2. Activate the environment:**

| Platform | Command |
|---|---|
| Windows (PowerShell) | `.venv\Scripts\activate` |
| macOS / Linux | `source .venv/bin/activate` |

**3. Install dependencies:**
```bash
# Using pip
pip install -r requirements.txt

# Or using uv
uv add "fastapi[standard]"
```

**4. Deactivate when done:**
```bash
deactivate
```

---

## 🚀 Running the App

Start the FastAPI development server with hot-reload:

```bash
uvicorn main:app --reload
```

Then visit:

| URL | Description |
|---|---|
| http://127.0.0.1:8000 | App home |
| http://127.0.0.1:8000/docs | Interactive Swagger UI |
| http://127.0.0.1:8000/redoc | ReDoc API documentation |

---

## 📓 Notebooks

Jupyter notebooks for experimentation and data exploration are located in the `notebooks/` folder.

To launch Jupyter:
```bash
jupyter notebook
```

---

## 🗂️ Git Setup

Create a `.gitignore` in the project root with the following:

```
# Virtual environment
.venv/

# Python cache
__pycache__/
*.pyc
*.pyo

# Jupyter checkpoints
.ipynb_checkpoints/

# Environment variables
.env
```

Then initialize and push your repo:
```bash
git add .gitignore README.md
git commit -m "Add README and ignore .venv"
git push
```

---

## 📄 License

This project is open-source. Feel free to use and adapt it for your own work.
