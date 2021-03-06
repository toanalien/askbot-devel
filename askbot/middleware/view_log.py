"""
This module records the site visits by the authenticated users

Included here is the ViewLogMiddleware
"""
from askbot import signals
from django.utils import timezone


class ViewLogMiddleware(object):
    """
    ViewLogMiddleware sends the site_visited signal

    """
    def process_view(self, request, view_func, view_args, view_kwargs):
        #send the site_visited signal for the authenticated users
        if request.user.is_authenticated():
            signals.site_visited.send(None, #this signal has no sender
                user=request.user,
                timestamp=timezone.now()
            )
