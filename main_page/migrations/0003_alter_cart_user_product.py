# Generated by Django 4.2 on 2023-04-29 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.category'),
        ),
    ]
