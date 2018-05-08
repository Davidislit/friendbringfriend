from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Posts
from .forms import Candidate

# Create your views here.
def index(request):
    #return HttpResponse('Hello from posts!')

    posts = Posts.objects.all()[:10]

    context = {
        'title': 'Latest Jobs',
        'posts': posts
    }

    return render(request, 'posts/index.html',context)


def details(request,id):
    #pull the post from the model
    post = Posts.objects.get(id=id)

    context = {
        'posts': post
    }

    return render(request, 'posts/details.html',context)


def getCandidate(request):
    if request.method == 'POST':
        form = Candidate(request.POST)
        if(form.is_valid()):
            return HttpResponseRedirect('/thanks/')
        else:
            form = Candidate()

    return render(request,'posts/index.html', {'form':form})
