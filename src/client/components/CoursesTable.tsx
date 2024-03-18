/* eslint-disable react/jsx-pascal-case */
import React, { useMemo } from 'react'
import {
  MaterialReactTable,
  useMaterialReactTable,
  MRT_GlobalFilterTextField,
  MRT_ToggleFiltersButton,
  type MRT_ColumnDef
} from 'material-react-table'
import { Box, Button } from '@mui/material'
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
    initialState: {
      showGlobalFilter: true
    },
    muiPaginationProps: {
      rowsPerPageOptions: [10, 25, 50, 200]
    },
    // muiSelectAllCheckboxProps: {
    //   sx: {
    //     display: 'flex',
    //     textAlign: 'center'
    //   }
    // },
    muiTableHeadCellProps: ({ column, table }) => {
      // Center align checkbox row-selection WIP
      if (column.id === 'mrt-row-select') {
        console.log(
          'column:', column
        )
        return {
          sx: {
            display: 'flex',
            textAlign: 'center'
          }
        }
      }
      return {
      }
    },
    positionToolbarAlertBanner: 'bottom',
    renderTopToolbar: ({ table }) => {
      const getSelectedCourses = (): number[] => {
        // Returns an array of the selected courses
        return Object.keys(table.getState().rowSelection)
          .map((key: string) => { return Number(key) + 1 })
      }
      const generateSchedule = (): void => {
        const selectedCourses = getSelectedCourses()
        const apiRoute = `/api/generate_schedule/${selectedCourses.join(',')}`
        axios({
          method: 'GET',
          url: apiRoute
        })
          .then(
            response => {
              axios({
                method: 'GET',
                responseType: 'blob',
                url: '/download_schedule'
              })
                .then(
                  response => {
                    const blob = new Blob(
                      [response.data],
                      { type: response.headers['content-type'] }
                    )
                    const url = window.URL.createObjectURL(blob)
                    const link = document.createElement('a')
                    link.href = url
                    link.setAttribute(
                      'download',
                      'demo-schedule.xlsx'
                    )
                    document.body.appendChild(link)
                    link.click()
                    window.URL.revokeObjectURL(url)
                    document.body.removeChild(link)
                  },
                  error => {
                    console.error('Failed to call /download_schedule API')
                    console.error(error)
                  }
                )
            },
            error => {
              console.error('Failed to call generate_schedule API')
              console.error(error)
            }
          )
      }
      return (
        <Box
          display='flex'
          gap='1rem'
          justifyContent='space-between'
          m={2}
        >
          <Box
            display='flex'
            gap='1rem'
          >
            <MRT_GlobalFilterTextField
              id='globalFilter'
              table={table}
            />
            <MRT_ToggleFiltersButton
              table={table}
            />
          </Box>
          <Box>
            <Button
              disabled={!table.getIsSomeRowsSelected()}
              variant='contained'
              onClick={generateSchedule}
            >
            Download Schedule
            </Button>
          </Box>
        </Box>
      )
    }
  })
  return (
    <MaterialReactTable
      table={table}
    />
  )
}

export default CoursesTable
