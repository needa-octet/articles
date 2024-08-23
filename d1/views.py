"""
to render html web pages
"""
import random
from articles.models import Article 
from django.http import HttpResponse
from django.template.loader import render_to_string,get_template
from django.shortcuts import get_object_or_404
name ="hy"
num=random.randint(1,4)

article_list=Article.objects.all()
my_list=[1,3,45,4536,1]
my_list_str=""
for x in my_list:
    my_list_str+=f"<li>number is: {x}\n</li>"

# HTML_STRING= """

# <h1>Hello {title} - {content}</h1>
# """.format(**context)
# templ=get_template("home-view.html")
# templ_str=templ.render(context=context)

def home_view(_request,id=None,*args, **kwargs):
    article_obj=get_object_or_404(Article, id=2)
    article_title=article_obj.title
    # article_obj=Article.objects.get(id=2)
    context={
        "title":article_obj.title,
        "content":article_obj.content,
        "my_list_str":article_list
    }
    # context={
    #     "title":article_obj.title,
    #     "content":article_obj.content,
    #     "my_list_str":article_list
    # }
    HTML_STRING=render_to_string("home-view.html",context=context)
    # print("id of Article",id)
    # HTML_STRING="hello world"
    return HttpResponse(HTML_STRING)