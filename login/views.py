from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views import generic
from .forms import *
from .models import *
from django.views.generic.edit import FormView
from django.urls import reverse
class IndexView(FormView):
	form_class = NameForm
	template_name = 'reg.html'
	success_url='display'
	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

class DisplayView(generic.TemplateView):
    template_name = 'view.html'

    def get_context_data(self, **kwargs):
        context = super(DisplayView, self).get_context_data(**kwargs)

        st4=[]
        st5=[]
        obj=Register.objects.all()
        for i in obj:
            st4.append(i.name)
            st5.append(i.rollno)
        context['st4'] = st4
        context['st5'] = st5
        return context


class LogView(FormView):
    form_class = LogForm
    template_name = 'log.html'
    success_url='success'

    def form_valid(self, form):
        # nam1 = self.request.POST.get('nam')
        # sid1 = self.request.POST.get('sid')
        nam1= form.cleaned_data['nam']
        sid1 = form.cleaned_data['sid']
        obj1=Logs.objects.create(nam=nam1)
        obj1.save()
        obj=Register.objects.filter(name=nam1, sid=sid1).exists()
        if (obj==True):
        	return HttpResponseRedirect(self.get_success_url())
        else:
        	return HttpResponseRedirect('failed')



class SuccessView(FormView):
    template_name = 'success.html'
    form_class = QuestForm
    success_url='home'
    def get_context_data(self, **kwargs):
     	context = super(SuccessView, self).get_context_data(**kwargs)
     	st3=[]
     	st9=[]
     	st10=[]
     	st11=[]
     	namee=''
     	obj1=Logs.objects.all()

     	obj4=Quest.objects.filter(status='1')
     	context['qst'] = obj4
     	for k in obj4:
     		st9.append(k.question)
     		st10.append(k.logid_id)
     		st11.append(k.id)
     		context['st9']=st9
     		context['st10']=st10
     		context['st11']=st11
     	return context



     	for j in obj1:
     		namee=j.nam
     	obj=Register.objects.filter(name=namee)
     	for i in obj:
     		st3.append(i.name)
     		context['st3'] = st3
     		return context
    
    def form_valid(self, form):
    	# q1= form.cleaned_data['question']
    	# obj1=Quest.objects.filter(question=q1)
    	# obj1.save()
    	form.save()
    	return super().form_valid(form)
    	
class FailedView(generic.TemplateView):
    template_name = 'failed.html'
class HomeView(generic.TemplateView):
   
    obj1=Logs.objects.all()
   # obj1.delete()
    template_name = 'home.html'



class AdminView(FormView):
    template_name = 'admin_home.html'
    form_class = ActForm
    success_url='admin'
    def get_context_data(self, **kwargs):
     	context = super(AdminView, self).get_context_data(**kwargs)
     	st5=[]
     	st6=[]
     	st7=[]
     	st8=[]
     	obj=Quest.objects.all()
     	for j in obj:
     		st5.append(j.question)
     		st6.append(j.status)
     		st7.append(j.logid_id)
     		st8.append(j.id)
     		context['st5'] = st5
     		context['st6'] = st6
     		context['st7'] = st7
     		context['st8'] = st8
     	return context
    def form_valid(self, form):
    	quest1 = form.cleaned_data['stats']
    	obj3=Quest.objects.filter(id=quest1)
    	for i in obj3:
    		i.status='1'
    		i.save()
    	return super().form_valid(form)

class AnswerView(FormView):
    template_name = 'answer.html'
    form_class = AnsForm
    success_url='success'
    # def my_func(request):
    # # Get query_name from request
    # 	ques = request.GET.get('question')
    # 	HttpResponse(quest)
    def get_context_data(self, *args, **kwargs):
    	context = super(AnswerView,self).get_context_data(**kwargs)
    	qid = self.kwargs['qid']
    	print(qid)
    	q_obj = Quest.objects.get(id=qid)
    	context['question'] = q_obj
    	
    	return context

    def form_valid(self, form):
    	answ1 = form.cleaned_data['txta']
    	obj4=Ans.objects.create(answer=answ1,status=0,questid=0)
    	obj4.save()
    	return super().form_valid(form)

