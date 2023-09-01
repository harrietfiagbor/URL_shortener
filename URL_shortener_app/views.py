from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic.base import TemplateView, RedirectView

# Models
from .models import Shortener

# forms
from .forms import ShortenerForm

# Create your views here.

class HomeView(TemplateView, request):
    template = "index.html"

    def get_context_data(self, **kwargs):
        # overwrite context data 
        context = super().get_context_data(**kwargs)
        # empty form
        context["form"] = ShortenerForm()

        if request.method == "POST":
            used_form = ShortenerForm(request.POST)
            
            if used_form.is_valid():
                # save to get short_url
                shortened_object = used_form.save()

                new_url = request.build_absolute_url('/') + shortened_object.short_url

                context['new_url'] = new_url
                context['long_url'] = shortened_object

                return context

            context['errors'] = used_form.errors
            return context

        else:
            return context

# TODO:1: make class redirect view 
# TIPS : Use 404 object and redirect url

class RedirectURLView(RedirectView):
 #    # get random code generated
 #    shortener = shortener.objects.get(short_url=shortened_part)
 # 
 #    # update the number of time link gets clicked
 #    shortener.times_followed += 1
 #
 #    shortener.save()
 #
 #    url = shortener.long_url
 #    pattern_name = "redirect"
    
    def get_redirect_url(self, *args, **kwargs):
        # FIXME : remove the lines below
        # get random code generated
        # shortener = shortener.objects.get(short_url=shortened_part)
        # shortener = get_object_or_404(Shortener, pk=kwargs['pk'])
        # update the number of time link gets clicked
        # shortener.times_followed += 1
        # shortener.save()

         # get random code generated
        shortener = shortener.objects.get(short_url=shortened_part)
     
        # update the number of time link gets clicked
        shortener.times_followed += 1

        shortener.save()

        url = shortener.long_url
        pattern_name = "redirect"

        return super().get_redirect_url(*args, **kwargs)

