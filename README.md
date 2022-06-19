# UI Code challenge
The goals of this challenge are to produce a small python flask app for the attached mock-up. There is also some dummy data provided that needs to be rendered into these views.

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
    - [ ] Settings
    - [ ] Static /
    - [x] Tests
    - [ ] Flask Blueprint
    - [ ] .env file
 - [ ] Load Json data from a file
     - [x] Base load
     - [ ] Validate data with pydentic
     - [ ] Read json data from URL
 - [ ] Base layout
    - [x] Base template
    - [x] Sidebar
    - [x] Dashboard
        - [ ] Counters
        - [ ] Graphs
        - [ ] Graphs data API
    - [x] Vulnerability
        - [ ] Table
        - [ ] Filters
    - [ ] Vulnerability detail
    - [ ] Adaptive version
      - [ ] Menu
      - [ ] Views
    - [ ] 404/500 errors templates
    - [ ] Favicon
    - [ ] Sidebar menu. Generate menu data in flask.
 - [ ] Dashboard view
    - [ ] Counters
    - [ ] Graph widgets. Data.
    - [ ] Graph widgets. Render.
 - [ ] Vulnerability view
    - [ ] Filters
    - [ ] Table
    - [ ] Pagination
    - [ ] Vulnerability detail
 - [ ] Frontend customisation
    - [ ] Gulp setup
    - [ ] Branding
    - [ ] Custom styles
    - [ ] Responsive layouts
 - [ ] Tests
 - [ ] Final check
    - [ ] Titles
    - [ ] Sentry
    - [ ] Local/Production
    - [ ] Type checking
    - [ ] Comments
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
```mkvirtualenv --python=$(which python3) challenge```
```pip install -r requirements/local.txt```
```export FLASK_APP=app.py```
```export FLASK_ENV=development```
```flask run```
Open http://localhost:5000 to view the Dashboard

### Testing
```python -m pytest -v```
