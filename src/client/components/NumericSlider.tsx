import React, { useState } from 'react'
import { Box, Slider } from '@mui/material'

const NumericSlider = ({
  id,
  min,
  max,
  step
}: {
  id: string
  min: number
  max: number
  step: number
}): JSX.Element => {
  const [value, setValue] = useState<number>(0)
  const handleChange = (
    event: Event,
    newValue: number | number[]
  ): void => {
    setValue(newValue as number)
  }

  return (
    <Box
      sx={
        {
          width: '100%'
        }
      }
    >
      <Slider
        id={id}
        max={max}
        min={min}
        step={step}
        value={value}
        onChange={handleChange}
      />
    </Box>
  )
}

export default NumericSlider
