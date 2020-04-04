from rest_framework import serializers

from articles.models import Article, Propose_Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'datetime', 'acm_fees', 'nonacm_fees', 'reward')
        
        
        
class Propose_ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propose_Article
        fields = ('id', 'title', 'content')
        
        


        
        
    
