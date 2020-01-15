from django.shortcuts import render
from operator import attrgetter
from award.models import AwardPost

# Create your views here.

def home_screen_view(request):

    context = { }
    award_posts = sorted(AwardPost.objects.all(), key=attrgetter('date_updated'), reverse=True)
    context['award_posts'] = award_posts
    
    return render(request, "personal/home.html",context)