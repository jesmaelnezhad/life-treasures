from django.http import HttpResponse
from django.shortcuts import render
import logging

log = logging.getLogger(__name__)


# Create your views here.
def index(request):
    log.info("Test logging info", extra={"user": request.user.pk})
    log.error("Test logging error", extra={"user": request.user.pk})
    log.warning("Test logging warning", extra={"user": request.user.pk})
    log.critical("Test critical", extra={"user": request.user.pk})

    return HttpResponse("Hello, world.")
