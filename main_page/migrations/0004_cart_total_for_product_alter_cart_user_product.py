# Generated by Django 4.2.1 on 2023-05-12 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_alter_cart_user_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_for_product',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.product'),
        ),
    ]
