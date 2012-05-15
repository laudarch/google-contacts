google-contacts
===============

Appengine Application to keep contacts up to date 


Installation
===========
Rename `config_exemple.py` to `config.py` with your credentials retrieved from [Google API Console].

Rename `app_exemple.yaml` to `app.yaml` with your application name.

Dev Server
----------
    $ python2.5 $PATH/google_appengine/dev_appserver.py $PATH/google-contacts/ --backends --clear_datastore --high_replication

Upload to AppEngine
-------------------
    $ python2.5 $PATH/google_appengine/appcfg.py update $PATH/google-contacts/

[Google API Console]: https://code.google.com/apis/console/