import React from 'react'
import { createRoot } from 'react-dom/client'
import App from './App'

document.addEventListener(
  'DOMContentLoaded', function () {
    const root = document.getElementById('root') as HTMLDivElement | null
    if (root !== null) {
      createRoot(root)
        .render(<App />)
    } else {
      throw Error('Root element not found.')
    }
  }
)
