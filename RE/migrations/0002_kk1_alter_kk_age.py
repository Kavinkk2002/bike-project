# Generated by Django 4.1.5 on 2023-09-05 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RE', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='kk1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=20)),
                ('Age', models.IntegerField(default='')),
                ('Department', models.CharField(default='', max_length=20)),
                ('Address', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='kk',
            name='Age',
            field=models.IntegerField(default=''),
        ),
    ]
