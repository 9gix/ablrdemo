const path = require('path');

module.exports = {
  context: path.resolve(__dirname, 'frontend'),
  entry: {
    'personal-info': './personal-info',
    'income-info': './income-info',
    'contact-info': './contact-info'
  },
  module: {
      rules: [
        {
          test: /\.m?js$/,
          exclude: /(node_modules|bower_components)/,
          use: {
            loader: 'babel-loader'
          }
        }
      ]
    },
  output: {
    path: path.resolve(__dirname, "myinfo/static/js"),
    filename: '[name].js'
  }
};