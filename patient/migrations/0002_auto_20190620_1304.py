# Generated by Django 2.2.2 on 2019-06-20 13:04

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custom_doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('month', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('specialities', models.CharField(max_length=1000)),
                ('education', models.CharField(max_length=1000)),
                ('hospitals', models.CharField(max_length=1000)),
                ('rate', models.FloatField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_no', models.CharField(max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Make_appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorEmailId', models.EmailField(max_length=254)),
                ('year', models.IntegerField()),
                ('month', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('hr', models.IntegerField()),
                ('min', models.IntegerField()),
                ('problems', models.CharField(max_length=9000)),
            ],
        ),
        migrations.CreateModel(
            name='Recharge_balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recharge_card', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Validate_appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_id', models.IntegerField()),
                ('year', models.IntegerField()),
                ('month', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('hr', models.IntegerField()),
                ('min', models.IntegerField()),
                ('changedatetime', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Custom_patient',
            fields=[
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('month', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Custom_user',
        ),
    ]
