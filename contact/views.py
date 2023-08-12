from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("hello world contact")


def page2(request):
    a = 2343 + 224
    b = 242 + 31
    c = 134 + 12
    d = a + b + c
    return HttpResponse(
        """<html>
<head>
<title>Page Title</title>
</head>
<body>
<h1>This is a Heading"""
        + str(d)
        + """
</h1>
<p>This is a paragraph.</p>

</body>
</html>"""
    )
