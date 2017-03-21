from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request,
                  'blog/post_list.html', {})

def where_is_my_sample(request):
    return render(request, 'blog/sample.html', {})