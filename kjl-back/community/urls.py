from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    # community
    path('',views.article_list_or_create),
    path('<int:article_pk>/', views.article_detail_or_update_or_delete),
    path('<int:article_pk>/comment/', views.comment_create),
    path('<int:article_pk>/<int:comment_pk>/', views.comment_update_or_delete)    
]