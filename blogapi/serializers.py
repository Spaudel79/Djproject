from rest_framework import routers, serializers, viewsets
from news.models import Blog


class Blogserializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields='__all__'



