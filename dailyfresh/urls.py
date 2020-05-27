"""pythonDjangoFriut URL Configuration

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
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'^serach',include('haystack.urls')),  #全文检索框架
    path(r'^tinymce',include('tinymce.urls')),# 富文本编辑器 url
    path(r'^user/', include('apps.user.urls', namespace='user')),  # 用户模块 user.urls
    # path(r'^cart/', include('apps.cart.urls', namespace='cart')),  # 购物车模块
    # path(r'^order/', include('apps.order.urls', namespace='order')),  # 订单模块
    path(r'^', include('apps.goods.urls', namespace='goods')),  # 商品模块
    # 这里将网页首页默认放在goods模块路径下,其它模块url路径与其模块名相同,有利于url管理,但 url层级不能过长,一般再3级左右

]
