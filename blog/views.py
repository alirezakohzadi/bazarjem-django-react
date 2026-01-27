from rest_framework import generics
from .serializers import BlogsSerializers
from .models import Blogs
from rest_framework.permissions import AllowAny

class BlogOptionDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializers
    lookup_field = "slug"
    
    
    
class AllBlogs(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializers
    