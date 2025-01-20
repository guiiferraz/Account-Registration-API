# Account Registration API


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=2f9fe3)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Dbeaver](https://img.shields.io/badge/dbeaver-382923?style=for-the-badge&logo=dbeaver&logoColor=white)


## About AR API

The AR API is a simple but well-structured application with the aim of managing and registering accounts from a base, such as Excel, to the database. 
Following the REST structuring model of an API and the HTTP request models .

This AR API has some practical features, such as:

* List all accounts registered in the currently database .
* Filter a search by the corresponding account name .
* Register multiple accounts automatically from a base like Excel .
* Register a single account in a practical way .
* Update any data or an account using your id .
* Delete an account also by its respective id that is no longer necessary .

The application was developed mainly using the Python language, However, it also uses resources from some libraries, for example:
The FastApi library, SQLAlchemy, Pandas and Pytest .  
For external tools, Docker was used to create a container and virtualize the Postgres database .  

The decision to create this API is due to the fact that i wanted to present a solution to a real market problem, in terms of efficiency, scalability
and reduction of human errors. Resulting in an optimization of the internal resources of a company that decides to use this API or rely on it, allowing
focus on other areas .  

## Getting started

### Prerequisites

First of all, you will need some prerequisites:  

* Git 2
* Python 3.13.0
* VSCode
* Docker
* Dbeaver

### Clonning

How to clone the AR API 
```
git clone <url do repositorio gui>
```

### Config .env variables

Open the project with vscode and create a .env file . Then, configure your variables like this for Postgres setup:  

```
USERNAME = {username}
PASSWORD = {your_password}
HOST = 'localhost'
PORT = 5432
DB_NAME = {database_name}
```

After, configure this variables for Docker running:  

```
POSTGRES_USER = {username}
POSTGRES_PASSWORD = {your_password}
POSTGRES_DB = {database_name}
```

### Docker 

Now open your terminal at the project path and run this code to create a docker container:

```
docker-compose up
```

To check if docker is runnig, try this command code:

```
docker-compose ps
```

### Libraries

Create your virtual environment and activate it with: 
```
python -m venv venv

venv/Scripts/activate
```
Now for the libraries, on your terminal use:
```
pip install -r requirements.txt
```

### Starting
How to start the AR API:
```
cd path/where/is/the/api/
cd ../src
python app.py
```
With your browser or Postman, now you can use the API endpoints .

## API Endpoints

Here, are the list with the main routes of AR API and what are their expected request bodies .​  

| route  | description |
| ------------- | ------------- |
| GET /accounts  | Returns a list of all accounts in the database  |
| GET /accounts/{name}  | Returns a list with the respective account in the database  |
| POST /accounts/register | Returns a success message when registering accounts in the database | 
| POST /accounts/register/new | Returns the request body that was registered |
| PUT /accounts/update/{id_account} | Returns the request body that was updated in the database |
| DEL /accounts/delete/{id_account} | returns a success message when deleting the respective account |

## Collaborators
Special thank you for all people that contributed for this project .

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/175043500?s=400&u=170ce2d530ce4f624358b4636761422b92b3a620&v=4" width="100px;" alt="Guilherme Ferraz Profile Picture"/><br>
        <sub>
          <b>Guilherme Ferraz</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://t.ctcdn.com.br/n7eZ74KAcU3iYwnQ89-ul9txVxc=/400x400/smart/filters:format(webp)/i490769.jpeg" width="100px;" alt="Elon Musk Picture"/><br>
        <sub>
          <b>Elon Musk</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://miro.medium.com/max/360/0*1SkS3mSorArvY9kS.jpg" width="100px;" alt="Foto do Steve Jobs"/><br>
        <sub>
          <b>Steve Jobs</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/110428601?v=4" width="100px;" alt="Marco Antonio Profile Picture"/><br>
        <sub>
          <b>Marco Antonio</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
