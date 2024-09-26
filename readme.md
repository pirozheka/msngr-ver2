## Чтобы открыть проект: 

git clone https://github.com/pirozheka/msngr-ver2.git

## Создание виртуального окружения

python -m venv venv

## Активация виртуального окружения (Windows)

venv\scripts\activate

## Переход в папку с проектом 

cd msngr-ver2

## Установка зависимостей

pip install -r requirements.txt

## В отдельном терминале! - Запуск Redis в Docker (необходимо для обмена сообщениями)

docker run --rm -p 6379:6379 redis:7

## Открыть папку и применить миграции БД
cd messenger
python manage.py makemigrations
python manage.py migrate

## Запустить сервер
python manage.py runserver

