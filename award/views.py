from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from award.models import AwardPost
from award.forms import CreateAwardPostForm,UpdateAwardPostForm
from account.models import Account

# Create your views here.
def create_award_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateAwardPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = CreateAwardPostForm()

    context['form'] = form

    return render(request,"award/create_award.html",context)

def detail_award_view(request,slug):
    context = {}

    award_post = get_object_or_404(AwardPost, slug=slug)
    context['award_post'] = award_post

    return render(request, 'award/detail_award.html', context)

def edit_award_view(request, slug):
	
	context = {}
	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	award_post = get_object_or_404(AwardPost, slug=slug)
	if request.POST:
		form = UpdateAwardPostForm(request.POST or None, request.FILES or None, instance=award_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			award_post = obj
	
	form = UpdateAwardPostForm(
			initial={
					"title": award_post.title, 
					"body": award_post.body,
					"image": award_post.image,
				}
			)
	context['form'] = form

	return render(request, 'award/edit_award.html', context)

def get_award_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		posts = AwardPost.objects.filter(
				Q(title__icontains=q) | 
				Q(body__icontains=q)
			).distinct()
		for post in posts:
			queryset.append(post)
	return list(set(queryset))
