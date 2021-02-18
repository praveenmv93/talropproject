from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, \
    RetrieveUpdateDestroyAPIView

from myblog.models import Posts
from myblog.serializers import PostSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import ValidationError


class PostLists(ListAPIView):

    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('id',)
    search_fields = ('post', 'title')


""" dummy codes are below only """


class PostCreate(CreateAPIView):
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        try:
            post = request.data.get('content')
            # titlte = request.data.get('title')
            # content = request.data.get('content')
            if post is None or post == "":
                raise ValidationError("content must not be empty")

        except Exception as e:
            print("exceptions ", e)

        return super().create(request, *args, **kwargs)


class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    lookup_field = 'id'
    serializer_class = PostSerializer

    def delete(self, request, *args, **kwargs):
        post_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(post_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            product = response.data
            from django.core.cache import cache
            cache.set('product_data_{}'.format(product['id']),
                      {
                          'name': product['name'],
                          'content': product['content']
                      })
        return response
