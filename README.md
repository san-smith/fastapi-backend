# Backend

## Создание образа

Для создания докер-образа выполните:

`docker build -t my_image .`

Здесь `my_image` - имя образа.

## Запуск и остановка контейнера

Для создания и запуска контейнера выполните:

`docker run -d -p 8000:8000 my_container my_image`

Для остановки контейнера выполните:

`docker stop my_container`
