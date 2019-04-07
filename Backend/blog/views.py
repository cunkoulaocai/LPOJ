from django.shortcuts import render
from .models import OJMessage,Blog
from .serializers import OJMessageSerializer,BlogSerializer
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .permission import LoginOnly,ManagerOnly

class OJMessageView(viewsets.ModelViewSet):
    queryset = OJMessage.objects.all().order_by("-id")
    serializer_class = OJMessageSerializer
    filter_fields = ('username','time')
    pagination_class = LimitOffsetPagination
    permission_classes = (LoginOnly,)

class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by("-id")
    serializer_class = BlogSerializer
    filter_fields = ('username','time')
    pagination_class = LimitOffsetPagination
    permission_classes = (ManagerOnly,)