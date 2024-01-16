/* eslint-disable sort-keys */
import React, { useEffect, useState } from 'react'
import CategoryMenu from './components/CategoryMenu'
import './style.css'
import type { FC } from 'react'
import Header from './components/Header'

import type { CategoriesOptions, Term } from './types'

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
  const termsOrder = {
    Winter: 0,
    Spring: 1,
    Summer: 2,
    Fall: 3
  }
  useEffect(
    () => {
      const apiUrl = 'http://localhost:5000'
      fetch(`${apiUrl}/course_attribute_options`)
        .then(async response => { return await (response.json() as Promise<Response>) })
        .then(response => {
          response.course_codes = Array.from(new Set(response.course_codes))
            .sort()
          response.instructors = Array.from(new Set(response.instructors))
            .sort()
          response.terms = Array.from(new Set(response.terms))
            .sort((
              a: Term, b: Term
            ) => { return termsOrder[a] - termsOrder[b] })
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
        className='mx-[20%] grid grid-cols-2'
      >
        <CategoryMenu
          isOptionsCategory={true}
          options={categoriesOptions.instructors}
          title='Instructor'
        />
        <CategoryMenu
          isOptionsCategory={true}
          options={categoriesOptions.courseCodes}
          title='Course Code'
        />
        <CategoryMenu
          isOptionsCategory={true}
          options={categoriesOptions.terms}
          title='Term'
        />
        <CategoryMenu
          isOptionsCategory={false}
          title='Year'
        />
      </div>
    </>
  )
}

export default App
