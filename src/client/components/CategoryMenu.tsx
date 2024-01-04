import React, { useEffect, useState } from 'react'
import { camelToTitleCase } from '../utils'

import type { IndexableRecord } from '../types'
import type { FC } from 'react'

interface CategoryMenuProps {
  name: 'instructor' | 'courseCode' | 'term' | 'year'
  selections?: IndexableRecord
}

export const CategoryMenu: FC<CategoryMenuProps> = ({ name, selections }) => {
  const title = camelToTitleCase(name)
  console.log(`Rendering <CategoryMenu /> ${title}...`)
  useEffect(() => {
    const apiUrl = 'http://localhost:5000'
    fetch(`${apiUrl}/course_attribute_options?target_year=2023&target_instructor=Ochoa`)
      .then(response => {
        console.log(response.json())
      })
      .catch(error => { console.log(error) })
  })
  const [options, setOptions] = useState<IndexableRecord | null>(null)
  useEffect(() => {
    console.log('useEffect Activated')
  })
  return (
    <div
      className='mx-auto mb-24 w-1/2 grid-cols-2'
      id="field-grid-wrapper"
    >
      <h1
        className="font-medium text-2xl text-center mb-2"
        id="instructor-header"
      >{title}
      </h1>
      <menu
        className='bg-night rounded-md'
      >
        <li>Ochoa</li>
        <li>Tucker</li>
      </menu>
    </div>
  )
}
