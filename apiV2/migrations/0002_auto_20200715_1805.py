# Generated by Django 3.0.8 on 2020-07-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiV2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='bir',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job_email',
            field=models.EmailField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='location',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='pagibig',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='philhealth',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='province',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='region',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sss',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='street',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
