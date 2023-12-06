# Generated by Django 4.2.7 on 2023-11-17 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_menu_order_number_alter_submenu_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submenu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='submenu', to='app.menu'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='order_number',
            field=models.IntegerField(null=True, unique=True, verbose_name='order number'),
        ),
    ]
