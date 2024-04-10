# TODO
## Issues

### Update Workflow
Fix workflows to account for refactored directories

## Features


### CICD
- Docker

### Refresh Database
Automatically refresh the database when changes are made to the calendar.

## Chores

### Setting up Flask development vs production server.
Current setup presumes development.

### API hosts on two addresses
When solving the Docker issue, note how the API is hosting on two separate addresses.
- Is this normal?
- If redundant, how can this be solved?

### Expanding Docker
The current system of Docker works, yet there are a couple composition issues regarding file management:
- Needs to bundle to client.
- Needs to make changes to the database, and save it when complete.

### Splitting up Workflows
Not certain if placing the building, testing, and linting under the same job is a good practice.
Consider breaking up the workflows into smaller sequential jobs, however that works.

### Overhaul Backend
Backend should be more object-oriented for simplicity's sake. And, it should be more modular where large chunks of code
is split into separate files.

Why:
- Improves separation of concerns and easier to follow flow of logic.
- Easier to test when code is in more digestible chunks.
- Underutilization of SQL Alchemy ORM. See example relating to Course method.

Examples: 
- The generation of a single sheet schedule should be a method of the Course object.
- The coloring and styling of sheets should be within its own method, considering how unwieldy the class is.

Things to consider:
- Think about differing architectural patterns in this re-work. Now would be a good time to employ them.

## Considerations

### Feature: Table for Single Course
A dedicated page demonstrating a table for a specified course.
The download button will still be where it usuall is. 
However, each entry will have a 'view' button

