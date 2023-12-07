from django.shortcuts import render
from django.http import JsonResponse


# def chart_list(request):
#     """数据统计表"""
#     return render(request, 'chart_list.html')
#
#
# def chart_bar(request):
#     """构造柱状图数据"""
#     # 数据可以去数据库中获取
#     legend = ["小明", "小芳"]
#     series_list = [
#         {
#             "name": '小明',
#             "type": 'bar',
#             "data": [50, 20, 36, 10, 40, 20]
#         },
#         {
#             "name": '小芳',
#             "type": 'bar',
#             "data": [52, 22, 16, 40, 40, 30]
#         }
#     ]
#     x_axis = ['1月', '2月', '3月', '4月', '5月', '6月']
#     result = {
#         "status": True,
#         "data": {
#             'legend': legend,
#             'series_list': series_list,
#             'x_axis': x_axis
#         }
#     }
#     return JsonResponse(result)
#
#
# def chart_pie(request):
#     """构造饼图数据"""
#     db_data_list = [
#         {"value": 2332, "name": 'IT部门'},
#         {"value": 42842, "name": '运营'},
#         {"value": 2577, "name": '新媒体'},
#     ]
#     result = {
#         "status": True,
#         "data": db_data_list
#     }
#     return JsonResponse(result)
#
#
# def chart_line(request):
#     # 数据可以去数据库中获取
#     legend = ["上海", "广州"]
#     series_list = [
#         {
#             "name": '上海',
#             "type": 'line',
#             "stack": 'Total',
#             "data": [50, 20, 36, 10, 40, 20]
#         },
#         {
#             "name": '广州',
#             "type": 'line',
#             "stack": 'Total',
#             "data": [52, 22, 16, 40, 40, 30]
#         }
#     ]
#     x_axis = ['1月', '2月', '3月', '4月', '5月', '6月']
#     result = {
#         "status": True,
#         "data": {
#             'legend': legend,
#             'series_list': series_list,
#             'x_axis': x_axis
#         }
#     }
#     return JsonResponse(result)
#
#
# def highcharts(request):
#     """highcharts示例"""
#     return render(request, 'highcharts.html')
