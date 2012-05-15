#!/usr/bin/env python
# -*- coding: utf-8 -*-

SETTINGS = {
    'APP_NAME': 'google-contacts',
    'CLIENT_ID':'Your client ID',
    'CLIENT_SECRET':'Your client secret',
    'SCOPES':['https://www.google.com/m8/feeds/',
              'https://docs.google.com/feeds/',
              'https://www.google.com/calendar/feeds/'],
    'USER_AGENT':'Appengine',
    'OAUTH2CALLBACK':'http://localhost:8080/oauth2callback'
    }
