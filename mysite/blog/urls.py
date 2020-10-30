from django.conf.urls import url
from blog import views

urlpatterns=[
    url(r'^$',views.PostListView.as_view('post_list')),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<ok>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/new$',views.CreatePostView.as_view(),name='post_new'),
    url(r'^post/(?P<ok>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
    url(r'^post/(?P<ok>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
    url(r'^drafts/$',views.DraftListView.as_view(),name='post_draft_list'),
    url(r'post/(?P<ok>\d+)/comment/$',views.add_comment_to_post(),name='add_comment_to_post'),
    url(r'comment/(?P<ok>\d+)/approve/$',views.comment_approve(),name='comment_approve'),
    url(r'comment/(?P<ok>\d+)/remove/$',views.comment_remove(),name='comment_remove'),
    url(r'post/(?P<ok>\d+)/publish/$',views.post_publish(),name='post_publish'),
]
