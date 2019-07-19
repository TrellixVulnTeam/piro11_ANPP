from django.shortcuts import render
from . models import Post

# Create your views here.

def post_list(request):
    qs = Post.objects.all()

    q = request.GET.get('q', '') #q가 있으면 가져오고 없으면 빈 문자열
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'blog/post_list.html',{
        'post_list':qs
    })