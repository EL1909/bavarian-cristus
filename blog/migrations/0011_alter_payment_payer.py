# Generated by Django 3.2.18 on 2024-10-28 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_payment_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]