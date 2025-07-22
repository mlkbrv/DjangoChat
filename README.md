# BlueChat - Modern Real-Time Chat Application

A modern, real-time chat application built with Django and WebSockets, featuring a beautiful WhatsApp-inspired interface with a blue color scheme.

![BlueChat Preview](https://img.shields.io/badge/BlueChat-Modern%20Chat%20App-blue?style=for-the-badge&logo=django)

## 🌟 Features

- **Real-time messaging** using WebSockets
- **Modern UI/UX** inspired by WhatsApp with blue theme
- **Responsive design** that works on all devices
- **Multiple chat rooms** for different conversations
- **Message history** with timestamps
- **User-friendly interface** with smooth animations
- **Auto-scroll** to latest messages
- **Message delivery indicators** (blue checkmarks)
- **Clean and intuitive** navigation

## 🚀 Tech Stack

- **Backend**: Django 5.2.4
- **Real-time Communication**: Django Channels
- **Database**: SQLite (easily configurable for PostgreSQL/MySQL)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Tailwind CSS
- **Icons**: Font Awesome
- **WebSocket**: ASGI with Daphne

## 📋 Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- Git

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd DjangoChat
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   
   **On Windows:**
   ```bash
   .venv\Scripts\activate
   ```
   
   **On macOS/Linux:**
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Open your browser and navigate to**
   ```
   http://127.0.0.1:8000/
   ```

## 📁 Project Structure

```
DjangoChat/
├── DjangoChat/                 # Main Django project settings
│   ├── __init__.py
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   ├── asgi.py               # ASGI configuration for WebSockets
│   └── wsgi.py               # WSGI configuration
├── chatapp/                   # Main chat application
│   ├── __init__.py
│   ├── models.py             # Database models
│   ├── views.py              # View functions
│   ├── consumers.py          # WebSocket consumers
│   ├── routing.py            # WebSocket routing
│   ├── urls.py               # App URL configuration
│   ├── admin.py              # Django admin configuration
│   └── templates/
│       └── chatapp/
│           ├── base.html     # Base template
│           ├── index.html    # Home page
│           └── room.html     # Chat room page
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
└── README.md                # This file
```

## 🗄️ Database Models

### ChatRoom
- `name`: Room name (CharField)
- `slug`: URL-friendly identifier (SlugField)

### ChatMessage
- `user`: Foreign key to User model
- `room`: Foreign key to ChatRoom
- `message_content`: Message text (TextField)
- `date`: Timestamp (DateTimeField, auto_now_add=True)

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Database Configuration
The application uses SQLite by default. To use PostgreSQL or MySQL, update the `DATABASES` setting in `settings.py`.

## 🎨 Customization

### Changing Colors
The application uses a blue color scheme. To customize colors:

1. **Primary Colors**: Update the gradient classes in `base.html`
2. **Message Bubbles**: Modify the `.message-bubble` CSS classes
3. **Buttons**: Update the gradient classes on buttons

### Adding New Features
- **File Uploads**: Extend the message input form
- **User Profiles**: Add user profile models and views
- **Message Reactions**: Add reaction functionality to messages
- **Voice Messages**: Integrate audio recording capabilities

## 🔌 API Endpoints

### WebSocket Endpoints
- `ws://localhost:8000/ws/{room_slug}/` - WebSocket connection for real-time messaging

### HTTP Endpoints
- `GET /` - Home page with chat rooms
- `GET /rooms/{slug}/` - Individual chat room
- `POST /rooms/{slug}/` - Send message to room

## 🚀 Deployment

### Using Heroku
1. Create a `Procfile`:
   ```
   web: daphne DjangoChat.asgi:application --port $PORT --bind 0.0.0.0
   ```

2. Add buildpacks:
   ```bash
   heroku buildpacks:add heroku/python
   heroku buildpacks:add heroku/nodejs
   ```

3. Deploy:
   ```bash
   git push heroku main
   ```

### Using Docker
1. Create a `Dockerfile`:
   ```dockerfile
   FROM python:3.9
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 8000
   CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
   ```

2. Build and run:
   ```bash
   docker build -t bluechat .
   docker run -p 8000:8000 bluechat
   ```

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Troubleshooting

### Common Issues

1. **WebSocket Connection Failed**
   - Ensure Django Channels is properly installed
   - Check that ASGI is configured correctly
   - Verify the channel layer settings

2. **Messages Not Appearing**
   - Check browser console for JavaScript errors
   - Verify WebSocket connection status
   - Ensure database migrations are applied

3. **Static Files Not Loading**
   - Run `python manage.py collectstatic`
   - Check static files configuration in settings

### Debug Mode
Enable debug mode in `settings.py`:
```python
DEBUG = True
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django team for the amazing framework
- Django Channels for WebSocket support
- Tailwind CSS for the utility-first CSS framework
- Font Awesome for the beautiful icons
- WhatsApp for the UI/UX inspiration

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/DjangoChat/issues) page
2. Create a new issue with detailed information
3. Contact the maintainers

---

**Made with ❤️ and ☕ by the BlueChat Team**

*Built for modern communication needs* 