# Generated by Django 4.1 on 2022-08-09 16:37

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=150)),
                ('count', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CollegeNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='News_image/')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('event_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('cap_id', models.CharField(max_length=50)),
                ('course', models.CharField(choices=[('bca', 'BCA'), ('bba', 'BBA'), ('bcom', 'BCOM'), ('ba-english', 'BA-ENGLISH'), ('bsc-physics', 'BSC-PHYSICS'), ('mcom', 'MCOM'), ('msc-physics', 'MSC-PHYSICS')], max_length=128)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=128)),
                ('student_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('father_name', models.CharField(max_length=128)),
                ('mother_name', models.CharField(max_length=128)),
                ('parent_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('institution', models.CharField(max_length=128)),
                ('month_and_year', models.CharField(max_length=128)),
                ('course_selected_for_plus_two', models.CharField(max_length=128)),
                ('percentage_obtained', models.CharField(max_length=128)),
                ('downloaded_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Developer/')),
                ('name', models.CharField(max_length=150)),
                ('designation', models.CharField(max_length=150)),
                ('linkedin_id', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LatestEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Latest_event/')),
                ('title', models.CharField(max_length=250)),
                ('event_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Testimonial/')),
                ('name', models.CharField(max_length=150)),
                ('designation', models.CharField(max_length=150)),
                ('company', models.CharField(max_length=150)),
            ],
        ),
    ]
