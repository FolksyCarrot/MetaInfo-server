![metaInfo](https://user-images.githubusercontent.com/86749126/146261527-4f0eb8d8-73e2-46ac-b07c-e02b9cde7117.png)

# Meta-Info Platform API

Meta-Info is an application with project managers and financial decision makers in mind. This App allows you to keep track of your projects, your employees, your customers, and the costs involved with them. 
## Local Setup

1. Clone this repository and change to the directory in the terminal.
2. Run `pipenv shell`
3. Run `pipenv install`
4. Run migrations and make migrations
5. Seed database with python3 manage.py loaddata {table name}

## LoadData Order
1. users
2. tokens
3. stores
4. managers
5. customers
6. employees
7. store_employees
8. projects
9. costs
Now that your database is set up all you have to do is run the command:

```
python3 manage.py runserver
```

## Meta-Info ERD

Here is the ERD for the models in the api: https://dbdiagram.io/d/61a686bd8c901501c0da20b7

## Documentation

Register a new User then begin by adding projects, customers, and employees.
You can add/edit/delete costs associated with projects.
Everything else has create/edit capabilities.
