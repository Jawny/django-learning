from django.shortcuts import render
from django.http import HttpResponse

posts = [
        {
            'author': 'johnny',
            'title': 'Blog post 1',
            'content': 'first post',
            'date_posted': 'October 13, 2023'
            },
        {
            'author': 'bob',
            'title': 'Blog post 2',
            'content': 'first post',
            'date_posted': 'October 20, 2023'
            },
        {
            'author': 'bill',
            'title': 'Blog post 3',
            'content': 'first post',
            'date_posted': 'October 23, 2023'
            },
        ]

def home(request):
    context = {
            'posts': posts
            }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
