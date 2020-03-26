from django.db import models

class Article(models.Model):
	article_title = models.CharField('Название попы', max_length = 100)
	article_text = models.TextField('Описание проблемы', max_length = 500)
	pub_date = models.DateTimeField('Дата публикации')

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	comment_date = models.DateTimeField('Дата комментария')
	comment_author = models.CharField('Автор комментария', max_length = 50)