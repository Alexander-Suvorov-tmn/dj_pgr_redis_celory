# Generated by Django 3.2.7 on 2021-09-08 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myparser', '0002_auto_20210908_0724'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('book', models.FileField(upload_to='files/%Y-%m-%d/')),
            ],
        ),
    ]