import django.contrib.auth.models
import django.utils.timezone
from django.db import migrations, models


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
                ('is_superuser', models.BooleanField(default=False, help_text='Суперпользователь с максимальным доступом', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Имеет ли пользователь права пользоваться администраторскими полномочиями.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Проверка на активность пользователя.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Логин')),
                ('full_name', models.CharField(max_length=255, verbose_name='Полное имя')),
                ('email', models.CharField(max_length=254, unique=True, verbose_name='Email')),
                ('storage_path', models.CharField(blank=True, default='', max_length=255, verbose_name='Путь к хранилищу пользователя')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Статус администратора')),
                ('groups', models.ManyToManyField(blank=True, help_text='Группы, к которым принадлежит этот пользователь. Пользователь получит все разрешения, предоставленные каждой из его групп.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Разрешения пользователя.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['username'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
