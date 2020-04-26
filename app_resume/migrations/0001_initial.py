# Generated by Django 3.0.2 on 2020-04-18 22:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Showresume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', ckeditor.fields.RichTextField(max_length=750, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('link', models.CharField(max_length=70, null=True)),
            ],
        ),
    ]
