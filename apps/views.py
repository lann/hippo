from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import edit

from guardian.mixins import PermissionRequiredMixin
from guardian.shortcuts import get_objects_for_user

from .models import App

class IndexView(generic.ListView, LoginRequiredMixin):
    context_object_name = 'apps'

    def get_queryset(self):
        """Return all applications that the logged-in user has view permission."""
        return get_objects_for_user(self.request.user, 'view_app', App)

class DetailView(generic.DetailView, PermissionRequiredMixin):
    permission_required = 'view_app'
    model = App

class CreateView(edit.CreateView, PermissionRequiredMixin):
    permission_required = 'add_app'
    model = App
    fields = ['name']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class UpdateView(edit.UpdateView, PermissionRequiredMixin):
    permission_required = 'change_app'
    model = App
    fields = ['name']

class DeleteView(edit.DeleteView, PermissionRequiredMixin):
    permission_required = 'delete_app'
    model = App
    success_url = reverse_lazy('apps:index')
