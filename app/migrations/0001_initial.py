# Generated by Django 4.0 on 2022-03-01 16:49

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('is_admin', models.BooleanField(default=False, verbose_name='Is admin')),
                ('is_registrar1', models.BooleanField(default=False, verbose_name='Is student registrar')),
                ('is_registrar2', models.BooleanField(default=False, verbose_name='Is staff registrar')),
                ('is_cashier', models.BooleanField(default=False, verbose_name='Is cashier')),
                ('is_expenses', models.BooleanField(default=False, verbose_name='Is expenses')),
                ('is_daily_report', models.BooleanField(default=False, verbose_name='Is Daily report')),
                ('is_weekly_report', models.BooleanField(default=False, verbose_name='Is Weekly report')),
                ('is_monthly_report', models.BooleanField(default=False, verbose_name='Is Monthly report')),
                ('is_expenses_report', models.BooleanField(default=False, verbose_name='Is Expenses report')),
                ('is_add', models.BooleanField(default=False, verbose_name='Is add')),
                ('nin', models.CharField(blank=True, max_length=255)),
                ('phone_num', models.CharField(blank=True, max_length=255)),
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
            name='Cons',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('one', models.CharField(blank=True, max_length=255, null=True)),
                ('amountOne', models.CharField(blank=True, max_length=255, null=True)),
                ('two', models.CharField(blank=True, max_length=255, null=True)),
                ('amountTwo', models.CharField(blank=True, max_length=255, null=True)),
                ('three', models.CharField(blank=True, max_length=255, null=True)),
                ('amountThree', models.CharField(blank=True, max_length=255, null=True)),
                ('four', models.CharField(blank=True, max_length=255, null=True)),
                ('amountFour', models.CharField(blank=True, max_length=255, null=True)),
                ('five', models.CharField(blank=True, max_length=255, null=True)),
                ('amountFive', models.CharField(blank=True, max_length=255, null=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Intakes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('intake_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('TUTION', 'TUTION'), ('APPLICATION', 'APPLICATION'), ('ACCEPTANCE', 'ACCEPTANCE'), ('OTHERS', 'OTHERS')], default='TUTION', max_length=100)),
                ('type', models.CharField(choices=[('cash', 'cash'), ('transfer', 'transfer')], default='cash', max_length=100)),
                ('amount', models.CharField(blank=True, max_length=100, null=True)),
                ('paymentTerms', models.CharField(choices=[('14 days', '14 days'), ('30 days', '30 days'), ('60 days', '60 days')], default='14 days', max_length=100)),
                ('total', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Paymenttype',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ptype_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_price', models.FloatField(default=0)),
                ('product_unit', models.CharField(max_length=255)),
                ('product_is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('programme_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('total', models.FloatField(default=0)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='student_status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('nin', models.CharField(blank=True, max_length=400, null=True)),
                ('ip_id', models.CharField(blank=True, max_length=400, null=True)),
                ('totalFee', models.CharField(blank=True, max_length=255, null=True)),
                ('student_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=300, null=True)),
                ('last_name', models.CharField(blank=True, max_length=300, null=True)),
                ('first_name', models.CharField(blank=True, max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.departments')),
                ('intake', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.intakes')),
                ('programme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.programme')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.student_status')),
            ],
        ),
        migrations.CreateModel(
            name='SopDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.product')),
                ('sop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.sop')),
            ],
        ),
        migrations.CreateModel(
            name='Reciept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, null=True)),
                ('student_name', models.CharField(blank=True, max_length=255, null=True)),
                ('student_id', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('tution', models.BooleanField(default=False)),
                ('acceptance', models.BooleanField(default=False)),
                ('application', models.BooleanField(default=False)),
                ('others', models.BooleanField(default=False)),
                ('stu_programme', models.CharField(blank=True, max_length=255, null=True)),
                ('stu_nin', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.CharField(blank=True, max_length=100, null=True)),
                ('total', models.FloatField(default=0)),
                ('balance', models.FloatField(default=0)),
                ('ptype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.paymenttype')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.invoice')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.students'),
        ),
    ]
