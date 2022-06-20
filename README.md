[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# UI Code challenge
The goals of this challenge are to produce a small python flask app for the attached mock-up. There is also some dummy data provided that needs to be rendered into these views.

# Short summary
This is the first draft for the project.
A lot still needs to be done.
You can check [todo section](#todo-1-st-version) to see following steps.

# Table of Contents
 - [Info](#info)
 - [Questions](#questions)
 - [TODO. 1-st version.](#todo-1-st-version)
 - [Features](#features)
 - [TODO. 2-d version.](#todo-2-d-version)
 - [Installation](#installation-development-environment-without-docker)
 - [Testing](#testing)

## Info
 - Mock Up.png - Dashboard and Vulnerability mockups
 - UI Code challenge.docx - description of the challenge
 - Vulnerability data.json - dummy data

## Questions
 - [ ] Use cases
 - [ ] Users roles
 - [ ] Tech. requiments

## TODO. 1-st version.
Rendering template in the backend. Flask + Bootstrap.
 - [ ] Project setup
    - [x] Readme
    - [x] Views
    - [x] Templates
    - [x] Settings
    - [ ] Static (Assets)
    - [x] Tests
    - [ ] Flask Blueprint
    - [x] .env file
    - [ ] Logging
    - [ ] Load json file DATA_FILE at app start
 - [ ] Load Json data from a file
     - [x] Base load
     - [ ] Validate data with pydentic
     - [ ] Read json data from URL
 - [ ] Base layout
    - [x] Base template
    - [x] Sidebar
    - [x] Dashboard
        - [x] Counters
        - [ ] Graphs
        - [ ] Graphs data API
    - [x] Vulnerability
        - [x] Table
        - [x] Filters
    - [ ] Vulnerability detail
    - [ ] Adaptive version
      - [ ] Menu
      - [ ] Views
    - [ ] 404/500 errors templates
    - [ ] Favicon
    - [ ] Sidebar menu. Generate menu data in flask.
 - [ ] Dashboard view
    - [x] Counters
    - [x] Graph widgets. Data. !Refactoring needed
    - [x] Graph widgets. Render. !Refactoring needed
    - [ ] Refactoring
 - [ ] Vulnerability view
    - [x] Filters
    - [x] Table
    - [ ] Pagination
    - [ ] Vulnerability detail
    - [ ] Custom table "Sort" argument name
    - [x] Column get parametrs !Refactoring needed
    - [ ] Refactoring
 - [ ] Frontend customisation
    - [ ] Gulp setup
    - [ ] Branding
    - [ ] Custom styles
    - [ ] Responsive layouts
 - [ ] Tests
 - [ ] Final check
    - [ ] Titles
    - [ ] Logging
    - [ ] Sentry
    - [ ] Local/Production
    - [ ] Type checking
    - [ ] Comments
    - [ ] Add a Table of Contents to README
 - [ ] Updates
 - [ ] Deployment with Docker
 - [ ] CI/CD

## Features
 - [ ] Login/logout pages
 - [ ] Users management
 - [ ] Vulnerability details page
 - [ ] Vulnerability management (Statuses, Assignee, Projects, etc..)
 - [ ] Pre-built filters
 - [ ] Notifications/Alerts
 - [ ] Statistics
 - [ ] ? Live graphs


## TODO. 2-d version.
React + backend API
 - [ ]  MongoDB setup
 - [ ]  Flask. Load Json data from a file to MongoDB
 - [ ]  Flask. Rest API
	 - [ ]  Auth
        - [ ] Login
        - [ ] Logout
	 - [ ]  Vulnerability list
        - [ ]  Filters
	 - [ ]  Vulnerability detail
	 - [ ]  Dashboard counters
	 - [ ]  Graphs
 - [ ]  React. Initial project
 - [ ]  React. Components
	 - [ ] Login page
        - [ ] Login form
	 - [ ] Sidebar
		 - [ ] Menu item
	 - [ ]  Dashboard
		 - [ ]  Counter
		 - [ ]  Graph
	 - [ ]  Vulnerability list
		 - [ ]  Table
		 - [ ]  Filters
         - [ ]  Pagination
	 - [ ]  Vulnerability detail
 - [ ]  React. Load data
 - [ ]  React. Tests
 - [ ]  React. Deployment


## Installation (development environment) without docker
 - ```mkvirtualenv --python=$(which python3) challenge```
 - ```pip install -r requirements/local.txt```
 - ```cp .env.dist .env``` / DATA_FILE setting - json data file
 - ```flask run```
 - Open http://localhost:5000 to view the Dashboard

## Testing
```python -m pytest -v```
