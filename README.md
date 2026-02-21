Here’s a **README.md** you can paste into your project.

````md
 🧁 Bakery Project (Django)

This project is a Django app built following the She Codes Django tutorial:
https://tutorials.shecodes.com.au/django/

---

✅ Prerequisites
- Python 3.10+ (recommended)
- pip (comes with Python)

Check your Python version:
```bash
python3 --version
````

---

## 1) Clone the project & go into the folder

```bash
git clone <YOUR_REPO_URL>
cd <YOUR_PROJECT_FOLDER>
```

---

## 2) Create and activate a virtual environment (venv)

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```


## 3) Install dependencies (requirements)

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> If you don’t have a `requirements.txt` yet, you can create one after installing packages:

```bash
pip freeze > requirements.txt
```

---

## 4) Run database migrations

```bash
python manage.py migrate
```

---

## 5) Create a superuser (admin login)

```bash
python manage.py createsuperuser
```

Follow the prompts to set:

* Username
* Email (optional)
* Password

---

## 6) Start the Django development server

```bash
python manage.py runserver
```

Open in your browser:

* App: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

Log into the admin with the superuser you created.

---

## Common Issues

### ❗ "command not found: python" (macOS/Linux)

Try:

```bash
python3 manage.py runserver
```

### ❗ Migrations not applied

Run:

```bash
python manage.py makemigrations
python manage.py migrate
```

### ❗ Deactivate venv

```bash
deactivate
```

---

## Project Notes

* Django settings and app structure follow the She Codes Django tutorial:
  [https://tutorials.shecodes.com.au/django/](https://tutorials.shecodes.com.au/django/)


