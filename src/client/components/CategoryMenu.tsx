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
