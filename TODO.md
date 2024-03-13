# TODO
## Issues
### [Small Issues]
- Create a database file if it does not exist.

## Features
### Too Small of Schedules
- Show the user how many entries in a given course.
- Filter out too small courses from generated schedule.

## Chores
### Update the database, don't remake it (low-priority)
- The current system recreates the database. Consider just updating it instead.

## Considerations
### Counting Courses
- Issue: How would you determine how many times a course, such as Siryaporn 3C, was taught the last few springs?
  - course_attribute_options only shows valid selectors; it does no _counting_
- Solutions:
  1. New API routes that counts the number of times a course occurred, or how many courses are within course_attribute_options
  2. Change `term` to `season`, (Winter, Spring, Fall); `term` is now the concatenation of season and year (Spring 2020). 

### Filter out small schedules

