# 🌐 Padmapriya R — Personal Portfolio Website

> A full-stack personal portfolio website built with **Python Flask**, **MySQL**, and modern **HTML/CSS/JavaScript**.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)](https://flask.palletsprojects.com)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?logo=mysql)](https://mysql.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 👩‍💻 About

**Student:** Padmapriya R  
**College:** Adhiyamaan College of Engineering, Hosur  
**Degree:** B.E. Computer Science & Engineering (III Year)  
**CGPA:** 8.86  
**Email:** ppadmapriya807@gmail.com  
**GitHub:** [github.com/ppadmapriya807-cell](https://github.com/ppadmapriya807-cell)  
**LinkedIn:** [linkedin.com/in/padmapriya-raja-701633335](https://www.linkedin.com/in/padmapriya-raja-701633335)

---

## ✨ Features

- 🎨 Modern blue-white responsive design
- 🏠 Hero section with typewriter animation
- 👩 About Me with education timeline
- 💡 Skills with animated progress bars
- 🗂️ Project cards with GitHub links
- 🏆 Certification cards
- 📩 Working contact form (saves to MySQL)
- 📄 Resume download
- 🌙 Smooth scroll & mobile hamburger menu
- 🚀 Deployment-ready (Render + Railway)

---

## 📁 Folder Structure

```
portfolio/
│
├── app.py                  ← Flask application (main backend)
├── config.py               ← Configuration settings
├── database.sql            ← MySQL schema & sample data
├── requirements.txt        ← Python dependencies
├── Procfile                ← For Render deployment
├── .env.example            ← Environment variable template
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html          ← Main HTML page
│
└── static/
    ├── css/
    │   └── style.css       ← All styles
    ├── js/
    │   └── main.js         ← All JavaScript
    └── Padmapriya_R_Resume.pdf  ← Your resume (add this!)
```

---

## 🚀 How to Run Locally (Step by Step)

### Step 1 — Clone the Repository
```bash
git clone https://github.com/ppadmapriya807-cell/portfolio.git
cd portfolio
```

### Step 2 — Create a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Set Up MySQL Database
Open MySQL in your terminal or MySQL Workbench and run:
```bash
mysql -u root -p < database.sql
```
This will:
- Create the `portfolio_db` database
- Create the `contacts` table
- Insert sample projects and certifications

### Step 5 — Configure Environment Variables
```bash
# Copy the example file
cp .env.example .env

# Open .env and fill in your MySQL password
```
Edit `.env`:
```
SECRET_KEY=any-random-secret-key
FLASK_DEBUG=True
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=YOUR_MYSQL_PASSWORD
MYSQL_DB=portfolio_db
```

### Step 6 — Add Your Resume
Place your resume PDF inside the `static/` folder:
```
static/Padmapriya_R_Resume.pdf
```

### Step 7 — Run the App
```bash
python app.py
```
Open your browser: **http://localhost:5000**

---

## 🌍 Deploy Online (Free)

### Option A — Render (Backend) + Railway (MySQL)

#### 1. Set up free MySQL on Railway
1. Go to [railway.app](https://railway.app) → New Project → MySQL
2. Copy the connection details (host, user, password, database)

#### 2. Deploy Flask on Render
1. Push your project to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your GitHub repo
4. Set these:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Add Environment Variables on Render dashboard:
   ```
   MYSQL_HOST     = (from Railway)
   MYSQL_USER     = (from Railway)
   MYSQL_PASSWORD = (from Railway)
   MYSQL_DB       = portfolio_db
   SECRET_KEY     = any-random-string
   FLASK_DEBUG    = False
   ```
6. Click **Deploy** — your portfolio goes live! 🎉

---

## 🗄️ Database Schema

```sql
CREATE TABLE contacts (
    id           INT AUTO_INCREMENT PRIMARY KEY,
    name         VARCHAR(100) NOT NULL,
    email        VARCHAR(150) NOT NULL,
    message      TEXT NOT NULL,
    submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

To view contact form submissions:
```sql
USE portfolio_db;
SELECT * FROM contacts ORDER BY submitted_at DESC;
```

---

## 🛠️ Tech Stack

| Layer     | Technology         |
|-----------|--------------------|
| Frontend  | HTML5, CSS3, JavaScript |
| Backend   | Python 3, Flask    |
| Database  | MySQL 8            |
| Hosting   | Render (app), Railway (DB) |
| Version Control | Git & GitHub |

---

## 📬 Contact

Feel free to reach out!

- 📧 Email: ppadmapriya807@gmail.com  
- 💼 LinkedIn: [Padmapriya Raja](https://www.linkedin.com/in/padmapriya-raja-701633335)  
- 🐙 GitHub: [ppadmapriya807-cell](https://github.com/ppadmapriya807-cell)

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

*Made with ❤️ and lots of ☕ by Padmapriya R*
