import React, { useMemo } from 'react'
import {
  MaterialReactTable,
  useMaterialReactTable,
  type MRT_ColumnDef
} from 'material-react-table'

// example data type
interface Course {
  instructor: string
  courseCode: string
  year: string
  term: string
}

// nested data is ok, see accessorKeys in ColumnDef below
const exampleData: Course[] = [
  {
    courseCode: 'CS 101',
    instructor: 'Dr. John Doe',
    term: 'Fall',
    year: '2023'
  },
  {
    courseCode: 'CS 102',
    instructor: 'Dr. Jane Doe',
    term: 'Winter',
    year: '2023'
  },
  {
    courseCode: 'ENG 110',
    instructor: 'Dr. Foo Bar',
    term: 'Summer',
    year: '2021'
  },
  {
    courseCode: 'ENG 111',
    instructor: 'Dr. Baz Quux',
    term: 'Fall',
    year: '2021'
  },
  {
    courseCode: 'CS 111',
    instructor: 'Dr. Baz Quux',
    term: 'Fall',
    year: '2022'
  }
]

const Example = (): JSX.Element => {
  // should be memoized or stable
  const columns = useMemo<Array<MRT_ColumnDef<Course>>>(
    () => {
      return [
        {
          accessorKey: 'instructor', // access nested data with dot notation
          header: 'Instructor',
          size: 150
        },
        {
          accessorKey: 'courseCode',
          header: 'Course Code',
          size: 50
        },
        {
          accessorKey: 'year', // normal accessorKey
          header: 'Year',
          size: 100
        },
        {
          accessorKey: 'term', // normal accessorKey
          header: 'Term',
          size: 150
        }
      ]
    },
    []
  )

  const table = useMaterialReactTable({
    columns,
    data: exampleData // data must be memoized or stable (useState, useMemo, defined outside of this component, etc.)
  })

  return (
    <MaterialReactTable
      table={table}
    />
  )
}

export default Example
