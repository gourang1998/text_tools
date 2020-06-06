from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newLineremove = request.POST.get('newLineremove', 'off')
    extraSpace = request.POST.get('extraSpace', 'off')
    if removepunc == "on":
        punctaution = '''!~`@#$%^&*()-_=+{}[]|"'|\/?<>;:'''
        analyzed = ""
        for char in djtext:
            if char not in punctaution:
                analyzed = analyzed + char
        param = {'purpose': 'Remove Punctaution', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', param)
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        param = {'purpose':'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html',param)
    if(newLineremove== "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !='\r':
                analyzed = analyzed + char
        param = {'purpose':'Remove New Line','analyzed_text':analyzed}
        djtext = analyzed
    #    return render(request, 'analyze.html', param)
    if(extraSpace== "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1]== " ":
                pass
            else:
                analyzed = analyzed + char
        param = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}


    if(removepunc!="on" and fullcaps!="on" and extraSpace!="on" and newLineremove!="on"):
        return HttpResponse("ERROR")

    return render(request, 'analyze.html', param)


