from django.shortcuts import redirect, render

def index_redirect(request):
    return render(request, 'crud/main.html')
