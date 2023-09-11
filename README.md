# A RESTful api for a social media app built with FastAPI

#### This API  has 4 routes

## 1) Post route

#### This route is reponsible for creating post, deleting post, updating post and Checking post

## 2) Users route

#### This route is about creating users and searching user by id

## 3) Auth route

#### This route is about login system

## 4) Vote route

 #### This route is about likes or vote system (like and disslike)

# how to run locally
First clone this repo by using following command
````

git clone https://github.com/StefanVodilovski/fastAPI.git

````
then 
````

cd fastapi-course

````

Then install fastapp using all flag like 

````

pip install fastapi[all]

````

Then go this repo folder in your local computer run follwoing command
````

uvicorn main:app --reload

````

Then you can use following link to use the  API

````

http://127.0.0.1:8000/docs 

````
## After you run this API you need a relational database (in this repo it's built with mysql, you can build it with postgres or sqlite)

Create a database in then create a file name .env and write the following things in you file 
````
DATABASE_HOSTNAME = 
DATABASE_PORT = 
DATABASE_PASSWORD = 
DATABASE_NAME = 
DATABASE_USERNAME = 
SECRET_KEY = 
ALGORITHM = 
ACCESS_TOKEN_EXPIRE_MINUTES =

````
where each field should have your custom values from the database and oauth2 key and algorithm.
