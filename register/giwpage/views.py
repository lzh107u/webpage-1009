from django.shortcuts import render
import time
from datetime import datetime
# Create your views here.

def timer():
    seconds = time.time()
    local_time = time.ctime( seconds )
    time_struct = time.localtime( seconds )
    
    if time_struct.tm_mday >= 8:
        # after 11/8, the stage changes into 'standard rate'
        return True
    else:
        return False
    

def render_index( request ):
    ret = timer()
    
    if ret is True:
        return render( request = request, template_name = "giwpage/index3.html" )
    else:
        return render( request = request, template_name = 'giwpage/index2.html' )