from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                       PermissionRequiredMixin)
from django.urls import reverse
from django.views.generic import (CreateView,DetailView,ListView,DeleteView,RedirectView)
from groups.models import Group,GroupMember
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from . import models
# Create your views here.
class CreateGroup(LoginRequiredMixin,CreateView):
    fields = ('name','description')
    model = Group
    
class SingleGroup(DetailView):
    model = Group

class ListGroups(ListView):
    model = Group
    
    def get_queryset(self):
        return Group.objects.filter()
    
class JoinGroup(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})
    
    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
        
        try:
            GroupMember.objects.create(user=self.request.user,group=group)
            
        except IntegrityError:
            messages.warning(self.request,'Warning Already a Member!')
          
        else:
            messages.success(self.request,'You Are Now a Member!') 
            
        return super().get(request,*args,**kwargs)
        
class LeaveGroup(LoginRequiredMixin,RedirectView):
    
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})
    
    def get(self,request,*args,**kwargs):
        try:
            membership = models.GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get('slug')
            ).get()
        
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request,'Sorry You Are Not in this Group!')
            
        else:
            membership.delete()
            messages.success(self.request,'You Have Left The Group!')
            
        return super().get(request,*args,**kwargs)
        
            