from django.conf.urls import url
from django.urls import path

from .views import home, login_view, register, logout_request, create_post, post_view, PostLikeRedirectView, like_view

urlpatterns = [
    path('', home, name='home'),
    path('login', login_view, name='login'),
    path('register', register, name='register'),
    path('logout', logout_request, name='logout'),
    path('thoughts', create_post, name='thoughts'),
    path('post/<int:id>/', post_view, name='post_detail'),
    path('like/<int:id>/', like_view, name='like_view'),
    # path('post/<int:id>/like', PostLikeRedirectView.as_view(), name='like'),
]
