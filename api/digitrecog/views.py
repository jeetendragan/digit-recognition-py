# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .apps import DigitrecogConfig

class call_model(APIView):
    def get(self, request):
        if request.method == 'GET':
            params = request.GET.get('sentence')
            return params+"hello"