# 📁 Django File Sharing Web Application

A modern, feature-rich file sharing platform built with Django 5.x and Bootstrap 5. This application allows users to upload, share, and manage files with a beautiful, responsive interface.

![Django](https://img.shields.io/badge/Django-5.2.4-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.0-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

## ✨ Features

### 🔐 User Management
- **User Registration & Authentication**: Secure signup, login, and logout
- **Profile Management**: Update profile information and profile pictures
- **User Search**: Find and connect with other users

### 📂 File Operations
- **File Upload**: Modern drag-and-drop interface with progress indicators
- **File Management**: View, edit, and delete uploaded files
- **File Sharing**: Share files with specific users or make them public
- **File Statistics**: Track download counts and file metrics
- **File Types Support**: Images, Documents, Videos, Audio, and more

### 🎨 Modern UI/UX
- **Responsive Design**: Mobile-first Bootstrap 5 interface
- **Modern File Grid**: Beautiful card-based file display
- **Interactive Elements**: Hover effects, animations, and transitions
- **User-Friendly Forms**: Crispy forms with validation
- **Pagination**: Efficient file browsing with page navigation

### 🔒 Privacy & Security
- **Private Files**: Keep files private to your account
- **Public Sharing**: Make files publicly accessible
- **User-Specific Sharing**: Share files with selected users
- **Secure File Storage**: Organized media file management

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/harpreet-03/Blog_Hub.git
   cd Blog_Hub
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   cd django_web_app
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser**
   Navigate to `http://127.0.0.1:8000/` to access the application.

## 📋 Dependencies

The project requires the following Python packages:

```
asgiref==3.9.0
crispy-bootstrap5==2025.6
Django==5.2.4
django-crispy-forms==2.4
pillow==11.3.0
pytz==2025.2
sqlparse==0.5.3
```

## 🏗️ Project Structure

```
Django-WebApp/
├── django_web_app/              # Main project directory
│   ├── manage.py               # Django management script
│   ├── requirements.txt        # Python dependencies
│   ├── db.sqlite3             # SQLite database
│   │
│   ├── django_web_app/        # Project settings
│   │   ├── __init__.py
│   │   ├── settings.py        # Django settings
│   │   ├── urls.py           # Main URL configuration
│   │   └── wsgi.py           # WSGI configuration
│   │
│   ├── blog/                  # File sharing app
│   │   ├── models.py         # Post/File models
│   │   ├── views.py          # View functions
│   │   ├── urls.py           # App URL patterns
│   │   ├── admin.py          # Admin configuration
│   │   ├── forms.py          # Form definitions
│   │   ├── templates/        # HTML templates
│   │   │   └── blog/
│   │   │       ├── base.html
│   │   │       ├── home.html
│   │   │       ├── post_form.html
│   │   │       ├── post_detail.html
│   │   │       ├── user_search.html
│   │   │       └── share_file.html
│   │   ├── static/           # CSS, JS, images
│   │   │   └── blog/
│   │   │       ├── main.css
│   │   │       └── main.js
│   │   └── migrations/       # Database migrations
│   │
│   ├── users/                 # User management app
│   │   ├── models.py         # User profile models
│   │   ├── views.py          # User views
│   │   ├── forms.py          # User forms
│   │   ├── signals.py        # User signals
│   │   ├── templates/        # User templates
│   │   │   └── users/
│   │   │       ├── register.html
│   │   │       ├── login.html
│   │   │       └── profile.html
│   │   └── migrations/       # Database migrations
│   │
│   └── media/                 # User uploaded files
│       ├── Files/            # Uploaded documents/files
│       ├── profile_pics/     # User profile pictures
│       └── default.jpg       # Default profile image
│
├── Screenshots/               # Application screenshots
└── README.md                 # This file
```

## 🎯 Usage Guide

### 1. **User Registration & Login**
- Navigate to the home page
- Click "Sign Up" to create a new account
- Fill in username, email, and password
- Login with your credentials

### 2. **Upload Files**
- Click "New Post" or "Upload File"
- Drag and drop files or click to select
- Add a title and description
- Choose privacy settings (public/private)
- Submit to upload

### 3. **Manage Files**
- View all your files on the home page
- Click on any file to view details
- Edit or delete files you own
- Download files by clicking the download button

### 4. **Share Files**
- Open any file detail page
- Click "Share File"
- Search for users to share with
- Select users and submit

### 5. **User Profile**
- Click on your username to access profile
- Update your information and profile picture
- View your file statistics

## 🔧 Configuration

### Settings Overview
Key settings in `django_web_app/settings.py`:

```python
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap5'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

# Authentication
LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'
```

### Environment Variables
For production deployment, consider setting:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to `False` for production
- `ALLOWED_HOSTS`: Add your domain names

## 🚀 Deployment

### Development
```bash
python manage.py runserver
```

### Production Deployment Options

#### 🚂 **1. Railway (Recommended for Django)**
Railway is excellent for Django apps with file uploads and databases.

**Steps:**
1. Create account at [railway.app](https://railway.app)
2. Install Railway CLI: `npm install -g @railway/cli`
3. Login: `railway login`
4. Deploy: `railway deploy`

**Features:**
- ✅ Built-in PostgreSQL database
- ✅ Automatic HTTPS
- ✅ File uploads support
- ✅ Easy environment variables
- ✅ Free tier available

#### ☁️ **2. Render.com**
Great alternative with similar features to Railway.

**Steps:**
1. Create account at [render.com](https://render.com)
2. Connect your GitHub repository
3. Use the `render.yaml` configuration file
4. Deploy automatically

**Features:**
- ✅ Free tier with PostgreSQL
- ✅ Automatic builds from GitHub
- ✅ Custom domains
- ✅ SSL certificates

#### 🔷 **3. Vercel (Limited for Django)**
⚠️ **Note**: Vercel has limitations for Django apps with file uploads.

**Steps:**
1. Install Vercel CLI: `npm install -g vercel`
2. Run: `vercel --prod`
3. Configure environment variables

**Limitations:**
- ❌ No persistent file storage
- ❌ No built-in database
- ❌ Serverless limitations for file uploads

#### 🟣 **4. Heroku**
Traditional PaaS platform (paid plans only now).

**Steps:**
1. Install Heroku CLI
2. Create Heroku app: `heroku create your-app-name`
3. Add PostgreSQL: `heroku addons:create heroku-postgresql:mini`
4. Deploy: `git push heroku main`

### Pre-deployment Checklist

1. **Update settings for production**:
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['your-domain.com']
   ```

2. **Set environment variables**:
   - `SECRET_KEY`: Your Django secret key
   - `DATABASE_URL`: PostgreSQL connection string
   - `DJANGO_SETTINGS_MODULE`: `django_web_app.production_settings`

3. **Collect static files**:
   ```bash
   python manage.py collectstatic
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

### Production Configuration Files

The project includes configuration files for multiple platforms:
- `railway.json` - Railway deployment
- `vercel.json` - Vercel deployment  
- `render.yaml` - Render deployment
- `production_settings.py` - Production Django settings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 API Endpoints

### Main URLs
- `/` - Home page with file listings
- `/post/new/` - Upload new file
- `/post/<id>/` - View file details
- `/post/<id>/update/` - Edit file
- `/post/<id>/delete/` - Delete file
- `/users/search/` - Search for users
- `/share-file/<id>/` - Share file with users
- `/user/<username>/` - View user's public files

### Authentication URLs
- `/register/` - User registration
- `/login/` - User login
- `/logout/` - User logout
- `/profile/` - User profile management

## 🛠️ Technologies Used

- **Backend**: Django 5.2.4, Python 3.13
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Forms**: Django Crispy Forms with Bootstrap 5
- **File Handling**: Pillow for image processing
- **Authentication**: Django's built-in authentication system

## 📊 Features in Detail

### File Upload System
- **Drag & Drop**: Modern file upload interface
- **File Validation**: Type and size restrictions
- **Progress Indicators**: Real-time upload progress
- **Multiple File Types**: Support for images, documents, videos, audio

### User Management
- **Profile System**: Customizable user profiles with pictures
- **User Search**: Find and connect with other users
- **Privacy Controls**: Manage file visibility and sharing

### File Sharing
- **Granular Permissions**: Share with specific users or make public
- **Share Management**: Track who has access to your files
- **Download Tracking**: Monitor file download statistics

## 🐛 Troubleshooting

### Common Issues

1. **Static files not loading**
   ```bash
   python manage.py collectstatic
   ```

2. **Database issues**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Permission errors on uploaded files**
   - Check media folder permissions
   - Ensure Django has write access to media directory

4. **Bootstrap/CSS not working**
   - Verify crispy forms installation
   - Check STATIC_URL and STATICFILES_DIRS settings

## 🎓 Original Assignment

This project was originally created as an assignment for an internship with the following requirements:

### Part 1:
1. Create a web-app where a user can login
2. User can upload files
3. User can view his/her uploaded files

### Part 2:
1. User can search and view profile of other users
2. They can share their uploaded files with any of those users
3. Users can see the shared files by other users also in uploaded files

### Additional Features:
1. In users profile user can set his/her profile picture
2. Users can download other users uploaded files
3. The user can upload any type of files such as images, videos, text files and different types of programs

All requirements have been implemented and enhanced with modern UI/UX design.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap team for the UI components
- Contributors who helped improve this project

## 📸 Screenshots

### Application Screenshots
The application includes the following key screens:

*Note: Screenshots are available in the `Screenshots/` directory showing the modern Bootstrap 5 interface with responsive design.*

---

**⭐ If you found this project helpful, please consider giving it a star!**

