import re
import random

from .myMarkdown import convert
#from markdown2 import Markdown

from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import util

class MyForm(forms.Form):
    q = forms.CharField(label = "",
        widget=forms.TextInput(attrs = {'class': 'search form-control', 'placeholder': 'Search Encyclopedia'}))

class CreateForm(forms.Form):
    Title = forms.CharField(widget=forms.TextInput(attrs = {'class': 'form-control', 'id': 'title'}))
    Content = forms.CharField(widget = forms.Textarea( 
    attrs = {'class': 'form-control', 'id': 'content', 'row': '10'}))

def index(request):    
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": MyForm()
    })

def entry(request, title):    
    ent = util.get_entry(title)
    if ent is None:
        return render(request, "encyclopedia/error.html", {
            "message": "Page not found!",
            "form": MyForm()
        })
    entry = convert(ent)
    return render(request, "encyclopedia/entry.html", {
        "entry": entry,
        "title": title,
        "form": MyForm()
    })

def randomPage(request):
    return HttpResponseRedirect(reverse("entry", args = (random.choice(util.list_entries()),)))

def search(request):
    query = request.GET.get("q")
    entries = [ent.lower() for ent in util.list_entries()]

    #to show a consistent name in the url bar we should take 
    #the entry's exact name instead of the searched parameter
    entries1 = util.list_entries()
    if query.lower() in entries:        
        i = entries.index(query.lower())
        return HttpResponseRedirect(reverse("entry", args = (entries1[i],)))
    else:
        store = []
        [store.append(x) for x in entries1 if re.match(query, x, re.IGNORECASE)]
        return render(request, "encyclopedia/search.html", {
            "entries": store,
            "form": MyForm(),
            "query": query
        })

def create(request):
    if request.method == "POST":
        forms = CreateForm(request.POST)
        if forms.is_valid():
            title = forms.cleaned_data["Title"]
            if title in util.list_entries():
                messages.error(request,'This wiki already exists!')
                return render(request, "encyclopedia/create.html", {
                    "form1": CreateForm(request.POST),
                    "form": MyForm(),
                    "title": title
                })
            util.save_entry(title, forms.cleaned_data["Content"])
            return HttpResponseRedirect(reverse("entry", args = (title,)))            
        else:
            messages.error(request,'Something went wrong!')
            return render(request, "encyclopedia/create.html", {
                "form1": CreateForm(request.POST),
                "form": MyForm(),
                "title": title
            })
    return render(request, "encyclopedia/create.html", {
        "form1": CreateForm(),
        "form": MyForm()
    })

def edit(request, title):    
    if request.method == "POST":
        forms = CreateForm(request.POST)
        if forms.is_valid():
            util.save_entry(title, forms.cleaned_data["Content"])
            return HttpResponseRedirect(reverse("entry", args = (title,)))
        else:
            messages.error(request,'Something went wrong!')
            return render(request, "encyclopedia/edit.html", {
                "form1": CreateForm(request.POST),
                "form": MyForm(),
                "title": title
            })
    myform = CreateForm(initial = {"Title": title, "Content": util.get_entry(title)})
    return render(request, "encyclopedia/edit.html", {
        "form1": myform,
        "form": MyForm(),
        "title": title
    })