# Generated by Django 4.2.7 on 2023-11-17 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_submenu_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submenu',
            name='order_number',
            field=models.IntegerField(null=True, verbose_name='order number'),
        ),
    ]