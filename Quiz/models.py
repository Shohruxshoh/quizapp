from django.db import models
from django.urls import reverse
 
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("category-list", args={self.slug})


class QuesModel(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True, help_text='Ex:option1')
    
    def __str__(self):
        return self.question