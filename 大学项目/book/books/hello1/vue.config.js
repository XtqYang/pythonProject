const {defineConfig} = require('@vue/cli-service')
module.exports = defineConfig({



    publicPath: './',


    lintOnSave: false,
    transpileDependencies: true,
    // 反向代理配置
    // devServer的配置
    devServer: {



    // 设置为 0.0.0.0 以允许外部访问
    host: '0.0.0.0',
    // 允许所有主机头
    allowedHosts: 'all',



        // 自定义端口
        port: 8080,
        // 自动打开浏览器
        open: true,



        // 用于配置反向代理
        proxy: {
            // 代理请求， 匹配所有以/api开头的请求
            '/api': {
                // 目标服务器，所有以/api开头的请求接口代理到目标服务器
                // target: 'https://5ju9367358.oicp.vip/',
                target: 'http://127.0.0.1:8000/',
                // 重写路径，此时用于匹配反向代理的/api可以替换为空
                pathRewrite: {'^/api': '/api'},
                // 如果代理到HTTPS服务器需要设置secure为true，默认为false
                secure: false
            }
        }


    }
})
