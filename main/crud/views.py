from django.shortcuts import render,HttpResponseRedirect
from.forms import stureg
from . models import User
from django.views import View
from django.views.generic.base import TemplateView,RedirectView

#add and view
class addview(TemplateView):
    template_name="home.html"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        form=stureg()
        user=User.objects.all()
        context={"fm":form,"user":user}
        return context
    def post(self,request):
        form=stureg(request.POST)
        if form.is_valid():
            unam=form.cleaned_data.get("name")
            uem=form.cleaned_data.get("email")
            upas=form.cleaned_data.get("password")
            vpn=User(name=unam,email=uem,password=upas)
            vpn.save()
            return HttpResponseRedirect("/")
#update
class updateuser(View):
    def get(self,request,id):
        pi=User.objects.get(pk=id)
        form=stureg(instance=pi)
        return render(request,"update.html",{"form":form})
    def post(self,request,id):
        pi=User.objects.get(pk=id)
        form=stureg(request.POST,instance=pi)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

#delete
class deleteuser(RedirectView):
    url="/"
    def get_redirect_url(self, *args, **kwargs):
        del_id=kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
        
    
