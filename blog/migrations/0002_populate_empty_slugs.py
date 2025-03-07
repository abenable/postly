# Generated by Django 5.1.6 on 2025-03-07 11:44

from django.db import migrations
from django.utils.text import slugify

def populate_empty_slugs(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Category = apps.get_model('blog', 'Category')

    # Handle Posts
    for post in Post.objects.filter(slug=''):
        base_slug = slugify(post.title)
        unique_slug = base_slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{base_slug}-{counter}"
            counter += 1
        post.slug = unique_slug
        post.save()

    # Handle Categories
    for category in Category.objects.filter(slug=''):
        base_slug = slugify(category.name)
        unique_slug = base_slug
        counter = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{base_slug}-{counter}"
            counter += 1
        category.slug = unique_slug
        category.save()

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_empty_slugs),
    ]
