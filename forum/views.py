from django.shortcuts import render
from django.views import View
from .models import Thread, Post, Reply
from members.models import Member
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators import csrf
from django.core.paginator import Paginator

import logging
logger = logging.getLogger(__name__)

class ForumDirectory(View):
    template_name='forum/forum_directory.html'

    def get(self, request):
        threads = Thread.objects.all().order_by('-created_at')
        context = {
            'threads': threads
        }

        return render(request, self.template_name, context)

class ThreadPage(View):
    template_name='forum/discussion.html'

    def get(self, request, pk):

        posts = Post.objects.filter(thread=pk).order_by('-created_at')
        replies = Reply.objects.filter(thread=pk).order_by('created_at')
        thread = Thread.objects.get(pk=pk)

        user_member = Member.objects.get(user=request.user.pk)

        context = {
            'thread': thread,
            'posts': posts,
            'replies': replies,
            'user': user_member
        }

        return render(request, self.template_name, context)

class CreateDiscussion(CreateView):
    template_name = 'forum/create_discussion.html'
    model = Thread
    fields = ('title', 'subtitle')
    

    def dispatch(self, *args, **kwargs):
        return super(CreateDiscussion, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        member = Member.objects.get(user=self.request.user)
        obj.created_by = member
        obj.created_by_string = member.first_name + member.last_name
        obj.save()

        success_url = '/forum/' + str(obj.pk)
        return HttpResponseRedirect(success_url)

class UpdateDiscussion(UpdateView):
    template_name = 'forum/update_discussion.html'
    model = Thread
    fields = ('title', 'subtitle')

    def dispatch(self, *args, **kwargs):
        return super(UpdateDiscussion, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()

        success_url = '/forum/' + str(obj.pk)
        return HttpResponseRedirect(success_url)
   

class CreatePost(CreateView):
    template_name = 'forum/create_post.html'
    model = Post
    fields = ('body',)

    def dispatch(self, *args, **kwargs):
        return super(CreatePost, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        member = Member.objects.get(user=self.request.user)
        obj.created_by = member
        obj.created_by_string = member.first_name + member.last_name
        thread_pk = self.kwargs.get('pk')
      
        thread = Thread.objects.get(pk=thread_pk)
        obj.thread = thread
        obj.save()
        success_url = '/forum/' + str(thread_pk) 
        return HttpResponseRedirect(success_url)

class UpdatePost(UpdateView):
    template_name = 'forum/update_post.html'
    model = Post
    fields = ('body',)

    def dispatch(self, *args, **kwargs):
        return super(UpdatePost, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        thread_pk = obj.thread.pk
        obj.save()

        success_url = '/forum/' + str(thread_pk)
        return HttpResponseRedirect(success_url)
    

class CreateReply(CreateView):
    template_name = 'forum/create_reply.html'
    model = Reply
    fields = ('body',)

    def dispatch(self, *args, **kwargs):
        return super(CreateReply, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        member = Member.objects.get(user=self.request.user)
        obj.created_by = member
        obj.created_by_string = member.first_name + member.last_name

        thread_pk = self.kwargs.get('pk')
        thread = Thread.objects.get(pk=thread_pk)
        obj.thread = thread

        post_pk = self.kwargs.get('post_pk')
        post = Post.objects.get(pk=post_pk)
        obj.post = post

        obj.save()
        success_url = '/forum/' + str(thread_pk)
        return HttpResponseRedirect(success_url)

class UpdateReply(UpdateView):
    template_name = 'forum/update_reply.html'
    model = Reply
    fields = ('body',)

    def dispatch(self, *args, **kwargs):
        return super(UpdateReply, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        thread_pk = obj.thread.pk
        obj.save()

        success_url = '/forum/' + str(thread_pk)
        return HttpResponseRedirect(success_url)

@csrf.csrf_exempt
def like(request):
    id = request.POST.get('pk')
    post = Post.objects.get(pk=id)
    post.likes += 1
    post.save()
    return HttpResponse('success')

@csrf.csrf_exempt
def flag(request):
    id = request.POST.get('pk')
    post = Post.objects.get(pk=id)
    post.flagged = True
    post.number_of_flags += 1
    post.save()
    return HttpResponse('success')


