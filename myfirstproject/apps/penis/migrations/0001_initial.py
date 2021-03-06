# Generated by Django 3.0.4 on 2020-03-27 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=100, verbose_name='Название попы')),
                ('article_text', models.TextField(max_length=500, verbose_name='Описание проблемы')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(verbose_name='Дата комментария')),
                ('comment_author', models.CharField(max_length=50, verbose_name='Автор комментария')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='penis.Article')),
            ],
        ),
    ]
