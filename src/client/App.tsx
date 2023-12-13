import React from 'react'

import type { FC } from 'react'

console.log('Executing App file')
const App: FC = () => {
  console.log('Executing app element FC!')
  return (
    <>
      <header>
        <h1
          id="title"
        >LDS React
        </h1>
        <p
          id="subtitle"
        >(Select all that apply)
        </p>
      </header>
      <div
        id="categories-grid-wrapper"
      >
        <div
          className="category-item-wrapper"
        >
          <h1
            className="category-header" id="instructor-header"
          >Instructor
          </h1>
        </div>
        <div
          className="category-item-wrapper"
        >
          <h1
            className="category-header" id="course-code-header"
          >Course Code
          </h1>
        </div>
        <div
          className="category-item-wrapper"
        >
          <h1
            className="category-header" id="term-header"
          >Term
          </h1>
        </div>
        <div
          className="category-item-wrapper"
        >
          <h1
            className="category-header" id="year-header"
          >Year
          </h1>
        </div>
      </div>
    </>
  )
}

export default App
