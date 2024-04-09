import React, { type FC } from 'react'
import { IconButton, useTheme } from '@mui/material'
import DarkModeIcon from '@mui/icons-material/DarkMode'
import LightModeOutlinedIcon from '@mui/icons-material/LightModeOutlined'

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
      {theme.palette.mode === 'dark' ? <DarkModeIcon /> : <LightModeOutlinedIcon />}
    </IconButton>
  )
}

export { ColorModeContext, ColorModeToggle }
