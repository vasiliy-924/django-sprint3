# Generated by Django 5.1.1 on 2025-03-24 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-created_at'], 'verbose_name': 'категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['name'], 'verbose_name': 'местоположение', 'verbose_name_plural': 'Местоположения'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pub_date'], 'verbose_name': 'публикация', 'verbose_name_plural': 'Публикации'},
        ),
    ]
