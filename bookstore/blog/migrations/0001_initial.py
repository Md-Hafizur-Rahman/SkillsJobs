# Generated by Django 4.0.5 on 2022-06-10 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('excerpt', models.TextField(null=True)),
                ('cat_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.category')),
            ],
        ),
    ]
