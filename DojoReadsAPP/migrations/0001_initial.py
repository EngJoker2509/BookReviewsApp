# Generated by Django 3.0 on 2023-01-03 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LoginAndRegAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=45, null=True)),
                ('review', models.CharField(max_length=255, null=True)),
                ('rating', models.IntegerField(null=True)),
                ('author', models.ManyToManyField(related_name='author_book', to='DojoReadsAPP.authors')),
            ],
        ),
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewBook', to='DojoReadsAPP.books')),
                ('review_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewUser', to='LoginAndRegAPP.User')),
            ],
        ),
    ]
