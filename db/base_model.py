'''
用户模块
用户表： df_user
地址表： df_address
商品模块
  商品种类表(df_goods_type)
  商品SPU表(df_goods)
  商品SKU表(df_goods_sku)
  商品图片表(df_goods_image)
  首页轮播商品表(df_index_banner)
  首页促销活动表(df_index_promotion)
  首页分类商品展示表(df_index_type_goods)
3) 购物车模块
  redis实现
4）订单模块
  订单信息表(df_order_info)
  订单商品表(df_order_goods)

对于一对多的关系，应该设计两张表，并且多表中存放外键
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
vim /etc/apt/sources.list

'''
from django.db import models

class BaseModel(models.Model):
    # 抽象模型基类
    create_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')  # auto_now_add, 为添加的时间，更新对象不会变动
    update_time=models.DateTimeField(auto_now=True,verbose_name='更新时间')
    is_delete=models.BooleanField(default=False,verbose_name='删除标记时间')
    class Meta:
        #指定这个类是一个抽象模型类
        abstract=True

