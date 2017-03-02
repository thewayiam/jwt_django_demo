import re
import json
import uuid

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, connections
from django.conf import settings
from django.utils import translation

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
#@permission_classes((IsAuthenticated, ))
def protected(request):
    return Response({'test': 'ok'}, status=status.HTTP_200_OK)
