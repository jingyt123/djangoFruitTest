"""
Django settings for pythonDjangoFriut project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qk3*%nop@pn2th-_y)a)0$7kef$tw&o_2abm&x9by^e66*77gv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 下面是一些自定义添加的第三方应用和项目应用
    'tinymce',# django-tinymce 富文本编辑器
    # 'haystack', #全文搜索的框架
    #'djcelery', 将耗时的程序放到celery中执行
    'apps.cart',# 购物车
    'apps.goods',#商品
    'apps.order',# 订单
    'apps.user',#用户

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# urlconf 根文件配置
ROOT_URLCONF = 'dailyfresh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]# 配置模板文件路径
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION =  'dailyfresh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE':'django.db.backends.mysql',
        'NAME':'djangofruit',
        'HOST':'localhost',
        'PORT':'3306',
        'USER':'root',
        'PASSWORD':'123456'
    }
}

# 指定django认证系统使用的用户模型类
AUTH_USER_MODEL='user.User'


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# 配置静态文件目录
STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]

# 富文本编辑器配置
TINYMCE_DEFAULT_CONFIG={
    'theme':'advanced',
    'width':'600',
    'height':'400',
}
# 搜素haystack 配置
HAYSTACK_CONNECTIONS={
    'default':{
        #使用whoosh 引擎
        'ENGINE':'haystack.backends.whoosh_cn_backend.WhooshEngine',
        #索引文件路径
        'PATH':os.path.join(BASE_DIR,'whoosh_index')
    }
}
# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

#邮箱配置
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.163.com'
EMAIL_PORT=25
#发什么邮件的邮箱
EMAIL_HOST_USER='要使用的发送163邮箱'
#在邮箱中设置客户端授权密码
EMAIL_HOST_PASSWORD='stmp授权码'
#收件人看到的发件人
EMAIL_FROM='收件人看到的发件人名称'

# 设置django框架缓存的数据保存在rediss数据库中
CACHES={
    "default":"django_redis.cache.RedisCache",
    #设置django缓存的数据保存在redistribution数据库中
    "LOCATION":"redis://127.0.0.1:6379/5",
    "OPTIONS":{
        "CLIENT_CLASS":"django_redis.client.DefaultClient",
    }

}
# Django 的 session 存储设置
SESSION_ENGINE="django.contrib.session.backends.cache"
#设置session信息存储在 CACHES 配置default对应的redis 中
SESSION_CACHE_ALIAS="default"
#指定登录页面对应URL='/user/login'
LOGIN_URL='/user/login'
#指定Django保存文件使用的文件存储类
DEFAULT_FILE_STORAGE='urils.fdfs.storage.FDFSStorage'
#指定FDFS客户端配置文件的路径
FDFS_CLIENT_CONF=os.path.join(BASE_DIR,'utils/fdfs/client.conf')
#指定FDFS 系统中的Nginx的ip 和Port
FDFS_NGINX_URL='http://172.16.110.128:8888/'