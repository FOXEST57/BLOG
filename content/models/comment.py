from django.db import models
from django.contrib.auth.models import User
from .article import Article

class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='Article')
  content = models.TextField(verbose_name='Contenu')
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
  author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments', verbose_name='Auteur')  

  def __str__(self):
    return f'Commentaire sur {self.article.title}'