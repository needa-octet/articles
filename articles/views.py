from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from .models import Article
# Create your views here.
@login_required
def article_search_view(request):
    # print("here is the request",request)
    query_dict=request.GET #THIS IS A DICTIONARY
    
    # query=query_dict.get("q")
    
    try:
        query=int(query_dict.get("q"))
    except:
        query=None
    article_obj=None
    if query is not None:
        article_obj=Article.objects.get(id=query)
    context={
        "object":article_obj
    }
    return render(request,"articles/search.html",context=context)

# @login_required
def article_create_view(request):
    form =ArticleForm(request.POST or None)
    context={
        "form":form
    }
    
    if form.is_valid():
        article_obj=form.save()
        # title=form.cleaned_data.get("title")
        # content=form.cleaned_data.get("content")
        # article_obj=Article.objects.create(title=title,content=content)
        # context['obj']=article_obj
        # context['created']=True
        context['form']=ArticleForm()
    return render(request,"articles/create.html",context=context)

@login_required
def article_detail_view(request,id=None):
    article_obj=None
    if id is not None:
        article_obj=Article.objects.get(id=id)
    context={
        "object":article_obj,
    }
    return render(request,"articles/details.html",context=context)