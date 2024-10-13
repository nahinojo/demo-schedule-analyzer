import React from 'react'
import { createRoot } from 'react-dom/client'
import App from './App'
import axios from 'axios'

axios.get_by_id('http://127.0.0.1:5000/test')
  .then(response => {
    console.log(response)
  })
  .catch(error => {
    console.error('Test API call failed')
    console.error(error)
  })

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
