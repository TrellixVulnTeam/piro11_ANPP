from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum, name='mysum'),
    re_path(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello, name='hello'),
    path('list1/', views.post_list1, name='post_list1'),
    path('list2/', views.post_list2, name='post_list2'),
    path('list3/', views.post_list3, name='post_list3'),
    path('excel/', views.excel_download, name='excel_download'),
]
