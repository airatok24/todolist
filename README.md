1. Создать виртуальное окружение, активировать его и установить зависимости
virtualenv venv
source venv/Scripts/activate
pip install -r requirements.txt
2. Заполнить файл .env.example нужными данными
3. Создаем контейнеры требующиеся для работы программы
docker-compose up -d
В проекте уже настроенно подлючение к базе данных созданной через docker-compose