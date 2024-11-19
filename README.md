# wishlist-magalu

#### This project provides a ready-to-run Django application using Docker Compose. Here's a step-by-step guide to get you up and running:
 
# Prerequisites
    
    Python installed: https://www.python.org/downloads/
    Docker installed: https://docs.docker.com/engine/install/
    Docker Compose installed: https://docs.docker.com/compose/install/
    A code editor or IDE of your choice


# Getting Started 
Download the project and run it using docker
    
    # Cloning the Repository
    git clone https://github.com/heltonteixeira92/wishlist-magalu.git
    
    # Go to Repository directory
    cd wishlist-magalu
    
    # Coping .env to the project directory
    cp contrib/env-sample .env
    
    # Running the project, attach -d to run in background
    docker compose up 


Open your web browser and navigate to http://localhost:8000/api/docs/schema/ui to access the api documentation

# How to run the project without docker
If you wish you can run the project without docker

  <sub>steps: </sub>
    
    # Installing poetry
    pip install poetry
    
    # Creating virtualenv and Installing dependencies 
    poetry install
    
    # Activating virtual environment
    poetry shell
    
    # Coping .env file, using windows just copy contrib/env-sample and past as .env
    cp contrib/env-sample .env
    
    # Change db variable settings with information from your local postgres
    DATABASE_URL=postgres://postgres:postgres@localhost/postgres

    # Appling migrations
    python manage.py migrate

    # Running project
    python manage.py runserver


## Examples using the requests library

Creating user for authentication
```python
import requests
payload = {'name': 'Myuser', 'email': 'myuser@test.com', 'password': '123@mudar'}
requests.post('http://localhost:8000/api/register/', data=payload)
```

Authenticating to obtain access token
```python
payload = {'email': 'myuser@test.com', 'password': '123@mudar'}
resp = requests.post('http://localhost:8000/api/token/', data=payload)
access_token = resp.json()['access']
```

Creating customer
```python
headers = {'Authorization': f'Bearer {access_token}'}
payload = {'name': 'Matilde Cunha', 'email': 'matildecunha@test.com'}
requests.post('http://localhost:8000/api/customers/', data=payload, headers=headers)
```

Creating product, to send image file add content_type='multipart/form-data'
```python
headers = {'Authorization': f'Bearer {access_token}'}
payload = {'title': 'Televisão 48', 'brand': 'Samsung', 'price': 899.90}
requests.post('http://localhost:8000/api/products/', data=payload, headers=headers)
```

Creating wishlist
```python
headers = {'Authorization': f'Bearer {access_token}'}
payload = {'product': 1, 'customer': 1}
requests.post('http://localhost:8000/api/wishlists/', data=payload, headers=headers)
```

Listing wishlist by customer
```python
headers = {'Authorization': f'Bearer {access_token}'}
requests.get('http://localhost:8000/api/wishlists/?customer=1', headers=headers)
```

for more see the api schema: http://localhost:8000/api/docs/schema/ui