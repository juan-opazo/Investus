# Generated by Django 3.2.18 on 2023-02-21 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_investment_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='stock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.stock'),
        ),
    ]
