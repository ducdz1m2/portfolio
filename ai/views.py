from django.shortcuts import render

# Create your views here.
def ai(request):
    return render(request, 'ai/ai.html')