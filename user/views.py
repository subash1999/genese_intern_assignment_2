from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from user.forms import CustomUserCreationForm
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
# Create your views here.
class RegistrationForm(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "user/register.html"
    def get_success_url(self):
        return reverse_lazy('login')

@method_decorator(login_required, name='dispatch')
class UserProfileView(generic.base.TemplateView):
    model = User
    context_object_name = 'user'
    template_name = 'user/user_profile.html'


@method_decorator(login_required, name='dispatch')
class UserProfileView(generic.base.TemplateView):
    model = User
    context_object_name = 'user'
    template_name = 'user/user_profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LogoutView(generic.RedirectView):
    """
    A view that logout user and redirect to homepage.
    """
    permanent = False
    query_string = True
    pattern_name = 'custom_auth:login'

    def get_redirect_url(self, *args, **kwargs):
        """
        Logout user and redirect to target url.
        """
        logout(self.request)
        if self.request.POST.get('next_page') is not None:
            return self.request.POST.get('next_page')

        if self.request.GET.get('next_page') is not None:
            return self.request.GET.get('next_page')

        return reverse('logout_msg')


class LogoutMsgView(generic.base.TemplateView):
    template_name = "user/logout_msg.html"
