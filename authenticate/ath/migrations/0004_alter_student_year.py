# Generated by Django 5.0.1 on 2024-02-17 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ath', '0003_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]