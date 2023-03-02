from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView, permission_classes
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from .models import Post
from .serializers import PostSerializer
from accounts.serializers import CurrentUserPostsSerializer
from .permissions import ReadOnly, AuthorOrReadOnly


class CustomPaginator(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = "page_size"


@api_view(http_method_names=["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def homepage(request: Request):
    if request.method == "POST":
        data = request.data
        response = {"data": data}
        return Response(data=response, status=status.HTTP_201_CREATED)

    response = {"message": "Hello"}
    return Response(data=response, status=status.HTTP_200_OK)


"""Creating a list API View using Function Based Views"""

# @api_view(http_method_names=["GET", "POST"])
# def list_posts(request: Request):
#     posts = Post.objects.all()

#     if request.method == "POST":
#         data = request.data
#         serializer = PostSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             response = {"message": "Post created successfully", "data": serializer.data}
#             return Response(data=response, status=status.HTTP_201_CREATED)

#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     serializer = PostSerializer(instance=posts, many=True)
#     return Response(data=serializer.data, status=status.HTTP_200_OK)


""" Creating Class Based APIView to list all the posts """


class PostListCreateView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    """
    a view for creating and listing posts
    """

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPaginator
    queryset = Post.objects.all()

    """using generic APIVIew and mixins"""

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
        return super().perform_create(serializer)

    @swagger_auto_schema(
        operation_summary="List all posts",
        operation_description="This returns a list of all posts"
    )
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a post",
        operation_description="This endpoint creates a post"
    )
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    """using normal class APIView to list and create"""
    # def get(self, request: Request, *args, **kwargs):
    #     posts = Post.objects.all()
    #     serializer = PostSerializer(instance=posts, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    # def post(self, request: Request, *args, **kwargs):
    #     data = request.data
    #     serializer = self.serializer_class(data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         response = {
    #             "message": "Post Created",
    #             "data": serializer.data,
    #         }

    #         return Response(data=response, status=status.HTTP_201_CREATED)

    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""Function based APIView to get, update and delete specific post"""
# @api_view(http_method_names=["GET"])
# def post_detail(request: Request, post_id:int):
#     post = get_object_or_404(Post, pk=post_id)
#     serializer = PostSerializer(instance=post)
#     response = {"message": "post", "data": serializer.data}
#     return Response(data=response, status=status.HTTP_200_OK)


# @api_view(http_method_names=["PUT"])
# def update_post(request:Request, post_id:int):
#     post = get_object_or_404(Post, pk=post_id)
#     data = request.data
#     serializer = PostSerializer(instance=post, data=data)

#     if serializer.is_valid():
#         serializer.save()
#         response = {
#             "message": "Post updated successfully",
#             "data": serializer.data
#         }
#         return Response(data=response, status=status.HTTP_200_OK)

#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(http_method_names=["DELETE"])
# def delete_post(request:Request, post_id:int):
#     post = get_object_or_404(Post, pk=post_id)
#     post.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)


class PostRetrieveUpdateDeleteView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = PostSerializer
    permission_classes = [AuthorOrReadOnly]
    queryset = Post.objects.all()

    """using generic APIView and mixins to retrieve, update and delete"""

    @swagger_auto_schema(
        operation_summary="Retrieve a post by id",
        operation_description="This endpoint retrieves a post by an id"
    )
    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a post by id",
        operation_description="This endpoint updates a post by an id"
    )
    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Deletes a post by id",
        operation_description="This endpoint deletes a post by an id"
    )
    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    """using normal Class APIView to retrieve, update, and delete"""
    # def get(self, request: Request, post_id: int, *args, **kwargs):
    #     post = get_object_or_404(Post, pk=post_id)
    #     serializer = self.serializer_class(instance=post)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    # def put(self, request: Request, post_id: int, *args, **kwargs):
    #     post = get_object_or_404(Post, pk=post_id)
    #     data = request.data
    #     serializer = self.serializer_class(instance=post, data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         response = {"message": "Post Updated Successfully", "data": serializer.data}
    #         return Response(data=response, status=status.HTTP_200_OK)

    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request: Request, post_id: int, *args, **kwargs):
    #     post = get_object_or_404(Post, pk=post_id)
    #     post.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated])
def get_current_user_posts(request: Request):
    user = request.user
    serializer = CurrentUserPostsSerializer(instance=user, context={"request": request})
    return Response(data=serializer.data, status=status.HTTP_200_OK)


class ListPostsForAuthor(
    generics.GenericAPIView, 
    mixins.ListModelMixin,
):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # user = self.request.user
        # first_name = self.kwargs.get("first_name")
        first_name = self.request.query_params.get("first_name") or None
        queryset = Post.objects.all()
        
        if first_name is not None:
            return Post.objects.filter(author__first_name=first_name)
        
        return queryset
    
    @swagger_auto_schema(
        operation_summary="List posts for an author (user)",
        operation_description="This endpoint retrieves a post by an id"
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
