import React from 'react'
import { CategoryMenu } from './components/CategoryMenu'
import './style.css'
import type { FC } from 'react'
import Header from './components/Header'

// import type { CategoriesSelections, CategoryName } from './types'

const App: FC = () => {
  // const [categoriesSelections, setCategoriesSelections] = useState<CategoriesSelections>({
  //   courseCode: null,
  //   instructor: null,
  //   term: null,
  //   year: null
  // })
  return (
    <>
      <Header />
      <div
        className='mx-[25%] grid grid-cols-2'
      >
        <CategoryMenu
          name='instructor'
        />
        <CategoryMenu
          name='courseCode'
        />
        <CategoryMenu
          name='term'
        />
        <CategoryMenu
          name='year'
        />
      </div>
    </>
  )
}

export default App
