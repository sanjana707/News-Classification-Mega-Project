from django.db import models

# Create your models here.
from django.db import models

class News(models.Model):
    news_id=models.AutoField
    news_title=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()