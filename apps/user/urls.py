from django.conf.urls import url
# from apps.user.views import RegisterView  # RegisterView为即将要实现的注册图类

app_name='user'

urlpatterns=[
    # url(r'^register$',RegisterView.as_view(),name='register'),  #注册
]

# 为了后续URL调整方便，我们为该路径起名register ，因此在模板中可以反解析该url使用
#{% url 'user:register' %}