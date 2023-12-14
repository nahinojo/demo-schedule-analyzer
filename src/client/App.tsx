import React, { useState } from 'react'

import type { FC } from 'react'
import type { CategoriesSelections, CategoryName } from './types'

const App: FC = () => {
  const [categoriesSelections, setCategoriesSelections] = useState<CategoriesSelections>({
    courseCode: null,
    instructors: null,
    term: null,
    year: null
  })
  return (
    <>
      <header>
        <h1
          id="title"
        >Lecture Demonstration Schedule Generator
        </h1>
        <p
          id="subtitle"
        >(Select all that apply)
        </p>
      </header>
      {
        <div
          id='categories-wrapper'
        >
          {
            Object.entries(categoriesSelections)
              .map((categoryName) => {
                const key = `${categoryName as string}`
                return (
                  <p
                    key={key}
                  >{categoryName}
                  </p>
                )
              })
          }
        </div>
      }
      {/* <div
        id="fields-grid-wrapper"
      >
        <div
          className="field-item-wrapper"
        >
          <h1
            className="field-header" id="instructor-header"
          >Instructor
          </h1>
        </div>
        <div
          className="field-item-wrapper"
        >
          <h1
            className="field-header" id="course-code-header"
          >Course Code
          </h1>
        </div>
        <div
          className="field-item-wrapper"
        >
          <h1
            className="field-header" id="term-header"
          >Term
          </h1>
        </div>
        <div
          className="field-item-wrapper"
        >
          <h1
            className="field-header" id="year-header"
          >Year
          </h1>
        </div>
      </div> */}
    </>
  )
}

export default App
