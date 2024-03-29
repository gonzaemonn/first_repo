# Generated by Django 4.0.4 on 2022-05-22 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='thumbnails/')),
            ],
        ),
    ]
