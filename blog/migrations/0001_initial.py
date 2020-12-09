# Generated by Django 3.1 on 2020-12-09 12:18

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('text', models.TextField(verbose_name='本文')),
                ('image', stdimage.models.StdImageField(blank=True, null=True, upload_to='thumbnails/')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='カテゴリ名')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='名無し', max_length=30, verbose_name='名前')),
                ('text', models.TextField(verbose_name='本文')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.article', verbose_name='紐付く記事')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category', verbose_name='カテゴリ'),
        ),
    ]
