from django.urls import path
import memo.views as views

urlpatterns = [
    path('', views.memo, name='memo'),
    path('create/', views.create_memo, name='create_memo'),
    path('<int:memo_id>/delete/', views.delete_memo, name='delete_memo'),
    path('<int:memo_id>/edit/', views.edit_memo, name='edit_memo'),
    path('<int:memo_id>/like/', views.like_memo, name='like_memo'),
]