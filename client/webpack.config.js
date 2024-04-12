const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')

const buildPath = () => {
  apiStaticDir = '/api/app/static/'
  endDir = __dirname.split(path.sep).at(-1)
  if (endDir === 'client') {
    return path.resolve(__dirname, `../${apiStaticDir}`)
  } else {
    return path.resolve(__dirname, `./${apiStaticDir}`)
  }
}

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
    path: buildPath()
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