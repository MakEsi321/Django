# Generated by Django 5.1.4 on 2024-12-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_articles_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Millionaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('net_worth', models.DecimalField(decimal_places=2, max_digits=15)),
                ('country', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.AlterModelOptions(
            name='articles',
            options={},
        ),
    ]
