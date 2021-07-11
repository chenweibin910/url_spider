# xadmin全局配置
import xadmin
from django.utils.safestring import mark_safe
# from kombu.transport.django import models as kombu_models
from xadmin import views

from .models import Home


class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "测试站点标题"  # 设置站点标题
    site_footer = "copyright@页脚"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠


class ThemeSettings(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, ThemeSettings)


# class KombuMessageAdmin:
#     search_fields = ["visible", "sent_at", "payload", "queue"]
#     list_display = ["visible", "sent_at", "show_payload", "queue"]
#     list_filter = ["visible", "sent_at", "payload", "queue"]
#     list_editable = ["visible", "sent_at", "payload", "queue"]
#     filter_horizontal = ["visible", "sent_at", "payload", "queue"]
#     ordering = ('id',)
#     model_icon = 'fa fa-book'

#     def show_payload(self, obj):
#         max_num = 100
#         if len(obj.payload) < max_num:
#             return mark_safe(obj.payload)
#         payload_dict = eval(obj.payload)
#         text = ""
#         for key, value in payload_dict.items():
#             # value = str(value)
#             if len(value) > max_num:
#                 text += "<b>{}</b>:".format(key)
#                 for i in range(0, len(value), max_num):
#                     text += "{}<br>".format(value[i:i + max_num])
#                 text += "<br>"
#                 continue
#             text += "<b>{}</b>: {}<br><br>".format(key, value)
#         return mark_safe(text)

#     show_payload.short_description = "数据"


# class KombuQueueAdmin:
#     list_display = ["id", "name"]


class HomeAdmin(object):
    site_title = "测试站点标题"  # 设置站点标题
    site_footer = "copyright@页脚"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠
    search_fields = ["id", "date", "exec_time", "info"]  # 检索字段
    list_display = ["id", "date", "exec_time", "show_info"]  # 要显示的字段
    list_filter = ["id", "date", "exec_time", "info"]  # 分组过滤的字段
    ordering = ('id',)  # 设置默认排序字段，负号表示降序排序
    list_per_page = 30  # 默认每页显示多少条记录，默认是100条
    model_icon = 'fa fa-book'  # 左侧小图标
    list_editable = ["date", "exec_time", "info"]  # 可编辑字段
    style_fields = {'date': 'm2m_transfer', 'exec_time': 'm2m_transfer'}  # 控制字段的显示样式
    filter_horizontal = ("date", "exec_time")  # 水平选择编辑多对多字段

    def show_info(self, obj):
        # 显示简介
        if not obj.info:
            return mark_safe('')
        if len(obj.info) < 50:
            return mark_safe(obj.info)

        short_id = f'{obj._meta.db_table}_short_text_{obj.id}'
        short_text_len = len(obj.info) // 4
        short_text = obj.info[:short_text_len] + '......'
        detail_id = f'{obj._meta.db_table}_detail_text_{obj.id}'
        detail_text = obj.info

        text = """<style type="text/css">
                        #%s,%s {padding:10px;border:1px solid green;} 
                  </style>
                    <script type="text/javascript">

                    function openShutManager(oSourceObj,oTargetObj,shutAble,oOpenTip,oShutTip,oShortObj){
                        var sourceObj = typeof oSourceObj == "string" ? document.getElementById(oSourceObj) : oSourceObj;
                        var targetObj = typeof oTargetObj == "string" ? document.getElementById(oTargetObj) : oTargetObj;
                        var shortObj = typeof oShortObj == "string" ? document.getElementById(oShortObj) : oShortObj;
                        var openTip = oOpenTip || "";
                        var shutTip = oShutTip || "";
                        if(targetObj.style.display!="none"){
                           if(shutAble) return;
                           targetObj.style.display="none";
                           shortObj.style.display="block";
                           if(openTip  &&  shutTip){
                            sourceObj.innerHTML = shutTip; 
                           }
                        } else {
                           targetObj.style.display="block";
                           shortObj.style.display="none";
                           if(openTip  &&  shutTip){
                            sourceObj.innerHTML = openTip; 
                           }
                        }
                        }
                    </script>
                    <p id="%s">%s</p>
                    <p><a href='###' onclick="openShutManager(this,'%s',false,'点击关闭','点击展开','%s')">点击展开</a></p>

                    <p id="%s" style="display:none">
                       %s
                    </p>
                    """ % (short_id, detail_id, short_id, short_text, detail_id, short_id, detail_id, detail_text)
        return mark_safe(text)

    show_info.short_description = '描述'


xadmin.site.register(Home, HomeAdmin)

# from djcelery.models import (
#     TaskState, WorkerState,
#     PeriodicTask, IntervalSchedule, CrontabSchedule,
# )


# class DjceleryPeriodicTaskAdmin:
#     list_display = ["id", "name", "task",  # "args", "kwargs", "queue", "exchange", "routing_key", "expires",
#                     "enabled", "last_run_at", "total_run_count", "date_changed", "description", "crontab", "interval"]
#     list_editable = ["enabled", "crontab", "interval"]
#     ordering = ("id",)


# class DjceleryCrontabAdmin:
#     list_display = ["id", "minute", "hour", "day_of_week", "day_of_month", "month_of_year"]
#     list_editable = ["minute", "hour", "day_of_week", "day_of_month", "month_of_year"]
#     ordering = ("id",)


# class DjceleryIntervalAdmin:
#     list_display = ["id", 'period', 'every']
#     list_editable = ['period', 'every']
#     ordering = ("id",)


# xadmin.site.register(IntervalSchedule, DjceleryIntervalAdmin)  # 存储循环任务设置的时间
# xadmin.site.register(CrontabSchedule, DjceleryCrontabAdmin)  # 存储定时任务设置的时间
# xadmin.site.register(PeriodicTask, DjceleryPeriodicTaskAdmin)  # 存储任务
# xadmin.site.register(TaskState)  # 存储任务执行状态
# xadmin.site.register(WorkerState)  # 存储执行任务的worker

# xadmin.site.register(kombu_models.Message, KombuMessageAdmin)
# xadmin.site.register(kombu_models.Queue, KombuQueueAdmin)
