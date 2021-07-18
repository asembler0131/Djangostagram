# Generated by Django 3.2.5 on 2021-07-18 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': '포스트_태그',
                'verbose_name_plural': '포스트_태그',
                'db_table': 'post_tag',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('img_src', models.ImageField(upload_to='image', verbose_name='이미지주소')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='등록일')),
                ('dsuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.dsuser', verbose_name='작성자')),
                ('tags', models.ManyToManyField(related_name='tagged', to='post.Tag', verbose_name='태그')),
            ],
            options={
                'verbose_name': '포스트',
                'verbose_name_plural': '포스트',
                'db_table': 'post',
                'ordering': ('create_date',),
            },
        ),
    ]
