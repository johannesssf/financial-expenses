from django.http import HttpResponse
from django.template.response import TemplateResponse

from core.forms import LoginForm


def home(request):
    form = LoginForm()
    return TemplateResponse(request, 'login.html', {'form': form})
