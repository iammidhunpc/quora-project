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
from django.contrib.auth.hashers import make_password
from django.template.loader import render_to_string

from django import template
from django.template import loader

from django.core.mail import send_mail
from django.core.signing import Signer
from django.contrib.auth.mixins import AccessMixin
from login.mixin import ActiveOnlyMixin




class HandleMix(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return self.handle_no_permission()
        if not request.user.is_active:
            return self.handle_not_activated()
        return super(ActiveOnlyMixin, self).dispatch(request, *args, **kwargs)




class IndexView(FormView):
    form_class = NameForm
    template_name = 'reg.html'
    success_url='log'
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.password = make_password( obj.password )
        form.save()

        signer = Signer()
        signed_value = signer.sign(obj.email)
        key = ''.join(signed_value.split(':')[1:])
        reg_obj = Registration.objects.create(user=obj, key=key)
        msg_html = render_to_string('email-act.html', {'key': key})
        messages.add_message(self.request, messages.WARNING, 'Confirmation mail is send to your accout  !')
        send_mail("123", "123", 'anjitha.test@gmail.com', [obj.email], html_message=msg_html, fail_silently=False)
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

        user = authenticate(username=nam1, password=sid1)
        print(nam1)
        print(sid1)
        print(user)
        if user:
            login(self.request,user)
            # Is the account active? It could have been disabled.
            if user.is_active:
                if user.is_superuser:
                    return HttpResponseRedirect('/login/home')
                else:
                    return HttpResponseRedirect(self.get_success_url())

            else:
                return HttpResponseRedirect('/login/log')
        else:
            messages.add_message(self.request, messages.WARNING, 'Invalid username or password !')
        # Bad login details were provided. So we can't log the user in.
            return HttpResponseRedirect('/login/log')


class LogAdminView(FormView):
    form_class = LogadminForm
    template_name = 'admin_login.html'
    def form_valid(self, form):
        # nam1 = self.request.POST.get('nam')
        # sid1 = self.request.POST.get('sid')
        nam1= form.cleaned_data['name']
        sid1 = form.cleaned_data['password']

        user = authenticate(username=nam1, password=sid1)
        print(nam1)
        print(sid1)
        print(user)
        if user:
            login(self.request,user)
            # Is the account active? It could have been disabled.
            if user.is_active:
                if user.is_superuser:
                    #obj=Register.objects.filter(name=nam1, password=sid1).exists()
                    #if (obj==True):
                    return HttpResponseRedirect('/login/admin')
                 
                else:
                    return HttpResponseRedirect('/login/adminlogin')
            else:
                messages.add_message(self.request, messages.WARNING, 'Invalid username or password !')

                return HttpResponseRedirect('/login/adminlogin')
        else:
            messages.add_message(self.request, messages.WARNING, 'Invalid username or password !')

            return HttpResponseRedirect('/login/adminlogin')



class SuccessView(ActiveOnlyMixin,FormView):
    template_name = 'success.html'
    form_class = QuestForm
    success_url='success'
    permission_denied_message = 'You must be logged in to view this page'
    not_activated_message = 'You haven\'t activated your account yet'
    # You will need to implement this view
    not_activated_redirect = 'home'

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        st3=[]
        st9=[]
        namee=''
        obj1=Logs.objects.all()
        obj6=Comm.objects.all()
        obj4=Quest.objects.filter(status='approved')
        obj5=Ans.objects.filter(status='approved')
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
        if q1=='':
            messages.add_message(self.request, messages.WARNING, 'Question cant be empty !')
        
        else:
            obj1=Quest.objects.create(logid=logids,status='pending',question=q1,users=self.request.user.username)
            messages.add_message(self.request, messages.WARNING, 'Your question is pending moderation from the admin !')
        return super(SuccessView,self).form_valid(form)  

class FailedView(generic.TemplateView):
    template_name = 'failed.html'


class AdminView(generic.TemplateView):
    template_name = 'admin_home.html'

class HomeView(generic.TemplateView):
   
    obj1=Logs.objects.all()

    template_name = 'home.html'






class QuestapView(ActiveOnlyMixin,FormView):
    template_name = 'questap.html'
    form_class = ActForm
    success_url='questap'
    permission_denied_message = 'You must be logged in to view this page'
    not_activated_message = 'You haven\'t activated your account yet'
    # You will need to implement this view
    not_activated_redirect = 'home'
    def get_context_data(self, **kwargs):
        context = super(QuestapView, self).get_context_data(**kwargs)
        st5=[]
        st6=[]
        st7=[]
        st8=[]
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
        context['question']=obj
        return context
class StatusView(FormView):
     def dispatch(self, request, *args, **kwargs):

        t = self.kwargs['statusid']
        obj3=Quest.objects.get(id=t)
        obj3.status='Approved'
        obj3.save()
        return HttpResponseRedirect('/login/questap')

    # def form_valid(self, form):
    # 	quest1 = form.cleaned_data['stats']
    # 	obj3=Quest.objects.filter(id=quest1)
    # 	for i in obj3:
    # 		i.status='1'
    # 		i.save()
    # 	return super().form_valid(form)

class AnsapView(ActiveOnlyMixin,FormView):
    template_name = 'ansap.html'
    form_class = AnsstatForm
    success_url='ansap'
    permission_denied_message = 'You must be logged in to view this page'
    not_activated_message = 'You haven\'t activated your account yet'
    # You will need to implement this view
    not_activated_redirect = 'home'
    def get_context_data(self, **kwargs):
        context = super(AnsapView, self).get_context_data(**kwargs)
        st10=[]
        st11=[]
        st12=[]
        st13=[]
        st14=[]
        st15=[]
        obj1=Ans.objects.all()
        obj=Quest.objects.all()
        for i in obj1:
            st10.append(i.id)
            st11.append(i.answer)
            st12.append(i.status)
            st13.append(i.ques)
            context['st10'] = st10
            context['st11'] = st11
            context['st12'] = st12
            context['st13'] = st13
 
        return context


class StatusAnsView(FormView):
     def dispatch(self, request, *args, **kwargs):

        t = self.kwargs['statusansid']
        obj3=Ans.objects.get(id=t)
        obj3.status='Approved'
        obj3.save()
        return HttpResponseRedirect('/login/ansap')     
        

class AnswerView(ActiveOnlyMixin,FormView):
    template_name = 'answer.html'
    form_class = AnsForm
    success_url='/login/success'
    permission_denied_message = 'You must be logged in to view this page'
    not_activated_message = 'You haven\'t activated your account yet'
    # You will need to implement this view
    not_activated_redirect = 'home'

    def get_context_data(self, *args, **kwargs):
        context = super(AnswerView,self).get_context_data(**kwargs)
        qid = self.kwargs['qid']
        q_obj = Quest.objects.get(id=qid)
        context['question'] = q_obj

        return context

    def form_valid(self, form):


        tmp = self.kwargs['qid']
        # import pdb;pdb.set_trace()
        int(tmp)
        qqobj = Quest.objects.get(id=tmp)
        answ1 = form.cleaned_data['txta']
        if answ1=='':

            messages.add_message(self.request, messages.WARNING, 'Answer cant be empty !')
            return HttpResponseRedirect('/login/answer')
        else:
            obj4=Ans.objects.create(answer=answ1,status='pending',ques=str(qqobj),questid=tmp,users=self.request.user.username)
            obj4.save()
        
            messages.add_message(self.request, messages.WARNING, 'your answer is pending modaration from the admin !')
            return HttpResponseRedirect(self.get_success_url())
        return super(AnswerView,self).form_valid(form)


class CommentView(ActiveOnlyMixin,FormView):
    template_name = 'comment.html'
    form_class = ComForm
    success_url='/login/success'
    permission_denied_message = 'You must be logged in to view this page'
    not_activated_message = 'You haven\'t activated your account yet'
    # You will need to implement this view
    not_activated_redirect = 'home'

    def get_context_data(self, *args, **kwargs):
        context = super(CommentView,self).get_context_data(**kwargs)
        aid = self.kwargs['aid']
        a_obj = Ans.objects.get(id=aid)
        context['answer'] = a_obj
        return context
    def form_valid(self, form):

       comment1 = form.cleaned_data['txtc']

       tmp1 = self.kwargs['aid']
       if comment1=='':
            messages.add_message(self.request, messages.WARNING, 'Answer cant be empty !')
            return HttpResponseRedirect('/login/answerdetail')
       else:

            obj5=Comm.objects.create(comment=comment1,ansid=tmp1,users=self.request.user.username)
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
class DeleteView(ActiveOnlyMixin,generic.TemplateView):
    template_name = 'success.html'
    success_url='/login/success'
    permission_denied_message = 'You must be logged in to view this page'
    not_activated_message = 'You haven\'t activated your account yet'
    # You will need to implement this view
    not_activated_redirect = 'home'
    def dispatch(self, request, *args, **kwargs):
        context = super(DeleteView,self).get_context_data(**kwargs)
        did = self.kwargs['did']

        q_obj = Quest.objects.filter(id=did)
        for i in q_obj:
            if (self.request.user.username == i.users):
                q_obj.delete()
                return HttpResponseRedirect('/login/success')
            else:
                messages.add_message(self.request, messages.WARNING, 'You cant delete other users question !')
                return HttpResponseRedirect('/login/success')
class DeleteansView(ActiveOnlyMixin,generic.TemplateView):
    template_name = 'success.html'
    success_url='/login/success'
    permission_denied_message = 'You must be logged in to view this page'
    not_activated_message = 'You haven\'t activated your account yet'
    # You will need to implement this view
    not_activated_redirect = 'home'
    def dispatch(self, request, *args, **kwargs):
        context = super(DeleteansView,self).get_context_data(**kwargs)
        daid = self.kwargs['daid']
        q_obj = Ans.objects.filter(id=daid)
        for i in q_obj:
            if (self.request.user.username == i.users):
                q_obj.delete()
                return HttpResponseRedirect('/login/success')
            else:
                messages.add_message(self.request, messages.WARNING, 'You cant delete other users answer !')
                return HttpResponseRedirect('/login/success')



class RegistrationSuccess(generic.TemplateView):
    template_name = 'registration-success.html'

    def get(self, request, *args, **kwargs):
        key = self.kwargs.get("key")
        try:
            reg_obj = Registration.objects.get(key=key)
            reg_obj.user.is_active = True
            reg_obj.save()
            context = {'user': reg_obj, 'status': True}
            return self.render_to_response(context)
        except Registration.DoesNotExist:
            return self.render_to_response({'status': False})

