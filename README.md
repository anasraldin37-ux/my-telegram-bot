# Telegram GitHub Bot 🤖

بوت تليجرام متكامل لمراقبة تحديثات مستودعات GitHub وإعادة إرسال الرسائل (Echo Bot).

## المميزات ✨

- 📤 **استقبال تنبيهات GitHub**: يتلقى تحديثات من مستودعات GitHub عبر Webhooks
- 🚀 **عرض تحديثات الـ Push**: يعرض معلومات الـ Commits مع المطور والمستودع والرسالة
- 💬 **Echo Bot**: يعيد إرسال أي رسالة عادية يستقبلها
- 🎯 **أمر البداية**: يرحب بالمستخدمين الجدد

## المتطلبات 📋

- Python 3.8 أو أحدث
- حساب Telegram و Bot Token
- Ngrok أو خادم للـ Webhooks
- GitHub Repository مع Webhook Settings

## التثبيت 🔧

### 1. استنساخ المستودع
```bash
git clone https://github.com/anasraldin37-ux/my-telegram-bot.git
cd my-telegram-bot
```

### 2. إنشاء بيئة افتراضية
```bash
python -m venv venv
source venv/bin/activate  # على Linux/Mac
# أو
venv\Scripts\activate  # على Windows
```

### 3. تثبيت المكتبات المطلوبة
```bash
pip install -r requirements.txt
```

### 4. إنشاء ملف .env
أنشئ ملف `.env` في جذر المشروع:
```env
TELEGRAM_TOKEN=your_bot_token_here
CHAT_ID=your_chat_id_here
PORT=5000
```

## كيفية الحصول على التوكن والـ Chat ID 🔐

### الحصول على Telegram Bot Token
1. افتح Telegram وابحث عن `@BotFather`
2. أرسل `/newbot`
3. اتبع التعليمات وستحصل على Token

### الحصول على Chat ID
1. ابحث عن `@userinfobot`
2. أرسل أي رسالة
3. ستحصل على `User ID` (استخدمه كـ CHAT_ID)

## إعدادات GitHub Webhook ⚙️

1. اذهب إلى مستودعك على GitHub
2. اذهب إلى `Settings` > `Webhooks`
3. اضغط `Add webhook`
4. في `Payload URL` أدخل: `https://your-domain/webhook`
5. في `Content type` اختر `application/json`
6. في `Which events would you like to trigger this webhook?` اختر `Push events`
7. اضغط `Add webhook`

## التشغيل 🚀

```bash
python main.py
```

سيبدأ البوت في الاستماع للرسائل:
- اكتب `/start` للترحيب
- أرسل أي رسالة عادية وسيعيدها البوت
- أي تحديث Push من GitHub سيظهر كإشعار

## البنية 📁

```
my-telegram-bot/
├── main.py              # الملف الرئيسي
├── requirements.txt     # المكتبات المطلوبة
├── .env                 # متغيرات البيئة (لا تشارك هذا)
└── README.md            # هذا الملف
```

## الدوال الرئيسية 🔧

### `start()`
- تستجيب لأمر `/start`
- ترحب بالمستخدم

### `echo()`
- تعيد إرسال أي رسالة نصية عادية

### `github_webhook()`
- تستقبل تحديثات من GitHub
- تستخرج معلومات الـ Commit
- ترسل إشعار للـ Chat ID المحدد

## استكشاف الأخطاء 🐛

### البوت لا يرسل الإشعارات
- تأكد من أن `CHAT_ID` صحيح
- تأكد من تفعيل الـ Webhooks في GitHub
- تحقق من السجلات (Logs)

### خطأ في الاتصال بـ Telegram
- تأكد من صحة `TELEGRAM_TOKEN`
- تحقق من اتصالك بالإنترنت

### Webhook غير مستقبلة
- استخدم Ngrok للـ Local Testing: `ngrok http 5000`
- استخدم URL من Ngrok في GitHub Webhook

## المساهمة 🤝

يمكنك تحسين المشروع بـ:
- إضافة المزيد من أنواع الأحداث (Pull Requests, Issues, etc.)
- تحسين رسائل الإشعارات
- إضافة المزيد من الأوامر

## الترخيص 📄

هذا المشروع مفتوح المصدر ومتاح للجميع.

## المؤلف 👨‍💻

أنس الدين
