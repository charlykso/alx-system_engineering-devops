# <center>Application server</center> 

## Background Context
Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.

## 0. Let’s serve what you built for [AirBnB clone v2 - Web framework](https://github.com/charlykso/AirBnB_clone_v2) on web-01. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

Requirements:

   * Make sure that task #3 of your [SSH project](https://github.com/charlykso/alx-system_engineering-devops/tree/master/0x0B-ssh) is completed for web-01. The checker will connect to your servers.
   * Git clone your AirBnB_clone_v2 on your web-01 server.
   * Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.
   * Your Flask application object must be named app (This will allow us to run and check your code).

## 1. Now that you have your development environment set up, let’s get your production application server set up with Gunicorn on web-01, port 5000. You’ll need to install Gunicorn and any libraries required by your application. Your Flask application object will serve as a [WSGI](https://www.fullstackpython.com/wsgi-servers.html) entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.

Requirements:

   * Install Gunicorn and any other libraries required by your application.
   * The Flask application object should be called app. (This will allow us to run and check your code)
   * You will serve the same content from the same route as in the previous task. You can verify that it’s working by binding a Gunicorn instance to localhost listening on port 5000 with your application object as the entry point.
   * In order to check your code, the checker will bind a Gunicorn instance to port 6000, so make sure nothing is listening on that port.

## 2. 