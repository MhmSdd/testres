import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///learnhub.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_SAMESITE= 'Lax'
    SESSION_COOKIE_SECURE= False 
    SECRET_KEY = 'X7b9kL2mQz8pWvT3rYcN5jF0hG4iA9oD_eBxU6nM'
    LANGUAGES = {
        'en': 'English',
        'ar': 'العربية'
    }

    BABEL_DEFAULT_LOCALE = 'en'

