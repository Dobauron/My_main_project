from django.urls import path


from .views import post_list, post_detail, PostListView

app_name = "my_blog"


urlpatterns = (
    path('blog/tag/<slug:tag_slug>/', post_list, name='post_list'),
    path('blog/', post_list, name='post_list'),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail,
         name= 'post_detail'),
)