# Generated by Django 3.2.7 on 2021-09-24 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_products_has_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=2, null=True),
        ),
    ]