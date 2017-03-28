from django.http import HttpResponse

home_html = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Yet Another Blog</title>
  </head>
  <body>
    <p>Hello, world!</p>
  </body>
</html>
'''


def home(request):
    return HttpResponse(home_html)
