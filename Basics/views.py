from django.shortcuts import render

# Create your views here.
def calculation(request):
    if request.method=="POST":
        num1=int(request.POST.get('txtno1'))
        num2=int(request.POST.get('txtno2'))
        btn=request.POST.get('btnsubmit')
        if btn=="+":
            result=num1+num2
        elif btn=="-":
            result=num1-num2
        elif btn=="*":
            result=num1*num2
        elif btn=="/":
            result=num1/num2
        return render(request,"Basics/Calculator.html",{'res':result})
    else:
        return render(request,"Basics/Calculator.html")

def LargestSmallest(request):
    if request.method=="POST":
        num1=int(request.POST.get('txtno1'))
        num2=int(request.POST.get('txtno2'))
        num3=int(request.POST.get('txtno3'))
        btn=request.POST.get('btnsubmit')
        if btn=="Find":
            if(num1>num2):
                if(num1>num3):
                    large=num1
                else:
                    large=num3
            else:
                if num2>num3:
                    large=num2
                else:
                    large=num3
            if(num1<num2):
                if(num1<num3):
                    small=num1
                else:
                    small=num3
            else:
                if num2<num3:
                    small=num2
                else:
                   small=num3
        return render(request,"Basics/LargestSmallest.html",{'large':large,'small':small})
    else:
        return render(request,"Basics/LargestSmallest.html")

def Ranklist(request):
    if request.method=="POST":
        name=request.POST.get("txtname")
        gender=request.POST.get("Gender")
        department=request.POST.get("department")
        m1=int(request.POST.get('txtm1'))
        m2=int(request.POST.get('txtm2'))
        m3=int(request.POST.get('txtm3'))
        btn=request.POST.get('btnsubmit')
        if btn=="Submit":
            total=m1+m2+m3
            percentage=(total/300)*100
            if(percentage>= 90):
                grade="A+"
            elif(percentage>=80):
                grade="A"
            elif(percentage>=60):
                grade="B"
            else:
                grade="C"
        return render(request,"Basics/Ranklist.html", {'name':name, 'gender':gender,'department':department})
    else:
        return render(request,"Basics/Ranklist.html")


                         
