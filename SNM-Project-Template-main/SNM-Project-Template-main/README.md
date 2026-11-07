# SNM-Project-Template
# Student Notes System (SNS)

A Flask-based Student Notes Management System that allows users to register, verify their email, log in, and manage personal notes through a simple and responsive web interface.

## Features

### User Authentication
- User registration with input validation.
- Password hashing using Bcrypt.
- Email OTP verification.
- Secure login and logout.
- Forgot password and password reset using timed tokens.

### Notes Management
- Add new notes.
- View saved notes.
- Edit existing notes.
- Delete notes.
- Display notes associated with the logged-in user.

### User Interface
- Dark navy theme with purple and cyan accents.
- Glassmorphism-inspired design.
- Responsive layouts.
- Styled forms, buttons, alerts, and note cards.

## Technologies Used

- **Frontend:** HTML, CSS, Jinja2
- **Backend:** Python, Flask
- **Database:** MySQL
- **Authentication:** Bcrypt, Flask Sessions
- **Email:** SMTP
- **Token Management:** ItsDangerous

## Project Structure

```text
SNM-Project-Template-main/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── hero-bg.jpg
│
└── templates/
    ├── base.html
    ├── index.html
    ├── register.html
    ├── login.html
    ├── verify.html
    ├── dashboard.html
    ├── profile.html
    ├── notes.html
    ├── addnotes.html
    ├── updatenotes.html
    ├── viewnotes.html
    ├── forgot_password.html
    └── reset_password.html
```

## Requirements

- Python 3
- MySQL Server
- pip
- Gmail SMTP credentials for email functionality

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/janu1996/Flask.git
```

### 2. Navigate to the SNS Project

```bash
cd Flask/SNM-Project-Template-main/SNM-Project-Template-main
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file and add:

```env
SECRET_KEY=your_secure_secret_key
```

Configure your MySQL database and email credentials in `config.py`.

Keep `.env` and credential files private. Never upload passwords or secret keys to GitHub.

### 7. Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Application Workflow

1. Open the home page.
2. Register with name, email, and password.
3. Verify the email using the OTP.
4. Log in to the application.
5. Access the dashboard and profile.
6. Add, view, edit, and delete personal notes.
7. Log out securely.

## Development Progress

- Flask application setup.
- User registration and login.
- Password hashing and OTP verification.
- Forgot password and reset password workflow.
- Dashboard and profile pages.
- Notes CRUD functionality.
- Responsive dark-theme UI.
- Notes page styling and form improvements.
- Bug fixes in notes creation, viewing, and editing.

## Security Notes

- Passwords are stored as hashed values.
- Authentication uses Flask sessions.
- Password reset uses timed tokens.
- Keep database credentials, email app passwords, and secret keys out of public repositories.

---

**Student Notes System (SNS)**  
Developed using Flask, Python, MySQL, HTML, and CSS.