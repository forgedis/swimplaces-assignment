FROM python:3.11.4

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /src

COPY requirements.txt /src/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /src/

EXPOSE 8000

ENV DJANGO_DEBUG True
ENV DJANGO_SETTINGS_MODULE swimmingplaces.settings

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]