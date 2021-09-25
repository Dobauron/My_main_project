from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.views.generic import ListView
from .forms import CommentForm
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    #take all object's parameter

    return render(request,
                  'my_blog/posts/post_list.html',
                  {'posts': posts})
    #return site with |post| data from data base

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'

    paginate_by = 5
    template_name = 'my_blog/posts/post_list.html'



def post_detail(request, year, month, day, post):
    details = get_object_or_404(Post, slug=post,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)

    # object that retrieves information from a database based on a post model

    comments = details.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = details
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'my_blog/posts/post_detail.html',
                  {'details': details,
                   'comments': comments,
                   'comment_form': comment_form})
    # return site with detail data |post|

