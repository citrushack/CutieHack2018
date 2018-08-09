# CutieHack2018
CutieHack 2018 Website

```
For the front end people: 
the main page html is located here:  CutieHack2018/cutie/landingapp/templates/index.html
and the static files are located here: CutieHack2018/cutie/landingapp/static/

To link stylesheet in html,
{% load static %} <!--tag needed to configure static files like css in django-->
<!--django will look for css/example.css file in the static folder-->
<link rel="stylesheet" href="{% static 'css/example.css' %}">

To link image in html,
{% load static %}
<img src="{% static 'images/example.png' %}" alt="My image" style="width:10px;height:10px;"/>

To link js in html,
{% load static %}
<script type="text/javascript" src="{% static 'js/example.js' %}"></script>
```
