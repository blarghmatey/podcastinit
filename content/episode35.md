Title: Episode 35 - Sylvain Thénault on ASTroid
Date: 2015-11-23
Category: Episodes
Tags: AST, syntax tree, Language Internals
url: sylvain-thenault-astroid.html
save_as: sylvain-thenault-astroid.html

### Summary
The Python AST (Abstract Syntax Tree) is a powerful abstraction that allows for a number of innovative projects. ASTroid is a library that provides additional convenience methods to simplify working with the AST. In this episode we spoke with Sylvain Thénault from Logilab about his work on ASTroid and how it is used to power the popular PyLint static analysis tool.

<iframe id="audio_iframe" src="https://www.podbean.com/media/player/uy64d-5ae695?from=yiiadmin&skin=103&postId=5957269&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- Subscribe on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Stitcher](http://www.stitcher.com/s?fid=64838&refid=stpr), [TuneIn](http://tunein.com/embed/follow/p726240/#) or [RSS](http://podcastinit.podbean.com/feed/)
- Follow us on [Twitter](https://twitter.com/Podcast__init__) or [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Give us feedback! Leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Tweet](https://twitter.com/Podcast__init__) to us, send us an [email](mailto:hosts@podcastinit.com) or leave us a message on [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)
- I would also like to thank Hired, a job marketplace for developers, for sponsoring this episode of Podcast.\_\_init\_\_. Use the link [hired.com/podcastinit](http://hired.com/podcastinit) to double your signing bonus.
- Linode is sponsoring us this week. Check them out at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $10 credit to try out their fast and reliable Linux virtual servers for your next project
- We are recording today on November 23rd, 2015 and your hosts as usual are Tobias Macey and Chris Patti
- Today we are interviewing Sylvain Thénault about ASTroid

<div class="well">
<a href="https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit"><img src="/images/hired-logo-dark-padding.png" alt="Hired Logo" style="float: left; width: 20%; margin-right: 20px;"></a>
<p>
On Hired software engineers & designers can get 5+ interview requests in a week and each offer has salary and equity upfront. With full time and contract opportunities available, users can view the offers and accept or reject them before talking to any company. Work with over 2,500 companies from startups to large public companies hailing from 12 major tech hubs in North America and Europe.  Hired is totally free for users and If you get a job you’ll get a $2,000 “thank you” bonus. If you use our <a href="https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit">special link</a> to signup, then that bonus will double to $4,000 when you accept a job. If you’re not looking for a job but know someone who is, you can refer them to Hired and get a $1,337 bonus when they accept a job.
</p>
</div>

<div class="well">
<a href="http://linode.com/podcastinit"><img src="/images/linode-banner-sponsor-large.png" alt="Linode Sponsor Banner"style="width: 100%;"></img></a><br/>
<p>Use the promo code <strong>podcastinit10</strong> to get a $10 credit when you sign up!</p>
</div>

### Interview with Sylvain Thénault
- Introductions
- How did you get introduced to Python? - Chris
- Can you explain what an Abstract Syntax Tree is and why it is a useful language feature? - Tobias
- What was your inspiration for creating ASTroid? - Chris
- What features does ASTroid offer over Python's standard AST package, and what makes those features important? - Chris
- I know that the ASTroid package is used in Pylint which is also maintained by Logilab. How does the AST facilitate static analysis of Python projects and are there cases where you have to fall back to text parsing? - Tobias
- Beyond static analysis, what are some of the other possible uses for the Python AST? - Tobias
- The documentation for the AST package in Python mentions that the specific syntax objects in the tree are subject to change between releases. Does the ASTroid package provide any abstractions to maintain a consistent API between versions or does it just provide a pass-through? - Tobias
- Have you encountered any challenges in testing ASTroid given that it operates at such a low level in the language? - Chris
- Do you have trouble attracting contributors given the great understanding of Python's inner working required? - Chris
- Does the implementation or representation of the AST differ between different distributions of Python such as CPython, PyPy and Jython? - Tobias
- What are some of the most interesting applications ASTroid has been used in? - Chris

### Picks
- Tobias
    - [Pre-Commit](http://pre-commit.com)
    - [Existential Comics](http://existentialcomics.com)
    - [htmlPy](http://amol-mandhane.github.io/htmlPy/)
- Chris
    - [Pretty Things - Fluffy White Rabbits](http://www.prettythingsbeertoday.com/wp/our-beers/fluffy-white-rabbits/)
    - [Fallout 4](https://www.fallout4.com)
- Sylvain
    - [PyReverse](https://www.logilab.org/blogentry/6883)
    - [CubicWeb](https://www.cubicweb.org/)

### Keep In Touch
- [Code Quality Mailing List](https://mail.python.org/mailman/listinfo/code-quality)
- [PyLint Dev Mailing List](https://lists.logilab.org/mailman/listinfo/pylint-dev)
- Twitter
    - [@sythenault](https://twitter.com/sythenault)
    - [@logilab](https://twitter.com/logilab)
- [Logilab](http://logilab.fr)

### Links
- [Visitor pattern](https://en.wikipedia.org/wiki/Visitor_pattern)
- [Pylint](http://www.pylint.org/)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
