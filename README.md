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
    
    cd wishlist-magalu
    
    cp contrib/env-sample .env
    
    docker compose up 


Open your web browser and navigate to http://localhost:8000/api/docs/schema/ui to access the api documentation

# How to run the project without docker
If you wish you can run the project without docker

  <sub>steps: </sub>
    
    # Installing poetry
    pip install poetry
    
    #  Creating virtualenv and Installing dependencies 
    poetry install
    
    # Activating virtual environment
    poetry shell
    
    # Creating .env file, using windows just copy contrib/env-sample and past as .env
    cp contrib/env-sample .env


