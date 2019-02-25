# Generated by Django 2.1.5 on 2019-02-25 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('regtime', models.DateTimeField(auto_now=True)),
                ('logintime', models.DateTimeField(auto_now=True)),
                ('school', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('classes', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=50)),
                ('realname', models.CharField(max_length=50)),
                ('qq', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('type', models.IntegerField(default=1)),
                ('score', models.IntegerField(default=0)),
                ('des', models.CharField(max_length=500, null=True)),
                ('rating', models.IntegerField(default=1500)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('ac', models.IntegerField(default=0)),
                ('submit', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserSubmittion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('problemid', models.CharField(max_length=50)),
                ('problemtitle', models.CharField(max_length=50)),
                ('result', models.IntegerField(default=0)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
