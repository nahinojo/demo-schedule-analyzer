import React, { type FC } from 'react'
import { Box, IconButton, useTheme } from '@mui/material'
import { Brightness4, Brightness7 } from '@mui/icons-material'

const ColorModeContext = React.createContext({
  toggleColorMode: () => {}
})

const ColorModeToggle: FC = () => {
  const theme = useTheme()
  const handleColorMode = React.useContext(ColorModeContext)
  return (
    <Box
      sx={
        {
          alignItems: 'center',
          bgcolor: 'background.default',
          borderRadius: 1,
          color: 'text.primary',
          display: 'flex',
          justifyContent: 'center',
          p: 0
        }
      }
    >
      <IconButton
        color="inherit" sx={{ mr: 1 }} onClick={handleColorMode.toggleColorMode}
      >
        {theme.palette.mode === 'dark' ? <Brightness7 /> : <Brightness4 />}
      </IconButton>
    </Box>
  )
}

export { ColorModeContext, ColorModeToggle }
