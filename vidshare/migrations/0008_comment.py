# Generated by Django 4.1.3 on 2022-11-13 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vidshare', '0007_author_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=55)),
                ('text', models.TextField(max_length=400)),
                ('date', models.DateField(auto_now_add=True)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='vidshare.video')),
            ],
        ),
    ]