# Generated by Django 5.1.2 on 2024-11-02 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Platform', '0002_remove_contacts_home_contacts_help'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='company',
            field=models.CharField(choices=[('Group', 'Group'), ('Company', 'Company')], max_length=100),
        ),
    ]