import React from 'react'
import type { FC } from 'react'

const Header: FC = () => {
  return (
    <header>
      <h1
        className='font-bold text-4xl text-center mt-16 text-white'
        id="title"
      >Lecture Demonstration Schedule Generator
      </h1>
      <p
        className='text-2xl text-center text-white mt-5 mb-20'
        id="subtitle"
      >(Select all that apply)
      </p>
    </header>
  )
}

export default Header
