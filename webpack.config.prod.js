const path = require("path")
const webpack = require('webpack')
const BundleTracker = require('webpack-bundle-tracker');
const BrowserSyncPlugin = require('browser-sync-webpack-plugin');
const ExtractTextPlugin = require("extract-text-webpack-plugin");
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin');

const DIST_PATH = path.resolve(__dirname, 'src', 'yaba_core', 'static', 'site');
const SRC_PATH = path.resolve(__dirname, 'src', 'webpack');
const FONT_LOADERS_CONFIG = 'outputPath=./fonts/&publicPath=/static/site/fonts/';


// Webpack Plugins
const providePlugin = new webpack.ProvidePlugin({
  $: "jquery",
  jQuery: "jquery"
})

const bundleTracker = new BundleTracker({filename: './webpack-stats.prod.json'})

const extractLess = new ExtractTextPlugin({
  filename: "./css/[name].[contenthash].min.css"
});

const optimizeCssAssets = new OptimizeCssAssetsPlugin({
  assetNameRegExp: /\.min\.css$/g,
  cssProcessor: require('cssnano'),
  cssProcessorOptions: {discardComments: {removeAll: true}},
  canPrint: true
})

const uglifyJs = new webpack.optimize.UglifyJsPlugin()


// Webpack config
module.exports = {
  context: __dirname,

  entry: path.resolve(SRC_PATH, 'js', 'index'),

  output: {
    path: path.resolve(DIST_PATH),
    filename: "js/[name].[hash].min.js",
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
    providePlugin,
    bundleTracker,
    optimizeCssAssets,
    uglifyJs
  ],


  resolve: {
    modules: ['node_modules'],
    extensions: ['.js', '.jsx']
  }
  ,
};
