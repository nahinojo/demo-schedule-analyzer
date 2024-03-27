import React from 'react'
import { CoursesTable } from './components'

import type { FC } from 'react'
import './style.css'

const App: FC = () => {
  return (
    <div
      className='max-w-screen-xl mx-auto mt-4'
      id='table-wrapper'
    >
      <CoursesTable />
    </div>
  )
}

export default App
