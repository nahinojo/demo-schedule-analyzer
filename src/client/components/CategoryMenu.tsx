import React from 'react'
import type { FC } from 'react'
import { Checkbox, FormGroup, FormControlLabel } from '@mui/material'
import { orange, grey } from '@mui/material/colors'

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
        className="font-medium text-2xl text-center mb-2 text-white"
        id="instructor-header"
      >{title}
      </h1>
      <div
        className='bg-night rounded-md'
        id='field-options-background'
      >{
          !!isNullOptions && (
            <p
              className='text-white'
            >Loading...
            </p>
          )
        }
        {
          !isNullOptions && (
            <FormGroup>
              {
                options?.map((
                  option, index
                ) => {
                  const label = { inputProps: { 'aria-label': `checkbox ${index}-${option}` } }
                  return (
                    <FormControlLabel
                      control={
                        (
                          <Checkbox
                            {...label}
                            sx={
                              {
                                color: grey[700],
                                // eslint-disable-next-line sort-keys
                                '&.Mui-checked': {
                                  color: orange[600]
                                }
                              }
                            }
                            defaultChecked={false}
                          />
                        )
                      }
                      sx={
                        {
                          color: 'white',
                          marginLeft: 0.25
                        }
                      }
                      key={index}
                      label={option}
                    />
                  )
                })
              }
            </FormGroup>
          )
        }
      </div>
    </div>
  )
}
