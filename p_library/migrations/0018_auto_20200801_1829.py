# Generated by Django 2.2.6 on 2020-08-01 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0017_auto_20200801_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='p_library.Author'),
        ),
        migrations.DeleteModel(
            name='Inspiration',
        ),
    ]