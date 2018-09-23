#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 下午 02:16
# @Author  : gao
# @File    : serializers.py
from rest_framework import serializers

from goods.models import Goods, GoodsCategory


# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


# ModelSerializer实现商品列表页
class GoodsSerializer(serializers.ModelSerializer):
    # 覆盖外键字段
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'


class CategorySerializer3(serializers.ModelSerializer):
    '''
    三级分类
    '''

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    '''
    二级分类
    '''
    # 在parent_category字段中定义的related_name="sub_cat"
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    商品一级类别序列化
    """
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"