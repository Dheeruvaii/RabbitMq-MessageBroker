from django.db import models

# Create your models here.
# Create your models here.
class Quote(models.Model):
    title = models.CharField(max_length=50)
    likes = models.PositiveIntegerField(default=0)

    def __dir__(self):
        return self.title
    
class QuoteUser(models.Model):
    user_id=models.IntegerField(blank=True)
    quote_id=models.IntegerField(unique=True,blank=True)

    def __str__(self):
        return f"user_id{self(self.user_id)} product_id{str(self.quote_id)}"