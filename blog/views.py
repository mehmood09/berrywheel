from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView

# Create your views here.
# GET all books or POST a new one
class BlogPostListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# GET one book, PUT/PATCH to update, DELETE to remove
class BlogPostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'  # We'll use the book's ID in the URL

class BlogPostList(APIView):
    def get(self, request, format=None):
        # Get he title from the query parameters (if none, default to empty string)
        title = request.query_params.get("title","")
        
        if title:
            # Filter the queryset based on the title 
            blog_posts = BlogPost.objects.filter(title__icontains=title) 
        else:
            # If no title is provided, return all blog posts
            blog_posts = BlogPost.objects.all()
            
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.date, status=status.HTTP_200_OK)