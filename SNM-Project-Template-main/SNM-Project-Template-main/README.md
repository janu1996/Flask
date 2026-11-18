# Student Notes System (SNS)

A Flask-based Student Notes System that helps students organize, manage, and securely access their personal notes and uploaded files through a simple, responsive web application.

SNS provides a centralized dashboard where users can track their notes and uploaded files, manage academic resources, and access their information whenever needed.

## Features

### 1. User Authentication and Security

- User registration with input validation.
- Email OTP verification.
- Secure login and logout.
- Password hashing using Bcrypt.
- Forgot password functionality.
- Password reset using timed tokens.
- Session-based user authentication.

### 2. Dashboard

- Personalized dashboard with a welcome message.
- Displays the total number of notes created by the logged-in user.
- Displays the total number of files uploaded by the logged-in user.
- Quick navigation to My Notes and My Files.
- Displays recently created notes.
- Provides a centralized overview of user activities.

### 3. Notes Management

- Create and save personal notes.
- View individual notes.
- Edit existing notes.
- Delete unwanted notes.
- Display notes associated with the logged-in user.
- Access and manage notes through the My Notes section.

### 4. File Management

- Upload personal files through the application.
- Store uploaded files in the application upload directory.
- View uploaded files.
- Download uploaded files.
- Delete uploaded files.
- Manage uploaded documents through the My Files section.

### 5. User Interface

- Modern dark navy theme with purple and cyan accents.
- Glassmorphism-inspired UI design.
- Responsive dashboard layout.
- Styled forms, buttons, alerts, and cards.
- Consistent navigation across application pages.
- User-friendly interface for notes and file management.

## Technologies Used

| Category | Technologies |
|---|---|
| Frontend | HTML5, CSS3 |
| Template Engine | Jinja2 |
| Backend | Python, Flask |
| Database | MySQL |
| Authentication | Flask Sessions, Bcrypt |
| Email Verification | SMTP, OTP |
| Token Management | ItsDangerous |
| Version Control | Git, GitHub |

## Project Structure

```text
SNM-Project-Template-main/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── hero-bg.jpg
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── verify.html
│   ├── dashboard.html
│   ├── profile.html
│   ├── notes.html
│   ├── addnotes.html
│   ├── updatenotes.html
│   ├── viewnotes.html
│   ├── myfiles.html
│   ├── uploadFile.html
│   ├── forgot_password.html
│   └── reset_password.html
│
└── upload/
    └── Uploaded user files
```

*Note: The structure above represents the main application organization. Template and configuration filenames should match the actual project files.*

## Application Workflow

1. User visits the SNS home page.
2. Registers with their name, email, and password.
3. Verifies their email using the OTP received.
4. Logs in using their registered credentials.
5. Accesses the personalized dashboard.
6. Views the total notes and uploaded files count.
7. Creates, views, edits, and deletes personal notes.
8. Uploads files and manages them through My Files.
9. Views or downloads uploaded files whenever required.
10. Deletes files that are no longer needed.
11. Logs out of the application.

## Installation and Setup

### Prerequisites

Make sure the following are installed:

- Python 3
- MySQL Server
- pip
- Git
- Gmail SMTP credentials for email functionality

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

### 6. Configure the Application

Create a `.env` file in the project directory and configure your secret key:

```env
SECRET_KEY=your_secure_secret_key
```

Configure the following in your local `config.py` file:

- MySQL database connection details.
- Database username and password.
- Email SMTP server settings.
- Email account credentials.

Make sure the database and required tables are created before running the application.

**Important:** Never commit `.env`, `config.py`, database passwords, email credentials, or secret keys to GitHub.

### 7. Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Main Application Modules

| Module | Description |
|---|---|
| Authentication | Registration, login, OTP verification and password reset |
| Dashboard | Displays user information, total notes, total files and recent notes |
| My Notes | Manage personal notes |
| Add Notes | Create and save new notes |
| View Notes | View saved note details |
| Update Notes | Edit existing notes |
| My Files | View and manage uploaded files |
| Upload Files | Upload personal documents |
| File Download | Download uploaded files |
| File Delete | Delete uploaded files |
| Profile | Access user profile |
| Logout | End the authenticated session |

## Security Considerations

- Passwords are stored using Bcrypt hashing.
- Authentication is managed using Flask sessions.
- Password reset uses timed tokens.
- Database and email credentials should remain private.
- Uploaded files should be accessed only by their authorized owners.
- User-uploaded documents should not be committed to the public GitHub repository.
- Secret keys and sensitive configuration files must be excluded using `.gitignore`.

## Development Progress

- Flask application setup and configuration.
- User registration and authentication.
- Email OTP verification.
- Password hashing and secure login.
- Forgot password and reset password functionality.
- Dashboard development.
- Total notes and uploaded files statistics.
- Notes CRUD functionality.
- File upload functionality.
- File viewing and downloading.
- File deletion functionality.
- My Notes and My Files management pages.
- Responsive dark-theme UI implementation.
- CSS styling and UI improvements.
- Bug fixes and application testing.

## Future Enhancements

- Search and filter notes.
- Categorize notes by subject.
- File type and size validation.
- Pagination for large collections of notes and files.
- Cloud-based file storage.
- Improved dashboard analytics.

---

## Project Information

**Project Name:** Student Notes System (SNS)

**Technology Stack:** Python, Flask, MySQL, HTML, CSS, Jinja2

**Repository:** https://github.com/janu1996/Flask

**Description:** A centralized platform for students to create and manage notes, upload and organize files, and access their academic resources through a personalized dashboard.

**Developed with Flask and Python.**