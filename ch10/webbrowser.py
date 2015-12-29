import webbrowser

methods = [n for n in dir(webbrowser) if not n.startswith('_')]
print methods

webbrowser.open('http://www.python.org')