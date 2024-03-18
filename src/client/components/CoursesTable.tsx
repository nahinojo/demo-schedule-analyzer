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

let courses: Course[] = []
axios.get('/api/get_course_table')
  .then(
    (response: APIResponse) => {
      courses = Object.values(response.data.data)
    },
    error => {
      console.error('Failed to call get_course_table API')
      console.error(error)
    }
  )

const CoursesTable = (): JSX.Element => {
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
    data: courses,
    enableDensityToggle: false,
    enableFullScreenToggle: false,
    enableRowSelection: true,
    muiPaginationProps: {
      rowsPerPageOptions: [10, 25, 50, 200]
    },
    positionToolbarAlertBanner: 'bottom'
  })
  const getSelectedCourses = (): number[] => {
    // Returns an array of the selected courses
    return Object.keys(table.getState().rowSelection)
      .map((key: string) => { return Number(key) })
  }
  console.log(getSelectedCourses())
  return (
    <MaterialReactTable
      table={table}
    />
  )
}

export default CoursesTable
