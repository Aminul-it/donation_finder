from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import CreateView , UpdateView,ListView,TemplateView,View,DetailView,TemplateView,DeleteView
from Event_app.models import event,Comment,Like
from django.urls import reverse , reverse_lazy
from  django.contrib.auth.decorators import login_required
from  django.contrib.auth.mixins import LoginRequiredMixin
from Event_app.forms import CommentForm
import uuid

import razorpay
from django.views.decorators.csrf import csrf_exempt
class my_event(LoginRequiredMixin,TemplateView):
    template_name = 'Event/my_event.html'


class create_event(CreateView,LoginRequiredMixin):
      model = event
      template_name = 'Event/create_event.html'
      fields = ('organizer','event_title','event_content','event_image', 'Start_date','End_date')

      def form_valid(self , form):
          event_obj = form.save(commit=False)
          event_obj.author = self.request.user
          title = event_obj.event_title
          event_obj.slug  = title.replace(" ","-")+ "-" + str(uuid.uuid4())
          event_obj.save()
          return HttpResponseRedirect(reverse('index'))
class EventList(ListView):
      context_object_name = 'events'
      model = event
      template_name  = 'Event/event_list.html'


@login_required
def event_details(request,slug):
    Event = event.objects.get(slug=slug)
    Comment_Form = CommentForm()
    already_interested = Like.objects.filter(event=Event , user = request.user)
    if already_interested:
        liked = True
    else:
        liked  = False
    if request.method == 'POST':
        Comment_Form  = CommentForm(request.POST)
        if Comment_Form.is_valid():
            comment = Comment_Form.save(commit=False)
            comment.user = request.user
            comment.event = Event
            comment.save()
            return HttpResponseRedirect(reverse('event_app:event_details', kwargs={'slug':slug}))
    return render(request, 'Event/event_details.html', context={'Event':Event ,'Comment_Form':Comment_Form  ,'liked':liked})
@login_required
def like(request,pk):
    Event = event.objects.get(pk=pk)
    user = request.user
    already_interested = Like.objects.filter(event=Event,user=user)
    if not already_interested:
        interested_post = Like(event=Event,user=user)
        interested_post.save()
    return HttpResponseRedirect(reverse('event_app:event_details', kwargs={'slug':Event.slug }))
@login_required
def unlike(request,pk):
    Event = event.objects.get(pk=pk)
    user = request.user
    already_not_interested = Like.objects.filter(event=Event,user=user)
    already_not_interested.delete()
    return HttpResponseRedirect(reverse('event_app:event_details', kwargs={'slug':Event.slug }))



"""
payment

"""

def home_donate(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = razorpay.Client(
            auth=('rzp_test_DpAaHaFXPmSMVX', 'sH2spxN4o9vG2sqaFIIsvvxy'))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'payment/index.html')

@csrf_exempt
def success(request):
    return render(request, 'payment/success.html')

"""
payment End
"""


class UpdateEvent(LoginRequiredMixin,UpdateView):
    model = event
    fields = ('event_title','event_content','event_image','End_date')
    template_name = 'Event/create_event.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('event_app:event_details' ,kwargs={'slug':self.object.slug})
