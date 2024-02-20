# NOTES

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