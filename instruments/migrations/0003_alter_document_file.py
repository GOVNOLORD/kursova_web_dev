# Generated by Django 5.0 on 2023-12-16 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0002_applicant_pdf_file_alter_applicant_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='media/'),
        ),
    ]
