# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def webcam(request):
	return render(request,"webcamjs/demos/basic.html")
