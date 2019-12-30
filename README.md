2019/12/30
1、
import products.views
path('', products.views.product_list),

导入products.views,然后直接跳转到products(app)中去
2、html的共同部分引用的设置
设置：
A
{% block Name %}
B	
{% endblock Name %}
A

其中A为共同的部分，B为可以修改的部分，Name为该block的name，
引用：
{% extends "XXX.html" %}

{% block Name %}
A
{% endblock Name %}

其中 XXX.html为需要引用的html的名称
A为自己编写的部分
Name为需要引用的block的name
extends可以翻译为继承，继承xxx.html