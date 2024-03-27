import React, { type FC } from 'react'
import { IconButton, useTheme } from '@mui/material'
import { Brightness4, Brightness7 } from '@mui/icons-material'

const ColorModeContext = React.createContext({
  toggleColorMode: () => {}
})

const ColorModeToggle: FC = () => {
  const theme = useTheme()
  const handleColorMode = React.useContext(ColorModeContext)
  return (
    <IconButton
      color="inherit" onClick={handleColorMode.toggleColorMode}
    >
      {theme.palette.mode === 'dark' ? <Brightness7 /> : <Brightness4 />}
    </IconButton>
  )
}

export { ColorModeContext, ColorModeToggle }
