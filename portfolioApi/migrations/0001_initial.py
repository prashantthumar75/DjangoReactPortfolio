<<<<<<< HEAD
# Generated by Django 4.1.2 on 2022-12-20 06:12
=======
# Generated by Django 4.1.2 on 2022-10-25 15:56
>>>>>>> 84cefccd43c36e597e37d9636f19b08cf697a451

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('title_2', models.CharField(blank=True, max_length=100, null=True)),
                ('description_one', tinymce.models.HTMLField(blank=True, null=True)),
                ('about_avatar', models.CharField(blank=True, max_length=100, null=True, verbose_name='Google Drive Image Id')),
            ],
            options={
                'verbose_name_plural': 'About Me Section',
            },
        ),
        migrations.CreateModel(
            name='HomeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greeting', models.CharField(blank=True, max_length=30, null=True, verbose_name='Greetings (eg: Hello)')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Full Name')),
                ('job_title', models.CharField(blank=True, max_length=100, null=True)),
                ('par_inro', models.TextField(blank=True, null=True, verbose_name='Introduction')),
                ('avatar_img', models.CharField(blank=True, max_length=100, null=True, verbose_name='Google Drive Image Id')),
                ('hireMe_link', models.CharField(blank=True, max_length=200, null=True)),
                ('cv_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Heros Section',
            },
        ),
        migrations.CreateModel(
            name='LanguagesIcons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('icon', models.CharField(blank=True, max_length=100, verbose_name='language Icon Image:(icons8.com)')),
                ('lang_name', models.CharField(blank=True, max_length=100, verbose_name='Language Name')),
                ('exp_level', models.CharField(blank=True, choices=[('Beginner', 'Beginner'), ('Junior', 'Junior'), ('Intermediate', 'Intermediate'), ('Experienced', 'Experienced')], max_length=200, verbose_name='Experience Level')),
            ],
            options={
                'verbose_name_plural': 'Skills section',
=======
                ('icon', models.CharField(blank=True, max_length=100)),
                ('lang_name', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Languages Icons',
>>>>>>> 84cefccd43c36e597e37d9636f19b08cf697a451
            },
        ),
        migrations.CreateModel(
            name='MyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(blank=True, max_length=90, null=True, verbose_name='Icon (eg: fa -fa-twitter)')),
<<<<<<< HEAD
                ('contact_info', models.CharField(blank=True, max_length=100, null=True, verbose_name='Contact Info (eg: johndoe2@gmail.com)')),
                ('contact_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Contact Name (eg: twitter)')),
            ],
            options={
                'verbose_name_plural': 'Contacts Section',
=======
                ('contact_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Contact Name (eg: twitter)')),
                ('contact_info', models.CharField(blank=True, max_length=100, null=True, verbose_name='Contact Info (eg: johndoe2@gmail.com)')),
            ],
            options={
                'verbose_name_plural': 'Contacts Section',
            },
        ),
        migrations.CreateModel(
            name='MyProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=40, null=True)),
                ('percentage', models.IntegerField(blank=True, null=True)),
                ('icon', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'verbose_name_plural': 'Skills Section',
>>>>>>> 84cefccd43c36e597e37d9636f19b08cf697a451
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_used', models.CharField(blank=True, max_length=100, null=True)),
                ('about_avatar', models.CharField(blank=True, max_length=100, null=True, verbose_name='Google Drive Image Id')),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('Project_title', models.CharField(blank=True, max_length=90, null=True)),
                ('Project_info', models.TextField(blank=True, null=True)),
                ('project_link', models.URLField(blank=True, null=True)),
                ('demo_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Projects Section',
            },
        ),
        migrations.CreateModel(
            name='ServicesOffred',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_image', models.CharField(blank=True, max_length=100, null=True, verbose_name='Google Drive Image Id')),
                ('service_name', models.CharField(blank=True, max_length=40, null=True)),
                ('shadow_icon', models.CharField(blank=True, max_length=40, null=True)),
                ('service_description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Services Section',
            },
        ),
        migrations.CreateModel(
            name='SocialMediaLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
<<<<<<< HEAD
                ('link', models.URLField(blank=True, null=True)),
                ('social_icon', models.CharField(blank=True, max_length=60, null=True, verbose_name='Icon (eg: fa -fa-twitter)')),
            ],
            options={
                'verbose_name_plural': 'Hero section Social Media Links',
=======
                ('social_icon', models.CharField(blank=True, max_length=60, null=True, verbose_name='Icon (eg: fa -fa-twitter)')),
            ],
            options={
                'verbose_name_plural': 'Social Media Links',
>>>>>>> 84cefccd43c36e597e37d9636f19b08cf697a451
            },
        ),
    ]
