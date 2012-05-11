from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from polls.models import Poll, Choice
from django.template import RequestContext
from django.core.urlresolvers import reverse


# function that shows the index page
# def index(request):
#     latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#     #output = ', '.join([p.question for p in latest_poll_list])
#     return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list, })


# function that shows a poll detail
# def detail(request, poll_id):
#     p = get_object_or_404(Poll, pk=poll_id)
#     return render_to_response('polls/detail.html', {'poll': p}, context_instance=RequestContext(request))


# function that shows a result page
# def results(request, poll_id):
#     p = get_object_or_404(Poll, pk=poll_id)
#     return render_to_response('polls/results.html', {'poll': p})


# function that makes a vote and show the result page
def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        choice_selected = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the poll voting form
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': 'Hubo un error al realizar la votacion', },
            context_instance=RequestContext(request))
    else:
        choice_selected.votes += 1
        choice_selected.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll_result', args=(p.id,)))


# function that shows the server error page
def server_error(request):
    return HttpResponse("Sorry, we have and error in the system")
