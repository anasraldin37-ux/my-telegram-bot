"""
ملف الإعدادات الرئيسي للبوت
Configuration file for the Telegram bot
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Configuration
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
ADMIN_ID = os.getenv('ADMIN_ID')

# AI Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
AI_MODEL = os.getenv('AI_MODEL', 'openai')

# Database
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///bot_database.db')

# Server
PORT = int(os.getenv('PORT', 5000))
HOST = os.getenv('HOST', '0.0.0.0')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# GitHub
GITHUB_SECRET = os.getenv('GITHUB_SECRET', 'your_secret')

# Logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = os.getenv('LOG_FILE', 'logs/bot.log')

# Redis
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')

# Bot Settings
MAX_MESSAGE_LENGTH = 4096
CONVERSATION_TIMEOUT = 3600  # ساعة واحدة
MAX_CONVERSATION_HISTORY = 10  # آخر 10 رسائل

# AI Settings
AI_TEMPERATURE = 0.7
AI_MAX_TOKENS = 2000
SYSTEM_PROMPT_AR = """أنت مساعد ذكي متخصص في الإجابة على الأسئلة باللغة العربية.
تتمتع بمعرفة واسعة في:
- البرمجة وتطوير الويب
- إدارة قواعد البيانات
- تطوير تطبيقات الجوال
- الذكاء الاصطناعي وتعلم الآلة
- وغيرها من المواضيع التقنية والعامة

تجيب بأسلوب ودود واحترافي وتحاول أن تكون مفيداً قدر الإمكان."""

SYSTEM_PROMPT_EN = """You are a smart assistant specialized in answering questions in English.
You have extensive knowledge in:
- Programming and web development
- Database management
- Mobile app development
- Artificial Intelligence and Machine Learning
- And many other technical and general topics

You answer in a friendly and professional manner and try to be helpful as much as possible."""
