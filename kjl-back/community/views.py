from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article,Comment
from .serializers import ArticleListSerializer,ArticleSerializer,CommentSerializer

# Create your views here.


@api_view(['GET','POST'])
def article_list_or_create(request):
    def article_list(request):
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles,many=True)
        return Response(serializer.data)

    def article_create(request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    if request.method == 'GET':
        return article_list(request)
    elif request.method == 'POST':
        return article_create(request)

@api_view(['GET','PUT','DELETE'])
def article_detail_or_update_or_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    def article_detail():
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def article_update():
        if request.user == article.user :
            serializer = ArticleSerializer(data=request.data,instance=article)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        
    def article_delete():
        if request.user == article.user :
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        return article_detail()
    elif request.method == 'PUT':
        return article_update()
    elif request.method == 'DELETE':
        return article_delete()

@api_view(['GET','POST'])
# comment는 list, create, update, delete
def comment_list_or_create(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    def comment_list():
        comments = article.comment_set.all()
        serializer = CommentSerializer(data=comments, many=True)
        return Response(serializer.data)
    def comment_create():
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            ### 여 아래부분 이해 안감
            comments = article.comment_set.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return comment_list()
    elif request.method == 'POST':
        return comment_create()

@api_view(['PUT','DELETE'])
def comment_update_or_delete(request,article_pk,comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def comment_update():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = article.comment_set.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)
            
    def comment_delete():
        if request.user == comment.user :
            comment.delete()
            comments = article.comment_set.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return comment_update()

    elif request.method == 'DELETE':
        return comment_delete()