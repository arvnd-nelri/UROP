# Generated by Django 4.2.3 on 2023-08-09 10:28

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mble', models.CharField(blank=True, max_length=10, null=True)),
                ('gdr', models.CharField(choices=[('0', '--- Select Your Gender ---'), ('1', 'Male'), ('2', 'Female')], default='0', max_length=5)),
                ('role_type', models.CharField(choices=[('0', 'Guest'), ('1', 'Student'), ('2', 'Teacher')], default='0', max_length=5)),
                ('eid', models.CharField(max_length=10)),
                ('pfimg', models.ImageField(default='pfle.png', upload_to='Profiles/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
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
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PfName', models.CharField(choices=[('None', 'Select'), ('Phonepe', 'Phonepe'), ('Google Pay', 'Google Pay'), ('Amazon', 'Amazon'), ('Paytm', 'Paytm'), ('Flipkart', 'Flipkart'), ('Myntra', 'Myntra'), ('Others', 'Others')], default='None', max_length=15, verbose_name='Platform Name')),
                ('Title', models.CharField(max_length=100, verbose_name='Title')),
                ('Company', models.CharField(max_length=100, verbose_name='Company')),
                ('ExpDate', models.DateField(verbose_name='Expiry Date')),
                ('Code', models.CharField(max_length=15, verbose_name='Coupon Code')),
                ('Description', models.FileField(upload_to='CouponDetails/')),
                ('Status', models.CharField(choices=[('Uploaded', 'Uploaded'), ('Requested', 'Requested'), ('Used', 'Used'), ('Expired', 'Expired')], default='Uploaded', max_length=20, verbose_name='Status')),
                ('st', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
