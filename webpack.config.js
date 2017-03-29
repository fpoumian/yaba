const path = require("path")
const webpack = require('webpack')
const BundleTracker = require('webpack-bundle-tracker');
const BrowserSyncPlugin = require('browser-sync-webpack-plugin');
const ExtractTextPlugin = require("extract-text-webpack-plugin");

const STATIC_PATH = path.resolve(__dirname, 'src', 'static', 'yaba');

const extractLess = new ExtractTextPlugin({
    filename: "[name].css",
    // disable: process.env.NODE_ENV === "development"
});

module.exports = {
    context: __dirname,

    entry: path.resolve(STATIC_PATH, 'js', 'index'),

    output: {
        path: path.resolve(STATIC_PATH, 'bundles'),
        filename: "[name].js",
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
                    loader: "url-loader?limit=10000&mimetype=application/font-woff"
                }
            },
            {
                test: /\.woff2$/,
                use: {
                    loader: "url-loader?limit=10000&mimetype=application/font-woff2"
                }
            },
            {
                test: /\.(eot|ttf|svg|gif|png)$/,
                use: {
                    loader: "file-loader?name=[name].[ext]"
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
                // (which should be serving on http://localhost:800/)
                // through BrowserSync
                proxy: 'http://localhost:8000',
                reloadDelay: 300,
                reloadDebounce: 500
            },
            // plugin options
            {
                // prevent BrowserSync from reloading the page
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
