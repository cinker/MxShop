from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.views import APIView
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from goods.filters import GoodsFilter
from goods.models import Goods, GoodsCategory, Banner, HotSearchWords
from goods.serializers import GoodsSerializer, CategorySerializer, BannerSerializer, IndexCategorySerializer, \
    HotWordsSerializer


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


class GoodsListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    商品列表页, 分页, 过滤, 排序
    '''
    queryset = Goods.objects.all().order_by('id')
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    throttle_classes = (UserRateThrottle, AnonRateThrottle)

    # authentication_classes = (TokenAuthentication,)
    # 自定义过滤器
    filter_class = GoodsFilter
    # 搜索,默认模糊查询
    search_fields = ('name', 'goods_brief')
    # 排序
    ordering_fields = ('sold_num', 'shop_price')

    # 商品点击数 + 1
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:
        商品分类列表数据
    read:
        某一类商品(一级分类)
    '''

    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页轮播图
    """
    queryset = Banner.objects.all().order_by("index")
    serializer_class = BannerSerializer


class IndexCategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页商品分类数据
    """
    # 获取is_tab=True（导航栏）里面的分类下的商品数据
    queryset = GoodsCategory.objects.filter(is_tab=True, name__in=["生鲜食品", "奶类食品"])
    serializer_class = IndexCategorySerializer


class HotSearchsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取热搜词列表
    """
    queryset = HotSearchWords.objects.all().order_by("-index")
    serializer_class = HotWordsSerializer
