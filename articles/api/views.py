# from rest_framework import viewsets

# class ArticleViewSet(viewsets.ModelViewSet):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()

from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from articles.models import Article, Propose_Article
from .serializers import ArticleSerializer, Propose_ArticleSerializer


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.AllowAny, )


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.AllowAny, )


class ArticleCreateView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ArticleUpdateView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ArticleDeleteView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticated, )




class P_ArticleListView(ListAPIView):
    queryset = Propose_Article.objects.all()
    serializer_class = Propose_ArticleSerializer
    permission_classes = (permissions.AllowAny, )


class P_ArticleDetailView(RetrieveAPIView):
    queryset = Propose_Article.objects.all()
    serializer_class = Propose_ArticleSerializer
    permission_classes = (permissions.AllowAny, )


class P_ArticleCreateView(CreateAPIView):
    queryset = Propose_Article.objects.all()
    serializer_class = Propose_ArticleSerializer
    permission_classes = (permissions.IsAuthenticated, )