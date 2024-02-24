# Generated by Django 4.2.6 on 2024-02-17 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matter', '0018_alter_matters_folder'),
        ('userprofile', '0001_initial'),
        ('chatter', '0002_remove_inboxmessage_messagedate'),
    ]

    operations = [
        migrations.CreateModel(
            name='tempchatmessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messagefrom', models.CharField(blank=True, max_length=60, null=True)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('messagebox', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('UNREAD', 'UNREAD'), ('READ', 'READ')], default='UNREAD', max_length=15, null=True)),
                ('updatedby', models.CharField(blank=True, max_length=60, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('messageto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.user_profile')),
                ('see_matter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='matter.matters')),
            ],
            options={
                'verbose_name_plural': 'Inbox Messages',
            },
        ),
    ]
