# Generated by Django 4.1.7 on 2023-05-06 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_main', '0002_contacts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.RenameField(
            model_name='contacts',
            old_name='enail',
            new_name='email',
        ),
    ]