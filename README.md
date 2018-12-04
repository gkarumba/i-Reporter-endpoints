
[![Build Status](https://travis-ci.org/gkarumba/i-Reporter-endpoints.svg?branch=ch-testing-endpoints-162298730)](https://travis-ci.org/gkarumba/i-Reporter-endpoints)  [![Coverage Status](https://coveralls.io/repos/github/gkarumba/i-Reporter-endpoints/badge.svg?branch=ch-testing-endpoints-162298730)](https://coveralls.io/github/gkarumba/i-Reporter-endpoints?branch=ch-testing-endpoints-162298730)  [![Maintainability](https://api.codeclimate.com/v1/badges/eaedfc4b38c12fec58e1/maintainability)](https://codeclimate.com/github/gkarumba/i-Reporter-endpoints/maintainability)

# i-Reporter-endpoints
This repo is a build of the API endpoints for an online reporting platform

## RESTful API Endpoints for ireporter
| Method        |       Endpoint                        |         Description                           |
| ------------- |       -------------                   |         -------------                         |
| `POST`        | `/api/v1/reports`                     |   Creates a new report                        |
| `GET`         | `/api/v1/reports`                     |   Gets all reports                            |
| `GET`         | `/api/v1/reports/<reportid>`          |   Gets a single report by id                  |
| `PUT`         | `/api/v1/reports/<reportid>/edit`     |   Edit a specific report by id                |
| `DELETE`      | `/api/v1/reports/<reportid>`          |   Deletes a specific report by id             |

## Getting Started

To get this repo running on your local machine for development and testing purposes.
Ensure that you have python 2.7
1. Create a new folder in the local machine
2. Open terminal and cd into the folder `cd <foldername>`
3. Create a virtual environment `virtualenv <nameofvirtualenv>`
4. Activate the virtual env `source <nameofvirtualenv>/bin/activate`

### Prerequisites
To have the repo on your machine run `git clone https://github.com/gkarumba/i-Reporter-endpoints.git`
To install all the dependencies run `pip install -r requirements.txt` 

### Running the flask app

To run the flask app
1. Run `export FLASK_APP=run.py`

2. Run `export FLASK_ENV=development`

3. Run `flask run` to start the server

## Running the tests

To test the endpoints ensure that `Postman` is installed in the local machine
Run `Postman` and set the localhost to `http://127.0.0.1:5000/`
Add the localhost with urls for the various endpoints, for example: 'http://127.0.0.1:5000/api/v1/reports' then start sending the requests


## Deployment

The APIs is hosted on [HEROKU] and can be access via : https://i-reporter-gkarumba.herokuapp.com/

## Running nosetests
run the following command on terminal : `nosetests --with-coverage --cover-package=app`
