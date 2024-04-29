# Generated by Django 4.2 on 2024-04-10 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateApplications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passingYear', models.IntegerField()),
                ('yearOfExperience', models.IntegerField(default=0)),
                ('resume', models.FileField(upload_to='resume')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rccepted')], default='Pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=100)),
                ('companyName', models.CharField(max_length=100)),
                ('salaryLow', models.IntegerField(default=0)),
                ('salaryHigh', models.IntegerField(default=0)),
                ('applyCount', models.IntegerField(default=0)),
                ('lastDateToApply', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SelectCandidateJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.candidateapplications')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.jobpost')),
            ],
        ),
        migrations.AddField(
            model_name='candidateapplications',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.jobpost'),
        ),
        migrations.AddField(
            model_name='candidateapplications',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
