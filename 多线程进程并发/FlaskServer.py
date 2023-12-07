# Flask的基本使用
# 环境安装:pip install flask
# 通过render_template类返回模板静态页面
from flask import Flask, render_template
from time import sleep

# 实例化一个Flask对象
app = Flask(__name__)


# 创建视图函数和路由地址
@app.route('/bobo')
def index_1():
    sleep(2)
    # 通过render_template类返回模板静态页面
    return render_template('test.html')


@app.route('/jay')
# 通过render_template类返回模板静态页面
def index_2():
    sleep(2)
    return render_template('test.html')


@app.route('/tom')
def index_3():
    sleep(2)
    return render_template('test.html')


# debug=True开启调试模式
app.run(debug=True, )
