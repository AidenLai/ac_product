# Generated by Django 3.2.6 on 2021-09-05 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aclab_productSystem', '0005_rename_product_productuser_key_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('isbn', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='Img/bookImg')),
            ],
        ),
        migrations.CreateModel(
            name='BookBorrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('return_day', models.DateTimeField(verbose_name='歸還日期')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='getBook', to='aclab_productSystem.book', verbose_name='借用書籍')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]