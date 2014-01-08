DoAnyThing
==========

QUICK START
-----------

	- git clone <see repo url>
	- cd allPowerful
	- ./setup.sh
	- source .ve/bin/activate
	- createdb allPowerful
	- createuser -P -e admin # enter "admin" as password
	- python allPowerful/manage.py syncdb
	- python allPowerful/manage.py migrate
	- To start the server, you must run it from within the allpowerful directory.
		Otherwise the TEMPLATE_DIR will not be found. This is to stay consistent
		with how it'd run within Heroku which puts the app in different directory.

START SERVER
---

	foreman start
	or
	python allpowerful/manage.py runserver


