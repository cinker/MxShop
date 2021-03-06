"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic import TemplateView
from django.views.static import serve
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from django.urls import path, include, re_path

from MxShop.settings import MEDIA_ROOT
from goods.views import GoodsListViewSet, CategoryViewSet, BannerViewset, IndexCategoryViewset, HotSearchsViewset
from trade.views import ShoppingCartViewset, OrderViewset, AlipayView
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from users.views import SmsCodeViewset, UserViewset

router = DefaultRouter()
# 配置商品的url
router.register(r'goods', GoodsListViewSet, base_name='goods')

# 配置Category的url
router.register(r'categorys', CategoryViewSet, base_name="categorys")

# 配置code的url
router.register(r'code', SmsCodeViewset, base_name="code")

# 注册
router.register(r'users', UserViewset, base_name="users")

# 配置用户收藏的url
router.register(r'userfavs', UserFavViewset, base_name="userfavs")

# 配置用户留言的url
router.register(r'messages', LeavingMessageViewset, base_name="messages")

# 配置收货地址
router.register(r'address', AddressViewset, base_name="address")

# 配置购物车的url
router.register(r'shopcarts', ShoppingCartViewset, base_name="shopcarts")

# 配置订单的url
router.register(r'orders', OrderViewset, base_name="orders")

# 配置首页轮播图的url
router.register(r'banners', BannerViewset, base_name="banners")

# 首页系列商品展示url
router.register(r'indexgoods', IndexCategoryViewset, base_name="indexgoods")

# 首页热搜词
router.register(r'hotsearchs', HotSearchsViewset, base_name="hotsearchs")

urlpatterns = [

    # 首页
    path('index/', TemplateView.as_view(template_name='index.html'),name='index'),
    path('admin/', xadmin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    re_path('^', include(router.urls)),
    path('docs/', include_docs_urls(title='生鲜超市')),

    # drf token
    path('api-token-auth/', views.obtain_auth_token),
    # jwt token
    path('login/', obtain_jwt_token),

    # 配置支付宝支付相关接口的url
    path('alipay/return/', AlipayView.as_view())
]
