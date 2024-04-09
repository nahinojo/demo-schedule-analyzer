const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  entry: {
    main: {
      filename: 'bundle.js',
      import: './index.tsx'
    }
  },
  mode: 'production',
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader', 'postcss-loader']
      }, 
      {
        exclude: /node_modules/,
        test: /\.tsx?$/,
        use: 'ts-loader'
      },
    ]
  },
  output: {
    path: path.resolve(
      __dirname, 'api/app/static/'
    )
  },
  performance: {
    maxAssetSize: 512000,
    maxEntrypointSize: 512000
  },
  resolve: {
    aliasFields: ['browser'],
    extensions: ['.tsx', '.ts', '.js']
  }
}