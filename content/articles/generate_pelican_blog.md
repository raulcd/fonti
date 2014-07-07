Title: Create Blog using Pelican and deploy in github pages
Date: 2014-07-07 18:30
Tags: pelican, blog, python
Summary: How to create your Pelican Blog and deploy on github pages

This website has been created using pelican. 
[Pelican](http://pelican.readthedocs.org/) is static site 
generator written in Python.

I did a quick research at the beggining in order to select the framework 
to use and after my first thoughts about creating it using 
[Django](https://www.djangoproject.com/) I realized 
that in order to keep things simple with Pelican I had all I needed.

Basically the features I was searching:

* Easy deployment and mantainance
* Write articles using Markdown
* Code syntax highlighting

Pelican is really easy to start with you just need to create your project and 
install pelican:

```console  
pip install pelican
```

If you want to use markdown you will need to install it as a dependency also:

```console
pip install markdown
```

Once you have installed pelican the only thing you need to do is generate the 
skeleton of the blog:

```console 
pelican-quickstart
```
It will prompt several questions about your site. Pelican deploys directly 
fabric script and a Makefile to make even easier your deploy.

Once this is done you will need to start writing your content under the 
content folder. You can add subfolders and this ones will be created as 
categories for your blogs.

I created the articles folder under content and started writing this article.

Once you have your article generated is time to generate your site. There are 
several ways to generate your code:

```console 
pelican content
# Or you can use the generated Makefile
make html
```

The first time I ran the commands I got an Exception because my locale was 
not set:

```python
File ".../lib/python2.7/locale.py", line 443, in _parse_localename
    raise ValueError, 'unknown locale: %s' % localename
ValueError: unknown locale: UTF-8
```

You can set your locale for your user (modifying your .bash_profile) or 
for the session:

```console 
export LC_ALL=en_UK.UTF-8
export LANG=en_UK.UTF-8
```

Once you have generated your content you can run a Development server 
to see the result:

```code
make serve
```

And you will be able to access localhost on the port 8000 by default 
to see the result.

