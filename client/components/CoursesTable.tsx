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
import { ColorModeToggle } from './ColorMode'
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
axios.get_by_id('/api/get_courses_table')
  .then(
    (response: APIResponse) => {
      courses = Object.values(response.data.data)
    },
    error => {
      console.error('Failed to call get_courses_table API')
      console.error(error)
    }
  )

const CoursesTable = (): JSX.Element => {
  const stringFilters = [
    'equals',
    'contains',
    'fuzzy'
  ]
  const defaultStringFilter = 'contains'
  const numberFilters = [
    'greaterThanOrEqualTo',
    'equals',
    'lessThanOrEqualTo'
  ]
  const defaultNumberFilter = 'greaterThanOrEqualTo'
  const columns = useMemo<Array<MRT_ColumnDef<Course>>>(
    () => {
      return [
        {
          accessorKey: 'instructor',
          columnFilterModeOptions: stringFilters,
          filterFn: defaultStringFilter,
          header: 'Instructor',
          size: 100
        },
        {
          accessorKey: 'courseCode',
          columnFilterModeOptions: stringFilters,
          filterFn: defaultStringFilter,
          header: 'Course Code',
          size: 100
        },
        {
          accessorKey: 'year',
          columnFilterModeOptions: numberFilters,
          filterFn: defaultNumberFilter,
          header: 'Year',
          size: 100
        },
        {
          accessorKey: 'term',
          columnFilterModeOptions: [
            ...stringFilters,
            'notEquals'
          ],
          filterFn: defaultStringFilter,
          header: 'Term',
          size: 100
        },
        {
          accessorKey: 'numDemoEvents',
          columnFilterModeOptions: numberFilters,
          filterFn: defaultNumberFilter,
          header: '# Events',
          size: 100
        }
      ]
    },
    []
  )

  const table = useMaterialReactTable({
    columns,
    data: courses,
    enableColumnFilterModes: true,
    enableDensityToggle: false,
    enableFullScreenToggle: false,
    enableRowSelection: true,
    initialState: {
      pagination: { pageIndex: 0, pageSize: 20 },
      showGlobalFilter: true
    },
    muiPaginationProps: {
      rowsPerPageOptions: [5, 20, 50, 200]
    },
    positionToolbarAlertBanner: 'bottom',
    renderTopToolbar: ({ table }) => {
      const isNoRowSelected = !table.getIsSomeRowsSelected() && !table.getIsAllRowsSelected()
      const getSelectedCourseIds = (): number[] => {
        const selectedCourses = Object.keys(table.getState().rowSelection)
        const selectedCourseIds = Object.values(selectedCourses)
          .map((key: string) => { return Number(key) + 1 })
        return selectedCourseIds
      }
      const generateSchedule = (): void => {
        const selectedCourses = getSelectedCourseIds()
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
              sx={{ ml: 1 }}
              table={table}
            />
            <ColorModeToggle />
          </Box>
          <Box>
            <Button
              disabled={isNoRowSelected}
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
