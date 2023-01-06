from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from .models import Tweet
from .forms import TweetForm
import random
from django.utils.http import is_safe_url, url_has_allowed_host_and_scheme
from django.conf import settings
from django.contrib import messages

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


# messages.debug(request, '%s SQL statements were executed.' % count)
# messages.info(request, 'Three credits remain in your account.')
# messages.success(request, 'Profile details updated.')
# messages.warning(request, 'Your account expires in three days.')
# messages.error(request, 'Document deleted.')


def home_view(request):
    return render(request, 'tweets/home.html', context=None)


def tweet_list_view(request):
    tweets = Tweet.objects.all().order_by('-id')
    tweet_list = []
    for tweet in tweets:
        likes = random.randint(0, 200)
        tweet_list.append({'id': tweet.id, 'content': tweet.content, 'likes': likes})
    data = {
        'tweet_list': tweet_list
    }
    return JsonResponse(data)
    # return render(request, 'tweets/home.html', context=None)

def tweet_create_view(request):
    # form = TweetForm(request.POST or None)
    if request.method == 'POST':
        form = TweetForm(request.POST)
        next_url = request.POST.get('next')
        if form.is_valid():
            data = form.save(commit=False)
            # if is_safe_url(next_url, ALLOWED_HOSTS):
            #     print('redirected')
            messages.success(request, 'New Tweet posted')
            return redirect(next_url)
            # if request.is_ajax():
            #     return JsonResponse({})

    # messages.error(request, 'New Tweet failed to post')
    # return redirect('tweets:home')
