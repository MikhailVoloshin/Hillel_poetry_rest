from django.contrib import admin, auth
from django.http import HttpResponse, JsonResponse
from django.urls import include, path


def check(request):
    data = {"name": "Misha"}
    return JsonResponse(data)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health-check/", check),
    path("posts/", include("posts.urls")),
]
