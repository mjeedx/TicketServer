# Generated by Django 2.2.12 on 2020-04-19 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0011_auto_20170922_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartridge',
            name='num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carts.Num'),
        ),
        migrations.AlterField(
            model_name='cartridge',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carts.Place'),
        ),
        migrations.AlterField(
            model_name='cartridge',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carts.Status'),
        ),
        migrations.AlterField(
            model_name='events',
            name='num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carts.Num'),
        ),
        migrations.AlterField(
            model_name='events',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carts.Place'),
        ),
        migrations.AlterField(
            model_name='events',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='carts.Status'),
        ),
        migrations.AlterField(
            model_name='num',
            name='modell',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carts.Modell'),
        ),
    ]
