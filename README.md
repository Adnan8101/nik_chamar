# Personal Journal System

A simple, secure Flask web application for personal journaling with rich text editing capabilities.

## Project Team
**ST AIML-B**
- Ayush Kumawat (12)
- Nikita Mishra (24)  
- Satyam Mishra (25)

## Features

- **Password Protection**: Single password (1310) to access the application
- **Rich Text Editor**: Write entries with advanced formatting using Quill.js
- **CRUD Operations**: Create, Read, Update, Delete journal entries
- **Search Functionality**: Search through your entries
- **Clean Preview**: Smart content cleaning removes HTML and session tokens
- **Responsive Design**: Modern UI using TailwindCSS
- **Simple & Secure**: Single-user system with CSRF protection

## Recent Fixes (September 2025)

✅ **CSRF Token Issue**: Fixed delete functionality with proper CSRF tokens  
✅ **Content Cleaning**: Removed HTML tags and session tokens from previews  
✅ **Dashboard Design**: Improved layout with better styling and card design  
✅ **Copyright Update**: Updated to 2025  
✅ **File Cleanup**: Removed unused directories and files  
✅ **Enhanced Formatting**: Better rich text display and editing  

## Setup Instructions

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python run.py
   ```

3. **Access the Application**
   - Open http://127.0.0.1:5000 in your browser
   - Enter password: `1310`
   - Start journaling!

## Project Structure

```
nic-py/
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── models.py            # Database models
│   ├── forms.py             # WTForms
│   ├── routes.py            # Application routes
│   └── templates/           # HTML templates
│       ├── base.html        # Base template
│       ├── access.html      # Password access page
│       ├── dashboard.html   # Main dashboard
│       ├── create_entry.html# Create new entry
│       ├── view_entry.html  # View entry
│       └── edit_entry.html  # Edit entry
├── config.py                # Configuration
├── requirements.txt         # Dependencies
├── run.py                   # Application entry point
└── README.md               # This file
```

## Technology Stack

- **Backend**: Flask 3.0.3, SQLAlchemy 3.1.1, WTForms 3.1.2
- **Frontend**: HTML5, TailwindCSS, JavaScript
- **Rich Text Editor**: Quill.js with enhanced toolbar
- **Database**: SQLite
- **Icons**: Font Awesome

## Usage

1. **Access**: Enter password `1310` on the home page
2. **Create**: Click "New Entry" to write a journal entry with rich formatting
3. **View**: Click on any entry title to read the full content
4. **Edit**: Use the edit button to modify existing entries
5. **Delete**: Remove entries you no longer need (now working properly!)
6. **Search**: Use the search bar to find specific entries
7. **Logout**: Click logout to return to password screen

## Database Schema

### JournalEntry
- `id`: Primary key
- `title`: Entry title (max 200 chars)
- `content`: Entry content (rich HTML)
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

## Security Features

- CSRF protection on all forms (fixed!)
- Session-based access control
- Password protection for application access
- Input validation and sanitization
- Content cleaning for safe display

## Rich Text Features

- **Headers**: H1, H2, H3 for content organization
- **Text Formatting**: Bold, italic, underline, strikethrough
- **Lists**: Ordered and unordered lists
- **Quotes**: Styled blockquotes
- **Code**: Inline code and code blocks
- **Colors**: Text and background colors
- **Alignment**: Text alignment options
- **Links**: Clickable hyperlinks

---

**Note**: This is a simple personal journal system designed for single-user local use. All major issues have been resolved as of September 2025.
