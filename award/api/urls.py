from django.urls import path

from award.api.views import(
	api_detail_award_view,
	api_update_award_view,
	api_delete_award_view,
	api_create_award_view
)

app_name = 'award'

urlpatterns = [
	path('<slug>/', api_detail_award_view, name="detail"),
	path('<slug>/update', api_update_award_view, name="update"),
	path('<slug>/delete', api_delete_award_view, name="delete"),
	path('create', api_create_award_view, name="create")
	
]

