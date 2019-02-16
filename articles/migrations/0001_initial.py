# Generated by Django 2.1.5 on 2019-01-18 15:39

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
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('title', models.TextField(help_text='Ce titre sera affiché en haut en h1 et sera en title de la page. Garder 50-60 caractères si possible.', max_length=100, verbose_name="Titre de l'article")),
                ('subtitle', models.TextField(max_length=100, verbose_name="Sous-titre de l'article")),
                ('content', models.TextField(help_text="Le contenu de l'article est en HTML", verbose_name="Contenu de l'article")),
                ('slug', models.TextField(help_text="Ce champ sera présent dans l'URL de l'article pour aider le référencement et donner du sens à l'URL.", verbose_name="Sous-URL de l'article")),
                ('is_display', models.TextField(default=True, help_text="Définit si l'article doit être consultable", verbose_name='Article visible ?')),
                ('is_index', models.TextField(default=True, help_text="Définit si l'article doit être indexé et affiché sur la liste des articles", verbose_name='Article indéxé ?')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="Auteur de l'article")),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
    ]
