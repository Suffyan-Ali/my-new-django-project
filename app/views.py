from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, Jenkins CI/CD with Django!")

