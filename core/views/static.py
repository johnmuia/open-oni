from django.conf import settings
from django.core import urlresolvers
from core.models import Batch, Title, Issue, Page
from core.decorator import cache_page
from django.shortcuts import render_to_response
from django.template import RequestContext

@cache_page(settings.DEFAULT_TTL_SECONDS)
def about(request):
    page_title = "About " + settings.SITE_TITLE
    crumbs = list(settings.BASE_CRUMBS)
    crumbs.extend([
        {'label':'About',
         'href': urlresolvers.reverse('openoni_about'),
         'active': True},
    ])
    return render_to_response('about.html', dictionary=locals(),
                              context_instance=RequestContext(request))

@cache_page(settings.DEFAULT_TTL_SECONDS)
def about_api(request):
    page_title = "About the Site and API"
    crumbs = list(settings.BASE_CRUMBS)
    crumbs.extend([
        {'label':'About API',
         'href': urlresolvers.reverse('openoni_about_api'),
         'active': True},
    ])
    batches = Batch.objects.all()
    batch = None
    lccn = None
    title = None
    issue = None
    page = None

    if len(batches) > 0:
      batch = batches[0]
      lccn = batch.lccns()[0]
      title = Title.objects.get(lccn=lccn)
      issue = title.issues.all()[0]
      page = issue.pages.all()[0]

    return render_to_response('about_api.html', dictionary=locals(),
                              context_instance=RequestContext(request))

@cache_page(settings.DEFAULT_TTL_SECONDS)
def help(request):
    page_title = "Help"
    crumbs = list(settings.BASE_CRUMBS)
    crumbs.extend([
        {'label':'Help',
         'href': urlresolvers.reverse('openoni_help'),
         'active': True},
    ])
    return render_to_response('help.html', dictionary=locals(),
                              context_instance=RequestContext(request))
