# NOTES

## Logical Order
### Initial Setup
1. Initialize empty DB
2. Populate with data.
   - This is useful for specifying before generating an Excel file.
3. Setup Flask App

### Parameterizing Schedule
Permit users to specify instructor(s), course_code(s), etc.
For every parameter change, update every other parameter to permissible/possible values
 
Update

### Generate Schedule
1. Extract data from DB.
2. Generate Excel

## Different ways to retrieve data

### 1: Using `session.get(Object, Index)`:
```
    course = session.get(Course, 1)
```
### 2: Using `select()` and `session.execute()` along with appropriate queries. 
```
    stmt = select(Course).where(Course.id == 1)
    course = session.execute(stmt).scalars().first()
```
Note that the use of `first()` only retrieves the first object in the executed `SELECT` query.