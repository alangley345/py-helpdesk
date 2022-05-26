# Generated by Django 4.0.4 on 2022-05-26 18:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Who is working on this ticket?', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TicketInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('assignee', models.ManyToManyField(help_text='Ticket Assignee', to='tickets.agent')),
                ('category', models.ManyToManyField(help_text='Ticket Category', to='tickets.category')),
            ],
        ),
    ]
