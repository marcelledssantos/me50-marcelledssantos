from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib import messages
import markdown2
import random

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "The requested page does not exist."
        })
    html_content = markdown2.markdown(content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })

def search(request):
    query = request.GET.get("q", "")
    entries = util.list_entries()
    # Busca exata (case-insensitive)
    for entry in entries:
        if entry.lower() == query.lower():
            return redirect("entry", title=entry)
    # Busca parcial
    results = [entry for entry in entries if query.lower() in entry.lower()]
    return render(request, "encyclopedia/search.html", {
        "results": results,
        "query": query
    })

def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        if util.get_entry(title):
            messages.error(request, "Já existe uma entrada com esse título.")
            return redirect("create")
        util.save_entry(title, content)
        # After saving the new page
        messages.success(request, "New entry created successfully!")
        return redirect("entry", title=title)
    return render(request, "encyclopedia/create.html")

def edit(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "The requested page does not exist."
        })
    if request.method == "POST":
        new_content = request.POST.get("content")
        util.save_entry(title, new_content)
        # After saving the edit
        messages.success(request, "Entry updated successfully!")
        return redirect("entry", title=title)
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })

def random_page(request):
    entries = util.list_entries()
    if entries:
        title = random.choice(entries)
        return redirect("entry", title=title)
    return render(request, "encyclopedia/error.html", {
        "message": "Nenhuma entrada encontrada."
    })