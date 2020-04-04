from django.db import models



class Article(models.Model):    
    
    EVENT_MODE = (
        (0, 'Choose an option'),
    ( 1, 'Online Event'),
    ( 2, 'Offline Mode')    
    )

    title = models.CharField(max_length=120)
    content = models.TextField()
    datetime = models.DateTimeField( null=True ) 
    acm_fees = models.IntegerField( null=True )
    nonacm_fees = models.IntegerField( null=True )
    mode = models.IntegerField( choices = EVENT_MODE, default = 0 )
    reward = models.CharField(max_length=120 , null=True)

    def __str__(self):
        return self.title
    
    
class Propose_Article(models.Model):    
    title = models.CharField(max_length=120)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
    
    

    
    

