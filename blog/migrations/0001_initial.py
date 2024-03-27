# Generated by Django 5.0.3 on 2024-03-27 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=100, verbose_name='full_name')),
                ('image', models.ImageField(upload_to='media/blog/author/%Y/%m/%d', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': '1.Authors',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(help_text='write title', max_length=100, verbose_name='title')),
                ('author', models.CharField(help_text='write author name', max_length=30, verbose_name='author')),
                ('description', models.TextField(verbose_name='description')),
                ('article', models.CharField(max_length=255, verbose_name='article')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': '2.Posts',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': '3.Tags',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('comment', models.TextField(verbose_name='comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post', verbose_name='post')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': '4.Comments',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='posts', to='blog.tags', verbose_name='tag'),
        ),
    ]
