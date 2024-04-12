# TODO
## Issues

### Update Workflow
Fix workflows to account for refactored directories

## Features

### Docker

### Testing
 - client. 

### Listen for Calendar Changes
Automatically refresh the database and client when changes are made to the calendar.

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

## Considerations

### Feature: Table for Single Course
A dedicated page demonstrating a table for a specified course.
The download button will still be where it usually is. 
However, each entry will have a 'view' button

