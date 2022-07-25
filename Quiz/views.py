from django.shortcuts import redirect,render, get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import createuserform, addQuestionform
from .models import QuesModel, Category
import random

 
# Create your views here.
@login_required(login_url='login/')
def category(request):
    category = Category.objects.all()
    return render(request, 'Quiz/category.html', {'category':category})

@login_required(login_url='login/')
def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)

    if request.method == 'POST':
        questions = QuesModel.objects.filter(category__slug=category.slug) 
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            # print(request.POST.get(q.question))
            # print(q.ans)
            # print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
            'category':category
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions = list(QuesModel.objects.filter(category__slug=category.slug))
        random.shuffle(questions)
        context = {
            'questions':questions
        }
        return render(request, 'Quiz/quiz.html', {'questions':questions, 'category':category})




@login_required(login_url='login/')
def home(request):
    if request.method == 'POST':
        questions=QuesModel.objects.all()
        random.shuffle(questions)
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            # print(request.POST.get(q.question))
            # print(q.ans)
            # print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'Quiz/home.html',context)
 
def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if request.method=='POST':
            form=addQuestionform(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'Quiz/addQuestion.html',context)
    else: 
        return redirect('home') 
 
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form = createuserform()
        if request.method=='POST':
            form = createuserform(request.POST)
            if form.is_valid() :
                form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'Quiz/register.html',context)
 
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'Quiz/login.html',context)
 
def logoutPage(request):
    logout(request)
    return redirect('/')