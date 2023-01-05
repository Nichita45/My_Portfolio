from django.urls import path
from base import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('blog/', views.posts, name='posts'),
    path('blog/create-post/', views.create_post, name='create_post'),
    path('blog/<int:id>', views.post, name='post'),
    path('blog/edit_post/<int:id>', views.edit_post, name='edit_post'),
    path('blog/delete_post/<int:id>', views.delete_post, name='delete_post'),
    path('signup/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login_user'),
]

