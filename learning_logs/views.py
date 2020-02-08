from django.shortcuts import render

# Create your views here.
def learning_logs(request):
    return render(request, 'learning_logs.html')