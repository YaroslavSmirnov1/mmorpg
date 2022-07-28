# Generated by Django 3.1.7 on 2021-04-05 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bulletin', '0004_auto_20210328_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='declaration',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользыватель'),
        ),
    ]
