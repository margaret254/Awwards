from django.shortcuts import render
from operator import attrgetter

from award.views import get_award_queryset
from award.models import AwardPost

# Create your views here.

def home_screen_view(request):

    context = { }

    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

    award_posts = sorted(get_award_queryset(query), key=attrgetter('date_updated'), reverse=True)
    context['award_posts'] = award_posts
    
    return render(request, "personal/home.html",context)