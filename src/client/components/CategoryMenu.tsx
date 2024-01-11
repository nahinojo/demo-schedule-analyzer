import React from 'react'
import type { FC } from 'react'

interface CategoryMenuProps {
  title: 'Instructor' | 'Course Code' | 'Term' | 'Year'
  options?: string[] | null
}

export const CategoryMenu: FC<CategoryMenuProps> = ({ title, options }) => {
  const isNullOptions = options === null
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
      >{
          !!isNullOptions && <li>Loading...</li>
        }
        {
          !isNullOptions && options?.map((
            option, index
          ) => {
            return (
              <li
                key={index}
              >{option}
              </li>
            )
          })
        }
      </menu>
    </div>
  )
}
