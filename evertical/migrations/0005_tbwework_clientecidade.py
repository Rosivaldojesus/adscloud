# Generated by Django 3.0 on 2020-09-28 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evertical', '0004_auto_20200921_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbwework',
            name='clienteCidade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='evertical.tbCidade'),
            preserve_default=False,
        ),
    ]
