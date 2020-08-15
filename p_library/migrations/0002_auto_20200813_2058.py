# Generated by Django 2.2.6 on 2020-08-13 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspiration',
            name='inspirer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inspired_works', to='p_library.Author'),
        ),
    ]
