from django.shortcuts import render

# Create your views here.


def render_index( request ):
    print( 'view, render_index: called.' )
    
    return render( request = request, template_name = "giwpage/index2.html" )