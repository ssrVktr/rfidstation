# Generated by Django 2.0.8 on 2018-09-18 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assets_management', '0001_initial'),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': '申请状态',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='年度')),
                ('date_of_application', models.DateField(verbose_name='申请日期')),
                ('application_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan_management.ApplicationStatus', verbose_name='申请状态')),
                ('assets', models.ManyToManyField(to='assets_management.Assets', verbose_name='资产')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Department', verbose_name='申报部门')),
                ('operator', models.ManyToManyField(null=True, related_name='plan_operator', to=settings.AUTH_USER_MODEL, verbose_name='操作人')),
            ],
            options={
                'permissions': (('can_see', '能看到计划管理模块'),),
                'verbose_name_plural': '计划管理',
            },
        ),
        migrations.CreateModel(
            name='Plan_Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=20, verbose_name='项目名称')),
                ('year', models.IntegerField(verbose_name='年度')),
            ],
            options={
                'verbose_name_plural': '计划汇总表',
            },
        ),
        migrations.CreateModel(
            name='SummaryStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': '计划书状态',
            },
        ),
        migrations.AddField(
            model_name='plan_summary',
            name='summary_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plan_management.SummaryStatus', verbose_name='计划书状态'),
        ),
        migrations.AddField(
            model_name='plan',
            name='plan_summary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='plan_management.Plan_Summary', verbose_name='所属计划书'),
        ),
        migrations.AddField(
            model_name='plan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_user', to=settings.AUTH_USER_MODEL, verbose_name='申报人'),
        ),
    ]
