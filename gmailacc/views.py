import logging
import httplib2
from apiclient.discovery import build
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from oauth2client.client import OAuth2WebServerFlow, FlowExchangeError
import atom.data
import gdata.data
import gdata.contacts
import gdata.gauth

"""from django_sample.plus.models import CredentialsModel
from django_sample import settings
from oauth2client import xsrfutil
from oauth2client.django_orm import Storage"""

flow = OAuth2WebServerFlow(
        client_id='273376754588-tsp5umvhcni12of38gr8bd146kb7nkl3.apps.googleusercontent.com',
        client_secret='5MaRcyfMVU8wWl11X7P1s4Rm',
        scope='https://www.google.com/m8/feeds/',
        redirect_uri='http://localhost:8000/gmailacc/auth/google')


def index(request):
    auth_uri = flow.step1_get_authorize_url()
    return HttpResponseRedirect(auth_uri)


def PrintAllContacts(gd_client):
    print("I am here")


def redirectresp(request):
    code = request.GET.get('code', '')
    auth2token = gdata.gauth.OAuth2TokenFromCredentials(flow)
    gd_client = gdata.
    print("lol")
    print(gd_client)
    return HttpResponse(code)