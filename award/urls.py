from django.urls import path
from award.views import(
    create_award_view,
    detail_award_view,
    edit_award_view,
)

app_name = 'award'

urlpatterns = [
    path('create/', create_award_view,name="create"),
    path('<slug>/', detail_award_view,name="detail"),
    path('<slug>/edit', edit_award_view,name="edit"),

]