# Generated by Django 4.2 on 2024-08-15 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, verbose_name='Название категорий')),
                ('slug', models.SlugField(max_length=255, verbose_name='Слаг категорий')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название поста:')),
                ('text', models.TextField(verbose_name='Текст поста:')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='1 картинка для поста(не объязательно):')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='2 картинка для поста(не объязательно):')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='3 картинка для поста(не объязательно):')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.category')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
