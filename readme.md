## Чтобы открыть проект: 

git clone https://github.com/pirozheka/msngr-ver2.git

## Создание виртуального окружения

python -m venv venv

## Активация виртуального окружения (Windows)

venv\scripts\activate

## Установка зависимостей

pip install -r requirements.txt

## Запуск Redis в Docker (необходимо для обмена сообщениями)

docker run --rm -p 6379:6379 redis:7

## Открыть в соседнем терминале и запустить сервер

python manage.py runserver

