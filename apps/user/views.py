import re
from django.shortcuts import render,redirect

from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
# django内置好的认证系统函数
from django.contrib.auth import authenticate,login,logout
#django 认证中的用户登入检测
from django.contrib.auth.decorators import login_required
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from apps.user.models import User,Address
from apps.order.models import OrderInfo,OrderGoods
from celery_tasks import tasks


class RegisterVies(View):
    ''' 注册'''
    def get(self,request):
        '''显示'''
        return render(request,'register.html')
    def post(self,request):
        ''' 注册处理'''
        #1 . 接收参数
        username=request.POST.get('user_name')
        password=request.POST.get('pwd')
        email=request.POST.get('email')
        #2 参数校验（后端校验）
        #校验参数的完整性
        if not all([username,password,email]):
            return render(request,'register.html',{'errmsg':'数据不完整'})
        #校验邮箱格式
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$',email):
            return render(request,'register.html',{'errmsg':'邮箱格式不正确'})
        #校验用户名是否已经注册
        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            user=None
        if user is not None:
            return render(request,'register.html',{'errmsg':'用户名已注册'})
        # 3.业务处理：注册
        user=User.objects.create_user(username,email,password)
        user.is_active=0  # 用户注册完成后还未激活，即默认激活状态为0，待激活后为1
        user.save()
        # 注册之后，需要给用户的注册邮箱发送激活邮件，在激活邮件中需要包含激活链接
        # 激活链接: /user/active/用户id
        # 存在问题: 其他用户恶意请求网站进行用户激活操作
        # 解决问题: 对用户的信息进行加密，把加密后的信息放在激活链接中，激活的时候在进行解密
        # /user/active/加密后token信息

        #对用户的身份进行加密，生成激活token信息
        serializer=Serializer(settings.SECRET_KEY,3600*7)   # 第一个参数是不能透露的密钥, 第二个参数是 过期时间
        info={'confirm':user.id}
        #返回bytes类型, 加密后的数据
        token=serializer.dumps(info) # 加密用户 id
        # serializer.loads(token)   返回解密后的数据
        #str
        token=token.decode()
        return redirect(reversed('goods:index'))

