from django.shortcuts import render
from blog.models import YptUser
import uuid
import datetime
# 跨域
from django.views.decorators.csrf import csrf_exempt
# 返回参数
from django.http import HttpResponse
# 分页
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# 传json
import json
from django.http import JsonResponse
# 分页
from django.core.paginator import Paginator
def show_page(request):
    #page = request.GET.get('page')
    #pageSize = int(request.GET.get('pageSize'))
    page = 1
    pageSize = 5
    response = {}
    book_list = YptUser.objects.all()
    paginator = Paginator(book_list, pageSize)
    response['total'] = paginator.count
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    response['list'] = json.loads(serializers.serialize("json", books))
    return JsonResponse(response)

def hello(request):
    return render(request, 'blog/index1.html')

def userlogin(request):
    name = request.GET.get("name")
    password = request.GET.get("password")
    user = YptUser.objects.filter(logname=name,password=password)
    if user != None:
        return JsonResponse({'name': 200, 'password': "登录成功!"})
    else:
        return JsonResponse({'name': 400, 'password': "登录失败!"})

# 请求
def hello_world(request):
    #if request.method == 'POST':
    user = YptUser.objects.create(
        userid = uuid.uuid1(),
        username =  '张三',
        password = '12456',
        position = '学生',
        creattime = datetime.datetime.now(),
        schooltime = datetime.datetime.now().strftime('2016-09-21'),
        logname = 'zs123123',
        schoolnumeral = 'xxxx0000xxxx',
        usertype = '启用',
        roleid = '无'
    )
    return JsonResponse({'result': 200, 'msg': '连接成功'})

# 接口
@csrf_exempt
def hello_woott(request):
    act = 0
    if request.method == 'GET':
        act = 1
    else:
        act = 2
    result = {'result': act, 'msg': '连接成功'}
    #json返回为中文
    return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")

# def articale_content(request):
#     article = BlogArticle.objects.all()[0]
#     title =article.title
#     content = article.content
#     date = article.publish_date
#     return_str = 'title: %s,content: %s' % (title,content)
#     return HttpResponse(return_str)
#
#
# def get_index_page(request):
#     all_artilce = BlogArticle.objects.all()
#     return render(request,'blog/index.html',
#                   {
#                       'aritle_list' : all_artilce
#                   })
# def log(request):
#     return render(request,'blog/logIn.html')
#
def kiss(request):
    return render(request,'blog/kiss.html')

def frame(request):
    return render(request,'blog/index.html')

def components(request):
    return render(request,'blog/components-blog-posts.html')

def add(request):
    return render(request,'blog/add-new-post.html')

def form(request):
    return render(request,'blog/form-components.html')

def tables(request):
    return render(request,'blog/tables.html')

def user(request):
    return render(request,'blog/user-profile-lite.html')

def errors(request):
    return render(request,'blog/errors.html')
#
#
#
# def get_detail_page(request,article_id):
#
#     curr_article = BlogArticle.objects.all()
#     ate = None
#     previous_index = None
#     next_index = None
#     previous_article = None
#     next_article = None
#     for index,curr in enumerate(curr_article):
#         if index == 0:
#             previous_index =1
#             next_index = previous_index + 1
#         elif index == len(curr_article) - 1:
#             previous_index = index
#             next_index = previous_index - 1
#         else:
#             previous_index = index - 1
#             next_index = index + 1
#         if curr.article_id == article_id:
#             ate = curr
#             previous_article = curr_article[0]
#             next_article = curr_article[1]
#             break
#     return render(request, 'blog/detail.html',
#                   {
#                       'curr_article': ate,
#                       'previous_article' : previous_article,
#                       'next_article': next_article
#                   })