from django.shortcuts import render
import time
from datetime import datetime
# Create your views here.

def timer():
    seconds = time.time()
    local_time = time.ctime( seconds )
    time_struct = time.localtime( seconds )
    
    if time_struct.tm_mon > 11:
        # after 11/30, the registration process can no longer be selected.
        return True
    else:
        return False
    

def render_index( request ):
    ret = timer()
    # ret = True
    if ret is True:
        return render( request = request, template_name = "giwpage/index4.html" )
    else:
        return render( request = request, template_name = 'giwpage/index3.html' )