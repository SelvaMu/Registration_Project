# Generated by Django 4.1.7 on 2023-02-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gapp', '0015_alter_employee_registration_database_employee_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer_Access_DataBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Incrementing_ID', models.IntegerField(null=True)),
                ('Employer_ID', models.CharField(max_length=100, null=True)),
                ('Student_Name', models.CharField(max_length=100)),
                ('Father_Mother_Name', models.CharField(max_length=100)),
                ('Email_ID', models.CharField(max_length=100)),
                ('Mobile_Number', models.CharField(max_length=100)),
                ('Aadhar_ID_Number', models.CharField(max_length=100)),
                ('Date_Of_Birth', models.DateField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('District', models.CharField(max_length=100)),
                ('Private_Job_Portal', models.CharField(max_length=100)),
                ('Physically_Disabled', models.CharField(max_length=100)),
                ('Registered_Date', models.DateField(max_length=100)),
                ('Highest_Qualification', models.CharField(max_length=100)),
                ('Qualified_Year', models.CharField(max_length=100)),
                ('Percentage', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Employeer_Access_DataBase',
        ),
    ]
