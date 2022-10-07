from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
     return HttpResponse('''<html>
     <title>WaterinTap</title>
     <h1>WaterinTap</h1>
     </html>''')
