# О проекте

Тестовое задание: 

Разработать Django REST API, который позволяет загружать файлы на сервер, а затем асинхронно обрабатывать их с использованием Celery.


## Используемые технологии:
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [DRF](https://www.django-rest-framework.org/)
- [RabbitMQ](https://www.rabbitmq.com/)


## Используемые версии библиотек:

- Django==4.2.7
- djangorestframework==3.14.0
- celery==5.3.5
- pika==1.3.2


## Инструкция по использованию
### Клонирование репозитория:
```
$ git clone https://github.com/MaximChernyakhovich/Django-File-Flow.git
```
### Инструкция по запуску:
```
$ cd Django-File-Flow
$ python manage.py makemigrations
$ python manage.py migrate
$ docker build -t django-file-flow:latest .
$ docker-compose up
```

## Примеры использования:

### Загрузка файла:

```
$ curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/path/to/file/file.file" http://localhost:8000/api/file-upload/
```


### Получение списка загруженных файлов:

```
$ curl -X GET http://localhost:8000/api/files/
```