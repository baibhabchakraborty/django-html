# Generated by Django 3.1.1 on 2020-10-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPosts',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
