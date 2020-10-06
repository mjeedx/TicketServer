# Generated by Django 2.2.12 on 2020-04-19 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_auto_20191210_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='is_shief',
        ),
        migrations.AddField(
            model_name='contacts',
            name='is_chief',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='company_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contacts.Company'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='department_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contacts.Department'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='mail_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contacts.Mail'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='position_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contacts.Position'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='tel_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contacts.Tel'),
        ),
    ]
