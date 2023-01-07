import logging

from django.http import HttpResponse
from django.shortcuts import render

log = logging.getLogger(__name__)


def chat_box(request, chat_box_name):
    # we will get the chatbox name from the url
    return render(request, "chatbox.html", {"chat_box_name": chat_box_name})


# Create your views here.
def index(request):
    log.info("Test logging info", extra={"user": request.user.pk})
    log.error("Test logging error", extra={"user": request.user.pk})
    log.warning("Test logging warning", extra={"user": request.user.pk})
    log.critical("Test critical", extra={"user": request.user.pk})

    return HttpResponse("Hello, world.")
