from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse
from pathlib import Path

# Create your views here.
def text_to_speech(request):
    if request.method == 'POST':
        form = TextFileForm(request.POST, request.FILES)