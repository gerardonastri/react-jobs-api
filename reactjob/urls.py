from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.getRoutes, name="routes"),
    path('jobs/',  views.getJobs, name="jobs"),
    path('jobs/create/', views.createJob, name="create-job"),
    path('jobs/<str:pk>',  views.getJob, name="job"),
    # path('jobs/category/<str:cat>',  views.getCategory, name="category"),
    path('auth/register/',  views.register, name="register"),
    path('auth/login/',  views.login, name="login")
]
