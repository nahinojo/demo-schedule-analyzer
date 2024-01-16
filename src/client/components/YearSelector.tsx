import React from 'react'
import type { FC } from 'react'

export const YearSelector: FC = () => {
  const currentYear = new Date()
    .getFullYear()
  return (
    <input
      className='w-20 opacity-0 text-white'
      defaultValue={currentYear}
      max={currentYear}
      min={2010}
      step={1}
      type='number'
    >
    </input>
  )
}
