# Generated by Django 5.0.4 on 2024-05-25 11:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPLICATION', '0003_rename_createat_formations_create_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='formations',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='formations',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='formations',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='formations',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formations',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]