from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
    #return HttpResponse("Hello World!")
#pipline
def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')
    #check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover= request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    #analyzed= djtext
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params ={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)

    if fullcaps == "on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if extraspaceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]== "":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if charcount == "on":
        analyzed = 0
        for char in djtext:
            analyzed+=1
        params = {'purpose': 'Count Of Character ', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)



    #else:
        #return HttpResponse("Error")
    return render(request, 'analyze.html', params)




#def capfirst(request):
 #   return HttpResponse("capitalize first")

#def newlineremove(request):
  #  return HttpResponse("newlinearemove")

#def spaceremove(request):
 #   return HttpResponse("spaceremove")


#def charcount(request):
  #  return HttpResponse("charcount")