from random import randrange

from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Bar3D
# from pyecharts.commons.utils import JsCode


app = Flask(__name__, static_folder="templates")


def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-基本示例",
                                      subtitle="我是副标题"),
            toolbox_opts=opts.ToolboxOpts(is_show=True))
    )
    return c


def bar_base2():
    js_code_str = '''
    function (params){
        var tt = ['1']
        return '{a} {tt[0]} {b}<br/>{c}{d}{e} {params} '
    }
    '''
    # [4,10,16,25,33,42,51,60,71]
    long_direction = ['71', '60', '51', '42', '33', '25', '16', '10', '4']
    wide_direction = ["东", "中", "西"]
    # data = [
    #     [0, 0, 29.8],
    #     [0, 1, 29.9],
    #     [0, 2, 30.6],
    #     [0, 3, 31.5],
    #     [0, 4, 30.8],
    #     [0, 5, 30.3],
    #     [0, 6, 29.9],
    #     [0, 7, 29.8],
    #     [0, 8, 28.8],
    #     [1, 0, 29.8],
    #     [1, 1, 29.3],
    #     [1, 2, 30.6],
    #     [1, 3, 30.6],
    #     [1, 4, 31.1],
    #     [1, 5, 31.2],
    #     [1, 6, 30.7],
    #     [1, 7, 29.1],
    #     [1, 8, 28.8],
    #     [2, 0, 29.8],
    #     [2, 1, 29.9],
    #     [2, 2, 30.6],
    #     [2, 3, 31.5],
    #     [2, 4, 30.8],
    #     [2, 5, 30.3],
    #     [2, 6, 29.9],
    #     [2, 7, 29.8],
    #     [2, 8, 28.8],
    # ]
    # data = [[long_direction[d[1]], wide_direction[d[0]], d[2]] for d in data]
    data = [
        [
            "71",
            "东",
            29.8
        ],
        [
            "60",
            "东",
            29.9
        ],
        [
            "51",
            "东",
            30.6
        ],
        [
            "42",
            "东",
            31.5
        ],
        [
            "33",
            "东",
            30.8
        ],
        [
            "25",
            "东",
            30.3
        ],
        [
            "16",
            "东",
            29.9
        ],
        [
            "10",
            "东",
            29.8
        ],
        [
            "4",
            "东",
            28.8
        ],
        [
            "71",
            "中",
            29.8
        ],
        [
            "60",
            "中",
            29.3
        ],
        [
            "51",
            "中",
            30.6
        ],
        [
            "42",
            "中",
            30.6
        ],
        [
            "33",
            "中",
            32.2
        ],
        [
            "25",
            "中",
            31.2
        ],
        [
            "16",
            "中",
            30.7
        ],
        [
            "10",
            "中",
            29.1
        ],
        [
            "4",
            "中",
            28.8
        ],
        [
            "71",
            "西",
            29.8
        ],
        [
            "60",
            "西",
            29.9
        ],
        [
            "51",
            "西",
            30.6
        ],
        [
            "42",
            "西",
            31.5
        ],
        [
            "33",
            "西",
            30.8
        ],
        [
            "25",
            "西",
            30.3
        ],
        [
            "16",
            "西",
            29.9
        ],
        [
            "10",
            "西",
            29.8
        ],
        [
            "4",
            "西",
            28.8
        ]
    ]
    c = (
        # init_opts=opts.InitOpts(width="1600px", height="800px")
        Bar3D()
        .add(
            series_name="温度/­°C",
            data=data,
            label_opts=opts.LabelOpts(is_show=False),
            xaxis3d_opts=opts.Axis3DOpts(
                type_="category", data=long_direction, name='站台号'),
            yaxis3d_opts=opts.Axis3DOpts(
                type_="category", data=wide_direction, name='位置'),
            zaxis3d_opts=opts.Axis3DOpts(
                type_="value", max_=33, min_=27, name="温度"),
        )
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                max_=33,
                min_=27,
                range_color=[
                    "#313695",
                    "#4575b4",
                    "#74add1",
                    "#abd9e9",
                    "#e0f3f8",
                    "#ffffbf",
                    "#fee090",
                    "#fdae61",
                    "#f46d43",
                    "#d73027",
                    "#a50026",
                ],
            ),
            title_opts=opts.TitleOpts(title="405捻线车间温度"),
            # tooltip_opts=opts.TooltipOpts(formatter='</br>{c}')
        )
    )
    return c.dump_options_with_quotes()


def bar_base3():
    long_direction = ['71', '60', '51', '42', '33', '25', '16', '10', '4']
    wide_direction = ["东", "中", "西"]
    data = [['71', '东', 39.8],
            ['60', '东', 39.9],
            ['51', '东', 40.6],
            ['42', '东', 41.5],
            ['33', '东', 40.8],
            ['25', '东', 40.3],
            ['16', '东', 39.9],
            ['10', '东', 39.8],
            ['4', '东', 38.8],
            ['71', '中', 39.8],
            ['60', '中', 39.3],
            ['51', '中', 40.6],
            ['42', '中', 40.6],
            ['33', '中', 42.2],
            ['25', '中', 41.2],
            ['16', '中', 40.7],
            ['10', '中', 39.1],
            ['4', '中', 38.8],
            ['71', '西', 39.8],
            ['60', '西', 39.9],
            ['51', '西', 40.6],
            ['42', '西', 41.5],
            ['33', '西', 40.8],
            ['25', '西', 40.3],
            ['16', '西', 39.9],
            ['10', '西', 39.8],
            ['4', '西', 38.8]]
    c = (
        Bar3D()
        .add(
            series_name="相对湿度/%",
            data=data,
            label_opts=opts.LabelOpts(is_show=False),
            xaxis3d_opts=opts.Axis3DOpts(
                type_="category", data=long_direction, name='站台号'),
            yaxis3d_opts=opts.Axis3DOpts(
                type_="category", data=wide_direction, name='位置'),
            zaxis3d_opts=opts.Axis3DOpts(
                type_="value", max_=45, min_=36, name="湿度"),
        )
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                max_=45,
                min_=36,
                range_color=[
                    "#313695",
                    "#4575b4",
                    "#74add1",
                    "#abd9e9",
                    "#e0f3f8",
                    "#ffffbf",
                    "#fee090",
                    "#fdae61",
                    "#f46d43",
                    "#d73027",
                    "#a50026",
                ],
            ),
            title_opts=opts.TitleOpts(title="405捻线车间湿度"),
            # tooltip_opts=opts.TooltipOpts(formatter=JsCode(js_code_str))
        )
    )
    return c.dump_options_with_quotes()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mobile")
def mobile():
    return render_template("mobile.html")


@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()


@app.route("/barChart2")
def get_bar_chart2():
    return bar_base2()

@app.route("/barChart3")
def get_bar_chart3():
    return bar_base3()


if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0',port=5000)