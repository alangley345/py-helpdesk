# Generated by Django 4.0.4 on 2022-05-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_ticketinstance_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('summary', models.CharField(default='No Summary', help_text='Summarize Issue', max_length=100)),
                ('agent', models.ManyToManyField(help_text='Ticket Assignee', to='tickets.agent')),
                ('category', models.ManyToManyField(help_text='Ticket Category', to='tickets.category')),
            ],
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Resolved', 'Resolved'), ('On-hold', 'On-hold')], default='Open', help_text='Current Status', max_length=10),
        ),
        migrations.DeleteModel(
            name='TicketInstance',
        ),
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.ManyToManyField(help_text='Enter ticket status', to='tickets.status'),
        ),
    ]
