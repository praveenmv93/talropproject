from django.conf.urls import url
from django.urls import path

from .api_views import PostLists, PostCreate, RetrieveUpdateDestroyView
from .views import home, login_view, register, logout_request, create_post, post_view, PostLikeRedirectView, like_view, \
    testview, sampleindex, days, get_staff, add_staff, edit_staff, del_staff, ziping

urlpatterns = [
    path('', home, name='home'),
    path('login', login_view, name='login'),
    path('register', register, name='register'),
    path('logout', logout_request, name='logout'),
    path('thoughts', create_post, name='thoughts'),
    path('index', days, name='index'),
    path('test', testview, name='testview'),
    path('post/<int:id>/', post_view, name='post_detail'),
    path('like/<int:id>/', like_view, name='like_view'),
    path('ziping', ziping, name='ziping'),
    # path('post/<int:id>/like', PostLikeRedirectView.as_view(), name='like'),
    path('api/', PostLists.as_view(), name='posts'),
    path('api/post/', PostCreate.as_view(), name='post_create'),
    path('api/post/<int:id>', RetrieveUpdateDestroyView.as_view(), name='post_operatons'),


    # from here, all urls for vue.js project


    path('api/staff/', get_staff, name='get_staff'),
    path('api/add-staff/', add_staff, name='add_staff'),
    path('api/edit-staff/', edit_staff, name='edit_staff'),
    path('api/del-staff/', del_staff, name='del_staff'),

]
