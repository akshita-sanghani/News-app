from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import userForms
from service.models import Service
from news.models import News
from contactenquiry.models import Contactenquiry
from django.core.paginator import Paginator

def aboutUs(request):
    return HttpResponse("Hello World!")

def courseId(request, courseid):
    return HttpResponse(courseid)

# def homePage(request):
#     data = {
#     "title" : "Home New",
#     "bdata" : "Wecome to Wscubetech !",
#     "clist" : ['PHP', 'JAVA', 'Django'],
#     "numbers" : [10,20,30,40,50],
#     "student_details" :[
#         {'name' : 'Pradeep', 'phone_no': 9874563210},
#         {'name' : 'sandeep', 'phone_no': 9876574121}
#     ]
#     } 
#     return render(request, 'index.html', data)

def homePage(request):
    data = {}
    newsData = News.objects.all()
    paginator = Paginator(newsData, 2)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    newsDatafinal = paginator.get_page(page_number)
    totalpages = newsDatafinal.paginator.num_pages
    # serviceData = Service.objects.all().order_by('service_title') # show ascending order
    # serviceData = Service.objects.all().order_by('id') # show ascending order by it's field.
    # serviceData = Service.objects.all().order_by('-service_title') - show data in descending order
    # serviceData = Service.objects.all().order_by('service_title')[2:4] # show limited data

    # to show the specific section
    # if request.method=='GET':
    #     st = request.GET.get('newsname')
    #     if st!=None:
    #         newsData = News.objects.filter(news_title__icontains=st)
    data = {
        # 'serviceData' : serviceData,
        'newsData': newsDatafinal,
        'lastpage': totalpages,
        'totalpagelist' : [n+ 1 for n in range(totalpages)]
    }
    return render(request, "index.html", data)

def newsDetails(request,slug):
    newsDetails = News.objects.get(news_slug=slug)
    data = {
        'newsDetails' : newsDetails
    }
    return render(request, 'newsDetails.html', data)
    
def about(request):
    return render(request, "about.html")

def post(request):
    return render(request, "post.html")

def contact(request):
    return render(request, "contact.html")

def saveEnquiry(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        en = Contactenquiry(name=name, email=email, phone=phone, message=message)
        en.save()
    return render(request, 'contact.html')

# GET method
# def userForm(request):
#     finalres = 0
#     try:
#         n1 = int(request.GET['num1'])
#         n2 = int(request.GET['num2'])
#         finalres = n1+ n2
#     except:
#         pass
#     return render(request, "userform.html", {'finalres': finalres})

# POST method - required csrf token
def userForm(request):
    finalres = 0
    data = {}
    try:
        if request.method == "POST":
            n1 = int(request.POST['num1'])
            n2 = int(request.POST['num2'])
            finalres = n1+ n2
            data= {
                'n1': n1,
                'n2': n2,
                'output': finalres
            }
    except:
        pass
    return render(request, "userform.html", data)

# submit data using action method - which redirect the URL and provided the result
def submitForm(request):
    finalres = 0
    try:
        if request.method == "POST":
            n1 = int(request.POST['num1'])
            n2 = int(request.POST['num2'])
            finalres = n1+ n2
            return HttpResponse(finalres)
    except:
        pass

# django forms
# def userForm(request):
#     finalres = 0
#     fn = userForms()
#     data = {'forms': fn}
#     try:
#         if request.method == "POST":
#             n1 = int(request.POST['num1'])
#             n2 = int(request.POST['num2'])
#             n3 = int(request.POST['num3'])
#             finalres = n1+ n2 + n3
#             data= {
#                 'forms' : fn,
#                 'output': finalres
#             }
#             url = '/about-us/?output={}'.format(finalres)
#             return redirect(url)
#     except:
#         pass
#     return render(request, "userform.html", data)


# calculator function
def calculator(request):
    c = ''
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == '+':
                c = n1 + n2
            elif opr == '-':
                c = n1 - n2
            elif opr == '*':
                c = n1 * n2
            elif opr == '/':
                c = n1 / n2
    except:
        c = 'Invalid opr...'
    return render(request, 'calculator.html', {'c': c})

# evenodd function
def evenodd(request):
    c = ''
    data = {}
    if request.method == "POST":
        n1 = eval(request.POST.get('num1'))
        if n1 % 2 == 0:
            c = "Even"
        else:
            c = "Odd"
        data = {
            'n1': n1,
            'c' : c
        }
    return render(request, 'evenodd.html', data)

# MarkSheet function
def marksheet(request):
    data = {}
    if request.method == "POST":
        sub1 = eval(request.POST.get('subject1'))
        sub2 = eval(request.POST.get('subject2'))
        sub3 = eval(request.POST.get('subject3'))
        sub4 = eval(request.POST.get('subject4'))
        sub5 = eval(request.POST.get('subject5'))
        total = sub1 + sub2 + sub3 + sub4 + sub5 
        per = total*100/500
        if per >=60:
            div = "First Div"
        elif per >=48:
            div = "Second Div"
        elif per >=35:
            div = "Third Div"
        else:
            div = "Fail"
        data = {
            'sub1': sub1,
            'sub2': sub2,
            'sub3': sub3,
            'sub4': sub4,
            'sub5': sub5,
            'total': total,
            'percentage': per,
            'division': div
        }
    return render(request, 'marksheet.html', data)

# validation function
def validation(request):
    c = ''
    data = {}
    if request.method == "POST":
        if request.POST.get('num1') == '':
            return render(request, 'validation.html', {'error': True})
        n1 = eval(request.POST.get('num1'))
        if n1 % 2 == 0:
            c = "Even"
        else:
            c = "Odd"
        data = {
            'n1': n1,
            'c' : c
        }
    return render(request, 'validation.html', data)