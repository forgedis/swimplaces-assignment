# Install requirements

## pip install

Follow this guide:
https://pip.pypa.io/en/stable/installation/

### Windows users:

    py -m pip install --upgrade pip

    py -m pip install Django
    py -m pip install djangorestframework
    py -m pip install psycopg2
    py -m pip install geopy

# Run the swimplaces

    docker-compose up --build

# Inside the docker console

    python manage.py makemigrations
    python manage.py migrate
    python manage.py import_csv swimplaces_export.csv

# Open the webapp on the following URL

    http://localhost:8000/
