from video.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import simplejson as json
# Authentication
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
DEVELOPER_KEY = "AIzaSyA1A0iNtiAFf_ZgLdwifWH24WVR9BKvcQw"


# Flick
def flickr(request):
	photos = Photo.objects.all().order_by('-dateadded')[:300]
	groups = Group.objects.all().order_by('name')
	return render_to_response('flickr.html',{'listPhotos':photos,'groups':groups,'user':request.user},context_instance=RequestContext(request))

# Videos

def index(request):
	videos = Video.objects.all().order_by('-publishedAt')
	channels = Channel.objects.all().order_by('name')
	return render_to_response('index.html',{'listVideo':videos,'channels':channels,'user':request.user},context_instance=RequestContext(request))

def video(request,uuid):
	video = Video.objects.get(uuid=uuid)
	plus_likes = len(Like.objects.filter(video=video,type=True))
	minus_likes = len(Like.objects.filter(video=video,type=False))
	likes = plus_likes - minus_likes
	is_like_true = bool(Like.objects.filter(video=video,user=request.user.id,type=True))
	is_like_false = bool(Like.objects.filter(video=video,user=request.user.id,type=False))
	return render_to_response('video.html',{'video':video, 'like': likes,'isliketrue': is_like_true,'islikefalse': is_like_false},context_instance=RequestContext(request))

#Users
def new_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid:
			if request.POST['username'] != '' and request.POST['password1'] and request.POST['password2']!= '':
				form.save()
				return HttpResponseRedirect('/')
			else:
				return render_to_response('newuser.html',{'form':form},context_instance=RequestContext(request))
	else:
		form = UserCreationForm()
		return render_to_response('newuser.html',{'form':form},context_instance=RequestContext(request))

def login_user(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/')
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid:
			username = request.POST['username']
			passwd = request.POST['password']
			access = authenticate(username=username, password=passwd)
			if access is not None:
				login(request, access)
				if 'next' in request.GET:
					next = request.GET['next']
				else:
					next='/'
				if next is not None:
					return HttpResponseRedirect(next)
				else:
					return index(request)
			else:
				return login_form(request,True)
	else:
		return login_form(request,False)
		

def login_form(request,isFirst):
	form = AuthenticationForm()
	return render_to_response('login.html',{'form':form,'message':isFirst},context_instance=RequestContext(request))

@login_required(login_url='/users/login/')
def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')


# Gamefications
def like(request,uuid):
	if request.user.is_anonymous():
		return HttpResponse(json.dumps({'code':401,'message':'Unauthorized','uuid':uuid}), mimetype='application/json')
	else:
		video = Video.objects.get(uuid=uuid)
		user = request.user
		try:
			query = Like.objects.get(video=video,user=user)
			if (query.type == False):
				query.delete()
				plus_likes = len(Like.objects.filter(video=video,type=True))
				minus_likes = len(Like.objects.filter(video=video,type=False))
				likes = plus_likes - minus_likes
				return HttpResponse(json.dumps({'code':201,'message':'Like removed','uuid':uuid,'likes':likes}), mimetype='application/json')
			else:
				return HttpResponse(json.dumps({'code':400,'message':'Like already exist','uuid':uuid}), mimetype='application/json')
		except Like.DoesNotExist:
			like = Like(video=video,user=user)
			like.save()
			likes = len(Like.objects.filter(video=video))
			return HttpResponse(json.dumps({'code':200,'message':'Like registred','uuid':uuid,'likes':likes}), mimetype='application/json')

def unlike(request,uuid):
	if request.user.is_anonymous():
		return HttpResponse(json.dumps({'code':401,'message':'Unauthorized','uuid':uuid}), mimetype='application/json')
	else:
		video = Video.objects.get(uuid=uuid)
		user = request.user
		try:
			query = Like.objects.get(video=video,user=user)
			if (query.type == True):
				query.delete()
				plus_likes = len(Like.objects.filter(video=video,type=True))
				minus_likes = len(Like.objects.filter(video=video,type=False))
				likes = plus_likes - minus_likes
				return HttpResponse(json.dumps({'code':201,'message':'Like removed','uuid':uuid,'likes':likes}), mimetype='application/json')
			else:
				return HttpResponse(json.dumps({'code':400,'message':'Like already exist','uuid':uuid}), mimetype='application/json')
		except Like.DoesNotExist:
			like = Like(video=video,user=user,type=False)
			like.save()
			plus_likes = len(Like.objects.filter(video=video,type=True))
			minus_likes = len(Like.objects.filter(video=video,type=False))
			likes = plus_likes - minus_likes
			return HttpResponse(json.dumps({'code':200,'message':'Like registred','uuid':uuid,'likes':likes}), mimetype='application/json')
