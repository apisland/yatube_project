from django.http import HttpResponse

def index(request):
    return HttpResponse('Байки из склепа')

def group_posts(request, any_slug):
    return HttpResponse(f'Групповые байки {any_slug}')

# Create your views here.
