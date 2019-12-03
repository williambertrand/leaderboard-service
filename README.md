# Starter API
Starter Flask API

## Getting Started

run `scripts/install-dependencies.sh`

run `scripts/run.sh` to run Flask app locally on port 5000

To run with gunicorn: `gunicorn -b localhost:8000 -w 4 tob_app:app` 

## Endpoints

/users

## ADDING MODELS: NOTE

When adding models, you must import the models to the main top_app.py file or else the migration script 
won't pick up the changes for the next generated migration


## CI /CD 
[ ] TODO

## Deploying
- This section depending on your deployment... 



## DB Starting from Scratch
Using Flask-Migrate

`flask db init` > This will create the migrations directory

## Making changes to the database

> To generate a migration automatically, Alembic compares the database schema as defined by the database models, against the actual database schema currently used in the database. It then populates the migration script with the changes necessary to make the database schema match the application models.

After editing the model files, run:

`flask db migrate` (with -m message parameter) to generate the migration script.

Then run the migration script with `flask db upgrade`