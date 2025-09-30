import os

class Config:
    SECRET_KEY = 'simple-journal-secret-key-1310'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///journal.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    
    # Application specific settings
    ACCESS_PASSWORD = '1310'  # Password to access the application
