from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages
from django.core.exceptions import PermissionDenied, ImproperlyConfigured
from django.shortcuts import redirect
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

class ActiveOnlyMixinadmin(AccessMixin):

    '''
    A view mixin that only allows users that are active on the site.
    '''

    permission_denied_message = ''
    not_activated_message = ''
    not_activated_redirect = ''

    def get_not_activated_message(self):
        return self.not_activated_message

    def handle_not_activated(self):

        ''' Deal with users that are logged in but not activated yet. '''

        message = self.get_not_activated_message()
        if self.raise_exception:
            raise PermissionDenied(message)
        messages.error(self.request, message)
        return redirect(self.get_not_activated_redirect())

    def get_not_activated_redirect(self):

        ''' Get the url name to redirect to if the user isn't activated. '''

        if not self.not_activated_redirect:
            raise ImproperlyConfigured(
                '{0} is missing the not_activated_redirect attribute. Define {0}.not_activated_redirect, or override '
                '{0}.get_not_activated_redirect().'.format(self.__class__.__name__))
        return self.not_activated_redirect

    def handle_no_permission(self,request):

        ''' Overwrite to allow a message to be sent. '''
        admin_url = ['/login/ansap','/login/questap']
        message = self.get_permission_denied_message()
        if self.raise_exception:
            raise PermissionDenied(message)

        print(request.get_full_path())
        messages.error(self.request, message)
        return HttpResponseRedirect(reverse_lazy('home'))

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission(request)
        if not request.user.is_active:
            return self.handle_not_activated()
        if not request.user.is_superuser:
            return self.handle_no_permission(request)
        return super(ActiveOnlyMixinadmin, self).dispatch(request, *args, **kwargs)