from . import util
import markdown2
from django.shortcuts import render, redirect
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def entry(request, title):
    entry = util.get_entry(title)
    if entry is None:
        return render(request, "encyclopedia/error.html", {
            "message": "The requested page was not found."
        })
    else:
        html_content = markdown2.markdown(entry)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })
def search(request): 
    query = request.GET.get("q", "")
    entries = util.list_entries()
    
    for entry in entries:
        if entry.lower() == query.lower():
            return redirect("entry", title=entry)
        
        
    results = []
    for entry in entries:
        if query.lower() in entry.lower():
            results.append(entry)
    
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "results": results
    })

def new(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/new.html", {
                "Error": "This page already exists."
            })
        util.save_entry(title, content)
        return redirect("entry", title=title)
    
    return render(request, "encyclopedia/new.html")

def edit(request, title):
    if request.method == "POST":
            content = request.POST.get("content")
            util.save_entry(title, content)
            return redirect("entry", title=title)
    content = util.get_entry(title)
    
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })
def random_page(request):
    entries = util.list_entries()
    entry = random.choice(entries)
    return redirect("entry", title=entry)