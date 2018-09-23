from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, generics, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.filters import GoodsFilter
from goods.models import Goods, GoodsCategory
from goods.serializers import GoodsSerializer, CategorySerializer


class GoodsPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    # 默认每页显示的个数
    page_size = 12
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数 http://127.0.0.1:8000/goods/?page=2&page_size=30
    page_query_param = 'page'
    # 每页最多能显示多少体条
    # 仅当 page_size_query_param 设置时有效
    max_page_size = 20


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    商品列表页, 分页, 过滤, 排序
    '''
    queryset = Goods.objects.all().order_by('id')
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # 自定义过滤器
    filter_class = GoodsFilter
    # 搜索,默认模糊查询
    search_fields = ('name', 'goods_brief')
    # 排序
    ordering_fields = ('sold_num', 'shop_price')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:
        商品分类列表数据
    read:
        某一类商品(一级分类)
    '''

    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
