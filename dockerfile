FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN chmod 755 /app

EXPOSE 8000

ENV NAME World

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
