"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from rest_framework_jwt.views import obtain_jwt_token
import xadmin
from django.urls import path, include, re_path
from django.views.static import serve
from MxShop.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls
from goods.views import GoodsListViewSet, CategoryViewSet, BannerViewset, HotSearchsViewset, IndexCategoryViewset
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
# 配置goods的url
router.register('goods', GoodsListViewSet, base_name='goods')
# 配置商品目录的url
router.register('categorys', CategoryViewSet, base_name="categorys")

# 配置首页轮播图的url
router.register('banners', BannerViewset, base_name="banners")
# 热搜词
router.register('hotsearchs', HotSearchsViewset, base_name="hotsearchs")
# 首页系列商品展示url
router.register('indexgoods', IndexCategoryViewset, base_name="indexgoods")

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('ueditor/', include('DjangoUeditor.urls')),
    # 文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    # drf文档，title自定义
    path('docs', include_docs_urls(title='幕学生鲜API')),
    # 商品列表页
    re_path('^', include(router.urls)),
    # token
    path('api-token-auth/', views.obtain_auth_token),
    # jwt的token认证接口
    path('jwt-auth/', obtain_jwt_token)
]
