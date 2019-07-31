from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import blog.views

urlpatterns =[
    path('hello_word',blog.views.hello_world),
    path("registerPage", blog.views.hello_woott, name='registerPage'),
    path("rest", blog.views.show_page),
    path("login", blog.views.hello),
    path("ajax", blog.views.userlogin),
    path("kiss", blog.views.kiss),
    path("frame", blog.views.frame),
    #静态页面
    path("components", blog.views.components),
    path("add", blog.views.add),
    path("form", blog.views.form),
    path("tables", blog.views.tables),
    path("user", blog.views.user),
    path("errors", blog.views.errors),
    # path('content',blog.views.articale_content),
    # path('index',blog.views.get_index_page),
    # #path('detail',blog.views.get_detail_page)
    # path('detail/<int:article_id>',blog.views.get_detail_page),
    # path('login/',blog.views.log),
    # path('kiss/',blog.views.kiss)
]

#设置静态文件路径
urlpatterns += staticfiles_urlpatterns()