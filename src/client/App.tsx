import React, { useEffect, useState } from 'react'
import { CategoryMenu } from './components/CategoryMenu'
import './style.css'
import type { FC } from 'react'
import Header from './components/Header'

import type { CategoriesOptions } from './types'

interface Response {
  course_codes: string[]
  instructors: string[]
  terms: string[]
}

const App: FC = () => {
  const [categoriesOptions, setCategoriesOptions] = useState<CategoriesOptions>({
    courseCodes: null,
    instructors: null,
    terms: null,
    years: null
  })
  useEffect(
    () => {
      console.log('Fetching course attribute options...')
      const apiUrl = 'http://localhost:5000'
      fetch(`${apiUrl}/course_attribute_options`)
        .then(async response => { return await (response.json() as Promise<Response>) })
        .then(response => {
          response.course_codes = Array.from(new Set(response.course_codes))
          response.instructors = Array.from(new Set(response.instructors))
          response.terms = Array.from(new Set(response.terms))
          setCategoriesOptions(categoriesOptions => {
            return {
              courseCodes: response.course_codes,
              instructors: response.instructors,
              terms: response.terms,
              years: null
            }
          })
        })
        .catch(error => { console.log(error) })
    }, []
  )
  return (
    <>
      <Header />
      <div
        className='mx-[25%] grid grid-cols-2'
      >
        <CategoryMenu
          options={categoriesOptions.instructors}
          title='Instructor'
        />
        <CategoryMenu
          options={categoriesOptions.courseCodes}
          title='Course Code'
        />
        <CategoryMenu
          options={categoriesOptions.terms}
          title='Term'
        />
        <CategoryMenu
          title='Year'
        />
      </div>
    </>
  )
}

export default App
