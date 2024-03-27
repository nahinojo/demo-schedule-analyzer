import React from 'react'
import { CoursesTable } from './components'
import { ColorModeContext } from './components/ColorMode'
import { createTheme, ThemeProvider } from '@mui/material/styles'

import type { FC } from 'react'
import './style.css'
import { CssBaseline } from '@mui/material'

const App: FC = () => {
  const [mode, setMode] = React.useState<'light' | 'dark'>('light')
  const colorMode = React.useMemo(
    () => {
      return {
        toggleColorMode: () => {
          setMode((prevMode: 'light' | 'dark') => { return (prevMode === 'light' ? 'dark' : 'light') })
        }
      }
    }, []
  )
  const theme = React.useMemo(
    () => {
      return createTheme({
        palette: {
          mode
        }
      })
    }, [mode]
  )
  return (
    <ColorModeContext.Provider
      value={colorMode}
    >
      <ThemeProvider
        theme={theme}
      >
        <CssBaseline
          enableColorScheme={true}
        />
        <div>
          <div
            className='max-w-screen-xl mx-auto mt-4'
            id='table-wrapper'
          >
            <CoursesTable />
          </div>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  )
}

export default App
