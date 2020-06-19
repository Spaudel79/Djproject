from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Blogserializer
from news.models import Blog
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class BlogUserviewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = Blogserializer

