# Task:
Design and implement a simple task management system web service.

### The web service should be able to:
- Add a new task
- Retrieve a task by its ID
- Update a task
- Delete a task

### Detailed Requirements
- Each task should have an ID, title, description, status (completed/not completed), and timestamp.
- Python 3.10 and Django/Flask
- RESTful APIbased application
- Implement error handling for the APIs
- Unit tests for one APIs


### Deliverables
- How to use the APIs (a simple API documentation)
- Instructions on how to build and run the web service, and run the tests (if any).
- Link to the git repository

### How To:
#### Starting
To start an application write following commands:
1. `docker-compose build`
2. `docker-compose up`
3. proceed to _http://127.0.0.1:8000/tasks-list/_  (or _http://localhost:8000/tasks-list/_) 

If you are not using docker - write this command in your console
`python manage.py runserver`

But don't forget to install requirements and _cd_ to correct dir

#### Using
Application has basic CRUD methods:   
- **Get** all tasks with
  
Request: GET `http://127.0.0.1:8000/tasks-list/'`

Result: `[
    {
        "id": 1,
        "title": "Test1",
        "description": "Lorem ipsum",
        "created_date": "2023-08-11T11:23:32.941009Z",
        "status": "U"
    }
]`
  
- **Get** a single task data with

Request: GET `http://127.0.0.1:8000/task-detail/<str:pk>/'`

Result:  
`{
    "id": 1,
    "title": "Test1",
    "description": "Lorem ipsum",
    "created_date": "2023-08-11T11:23:32.941009Z",
    "status": "U"
}`

- **Create** new task with 
  
Request: POST
`http://127.0.0.1:8000/task-create/`

JSON:
`{
    "title": "TestCreate2",
    "description": "Some Text for test"
}`

Response:

`{
    "id": 3,
    "title": "TestCreate2",
    "description": "Some Text for test",
    "created_date": "2023-08-12T08:31:23.902793Z",
    "status": "U"
}`


- **Update** task with `'task-update/<str:pk>/'`
  
Request POST `http://127.0.0.1:8000/task-update/2/`

JSON:
`{
    "title": "Task2Updated",
    "description": "Updated description"
}`

Response:
`{
    "id": 2,
    "title": "Task2Updated",
    "description": "Updated description",
    "created_date": "2023-08-12T08:30:59.199062Z",
    "status": "U"
}`
- **Delete** task with
Request DELETE `http://127.0.0.1:8000/task-delete/2/`
  
Response `"Task 2 deleted."`

#### Testing
For application tests run the command:

`python manage.py test -v 2`


### Additional Questions Answers:

**Q1.** How would you use a CI/CD pipeline to automate the deployment process?
   <br>
**A1:** It depends on whole system pipeline but, for this example basic operations I can imagine would be:
- Running testing in CI/CD
- Creating docker image of app with secrets and loading it somewhere to use (Google Cloud Storage)
- Running commands with cloud service APIs to launch prepared image on some cloud service 

  
**Q2.** What stages would you include in your CI/CD pipeline and what would be their scope
<br>
**A2:** 
- Testing
- Building
- Deployment
