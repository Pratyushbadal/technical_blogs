# Technical Blogs Platform

A Django-based web application that allows users to register, log in, and manage technical blog posts. It provides a clean interface to create, view, and manage content effectively.

## Features

- User registration and login
- Blog post creation, editing, and deletion
- Responsive UI using Bootstrap
- Admin panel for managing users and posts
- Organized templates and static files

## Technologies Used

- Python 3.x
- Django 4.x
- SQLite (default)
- HTML, CSS, JavaScript, Bootstrap

## Project Structure

```
technical_blogs/
├── manage.py
├── technical_blogs/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── templates/
│   ├── index.html
│   ├── blog.html
│   └── ...
├── static/
│   ├── css/
│   ├── js/
│   └── images/
```

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Pratyushbadal/technical_blogs.git
cd technical_blogs
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run database migrations
```bash
python manage.py migrate
```

### 5. Start the development server
```bash
python manage.py runserver
```

Open your browser and visit `http://127.0.0.1:8000/`
