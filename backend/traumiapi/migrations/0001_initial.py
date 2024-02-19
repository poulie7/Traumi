# Generated by Django 4.2.5 on 2024-02-19 09:17

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
                ('productName', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('onStock', models.BooleanField(default=False)),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
