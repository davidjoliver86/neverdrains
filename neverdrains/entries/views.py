from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the entries index.")


def entry_detail(request, entry_id):
    return HttpResponse(f"This is entry ID {entry_id}.")
