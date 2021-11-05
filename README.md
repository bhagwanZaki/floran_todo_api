# Floran Todo ReactDj App
<p align="center" width="100%">
    <img src="https://github.com/bhagwanZaki/react-dj-todo/blob/main/assests/logo.png"> 
</p>

## Intoduction 

Floran todo is todo app that will help you to manage your daily tasks and give you a graphical representation of task completed every day.
<br> This app uses React for it frontend and Django Rest API for backend purposes. Currently the SQLite is used as the database but once the app is ready to deploy database will be shifted to PostgreSQl

## Feature Available 

<ul>
    <li>  Graphical Represetation of task completed per day
    <li>User Registration
    <li> Add/Delete/Complete Todo
   
</ul>

## Pictures

<p align="center" width="100%">
    <h2> Welcome Page </h2>
    <img src="https://github.com/bhagwanZaki/react-dj-todo/blob/main/assests/main%20page.png"> 
    <h2> Mainpage </h2>
    <img src="https://github.com/bhagwanZaki/react-dj-todo/blob/main/assests/dashboard.png"> 
</p>


## Requirement 

Python v.3.8+
<br>Node.JS 

## Usuage

### Clone Repository

Copy Paste the following commands to clone the repo

```bash
    git clone https://github.com/bhagwanZaki/react-dj-todo.git
```
Go inside the directory and install the module from requirements.txt

```bash
  pip install -r requirements.txt
 ```
 
 Then make the migrations and then migrate the database
 
 ```bash
    python manage.py makemigrations
    python manage.py migrate
  ```
  
  Create the superuser 
  
  ```bash
    python manage.py createsuperuser
  ```
  
  Now run the django server
  
  ```bash
    python manage.py runserver
  ````
  
  <h3>Now Open the new terminal or CMD and then direct to frontend folder inside the clone directory</h3>
  
  Now Run the script
  
  ```bash
    npm run dev
  ```
  
  <h2>Now you goto localhost:8000 to see the website</h2>
  
  ```bash
      http://127.0.0.1:8000/
  ```
  
