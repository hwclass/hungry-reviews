# hungry-reviews
An experimental coding adventure with Python, Node and ReThinkDB. 

###Technical Spec
* [Python3](www.python.org) / as backend lang
* [Flask](flask.pocoo.org) / as server-side service provider

###Setup

####Update Homebrew

```javascript
brew doctor
brew update
```

####Check if you have installed Python3

```javascript
brew install python3
```

####Create a virtual environment then activate it

```javascript
virtualenv --no-site-packages env
source env/bin/activate
```

####Install Flask with pip3

```javascript
pip3 install flask
pip3 install flask-wtf
```

####Set the requirements

```javascript
pip freeze > requirements.txt
```

####Run the application

```javascript
python3 run.py
```

####Open the browser and hit localhost://5000

```javascript
python3 run.py
```

####You can check the grouped data after completed by hitting the following:

```javascript
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://localhost:5000/api/v.0/reviews
```


