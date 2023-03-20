# Generated by Django 4.1.7 on 2023-03-20 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlemanasChecasAustriacasAle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategoria', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('maltas', models.CharField(max_length=40)),
                ('lupulo', models.CharField(max_length=40)),
                ('levadura', models.CharField(max_length=40)),
                ('adicionales', models.CharField(max_length=40)),
                ('procesoDeCoccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AlemanasChecasAustriacasLager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategoria', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('maltas', models.CharField(max_length=40)),
                ('lupulo', models.CharField(max_length=40)),
                ('levadura', models.CharField(max_length=40)),
                ('adicionales', models.CharField(max_length=40)),
                ('procesoDeCoccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AmericanasAle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategoria', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('maltas', models.CharField(max_length=40)),
                ('lupulo', models.CharField(max_length=40)),
                ('levadura', models.CharField(max_length=40)),
                ('adicionales', models.CharField(max_length=40)),
                ('procesoDeCoccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Americanaslager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategoria', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('maltas', models.CharField(max_length=40)),
                ('lupulo', models.CharField(max_length=40)),
                ('levadura', models.CharField(max_length=40)),
                ('adicionales', models.CharField(max_length=40)),
                ('procesoDeCoccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BelgasFrancesasAle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategoria', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('maltas', models.CharField(max_length=40)),
                ('lupulo', models.CharField(max_length=40)),
                ('levadura', models.CharField(max_length=40)),
                ('adicionales', models.CharField(max_length=40)),
                ('procesoDeCoccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BritanicasAle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategoria', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('maltas', models.CharField(max_length=40)),
                ('lupulo', models.CharField(max_length=40)),
                ('levadura', models.CharField(max_length=40)),
                ('adicionales', models.CharField(max_length=40)),
                ('procesoDeCoccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='InternacionalesAle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategoria', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('maltas', models.CharField(max_length=40)),
                ('lupulo', models.CharField(max_length=40)),
                ('levadura', models.CharField(max_length=40)),
                ('adicionales', models.CharField(max_length=40)),
                ('procesoDeCoccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='InternacionalesLager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategoria', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('maltas', models.CharField(max_length=40)),
                ('lupulo', models.CharField(max_length=40)),
                ('levadura', models.CharField(max_length=40)),
                ('adicionales', models.CharField(max_length=40)),
                ('procesoDeCoccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Otras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategoria', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('maltas', models.CharField(max_length=40)),
                ('lupulo', models.CharField(max_length=40)),
                ('levadura', models.CharField(max_length=40)),
                ('adicionales', models.CharField(max_length=40)),
                ('procesoDeCoccion', models.CharField(max_length=200)),
            ],
        ),
    ]
