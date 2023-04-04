<!DOCTYPE HTML>
<head>  
{% block head %}
{% endblock %}
</head>
<body><a href="{% url 'home' %}"> Take me home</a>
{% block content %}
{% endblock %}
</body>
