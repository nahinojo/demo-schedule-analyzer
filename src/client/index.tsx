import React from 'react'
import { createRoot } from 'react-dom/client'
import App from './App'

const root = document.getElementById('root') as HTMLDivElement | null
console.log('Executing index.tsx')
if (root !== null) {
  // Not actually rendering for some reason
  createRoot(root)
    .render(<App />)
}
