# 📝 Technical Blogs Platform

A full-featured Django-based web application for publishing and managing technical blogs. Users can register, log in, create blog posts, and browse content in a clean, responsive interface.

## 🌟 Features

- ✍️ Create, edit, and delete blog posts
- 👤 User registration and login system
- 📄 Rich templates with Bootstrap styling
- 🧭 Navigation between blog posts
- 🔒 Admin panel for managing content

## 🔧 Technologies Used

- **Backend:** Django 4.x, Python 3.x
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** SQLite (default)
- **Others:** Django Templates, Django Admin

## 📁 Project Structure

technical_blogs/
├── manage.py
├── technical_blogs/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── ...
├── templates/
│ ├── index.html
│ ├── blog.html
│ └── ...
├── static/
│ ├── css/
│ ├── js/
│ └── images/

bash
Copy
Edit

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Pratyushbadal/technical_blogs.git
cd technical_blogs
2. Create a virtual environment and activate it
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run migrations
bash
Copy
Edit
python manage.py migrate
5. Start the development server
bash
Copy
Edit
python manage.py runserver
Visit http://127.0.0.1:8000/ to view the site.

✅ To Do
Add comment system

Pagination

Blog categories and tags

📬 Contact
If you have any questions, feel free to reach out:

📧 pratyushbadal90@gmail.com
🔗 LinkedIn
