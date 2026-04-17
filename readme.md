# 📝 ToDo Task Web Application

A full-stack ToDo web application built using **Django** and deployed on **Render** with a **PostgreSQL (Supabase)** database.

---

## 🚀 Live Demo

🔗 https://todo-task-81pu.onrender.com

---

## 📌 Features

* 🔐 User Authentication (Register, Login, Logout)
* 📝 Create, Update, Delete Tasks
* ✅ Mark tasks as complete/incomplete
* 👤 User-specific task management
* 🔒 Secure password hashing (Django Auth)
* 🌐 Deployed on cloud (Render)
* 🗄️ Cloud database using Supabase (PostgreSQL)

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Database:** PostgreSQL (Supabase)
* **Deployment:** Render
* **Server:** Gunicorn
* **Static Files:** WhiteNoise
* **Environment Variables:** python-decouple

---

## 📂 Project Structure

```
ToDo-Task/
│
├── Task/                # Main Django project
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── todo/                # App
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── migrations/
│
├── requirements.txt
├── manage.py
└── .env (not included in repo)
```

---

## ⚙️ Installation (Local Setup)

### 1️⃣ Clone the repository

```
git clone https://github.com/yashsaxena15/ToDo-Task.git
cd ToDo-Task
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup environment variables

Create a `.env` file:

```
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=postgres
DB_USER=postgres.xxxxx
DB_PASSWORD=your_password
DB_HOST=your_host
DB_PORT=6543
ALLOWED_HOSTS=
```

---

### 5️⃣ Run migrations

```
python manage.py migrate
```

---

### 6️⃣ Run server

```
python manage.py runserver
```

---

## ☁️ Deployment (Render)

* Connected GitHub repository
* Added environment variables in Render dashboard
* Used Gunicorn as WSGI server
* Configured:

```
Build Command:
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput

Start Command:
gunicorn Task.wsgi:application --bind 0.0.0.0:$PORT
```

---

## 🧠 Key Learnings

* Django deployment on Render
* PostgreSQL integration with Supabase
* Environment variable management
* Debugging production errors
* Handling migrations in cloud environment

---

## 📸 Screenshots

<!-- *Add screenshots here (optional)* -->
![Task List](https://github.com/yashsaxena15/ToDo-Task/blob/main/ScreenShots/image.png)

![Login Panel](https://github.com/yashsaxena15/ToDo-Task/blob/main/ScreenShots/Screenshot%202026-03-23%20174317.png)

![Create Task](https://github.com/yashsaxena15/ToDo-Task/blob/main/ScreenShots/Screenshot%202026-03-23%20174504.png)


---

## 📬 Contact

* GitHub: https://github.com/yashsaxena15
* LinkedIn: https://www.linkedin.com/in/yashsaxena15

---

## ⭐ Give a Star

If you found this project helpful, please ⭐ the repository!
