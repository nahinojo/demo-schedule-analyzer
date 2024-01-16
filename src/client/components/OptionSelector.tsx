import React from 'react'
import { FormGroup, FormControlLabel, Checkbox } from '@mui/material'
import { orange, grey } from '@mui/material/colors'

import type { FC } from 'react'
import type { Options } from '../types'

interface OptionSelectorProps {
  options: Options
}

export const OptionSelector: FC<OptionSelectorProps> = ({ options }) => {
  return (
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
