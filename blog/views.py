from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

# blog list up
class PostList(ListView):
    model = Post # 클래스명
    template_name = 'blog/index.html' # 렌더링할 템플릿

# def index(request):
#     posts = Post.objects.all().order_by('-pk')

#     return render(
#         request, 
#         'blog/index.html', 
#         {
#             'posts' : posts
#         }
#     )

class PostDetail(DetailView):
    model = Post # 클래스명

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post' : post,
        }
    )
