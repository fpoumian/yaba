const path = require("path")
const webpack = require('webpack')
const BundleTracker = require('webpack-bundle-tracker');
const BrowserSyncPlugin = require('browser-sync-webpack-plugin');
const ExtractTextPlugin = require("extract-text-webpack-plugin");

const DIST_PATH = path.resolve(__dirname, 'src', 'yaba_core', 'static', 'site');
const SRC_PATH = path.resolve(__dirname, 'src', 'webpack');
const FONT_LOADERS_CONFIG = 'outputPath=./fonts/&publicPath=/static/site/fonts/';

const extractLess = new ExtractTextPlugin({
  filename: "./css/[name].css"
});

module.exports = {
  context: __dirname,

  entry: path.resolve(SRC_PATH, 'js', 'index'),

  output: {
    path: path.resolve(DIST_PATH),
    filename: "js/[name].js",
  },

  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: [
          {
            loader: 'babel-loader',
            options: {
              presets: [
                ['es2015', {modules: false}]
              ]
            }
          }
        ]
      },
      {
        test: /\.less$/,
        use: extractLess.extract({
          use: [{
            loader: "css-loader"
          }, {
            loader: "less-loader"
          }],
          // use style-loader in development
          fallback: "style-loader"
        })
      },
      {
        test: /\.woff$/,
        use: {
          loader: "url-loader?limit=10000&mimetype=application/font-woff&name=[hash].[ext]&" + FONT_LOADERS_CONFIG
        }
      },
      {
        test: /\.woff2$/,
        use: {
          loader: "url-loader?limit=10000&mimetype=application/font-woff2&name=[hash].[ext]&" + FONT_LOADERS_CONFIG
        }
      },
      {
        test: /\.(eot|ttf)$/,
        use: {
          loader: "file-loader?name=[name].[ext]&" + FONT_LOADERS_CONFIG
        }
      },
      {
        test: /\.(svg|gif|png)$/,
        use: {
          loader: "file-loader?name=./img/[name].[ext]"
        }
      }
    ]
  },

  plugins: [
    extractLess,
    new webpack.ProvidePlugin({
      $: "jquery",
      jQuery: "jquery"
    }),
    new BundleTracker({filename: './webpack-stats.json'}),
    new BrowserSyncPlugin(
      // BrowserSync options
      {
        // browse to http://localhost:3000/ during development
        host: 'localhost',
        port: 3000,
        // proxy the Django Dev Server endpoint
        // (which should be serving on http://localhost:8000/)
        // through BrowserSync
        proxy: 'http://localhost:8000',
        reloadDelay: 300,
        reloadDebounce: 500
      },
      // plugin options
      {
        reload: true
      }
    )
  ],

  resolve: {
    modules: ['node_modules'],
    extensions: ['.js', '.jsx']
  }
  ,
};
