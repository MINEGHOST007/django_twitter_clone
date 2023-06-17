
from django.urls import path
# from . import views
from .views import HomeView, ArticleView, AddView ,EditView ,RemoveView, CategoryView , LikeView , BookView, BookView2, ProfileView,CommentView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    # path('', views.home ,name="home" ),
    path('',HomeView.as_view(),name="home"),

    path('article/<int:pk>/', ArticleView.as_view(), name='detail_view'),

    path('share/' , AddView.as_view(), name="share" ),

    path('article/edit/<int:pk>/',EditView.as_view(),name="edit" ),

    path('article/delete/<int:pk>/',RemoveView.as_view(),name="delete" ),

    path('category/<str:cats>/', CategoryView , name='category'),

    path('like/<int:pk>',LikeView , name="like_post"),

    path('book/<int:pk>',BookView , name="book_post"),

    path('bookmark/<int:pk>/',BookView2,name="bookmark"),

    path('profile/<int:pk>/', ProfileView ,name="profile"),

    path('article/<int:pk>/comment',CommentView.as_view(), name="commentt")

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


# path('bookmark/<int:cats>/',BookView , name="book_post"),