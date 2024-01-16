import React from 'react'
import { OptionSelector } from './OptionSelector'
import { YearSelector } from './YearSelector'

import type { FC } from 'react'
import type { Options } from '../types'

interface CategoryMenuProps {
  title: 'Instructor' | 'Course Code' | 'Term' | 'Year'
  isOptionsCategory: boolean
  options?: Options
}

const CategoryMenu: FC<CategoryMenuProps> = ({ title, options, isOptionsCategory }) => {
  const isUndefinedData = options === undefined
  const isNullData = options === null
  if (!isNullData) {
    const isInvalidCategoryDataType = isOptionsCategory !== (typeof options === 'object')
    if (isInvalidCategoryDataType) {
      console.error('Invalid data type for categoryData.')
      console.error(
        'categoryData:', options, '\nisOptionsCategory:', isOptionsCategory
      )
      return null
    }
  }
  const isDisplayOptions = !isNullData && !isUndefinedData && isOptionsCategory
  const isDisplayYear = isUndefinedData && !isOptionsCategory
  return (
    <div
      className='mx-auto mb-24 w-1/2 grid-cols-2'
      id="field-grid-wrapper"
    >
      <h1
        className="font-medium text-2xl text-center mb-2 text-white"
        id="instructor-header"
      >{title}
      </h1>
      <div
        className='bg-night rounded-md max-h-80 overflow-y-auto py-1'
        id='field-options-background'
      >{
          !!isNullData && (
            <p
              className='text-white ml-1'
            >Loading...
            </p>
          )
        }
        {
          !!isDisplayOptions && (
            <OptionSelector
              options={options}
            />
          )
        }
        {
          !!isDisplayYear && (
            <YearSelector />
          )
        }
      </div>
    </div>
  )
}

export default CategoryMenu
