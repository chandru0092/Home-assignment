# 1. About this repository

This repo has script for message management like POST, GET and DELETE message from the application

clone repo : git clone {repositary URL}

# 2. Prerequisites

	* Install any one IDE for Python(Visual studio code, PyCharm)
		* Link for Visual Studio Code(Python extensions needs to install separetly)
	  		https://code.visualstudio.com/docs/?dv=win64user
		* Link for Pycharm Installation
			https://www.jetbrains.com/help/pycharm/installation-guide.html#toolbox

	* Install pip from below link
	  	https://phoenixnap.com/kb/install-pip-windows

	* Install python 3.X
	  	https://www.python.org/downloads/

	* Install required modules of the application
		pip install flask==1.1.2
		pip install flask-restplus
		pip install Werkzeug==1.0.1
		pip install redis

# 3. Module/Library Explanations

	Python:
	=======
		Python is general programming language and Downloading and Installing Python is free and easy.

	Flask:
	======
		Flask is a popular web framework , meaning it is a third party python Library used for developing web applications and API’s.
	
	Flask Rest Plus and Werkzeug:
	=============================
		Flask-RESTPlus and Werkzeug is an extension for Flask which encourages best practices with minimal setup. It provides a collection of decorators and tools to describe API and expose its documentation using Swagger. 
	
	Redis:
	=======
		Redis is python client database and stores value in key-value format.

# 4. Files

	start_app.py   ----->  Start app file will start the application with host URL and Port .
	app_helper     ----->  Start app file will use the methods or functions from this file .
	redis_helper   ----->  Here we have functions and methods to store the values or messages in redis engine.
	request_models ----->  This file has all the request models of API 
				* what are the request parameters 
				* what type of parameter it is like string, list and dropdown
	message_namespace -->  This file has Response and API models
				* what are the response parameters and status codes of API
	test_message_application ---> This file performs unit testing of application API .
	Dockerfile 		----->  Dockerfile of application with all installation commands


# 5. Application Details (How to start the applciation)

	After installed all the pre requistes, you can start the application with below command

	---python start_app.py

	Once started the application , you will see below output

	PS C:\QlikAssignment> python .\start_app.py
		* Serving Flask app "start_app" (lazy loading)
		* Environment: production
		WARNING: This is a development server. Do not use it in a production deployment.
		Use a production WSGI server instead.
		* Debug mode: on
		* Restarting with stat
		* Debugger is active!
		* Debugger PIN: 271-357-746
		* Running on http://127.0.0.1:5002/ (Press CTRL+C to quit)
	
	**Application URL : http://127.0.0.1:5002/**

	HTTP Methods:
	=============
	* GET - (Retrieve) Get the data from the redis server in encrypted form.
	* POST - (Create) Used to send data in encrypted format to redis server.
	* DELETE - Delete all current represendations of target resource.
