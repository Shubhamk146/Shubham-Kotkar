from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 


# Concrete View Classes
# The following classes are the concrete generic views. If you're using generic views this is normally the level you'll be working at unless you need heavily customized behavior.
# The view classes can be imported from rest_framework.generics.
# CreateAPIView
# Used for create-only endpoints.
# ListAPIView
# Used for read-only endpoints to represent a collection of model instances.
# RetrieveAPIView
# Used for read-only endpoints to represent a single model instance.
# DestroyAPIView
# Used for delete-only endpoints for a single model instance.
# UpdateAPIView
# Used for update-only endpoints for a single model instance.
# ListCreateAPIView
# Used for read-write endpoints to represent a collection of model instances.
# RetrieveUpdateAPIView
# Used for read or update endpoints to represent a single model instance.
# RetrieveDestroyAPIView
# Used for read or delete endpoints to represent a single model instance.
# RetrieveUpdateDestroyAPIView
# Used for read-write-delete endpoints to represent a single model instance.