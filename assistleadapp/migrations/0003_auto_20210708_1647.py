# Generated by Django 3.0 on 2021-07-08 11:17

from django.db import migrations, models
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assistleadapp', '0002_company_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin_url', models.CharField(max_length=250)),
                ('retrieval_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('linkedin_user', models.CharField(blank=True, max_length=250)),
                ('data', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
        migrations.DeleteModel(
            name='Company_Profile',
        ),
    ]
