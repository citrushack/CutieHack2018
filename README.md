# CutieHack2018
CutieHack 2018 Website

```
For the front end people: 
the main page html is located here:  CutieHack2018/cutie/landingapp/templates/index.html
and the static files are located here: CutieHack2018/cutie/landingapp/static/

To link css in html,
{% load static %}
<link rel="stylesheet" href="{% static 'css/example.css' %}">

To link image in html,
{% load static %}
<img src="{% static 'images/example.png' %}" alt="My image" />

To link js in html,
{% load static %}
<script type="text/javascript" src="{% static 'js/example.js' %}"></script>
```
for c9 users: https://community.c9.io/t/updating-django/15335