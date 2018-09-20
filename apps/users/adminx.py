#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 下午 01:15
# @Author  : gao
# @File    : adminx.py
import xadmin
from users.models import VerifyCode
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "慕学生鲜后台"
    site_footer = "mxshop"
    menu_style = "accordion"


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)