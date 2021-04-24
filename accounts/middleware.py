from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, redirect


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if not  request.user.is_authenticated:
            return HttpResponseRedirect('/login')  # Here I call login
        response = self.get_response(request)
        return response