/* eslint-disable @typescript-eslint/no-var-requires */
const autoprefixer = require('autoprefixer')
const tailwindcss = require('tailwindcss')

module.exports = {
  plugins: [
    autoprefixer,
    'postcss-preset-env',
    tailwindcss
  ]
}