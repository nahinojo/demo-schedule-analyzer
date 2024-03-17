import React, { useMemo } from 'react'
import {
  MaterialReactTable,
  useMaterialReactTable,
  type MRT_ColumnDef
} from 'material-react-table'
import axios from 'axios'

// example data type
interface Course {
  instructor: string
  courseCode: string
  year: string
  term: string
}

interface APIResponse {
  data: {
    data: Record<number, Course>
  }
}

let details: Course[] = []
axios.get('/api/get_course_table')
  .then(
    (response: APIResponse) => {
      details = Object.values(response.data.data)
    },
    error => {
      console.error('Failed to call get_course_table API')
      console.error(error)
    }
  )

const Example = (): JSX.Element => {
  // should be memoized or stable
  const columns = useMemo<Array<MRT_ColumnDef<Course>>>(
    () => {
      return [
        {
          accessorKey: 'instructor',
          header: 'Instructor',
          size: 150
        },
        {
          accessorKey: 'courseCode',
          header: 'Course Code',
          size: 50
        },
        {
          accessorKey: 'year',
          header: 'Year',
          size: 100
        },
        {
          accessorKey: 'term',
          header: 'Term',
          size: 150
        }
      ]
    },
    []
  )

  const table = useMaterialReactTable({
    columns,
    data: details // data must be memoized or stable (useState, useMemo, defined outside of this component, etc.)
  })

  return (
    <MaterialReactTable
      table={table}
    />
  )
}

export default Example
