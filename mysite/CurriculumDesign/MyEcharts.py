from django.http import HttpResponse
from django.shortcuts import render
from pyecharts import options as opts
from pyecharts.charts import Bar
from .InfoDeal import InfoDeal
from pyecharts.globals import ThemeType


def index(request):
    # 数据接口，连接数据库已处理好的数据
    rank_data = InfoDeal().return_rank_info()
    rank = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
        .add_xaxis(rank_data[0])
        .add_yaxis("得票数", rank_data[1],
                   # MarkPointOpts：标记点配置项
                   markpoint_opts=opts.MarkPointOpts(
            # 标记点数据
            data=[
                # MarkPointItem：标记点数据项
                opts.MarkPointItem(
                    # 标注名称
                    name="最大票数",

                    # 特殊的标注类型，用于标注最大值最小值等。可选:
                    # 'min' 最大值、'max' 最大值 、'average' 平均值。
                    # 自己试了一下，如果同时设置type_和coord，只会显示coord的标记点
                    # type_ = 'min',
                    type_='max',
                ), opts.MarkPointItem(
                    # 标注名称
                    name="最小票数",

                    # 特殊的标注类型，用于标注最大值最小值等。可选:
                    # 'min' 最大值、'max' 最大值 、'average' 平均值。
                    # 自己试了一下，如果同时设置type_和coord，只会显示coord的标记点
                    # type_ = 'min',
                    type_='min',
                )
            ]))
        .set_series_opts(title_opts=opts.TitleOpts(title="选票前10名学生排行", subtitle="名字"))
        .set_global_opts(
        xaxis_opts=opts.AxisOpts(
            axislabel_opts={"rotate":45}
        )
    ))

    data={'rank': rank.render_embed()}
    return render(request, 'rank.html', {'c': data})
