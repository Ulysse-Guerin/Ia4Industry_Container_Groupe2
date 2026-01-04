# TP3 – Development Stack with Docker

#Members: Ulysse Guérin, Titouan Gabagnou, Paul de Haro, Marc Antoine Orecchioni

## Description
This project provides a Docker-based development stack to evaluate and plot
the Riemann zeta function for complex arguments.  
The environment is fully containerized and reproducible.

The project includes:
- `code1.py`: computes ζ(1/2 + it) on [0,30], plots the real and imaginary parts, counts zero crossings.
- `code2.py`: additional experiments or code (user-defined).

## Requirements
- Docker
- Docker Compose

## Project Structure

- `code/` contains the Python scripts: code1.py, code2.py  
- `dev-stack/` contains supporting files for development  
- `docker-compose.yml` orchestrates the container  
- `Dockerfile.dev` defines the development image

## Installation & Running

### 1. Build and start the container
docker-compose build
docker-compose up -d



### 2. Execute code
code1.py is a python script directly written on the terminal, to run it you have two possibilities:
python3 code1.py 
Or : 
docker-compose exec dev python code1.py (Note: for this command, you must be in folder code. Furthermore, it won't show graph as docker has no visual interface)


code2.py is a python script you can only modify through Jupyter, to access it :

### 2.1 Access JupyterLab
From your host machine, run:
docker-compose up -d

Then get the access URL and token with:
docker logs dev-environment | grep token

Open the URL in your browser (use the 127.0.0.1:8888 link) to access JupyterLab. 
All files in the code  directory, including code1.py, code2.py, and any new scripts you create, will be visible in the same environment



### 3. Stop environment

To stop the container:
docker-compose down


Or:
docker-compose up -d
This stops the container and cleans up any running instances of JupyterLab. You can restart it anytime with:

### 4.Notes 
The composed image is roughly 7.2GB
