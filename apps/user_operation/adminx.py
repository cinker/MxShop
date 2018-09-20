#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 下午 01:15
# @Author  : gao
# @File    : adminx.py
import xadmin
from user_operation.models import UserLeavingMessage, UserAddress, UserFav


class UserFavAdmin(object):
    list_display = ['user', 'goods', "add_time"]


class UserLeavingMessageAdmin(object):
    list_display = ['user', 'message_type', "message", "add_time"]


class UserAddressAdmin(object):
    list_display = ["signer_name", "signer_mobile", "district", "address"]

xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)