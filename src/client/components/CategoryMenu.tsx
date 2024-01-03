import React from 'react'

import type { FC } from 'react'

interface CategoryMenuProps {
  title: 'Instructor' | 'Course Code' | 'Term' | 'Year'
  selections?: Record<number, string>
}

export const CategoryMenu: FC<CategoryMenuProps> = ({ title, selections }) => {
  return (
    <div
      className='fields-selection-menu-wrapper'
    >
      <h1
        className="field-header text-blue"
        id="instructor-header"
      >{title}
      </h1>
      <menu
        className=''
      >
        <li
          className='text-yellow-500'
        >words
        </li>
      </menu>
    </div>
  )
}
