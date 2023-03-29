# Generated by Django 4.1.7 on 2023-03-28 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppFinal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='americanasale',
            name='subCategoria',
        ),
        migrations.AddField(
            model_name='americanasale',
            name='emailDeContacto',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='americanasale',
            name='fechaDePublicacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='americanasale',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
