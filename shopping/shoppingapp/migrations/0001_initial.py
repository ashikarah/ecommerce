# Generated by Django 4.0.6 on 2022-07-11 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('desc', models.TextField(blank=True)),
                ('img', models.ImageField(blank=True, upload_to='gallery')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('desc', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='pic')),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingapp.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('name',),
            },
        ),
    ]
