# Personal Journal System - Desktop GUI Application

A simple, secure desktop GUI application for personal journaling built with Python tkinter.

## Project Team
**ST AIML-B**
- Ayush Kumawat (12)
- Nikita Mishra (24)  
- Satyam Mishra (25)

## Features

- **Password Protection**: Single password (1310) to access the application
- **Desktop GUI**: Clean, modern interface using tkinter
- **CRUD Operations**: Create, Read, Update, Delete journal entries
- **Search Functionality**: Search through your entries
- **Clean Text Display**: Smart content cleaning removes HTML and unwanted tokens
- **SQLite Database**: Local database storage
- **Responsive Layout**: Scrollable entries list with modern card design

## Recent Changes (October 2025)

✅ **Converted to Desktop GUI**: Removed Flask web interface, now uses tkinter  
✅ **SQLite Database**: Direct SQLite integration without ORM  
✅ **Simplified Dependencies**: Only uses Python standard library modules  
✅ **Modern GUI Design**: Clean, modern interface with proper styling  
✅ **Same Core Functionality**: All CRUD operations preserved  
✅ **Password Protection**: Same 1310 password access system  

## Setup Instructions

1. **No Dependencies Required**: Uses only Python standard library
   ```bash
   # tkinter, sqlite3, datetime, re, os are all built-in
   ```

2. **Run the Application**
   ```bash
   python run.py
   ```
   Or directly:
   ```bash
   python journal_gui.py
   ```

3. **Access the Application**
   - Enter password: `1310`
   - Start journaling in the desktop app!

## Project Structure

```
nic-py/
├── database.py              # Database operations class
├── journal_gui.py           # Main GUI application
├── run.py                   # Application entry point
├── requirements.txt         # Dependencies (standard library only)
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## Technology Stack

- **GUI Framework**: Python tkinter
- **Database**: SQLite3 (built-in)
- **Language**: Python 3.x
- **Styling**: Custom tkinter themes and colors

## GUI Features

### **Main Dashboard**
- Clean, modern interface with card-based entry display
- Search functionality with real-time filtering
- Entry statistics (total count)
- Scrollable entries list
- Preview of entry content (first 150 characters)

### **Entry Management**
- **Create**: Full-screen form with title and content fields
- **View**: Dedicated view window with formatted display
- **Edit**: Edit existing entries in popup window
- **Delete**: Confirmation dialog before deletion

### **Design Elements**
- **Modern Colors**: Professional blue/gray color scheme
- **Typography**: Inter font family for clean readability
- **Interactive Elements**: Hover effects and proper cursor styles
- **Responsive Layout**: Proper window sizing and scrolling

## Usage

1. **Launch**: Run `python run.py`
2. **Access**: Enter password `1310`
3. **Create**: Click "New Entry" to write a journal entry
4. **View**: Click on entry titles or "View" button to read full content
5. **Edit**: Use "Edit" button to modify existing entries
6. **Delete**: Use "Delete" button with confirmation dialog
7. **Search**: Type in search box to filter entries
8. **Logout**: Click "Logout" to return to password screen

## Database Schema

### **journal_entries** table:
- `id`: INTEGER PRIMARY KEY AUTOINCREMENT
- `title`: TEXT NOT NULL (entry title)
- `content`: TEXT NOT NULL (entry content)
- `created_at`: TIMESTAMP (creation time)
- `updated_at`: TIMESTAMP (last update time)

## Security Features

- Password protection for application access
- Local SQLite database (no network access)
- Input validation and sanitization
- Confirmation dialogs for destructive operations

## GUI Windows

1. **Access Window**: Password entry with modern design
2. **Main Dashboard**: Entry list with search and stats
3. **Create/Edit Form**: Popup window for entry management
4. **View Window**: Full entry display with action buttons

## Advantages of GUI Version

✅ **No Web Dependencies**: No Flask, no web server required  
✅ **Faster Performance**: Direct desktop application  
✅ **Better User Experience**: Native desktop interface  
✅ **Offline First**: No internet connection needed  
✅ **Simpler Setup**: Just run the Python file  
✅ **Modern Design**: Clean, professional interface  

---

**Note**: This is a desktop GUI version of the personal journal system. All core functionality has been preserved while providing a better user experience through a native desktop interface.
