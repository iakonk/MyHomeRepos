from server_state.models import *
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
     This view returns current server state and all possible pre-defined server states,
     Based on that buttons will be added for each pre-defined state,
     Current state will be written in the "status" area
    """
    return render(request, 'index.html',
                  {'server_state': ServerState.objects.all(), 'possible_states': POSSIBLE_STATES})


def change_state(request, state):
    """
    This view changes current server state, received from user.
    :param request:
    :param state: Button text from possible_states dictionary
    :return: return success response
    """
    existing_state = ServerState.objects.all()
    for status in existing_state:
        status.current_state = state
        status.save()
    return HttpResponse('<h3>Done!</h3>')
