# flask pyecharts 数据可视化展示

## 安装依赖

```
pip install -r requirements.txt
```

## 启动

```
python3 app.py
```



## 学习笔记

### 允许其他主机访问

```
app.run(host='0.0.0.0',port=5000)
```

> 使用以上方式启动可能存在跨域问题，可以通过以下方式简单解决

```
var chart3 = echarts.init(document.getElementById('bar3'), 'white', {renderer: 'canvas'});
                $.ajax({
                    type: "GET",
                    url: window.location.origin + "/barChart3",
                    dataType: 'json',
                    success: function (result) {
                        chart3.setOption(result);
                    }
                });
```

在index.html页面的ajax请求中使用`window.location.origin`解决跨域问题

### pyecharts相关

官网文档 https://pyecharts.org/#/zh-cn/intro

[Flask 前后端分离模式整合](https://pyecharts.org/#/zh-cn/web_flask?id=flask-前后端分离)

#### [Step 0，Step 1 参见上面模板渲染章节内容](https://pyecharts.org/#/zh-cn/web_flask?id=step-0，step-1-参见上面模板渲染章节内容)

#### [Step 3: 新建一个 HTML 文件](https://pyecharts.org/#/zh-cn/web_flask?id=step-3-新建一个-html-文件)

新建 HTML 文件保存位于项目根目录的 templates 文件夹，这里以如下 index.html 为例. 主要用到了 `jquery` 和 `pyecharts` 管理的 `echarts.min.js` 依赖

**可以把使用到的`jquery.min.js`,`echarts.min.js`,`echarts-gl.min.js`放到本地的静态目录下提高访问速度。**

index.html

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Awesome-pyecharts</title>
    <script src="https://cdn.bootcss.com/jquery/3.0.0/jquery.min.js"></script>
    <script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts.min.js"></script>
</head>
<body>
    <div id="bar" style="width:1000px; height:600px;"></div>
    <script>
        $(
            function () {
                var chart = echarts.init(document.getElementById('bar'), 'white', {renderer: 'canvas'});
                $.ajax({
                    type: "GET",
                    url: "http://127.0.0.1:5000/barChart",
                    dataType: 'json',
                    success: function (result) {
                        chart.setOption(result);
                    }
                });
            }
        )
    </script>
</body>
</html>
```

#### [Step 4: 编写 flask 和 pyecharts 代码渲染图表](https://pyecharts.org/#/zh-cn/web_flask?id=step-4-编写-flask-和-pyecharts-代码渲染图表)

请将下面的代码保存为 app.py 文件并移至项目的根目录下。

目录结构如下

```shell
sunhailindeMacBook-Pro:pyecharts_flask sunhailin$ tree -L 1
.
├── app.py
└── templates
```

注: 目前由于 json 数据类型的问题，无法将 pyecharts 中的 JSCode 类型的数据转换成 json 数据格式返回到前端页面中使用。因此在使用前后端分离的情况下尽量避免使用 JSCode 进行画图。

app.py

```python
from random import randrange

from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Bar


app = Flask(__name__, static_folder="templates")


def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()


if __name__ == "__main__":
    app.run()
```

#### [Step 5: 运行项目](https://pyecharts.org/#/zh-cn/web_flask?id=step-5-运行项目)

```shell
$ python app.py
```

使用浏览器打开 [http://127.0.0.1:5000](http://127.0.0.1:5000/) 即可访问服务
