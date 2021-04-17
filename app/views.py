from django.shortcuts import render,redirect
from django.views.generic import TemplateView,DetailView
from django.views.generic.list import ListView
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

from app.models import Account,Transaction
from random import randint
import datetime

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

# def index(request):
#     return render(request,'index.html')

class UserView(ListView):
    model = Account
    context_object_name = 'accounts'
 

    def get_queryset(self, *args, **kwargs):
        qs = super(UserView, self).get_queryset(*args, **kwargs)
        
        # qs = qs.order_by("-id")
        print(qs)
        return qs

# def showuser(request):
#     account = Account.objects.all()

#     return render(request,'app/account_list.html',{'accounts':account})

def transferview(request):
    aid = request.GET.get('aid')
    iuser = Account.objects.get(id=aid)
    print(iuser)
    touser = Account.objects.exclude(id=aid)
    print('---->>>>  ',touser)

    return render(request,'transfer.html',{'me':iuser,'touser':touser})

def sendmoney(request):
    method = request.method
    if method == 'POST':


        money = int(request.POST.get('money'))
        rid = request.POST.get('user')
        sid = request.POST.get('sender')

        sender = s = Account.objects.get(id=sid) if sid.isnumeric() else Account.objects.get(name=sid)
        reciever = r = Account.objects.get(id=rid) if rid.isnumeric() else Account.objects.get(name=rid)

        if sender.balance > money:
            
            s.balance -= money
            r.balance += money

            s.save()
            r.save()

            request.session['status'] = 'success'
            request.session['from'] = s.name
            request.session['to'] = r.name
            request.session['amount'] = money
           
            d = datetime.datetime.now()
            request.session['time'] = d.strftime("%c")

            t_status = 'Payment Successful'
            t_id = randint(000000,999999) + d.year
            print('##############',t_id) 
            request.session['tid'] = t_id

            t_history = Transaction(to=r.name,From=s.name,amount=money,status='Success',t_id=t_id,time=d)
            t_history.save()
            return redirect('/app/sendmoney')

        else:
            print('Insufficient balance')   

            request.session['status'] = 'Failed'
            request.session['from'] = s.name
            request.session['to'] = r.name
            request.session['amount'] = money
            d = datetime.datetime.now()
            request.session['time'] = d.strftime("%c")

            t_status = 'You have Insufficient Balance'
            t_id = randint(000000,999999) + d.year
            print('##############',t_id) 
            request.session['time'] = d.strftime("%c")
            request.session['tid'] = t_id

            t_history = Transaction(to=r.name,From=s.name,amount=money,status='Failed',t_id=t_id,time=d)
            t_history.save()

            return render(request,'failed.html',{'pay_status':t_status})
        
        print(money,rid,' ++++++++++++  ',sid)
        
        
    return render(request,'send.html')

# def viewhistory(request):
#     allhistory = Transaction.objects.all().order_by('-id')
#     p = Paginator(allhistory,5)
#     page = request.GET.get('page',1)

#     try:
#         pageobj = p.page(page)
#     except PageNotAnInteger:
#         pageobj = p.page(1)
#     except EmptyPage:

#         pageobj =  p.page(p.num_pages) 

#     print(page)    
#     print(pageobj)


#     return render(request,'history.html',{'transactions':allhistory,'pages':pageobj})    

class ViewHistory(ListView):
    model = Transaction
    template_name = 'history.html'  
    context_object_name = 'transactions'  # Default: object_list
    paginate_by = 10
    queryset = Transaction.objects.all().order_by('-id')  # Default: Model.objects.all()

def deltransac(request):
    tid = request.GET.get('id')
    print('*******',tid)
    history = Transaction.objects.get(id=tid)    
    history.delete()

    return redirect('/app/history')

def repeat_transac(request):
    tid = request.GET.get('id')
    trans_details  = Transaction.objects.get(id=tid)    

    return render(request,'repeat.html',{'pay':trans_details})

class Customers(ListView):
    model = Account
    context_object_name = 'customers'  
    template_name = 'customers.html' 

def profile(request):
    who = request.GET.get('name')   
    profile = Account.objects.get(name=who) 
    return render(request,'profile.html',{'p':profile})

def your_transactions(request):

    you = request.GET.get('t')
    transac = Transaction.objects.filter(From=you).order_by('-id')
    return render(request,'user-transactions.html',{'transactions':transac}) 

class AboutPage(TemplateView):
    template_name = 'About.html'    