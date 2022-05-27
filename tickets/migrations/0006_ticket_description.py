# Generated by Django 4.0.4 on 2022-05-27 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_ticket_alter_status_status_delete_ticketinstance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='description',
            field=models.TextField(default='Needs Description', help_text='Describe your issue here:', max_length=500),
        ),
    ]