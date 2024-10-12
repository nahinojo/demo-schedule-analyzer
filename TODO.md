# TODO
## Issues

### Update Workflow
Fix workflows to account for refactored directories

## Features

### Database Overhaul!

Each datbase `Model` should have a related `ModelRepository` and (optional) 
`ModelService`.

`ModelRepository` should be used to perform CRUD operations on the database.

`ModelService` should perform any additional business logic associated with 
the `Model`. 

### Schedule as a Database Model

### Client Testing

### Listen for Calendar Changes
Automatically refresh the database and client when changes are made to the 
calendar.

## Chores

### Docker
Prevent duplication of db when building. Try not to copy database over.

### Splitting up Workflows
Not certain if placing the building, testing, and linting under the same job is
a good practice.
Consider breaking up the workflows into smaller sequential jobs, however that 
works.

## Considerations

### Feature: Table for Single Course
A dedicated page demonstrating a table for a specified course.
The download button will still be where it usually is. 
However, each entry will have a 'view' button

### View calendar data on the website

