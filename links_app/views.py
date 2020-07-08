from django.shortcuts import render, redirect
from links_app.models import Link
import uuid
import json
from django.http import HttpResponse


def generate_short_url(request):
    if request.method == "POST":
        request_data = json.loads(request.body)
        long_url = request_data.get("long_url")
        if not (
                long_url.startswith("http://")
                or long_url.startswith("https://")
        ):
            long_url = f"http://{long_url}"

        link = Link.objects.create(
            short_url=f"{uuid.uuid4()}",
            long_url=long_url
        )
        return HttpResponse(
            f"http://localhost:8000/link/{link.short_url}")


def get_long_url(request, url):
    if request.method == "GET":
        qs = Link.objects.filter(short_url=url)
        if qs.exists():
            link = qs.first()
            return redirect(f'{link.long_url}')
        return HttpResponse("error")


def get_all_short_url(request):
    if request.method == "GET":
        return HttpResponse(
            [" --- " + link.short_url for link in Link.objects.all()]
        )
        return HttpResponse("error")
