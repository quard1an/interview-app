FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get update \
&& apt-get -y install libpq-dev gcc 
RUN pip install -r requirements.txt

COPY . .

RUN python3 interview_app/manage.py test

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "interview_app.wsgi"]
