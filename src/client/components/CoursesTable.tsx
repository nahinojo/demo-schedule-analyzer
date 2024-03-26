/* eslint-disable react/jsx-pascal-case */
import React, { useMemo, useState } from 'react'
import {
  MaterialReactTable,
  useMaterialReactTable,
  MRT_GlobalFilterTextField,
  MRT_ToggleFiltersButton,
  type MRT_ColumnDef
} from 'material-react-table'
import { Box, Button } from '@mui/material'
import NumericSlider from './NumericSlider'
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
  const stringFilters = [
    'equals',
    'contains',
    'fuzzy'
  ]
  const [numDemoEventsMax, setNumDemoEventsMax] = useState<number>(30)
  const handleNumDemoEventsMaxChange = (
    event: Event,
    newValue: number
  ): void => {
    console.log(
      'numDemoEventsMax: ',
      newValue,
      '\n',
      'event: ',
      event,
      '\n',
      'newValue: ',
      newValue
    )
    setNumDemoEventsMax(newValue)
  }
  const columns = useMemo<Array<MRT_ColumnDef<Course>>>(
    () => {
      return [
        {
          accessorKey: 'instructor',
          columnFilterModeOptions: stringFilters,
          header: 'Instructor',
          size: 100
        },
        {
          accessorKey: 'courseCode',
          columnFilterModeOptions: stringFilters,
          header: 'Course Code',
          size: 100
        },
        {
          accessorKey: 'year',
          columnFilterModeOptions: ['equals', 'greaterThan'],
          header: 'Year',
          size: 100
        },
        {
          accessorKey: 'term',
          columnFilterModeOptions: stringFilters,
          header: 'Term',
          size: 100
        },
        {
          accessorKey: 'numDemoEvents',
          filterFn: (
            row, id: string, filterValue: number
          ) => { return Number(row.getValue(id)) >= filterValue },
          // Filter: () => {
          //   <NumericSlider />
          // },
          header: '# Events',
          // filterVariant: 'range-slider',
          // Consider using a custom slider and custom filter function
          // muiFilterSliderProps: {
          //   max: 50,
          //   min: 1,
          //   onChange: handleNumDemoEventsMaxChange,
          //   value: numDemoEventsMax
          // },
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
      pagination: { pageIndex: 0, pageSize: 15 },
      showGlobalFilter: true
    },
    muiPaginationProps: {
      rowsPerPageOptions: [5, 15, 50, 200]
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
