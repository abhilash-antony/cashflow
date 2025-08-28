# 💰 CashFlow - Expense Tracker

CashFlow is a simple and intuitive **Django-based expense tracker** that helps users manage their daily spending.
It provides features to add, categorize, filter, and analyze expenses, making personal finance management effortless.

---

## 🚀 Features

* Add, update, delete, and restore expense records.
* Categorize expenses by type.
* Filter transactions by **category** and **date range**.
* Download statements (planned feature).
* Modern, responsive UI with Bootstrap.
* Custom confirmation dialogs for safe operations.
* Logo branding & favicon support.

---

## 🛠️ Tech Stack

* **Backend:** Django, Python
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite (default, easy to switch to PostgreSQL/MySQL)
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
CashFlow/
│── expenses/          # Core app for expense management
│── templates/         # HTML templates
│── static/            # Static files (CSS, JS, images, logo)
│── db.sqlite3         # Database
│── manage.py          # Django project manager
```

---

## ⚡ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/abhilash-antony/cashflow.git
cd cashflow
```

### 2️⃣ Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Run Migrations

```bash
python manage.py migrate
```

### 4️⃣ Start the Development Server

```bash
python manage.py runserver
```

App will be live at 👉 `http://127.0.0.1:8000/`

---

## 📌 Future Enhancements

* Export statements as **PDF/Excel**.
* Dashboard with charts & insights.
* User authentication for personal accounts.
* Mobile-friendly optimizations.

---

## 🖼️ Preview

![CashFlow Logo](expenses/static/expenses/CashFlow.png)

---

## 👨‍💻 Author

**Abhilash Antony**
📧 [Contact Me](mailto:abhilash.antony@arts.christuniversity.in)
🌐 [LinkedIn](https://linkedin.com/in/abhilash-antony)

---
