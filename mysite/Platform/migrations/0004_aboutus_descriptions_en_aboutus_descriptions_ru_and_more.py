# Generated by Django 5.1.2 on 2024-11-03 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Platform', '0003_alter_contacts_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='descriptions_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='descriptions_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='nameperson_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='nameperson_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='profession_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='profession_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='company_en',
            field=models.CharField(choices=[('Group', 'Group'), ('Company', 'Company')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='company_ru',
            field=models.CharField(choices=[('Group', 'Group'), ('Company', 'Company')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='firstname_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='firstname_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='help_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='help_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='lastname_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='lastname_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='countrys_en',
            field=models.CharField(choices=[('America', 'America'), ('Germany', 'Germany'), ('Austria', 'Austria'), ('Italy', 'Italy'), ('Spain', 'Spain'), ('Greate Britain', 'Greate Britain'), ('China', 'China'), ('Latvia', 'Latvia'), ('Indonesia', 'Indonesia'), ('Holland', 'Holland'), ('Ireland', 'Ireland'), ('Cyprus', 'Cyprus'), ('Canada', 'Canada')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='countrys_ru',
            field=models.CharField(choices=[('America', 'America'), ('Germany', 'Germany'), ('Austria', 'Austria'), ('Italy', 'Italy'), ('Spain', 'Spain'), ('Greate Britain', 'Greate Britain'), ('China', 'China'), ('Latvia', 'Latvia'), ('Indonesia', 'Indonesia'), ('Holland', 'Holland'), ('Ireland', 'Ireland'), ('Cyprus', 'Cyprus'), ('Canada', 'Canada')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='higher_en',
            field=models.CharField(choices=[('Secondary Educations', 'Secondary Educations'), ('Higher Educations', 'Higher Educations'), ('Language courses for youth', 'Language courses for youth'), ('Children language camps', 'Children language camps')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='higher_ru',
            field=models.CharField(choices=[('Secondary Educations', 'Secondary Educations'), ('Higher Educations', 'Higher Educations'), ('Language courses for youth', 'Language courses for youth'), ('Children language camps', 'Children language camps')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='specializations_en',
            field=models.CharField(choices=[('IT Technologies', 'IT Technologies'), ('Business', 'Business'), ('Medicine', 'Medicine'), ('International Relationship', 'International Relationship'), ('Tourism', 'Tourism')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='specializations_ru',
            field=models.CharField(choices=[('IT Technologies', 'IT Technologies'), ('Business', 'Business'), ('Medicine', 'Medicine'), ('International Relationship', 'International Relationship'), ('Tourism', 'Tourism')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='exams_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='exams_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studyabroad',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='studyabroad',
            name='description_ru',
            field=models.TextField(null=True),
        ),
    ]