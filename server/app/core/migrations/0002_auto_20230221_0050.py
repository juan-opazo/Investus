# Generated by Django 3.2.18 on 2023-02-21 00:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='User_Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shares', models.DecimalField(decimal_places=2, max_digits=8)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.stock')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='owners',
            field=models.ManyToManyField(through='core.User_Stock', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('type', models.CharField(choices=[('CA', 'Cash'), ('FA', 'Factoring'), ('ST', 'Stocks')], max_length=2)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.stock')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
