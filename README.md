# Wiki

This project mainly focuses on designing a simple wiki with [Django](https://en.wikipedia.org/wiki/Django_(web_framework)), [HTML](https://en.wikipedia.org/wiki/HTML) and [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) where you can go and refer different concepts.

This project's source code includes 3 folders and a manage.py file which manages the whole application. Below are the **main files** under those folders.

encyclopedia/:
* urls.py -> stores the urls under this specific application
* util.py -> an assistance for file management with save, get and list functions.
* views.py -> A view function, or view for short, is a Python function that takes a Web request and returns a Web response.([source](https://docs.djangoproject.com/en/3.1/topics/http/views/))
* myMarkdown.py -> this is a utility module which converts a [markdown](https://en.wikipedia.org/wiki/Markdown) text to [HTML](https://en.wikipedia.org/wiki/HTML), this was given as a challenge and I tried my best to make it work. *It only supports headings, boldface text, unordered lists, links, and paragraphs*.
* the static and templates subfolders are for HTML and CSS source files.

entries/:
* contains entry *.md* files

wiki/:
* contains the application configuration files like *settings.py* and *urls.py*.
