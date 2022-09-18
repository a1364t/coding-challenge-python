# What is this project?
 
This is a simple program (as a code challenge) that can filter JSON data and return new fields.

This project was deployed on Heroku: [Coding Challenge](https://nine-code-challenge123.herokuapp.com/)

## Usage

Just clone the code and use it. It is in pure python 3.
A request payload is posted to the API in JSON format. The JSON data include some fields and some nested dictionary fields. JSON data is filtered based on DRM enabled and episodeCount > 0. The returned JSON contains the following field from the request:

- image - corresponding to image/showImage from the request payload
- slug
- title

## How to run the code

- First, install virtual environment by this command:
``` 
$ pip install virtualenv
```
- Clone the project to your local machine.
```
$ git clone https://github.com/a1364t/coding-challenge-python
```
- Activate virtual env:
```
$ source env/bin/Activate
```
- Finally, install the required packages with the command below:
```
(env) $ pip install -r requirements.txt
```

- The only step needed is to run the server. At the root directory of the project run:
```
$ python manage.py runserver
```

## Challenge/bugs

Nested serializers were the main challenge in this project.
The season field is a list of one or more dictionaries. This field doesn't work properly in this project.
