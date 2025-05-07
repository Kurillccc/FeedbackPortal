# FeedbackPortal

Django-приложение для сбора обращений от пользователей. Поддерживает текстовые сообщения и прикрепление файлов. Имеет админку для просмотра обращений.

## ✨ Функционал:

- Форма обратной связи с полями: сообщение, файл

- Загрузка файлов

-  Проверка валидности формы

- Админка с управлением обращениями

## 🤖 Стек:

- Python 3.12

- Django

- HTML / CSS

- SQLite

## 📸 Скриншоты

### 🏠 Главная страница
<img src="https://github.com/user-attachments/assets/30d65187-7647-43cc-98bc-a843e3cbb163" width="800"/>

### ✉️ Форма обратной связи
<img src="https://github.com/user-attachments/assets/dfdb5cf8-1b2c-4b98-bc35-67a88607b48a" width="800"/>

### ✅ После отправки
<img src="https://github.com/user-attachments/assets/c71dcd44-8ca9-4732-a9ac-024e478c5116" width="800"/>

### ⚙️ Админка
<img src="https://github.com/user-attachments/assets/649b3411-31bd-4731-b136-764738f5b1b3" width="800"/>

## ⚡ Инструкция по запуску:

1. Клонируем репозиторий

git clone https://github.com/Kurillccc/FeedbackPortal
cd feedback-portal

2. Создание и активация виртуального окружения

python3 -m venv .venv
source .venv/bin/activate  (или .venv\Scripts\activate на Windows)

3. Установка зависимостей

pip install -r requirements.txt

4. Применяем миграции

python manage.py migrate

5. Создаем суперпользователя (для админки)
python manage.py createsuperuser

6. Запуск сервера
python manage.py runserver
