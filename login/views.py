from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views import generic
from .forms import *
from .models import *
from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
class IndexView(FormView):
    form_class = NameForm
    template_name = 'reg.html'
    success_url='display'
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.password = make_password( obj.password )
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
            st5.append(i.email)
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
        nam1= form.cleaned_data['name']
        sid1 = form.cleaned_data['password']
        obj1=Logs.objects.create(name=nam1)
        obj1.save()

        user = authenticate(name=nam1, password=sid1)
        print(nam1)
        print(sid1)
        print(user)
        if user:
            login(self.request,user)
            # Is the account active? It could have been disabled.
            if user.is_active:
                    #obj=Register.objects.filter(name=nam1, password=sid1).exists()
                    #if (obj==True):
                return HttpResponseRedirect(self.get_success_url())
                 #   else:
                  #      return HttpResponseRedirect('failed')
            else:
                return HttpResponse("Enter valid details")
        else:
        # Bad login details were provided. So we can't log the user in.
            return HttpResponse("try again")



class SuccessView(FormView):
    template_name = 'success.html'
    form_class = QuestForm
    success_url='success'
    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        st3=[]
        st9=[]
        namee=''
        obj1=Logs.objects.all()
        obj6=Comm.objects.all()
        obj4=Quest.objects.filter(status='1')
        obj5=Ans.objects.filter(status='1')
        context['answers'] = obj5
        context['questions']=obj4
        context['comments']=obj6
        context['users']=obj1
        for j in obj1:
            namee=j.name
        obj=Register.objects.filter(name=namee)
        for i in obj:
            st3.append(i.name)
            context['st3'] = st3
            return context

    def form_valid(self, form):
        ob9=Logs.objects.all()
        for i in ob9:
            logids=i.id
        
        q1=form.cleaned_data['ques']
        obj1=Quest.objects.create(logid=logids,status=0,question=q1)
        messages.add_message(self.request, messages.WARNING, 'your question is pending moderation from the admin !')
        return super(SuccessView,self).form_valid(form)  

class FailedView(generic.TemplateView):
    template_name = 'failed.html'


class AdminView(generic.TemplateView):
    template_name = 'admin_home.html'

class HomeView(generic.TemplateView):
   
    obj1=Logs.objects.all()
   # obj1.delete()
    template_name = 'home.html'



class QuestapView(FormView):
    template_name = 'questap.html'
    form_class = ActForm
    success_url='questap'
    def get_context_data(self, **kwargs):
     	context = super(QuestapView, self).get_context_data(**kwargs)
     	st5=[]
     	st6=[]
     	st7=[]
     	st8=[]
     	st10=[]
     	st11=[]
     	st12=[]
     	st13=[]
     	obj=Quest.objects.all()
     	for j in obj:
     		st5.append(j.question)
     		st6.append(j.status)
     		st7.append(j.logid)
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

class AnsapView(FormView):
    template_name = 'ansap.html'
    form_class = AnsstatForm
    success_url='ansap'
    def get_context_data(self, **kwargs):
     	context = super(AnsapView, self).get_context_data(**kwargs)

     	st10=[]
     	st11=[]
     	st12=[]
     	st13=[]
     	obj1=Ans.objects.all()
     	for i in obj1:
     	 	st10.append(i.id)
     	 	st11.append(i.answer)
     	 	st12.append(i.status)
     	 	st13.append(i.questid)
     	 	context['st10'] = st10
     	 	context['st11'] = st11
     	 	context['st12'] = st12
     	 	context['st13'] = st13
     	return context
    def form_valid(self, form):

    	ans1 = form.cleaned_data['statans']
    	print(ans1)
    	obj4=Ans.objects.filter(id=ans1)
    	for i in obj4:
    	 	i.status='1'
    	 	i.save()
    	return super().form_valid(form)



class AnswerView(FormView):
    template_name = 'answer.html'
    form_class = AnsForm
    success_url='/login/success'

    def get_context_data(self, *args, **kwargs):
        context = super(AnswerView,self).get_context_data(**kwargs)
        qid = self.kwargs['qid']
        q_obj = Quest.objects.get(id=qid)
        context['question'] = q_obj

        return context

    def form_valid(self, form):

        answ1 = form.cleaned_data['txta']

        tmp = self.kwargs['qid']
        obj4=Ans.objects.create(answer=answ1,status=0,questid=tmp)
        obj4.save()
        messages.add_message(self.request, messages.WARNING, 'your answer is pending modaration from the admin !')
        return super(AnswerView,self).form_valid(form)


class CommentView(FormView):
    template_name = 'comment.html'
    form_class = ComForm
    success_url='/login/success'

    def get_context_data(self, *args, **kwargs):
        context = super(CommentView,self).get_context_data(**kwargs)
        aid = self.kwargs['aid']
        a_obj = Ans.objects.get(id=aid)
        context['answer'] = a_obj
        return context
    def form_valid(self, form):

       comment1 = form.cleaned_data['txtc']

       tmp1 = self.kwargs['aid']
       obj5=Comm.objects.create(comment=comment1,ansid=tmp1)
       obj5.save()
       return super(CommentView,self).form_valid(form)
# class DeleteView(generic.TemplateView):
#     template_name = 'success.html'
#     success_url='/login/success'
#     def get_context_data(self, *args, **kwargs):
#         context = super(DeleteView,self).get_context_data(**kwargs)
#         did = self.kwargs['did']
#         q_obj = Quest.objects.filter(id=did)
#         q_obj.delete()
#     def get_success_url(self, **kwargs):         
#         return reverse_lazy('/login/success', kwargs = {'pk': self.kwargs['did']})
class DeleteView(generic.TemplateView):
    template_name = 'success.html'
    success_url='/login/success'
    def get_context_data(self, *args, **kwargs):
        context = super(DeleteView,self).get_context_data(**kwargs)
        did = self.kwargs['did']
        q_obj = Quest.objects.filter(id=did)
        q_obj.delete()

    # def get_success_url(self, **kwargs):         
    #     return reverse_lazy('delete_detail', kwargs = {'pk': self.kwargs['did']})

        
class DeleteansView(generic.TemplateView):
	template_name = 'success.html'
	#success_url='/login/success'
	def get_context_data(self, *args, **kwargs):
		context = super(DeleteansView,self).get_context_data(**kwargs)
		daid = self.kwargs['daid']
		q_obj = Ans.objects.filter(id=daid)
		q_obj.delete()


