# Generated by Django 5.1.1 on 2024-09-29 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_remove_usuario_is_active_remove_usuario_is_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rol',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
