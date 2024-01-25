# TODO
## Issues
**Typing**

How would you define a new type to be used to typeset a parameter? If you defined the type `Demos` as `Demos = list[Demo]`,
how would you be able to use this in other modules?

## Features
Reorganize webpage to show list of demos to download. Attributes become filters.
## Chores
### Refactor for Manage SQLAlchmeny Database
A plan needs to be made for how data is going to be stored and manipulated.

There's not really any point to abstracting out the methods of getting values from the db, nor adding a new course, since both methods are quite simple.

## Considerations
- Show the user how many courses and/or entries per course are in the to-be-generated Excel document