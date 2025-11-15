# 📘 Notes App – Backend (Django REST API)

This is the **backend API** for the Notes Application, built using **Django**, **Django REST Framework**, and **JWT authentication** (SimpleJWT).  
It handles:

- User Signup  
- User Signin  
- Authentication  
- CRUD operations for Notes  

This backend is consumed by the **Next.js frontend**.

---

## 🚀 Live API (Render)

Backend URL:  
👉 https://your-backend.onrender.com  
*(Replace this with your actual Render service link)*

---

## 🧩 Tech Stack

- **Python 3.10+**
- **Django 5**
- **Django REST Framework**
- **JWT Authentication (SimpleJWT)**
- **SQLite / PostgreSQL compatible**
- **CORS Headers**

---

## 📁 Project Structure

```
/backend
  /users
  /notes
  /backend (settings)
manage.py
requirements.txt
```

---

## ⚙️ Local Setup instructions

### **1. Clone the repo**

```bash
git clone https://github.com/<your-username>/notes-backend.git
cd notes-backend
```

### **2. Create and activate virtual environment**

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### **3. Install dependencies**

```bash
pip install -r requirements.txt
```

### **4. Apply migrations**

```bash
python manage.py migrate
```

### **5. Run development server**

```bash
python manage.py runserver 8000
```

Backend opens at:

👉 http://127.0.0.1:8000

---

## 🔐 Environment Variables

Create a file:

```
.env
```

Add:

```env
SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
```

For production in Render:

```
SECRET_KEY=<secure-production-secret>
DJANGO_DEBUG=False
```

---

## 🌐 CORS Setup

Inside `settings.py`:

```py
CORS_ALLOWED_ORIGINS = [
    "https://your-frontend-url.vercel.app",
    "http://localhost:3000",
]
```

---

## 🔥 API Endpoints

### **Authentication**

#### 📌 Signup  
`POST /api/auth/signup/`

Send:

```
{
  "user_name": "Vijay",
  "user_email": "email@example.com",
  "password": "123456"
}
```

Response:

```
{
  "token": "<jwt-access-token>",
  "refresh": "<jwt-refresh-token>",
  "user": {
    "user_id": "<uuid>",
    "user_email": "email@example.com",
    "user_name": "Vijay"
  }
}
```

---

#### 📌 Signin  
`POST /api/auth/signin/`

Body:

```
{
  "user_email": "email@example.com",
  "password": "123456"
}
```

---

### **Notes**

📌 **Get all notes (requires token)**  
`GET /api/notes/`

📌 **Create new note**  
`POST /api/notes/`

Body:

```
{
  "note_title": "My title",
  "note_content": "My content"
}
```

📌 **Update note**  
`PUT /api/notes/<id>/`

📌 **Delete note**  
`DELETE /api/notes/<id>/`

---




