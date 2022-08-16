#This file is made by myself
from email.policy import default
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
# def about(request):
#     return HttpResponse('''<h1>About hello</h1> <a href="https://www.google.com/search?q=how+to+add+new+line+in+html&rlz=1C1CHBD_enIN891IN891&sxsrf=ALiCzsZC4KG13kqM162MLS_QfmvC-4Ih-w%3A1660154992387&ei=cPTzYraeF5-gz7sPl9eP4AI&ved=0ahUKEwi2lt-k77z5AhUf0HMBHZfrAywQ4dUDCA4&uact=5&oq=how+to+add+new+line+in+html&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIGCAAQHhAHMgYIABAeEAcyBggAEB4QBzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIABBHELADOgcIABCwAxBDSgQIQRgASgQIRhgAUEBY8xlg8ixoAXABeACAAeYCiAH3GZIBCDAuMi4xMS4xmAEAoAEByAEKwAEB&sclient=gws-wiz">Some help</a>''')
# def contacts(request):
#     return HttpResponse('''<h1>CONTACTS</h1>''')  
# def history(request):
#     return HttpResponse('''<h1>History</h1>''')     
def analyze(request):
    djtext=request.POST.get('Text','default')
    djcheck=request.POST.get("Remove_Punctuations" ,'off')
    capitalcheck=request.POST.get("CAPITALIZE" ,'off')
    newlinecheck=request.POST.get("Remove_new_lines" ,'off')
    extraspacecheck=request.POST.get("Remove_extra_spaces" ,'off')
    countcheck=request.POST.get("Count_Characters" ,'off')
    # print(djtext)
    # print(djcheck)
    # return HttpResponse("remove punc") 
    analyzed=""
    if djcheck=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        # params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        # print(analyzed)
        # return render(request,'analyze.html',params)
    if(capitalcheck=='on'):
        analyzed=djtext.upper()
        # params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params) 
    if(newlinecheck=='on'):
        analyzed=''
        for char in djtext:
            if char!='/n':
                analyzed=analyzed+char
        # params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)  
        djtext=analyzed
    if(extraspacecheck=='on'):
        analyzed=''
        for i,char in enumerate(djtext):
            if not(djtext[i]==" " and djtext[i+1]==" "):
                analyzed=analyzed+char
        # params= {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)
        djtext=analyzed
    elif(countcheck=='on'):
        count=0
        for char in djtext:
            if char!=" ":
                count=count+1
        params= {'purpose':'Removed Punctuations','analyzed_text':f"There are {count} characters"}
        return render(request,'analyze.html',params)            
    if analyzed=="":
        return HttpResponse("Error")
    else:
        params= {'purpose':'Removed Punctuations','analyzed_text':djtext}
        return render(request,'analyze.html',params)   