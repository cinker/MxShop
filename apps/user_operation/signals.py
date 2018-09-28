#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 下午 08:21
# @Author  : gao
# @File    : signals.py
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from user_operation.models import UserFav


# post_save : model变化方式
# sender : 变动的model
@receiver(post_save, sender=UserFav)
def create_userfav(sender, instance=None, created=False, **kwargs):
    if created:
        goods = instance.goods
        goods.fav_num += 1
        goods.save()


@receiver(post_delete, sender=UserFav)
def delete_userfav(sender, instance=None, created=False, **kwargs):
    goods = instance.goods
    goods.fav_num -= 1
    goods.save()
