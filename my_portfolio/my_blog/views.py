from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    #take all object's parameter

    return render(request,
                  'my_blog/posts/post_list.html',
                  {'posts': posts})
    #return site with |post| data from data base

def post_detail(request, year, month, day, post):
    details = get_object_or_404(Post, slug=post,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)

    #object that retrieves information from a database based on a post model

    return render(request,
                  'my_blog/posts/post_detail.html',
                  {'details': details}
                  )
    # return site with detail data |post|
