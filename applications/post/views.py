from rest_framework import generics
from applications.post.models import Post
from applications.post.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from applications.post.permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

# Create your views here.

# class CustomPagination(PageNumberPagination):
#     page_size = 1
#     page_size_query_param = 'page_size'
#     max_page_size = 10000

class Bla:
    # class PostListAPIView(generics.ListAPIView):
    #     queryset = Post.objects.all()
    #     serializer_class = PostSerializer

    # class PostCreateAPIView(generics.CreateAPIView):
    #     serializer_class = PostSerializer

    # class PostUpdateAPIView(generics.UpdateAPIView):
    #     queryset = Post.objects.all()
    #     serializer_class = PostSerializer
    #     lookup_field='id'

    # class PostDeleteAPIView(generics.DestroyAPIView):
    #     queryset = Post.objects.all()
    #     serializer_class = PostSerializer
    #     lookup_field='id'

        
    # class PostDetailAPIView(generics.RetrieveAPIView):
    #     queryset = Post.objects.all()
    #     serializer_class = PostSerializer
    #     lookup_field='id'
    pass


class PostListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsOwner]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['owner', 'title']
    search_fields = ['title']
    ordering_fileds = ['id']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # return super().perform_create(serializer)

    # def get_queryset(self): 
    #     queryset = super().get_queryset()
    #     # queryset = queryset.filter(owner=12)
    #     filter_owmer = self.request.query_params.get('owner')
    #     if filter_owmer:
    #         queryset = queryset.filter(owner=filter_owmer)
    #     return queryset

class PostDeleteDetailUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Post.objects.all()
    serializer_class = PostSerializer



