# Generated by Django 2.2.6 on 2020-07-24 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0012_auto_20200724_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='redaction',
        ),
        migrations.DeleteModel(
            name='Redaction',
        ),
    ]