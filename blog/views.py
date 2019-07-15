from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/principal', {})
# Create your views here.
