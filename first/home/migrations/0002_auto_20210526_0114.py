# Generated by Django 3.2.2 on 2021-05-25 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
