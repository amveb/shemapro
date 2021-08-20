# Generated by Django 2.2.18 on 2021-06-28 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_email',
            field=models.EmailField(max_length=255, verbose_name='Электронная почта'),
        ),
    ]
