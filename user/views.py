from django.contrib.auth.mixins import UserPassesTestMixin
from user.spreadsheet import Spreadsheet
from django.shortcuts import redirect, render
from user.forms import CustomUserCreationForm, UserProfileForm,UserUpdateForm
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from post.models import Post
import xlwt
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Count

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


@method_decorator(login_required,name='post')
@method_decorator(login_required,name='get')
@method_decorator(login_required,name='dispatch')
class UpdateUserProfileView(generic.base.View):
    template_name = 'user/edit_user_profile.html'
    user_form = UserUpdateForm
    user_profile_form = UserProfileForm

    def __int__(self,*args, **kwargs):
        # first call parent's constructor
        super(UpdateUserProfileView, self).__init__(*args, **kwargs)
        self.user_form = UserUpdateForm(instance = self.request.user)
        if hasattr(self.request.user, 'userprofile'):
            self.user_profile_form = self.user_profile_form(instance=self.request.user.userprofile)


    def post(self,request):      
        user_form = self.user_form(request.POST, instance=request.user)

        request.POST = request.POST.copy()

        user_profile_form = self.user_profile_form(request.POST, request.FILES)

        if hasattr(request.user, 'userprofile'):
            request.POST['id'] = request.user.userprofile.id
            user_profile_form = self.user_profile_form(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            # the save function defined in the models.py will remove the old image file
            profile = user_profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect(reverse('user:profile'))
        else:
            return render(request, self.template_name, {'user_form': user_form, 'user_profile_form': user_profile_form})        


    def get(self,request):
        self.user_form = UserUpdateForm(instance = request.user)
        if hasattr(self.request.user, 'userprofile'):
            self.user_profile_form = self.user_profile_form(instance=request.user.userprofile)
        return render(request, self.template_name, {'user_form': self.user_form, 'user_profile_form': self.user_profile_form})
        

@method_decorator(login_required, name='dispatch')
class UserProfileView(generic.base.TemplateView):
    model = User
    context_object_name = 'user'
    template_name = 'user/user_profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(login_required, name='dispatch')
class UserMyPostView(generic.ListView):
    template_name = 'user/my_posts.html'
    model = Post
    paginate_by = 5
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        return context

    def get_queryset(self):
        object_list = self.model.objects.all()
        object_list = object_list.filter(user=self.request.user)
        self.count = object_list.count()
        return object_list


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

class SessionExpireView(generic.base.TemplateView):
    template_name = "user/session_expire.html"

@method_decorator(login_required,name='post')
@method_decorator(login_required,name='get')
@method_decorator(login_required,name='dispatch')
class ExportUserAndPostView( UserPassesTestMixin,generic.base.View):
    template_name = 'user/export_user_and_post_data.html'

    def test_func(self):
        return self.request.user.is_superuser

    def post(self,request):
        users = User.objects.annotate(post_count=Count('post')).filter(post_count__gt=0).order_by("-first_name","-last_name")
        row_list = [
            ["S.N","User ID","First Name","Last Name", "Email", "Address", "Phone", "Posts"]
        ]
        for i,user in enumerate(users,start=1):
            row = []
            row += [i,user.id,user.first_name,user.last_name,user.email]
            
            if hasattr(user,'userprofile'):
                if not user.userprofile.address == "None":
                    row += [user.userprofile.address]
                else:
                    row += [""]
                if not user.userprofile.phone == "None":
                    row += [user.userprofile.phone]
                else:
                    row += [""]
            else:
                row += ["",""]
            
            post_title = []
            for i,post in enumerate(user.post_set.all(),start=1):
                post_title.append(str(i)+") "+post.title)
            row.append(" ,".join(post_title))

            row_list.append(row)

        sheet = Spreadsheet();
        sheet.write(row_list)

        result = sheet.read()
        columns_name = result[0]
        exported_data = result[1:]

        return render(request, "user/data_exported_success.html",{"exported_data":exported_data,'columns_name':columns_name})

    def get(self,request):
        return render(request, self.template_name)

