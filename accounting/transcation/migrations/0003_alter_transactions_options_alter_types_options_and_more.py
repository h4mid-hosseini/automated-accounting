# Generated by Django 4.2.7 on 2023-11-24 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcation', '0002_types_transactions_is_cost_transactions_price_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transactions',
            options={'verbose_name': 'transaction', 'verbose_name_plural': 'transactions'},
        ),
        migrations.AlterModelOptions(
            name='types',
            options={'verbose_name': 'type', 'verbose_name_plural': 'types'},
        ),
        migrations.AlterField(
            model_name='transactions',
            name='extra_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]