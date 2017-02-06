from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from .models import Incident
from django.http import Http404
from django.views.decorators.http import require_http_methods
from django.db import IntegrityError
from django.core.urlresolvers import reverse
from django.contrib import messages


@login_required()
def list(request):
    return TemplateResponse(
        request, 'dashboard/alerts.html',
        {"alerts":["1",2,3,3,3,4,4,3,4,5,5,5,6]}
    )
