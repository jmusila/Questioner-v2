## Questioner-v2 Version2 with postgres database:
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![Build Status](https://travis-ci.com/jonathanmusila/Questioner-v2.svg?branch=develop)](https://travis-ci.com/jonathanmusila/Questioner-v2)  [![Maintainability](https://api.codeclimate.com/v1/badges/678ac372abdcdaa1524b/maintainability)](https://codeclimate.com/github/jonathanmusila/Questioner-v2/maintainability)  [![Coverage Status](https://coveralls.io/repos/github/jonathanmusila/Questioner-v2/badge.svg?branch=develop)](https://coveralls.io/github/jonathanmusila/Questioner-v2?branch=develop)


## Summary

- Questioner is a platform where people can see meetups, ask questions and attend meetups. 

## NOTE
* The project is managed using PivotalTracker board [click here](https://www.pivotaltracker.com/n/projects/2235195)

* To see the app documentation [click here](https://my-postgres-questioner-v2-api.herokuapp.com/api/v2)

* To see API hosted on heroku [click here](https://my-postgres-questioner-v2-api.herokuapp.com/api/v2)


## Getting Started 

* Clone the repository: 

    ```https://github.com/jonathanmusila/Questioner-v2.git```

* Navigate to the cloned repo.

### Prerequisites

```
1. Python3
2. Flask
3. Postman
```

## Installation 
After navigating to the cloned repo;

Create a virtualenv and activate it ::

    create a directory 
    cd into the directory
    virtualenv -p python3 venv
    source venv/bin activate

Install the dependencies::

    pip install -r requirements.txt 

## Configuration

After activativating the virtualenv, run:

    ```
    export APP_SETTINGS="development"
    export FLASK_APP="run.py"
    export FLASK_DEBUG=1
    SECRET="iamsecretethenuseentheunknowntheundead"

    ```
## Running Tests
Run:
```
pytest --cov-report term-missing --cov=app/api
```

### Testing on Postman
Fire up postman and start the development server by:
  ```
  $ flask run
  ```

Test the following endpoints:

### Meetups endpoints

| EndPoint                       | Functionality                           |
| -------------------------------|:---------------------------------------:|
| GET     /meetups/upcoming      | Gets all meetups as a list              |
| GET    /meetups/upcoming/id    | Gets a single meetup by id              |
|                                                                          |

### Questions endpoints

| EndPoint                            | Functionality                           |
| ------------------------------------|:---------------------------------------:|
| POST     /meetups/id/questions      | Posts new question                      |
| PATCH     /meetups/id/upvote        | Patches a upvote to a question          |
| PATCH     /meetups/id/upvote        | Patches a upvote to a question          |
|                                                                               |

### Admin endpoints

| EndPoint                            | Functionality                           |
| ------------------------------------|:---------------------------------------:|
| DELETE  /meetups/upcoming/id        | Deletes a single meetup by id           |
| POST     /meetups/upcoming          | Posts new meetup                        |
|                                                                               |


### User endpoints

| EndPoint                            | Functionality                           |
| ------------------------------------|:---------------------------------------:|
| POST     /auth/signup               | Posts a sinup user                      |
| POST     /auth/login                | Posts a login user                      |
|                                                                               |

## Authors

* **Jonathan Musila** - *Initial work* - [jonathanmusila](https://github.com/jonathanmusila)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

#### Contribution
Fork the repo, create a PR to this repository's develop branch.
