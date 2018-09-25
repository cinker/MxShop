#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 下午 05:52
# @Author  : gao
# @File    : filters.py
import django_filters
from django.db.models import Q

from goods.models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    '''
    商品过滤的类
    '''
    # 两个参数，field_name是要过滤的字段，lookup是执行的行为，‘小与等于本店价格’
    pricemin = django_filters.NumberFilter(field_name="shop_price", lookup_expr='gte', label='最低价')
    pricemax = django_filters.NumberFilter(field_name="shop_price", lookup_expr='lte', label='最高价')
    top_category = django_filters.NumberFilter(method='top_category_filter', label='分类ID')

    # 自定义过滤方法,不管当前点击的是一级分类二级分类还是三级分类，都能找到。
    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'is_hot']
