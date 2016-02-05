from django.contrib import admin
from server_state.models import *


class ServerStateAdmin(admin.ModelAdmin):
    pass
admin.site.register(ServerState, ServerStateAdmin)
