# Generated by Django 5.0.2 on 2024-03-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_len', models.IntegerField()),
                ('text_len', models.IntegerField()),
            ],
        ),
    ]
