# Postly - A Modern Blog Platform

Postly is a robust Django-based web application that provides a modern blogging platform with comprehensive user authentication and management features.

## Features

- **User Authentication System**

  - Email-based authentication
  - User registration and login
  - Password reset functionality
  - Password change capability
  - User profile management

- **Security Features**

  - CSRF protection
  - XSS filtering
  - Content Security Policy
  - Secure cookie handling
  - Protection against clickjacking

- **User Interface**
  - Clean and responsive design using Bootstrap
  - Intuitive navigation
  - User-friendly forms with validation
  - Flash messages for user feedback

## Technology Stack

- **Backend**: Django 5.1
- **Database**: MySQL
- **Frontend**: Bootstrap 5
- **Languages**: Python, HTML, CSS, JavaScript

## Prerequisites

- Python 3.12 or higher
- MySQL 5.7 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/abenable/postly
   cd postly
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install django mysqlclient
   ```

4. Configure the database:

   - Create a MySQL database named 'postly'
   - Update the database configuration in `postly/settings.py` if needed

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://localhost:8000`

## Project Structure

```
postly/
├── blog/                  # Blog application
├── user/                  # User management application
├── static/               # Static files (CSS, JS, images)
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   └── user/            # User-related templates
├── postly/              # Project configuration
└── manage.py            # Django management script
```

## Development

- **Static Files**: Place your CSS files in `static/css/`
- **Templates**: Add new templates in the `templates/` directory
- **Database Models**: Define models in the respective app's `models.py`

## Security Configuration

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure proper `ALLOWED_HOSTS`
3. Set up proper email backend configuration
4. Enable HTTPS-related security settings
5. Update `SECRET_KEY` with a secure value

## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
