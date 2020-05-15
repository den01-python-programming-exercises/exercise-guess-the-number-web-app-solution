# Exercise - Guess the number in a Flask web app

This exercise will explore how we can build the *guess a number* functionality into a web app using Python's Flask library. We won't worry about the mechanisms of creating the pages and we won't bother with any HTML, CSS or JavaScript. The exercise files will contain all the relevant files you need to get going and just implement the Python part.

### Getting started with Flask - Hello World

The most basic task we can achieve in Flask is the age-old "*Hello World!*" application. Here's how it looks:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

This code is contained inside this repository in the `src` folder and is called `hello_world_app.py`. To get and run the code, from a terminal run:

```plaintext
user@host:~$ git clone <your-repo-url-here>
user@host:~$ cd <your-repo-name>
user@host:~$ virtualenv flask_env
user@host:~$ source flask_env/bin/activate
user@host:~$ pip install flask
user@host:~$ cd src
user@host:~$ python3 hello_world_app
```

This will set up the virtual environments and assumes the following:

- [You have Python installed](https://scott3142.uk/python-programming/codelabs/getting-started/index.html)
- [YOu can activate a virtual environment](https://scott3142.uk/python-programming/codelabs/getting-started/index.html?index=..%2F..index#3)
- [You can install packages inside your virtual environment using pip](https://scott3142.uk/python-programming/codelabs/getting-started/index.html?index=..%2F..index#2)

This code outputs "Hello, World!" in a web browser on your computer's localhost port 5000 (i.e. at [http://localhost:5000](http://localhost:5000)). You can stop the web app running at any time by pressing Ctrl-C in the terminal.

### Building the app - loading the static files

The exercise template contains the following files:

```plaintext
.
+-- README.md
+-- tests/
|   +-- test_app.py
+-- src/
|   hello_world_app.py
|   web-app/
```

and the web-app folder (which is where we'll mostly be working) looks like this:

```plaintext
.
+-- web_app.py
+-- static/
|   +-- <web files we don't need to worry about>
+-- templates/
|   +-- splash.html
|   +-- holding.html
```

Let's take a look at `web_app.py`:

```python

```

**Note:** *There is no automatic testing for this exercise - you are responsible for writing and running your own tests!*
