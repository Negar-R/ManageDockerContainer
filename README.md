[![Python Version](https://img.shields.io/badge/python-3.9-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-4.1-brightgreen.svg)](https://djangoproject.com)
[![Django Rest Version](https://img.shields.io/badge/djangorest-3.14-brightgreen.svg)](https://www.django-rest-framework.org)

## Purpose of system

This is a simple django project to manage docker containers.



## URL's introduction

After you clone the project and set it ups, you can use this table to call APIs.

URL | Description
--- | ---
``URL/apps`` | In this url you can `GET` all App objects and also create a new one by `POST` method.
``URL/apps/total_history`` | You can access the history of all App objects here from the newest one.
``URL/apps/ID`` | To `RETRIEVE` a specific app and see its details. Also, it is possible to `UPDATE` or `DELETE` an app via this url.
``URL/apps/ID/run`` | If you want to run your app and create a docker container from a specific app, call this url.
``URL/apps/ID/history`` | All history of running an app from the latest one to the oldest can be found here. You can get some details information about an app's containers.


### Notes:

- Calling `UPDATE` API only updates a specific App object and its future containers. It does not make any changes to previous running or stopped containers of this app.

- I put some comments inside the code to explain some technical notes.
