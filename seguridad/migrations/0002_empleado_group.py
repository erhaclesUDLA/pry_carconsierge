# Generated by Django 2.2.4 on 2021-07-31 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('seguridad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='auth.Group'),
        ),
    ]
