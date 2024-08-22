"""
to render html web pages
"""
import random
from articles.models import Article 
from django.http import HttpResponse
from django.template.loader import render_to_string,get_template
name ="hy"
num=random.randint(1,4)
article_obj=Article.objects.get(id=2)
article_title=article_obj.title
article_list=Article.objects.all()
my_list=[1,3,45,4536,1]
my_list_str=""
for x in my_list:
    my_list_str+=f"<li>number is: {x}\n</li>"
context={
    "title":article_obj.title,
    "content":article_obj.content,
    "my_list_str":article_list
}
# HTML_STRING= """

# <h1>Hello {title} - {content}</h1>
# """.format(**context)
# templ=get_template("home-view.html")
# templ_str=templ.render(context=context)
HTML_STRING=render_to_string("home-view.html",context=context)

def home_view(_request,id=None,*args, **kwargs):
    # print("id of Article",id)
    return HttpResponse(HTML_STRING)