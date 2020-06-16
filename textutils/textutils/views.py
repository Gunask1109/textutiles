from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
    #return HttpResponse("Hello World!")
#pipline
def analyze(request):
    #get the text
    djtext=request.GET.get('text','default')
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    print(djtext)
    #analyzed= djtext
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params ={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")

#def capfirst(request):
 #   return HttpResponse("capitalize first")

#def newlineremove(request):
  #  return HttpResponse("newlinearemove")

#def spaceremove(request):
 #   return HttpResponse("spaceremove")


#def charcount(request):
  #  return HttpResponse("charcount")