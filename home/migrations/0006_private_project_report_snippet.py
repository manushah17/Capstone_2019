# Generated by Django 2.1.1 on 2019-04-01 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_public_project_report_snippet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Private_Project_Report_Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Private Project Report Snippet',
            },
        ),
    ]
