# Generated by Django 3.0 on 2020-09-21 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evertical', '0002_auto_20200921_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbpreventivas',
            name='manualSistema',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='evertical.tbSistemas'),
            preserve_default=False,
        ),
    ]
