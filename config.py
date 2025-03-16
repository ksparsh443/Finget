import os


class Config:
    API_KEY = os.getenv("API_KEY", "your_default_key")
