from django.db import models


# List of available server states
POSSIBLE_STATES = (
        ('NORMAL', 'Schedule server normal'),
        ('OFF', 'Schedule server shutdown'),
        ('ON', 'Schedule server boot'),
    )

SERVER_STATE = (
        ('NORMAL', 'Schedule server normal'),
        ('OFF', 'Schedule server shutdown'),
        ('ON', 'Schedule server boot'),
    )


class ServerState(models.Model):
    """
        Sets the current state of the server and tracks timestamp of the last update
    """
    current_state = models.CharField('Current state', max_length=10, choices=POSSIBLE_STATES, default=SERVER_STATE[0][0])
    last_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
