Title: Episode 65 - MyPy with David Fisher and Greg Price
Date: 2016-07-09
Category: Episodes
Tags: Type Theory, Static Types
url: david-greg-mypy.html
save_as: david-greg-mypy.html

### Summary
As Python developers we are fond of the dynamic nature of the language. Sometimes, though, it can get a bit _too_ dynamic and that's where having some type information would come in handy. Mypy is a project that aims to add that missing level of detail to function and variable definitions so that you don't have to go hunting 5 levels deep in the stack to understand what shape that data structure is supposed to be. This week we spoke with David Fisher and Greg Price about their work on Mypy and its use within Dropbox and the broader community. They explained how it got started, how it works under the covers, and why you should consider adding it to your projects.

<iframe src="https://www.podbean.com/media/player/rzabg-60d559?from=yiiadmin&skin=103&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)
- Linode is sponsoring us this week. Check them out at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $20 credit to try out their fast and reliable Linux virtual servers for your next project
- We are also sponsored by Sentry this week. Stop hoping your users will report bugs. Sentry's real-time tracking gives you insight into production deployments and information to reproduce and fix crashes. Check them out at [getsentry.com](https://getsentry.com/welcome/)
- Visit our site to subscribe to our show, sign up for our newsletter, read the show notes, and get in touch.
- To help other people find the show you can leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), or [Google Play Music](https://play.google.com/music/m/I7ogju4xv6adasgqz6545jndgsy?t=Podcastinit_-_Python_and_the_people_who_make_it_great), and tell your friends and co-workers
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) for your opportunity to find out about upcoming guests, suggest questions, and propose show ideas.
- Your hosts as usual are Tobias Macey and Chris Patti
- Today we're interviewing David Fisher and Greg Price about Mypy, a library for adding optional static types to your Python code.

<div class="well">
<a href="http://linode.com/podcastinit"><img src="/images/linode-banner-sponsor-large.png" alt="Linode Sponsor Banner" style="width: 100%;"></img></a><br/>
<p>Use the promo code <strong>podcastinit20</strong> to get a $20 credit when you sign up!</p>
</div>

<div class="well">
<a href="https://getsentry.com/welcome/?utm_source=podcastinit&utm_medium=podcast&utm_campaign=sponsored&code=podcastinit"><img src="/images/sentry-horizontal-black.png" style="background: white; margin: auto; display: block; padding: 10px; width: 90%;"/></a><br/>
<p>Stop hoping your users will report bugs. Sentry's real-time tracking gives you insight into production deployments and information to reproduce and fix crashes. Use the code <b>podcastinit</b> at <a href="https://www.getsentry.com/signup/?code=podcastinit&utm_source=podcastinit&utm_medium=podcast&utm_campaign=sponsored">signup</a> to get a $50 credit!</p>
</div>es

### Interview with David Fisher and Greg Price
- Introductions
- How did you get introduced to Python? - Chris
- Can you explain a bit about what Mypy is and its origin story? - Tobias
- What are the benefits of using Mypy for both new and existing projects? - Tobias
- How does the Mypy compilation step work? - Tobias
- What are the biggest technical challenges in implementing Mypy? - Chris
- Are there any limitations imposed by the syntax of Python that prevented you from implementing any features or syntax that you would have liked to include in Mypy? - Tobias
- In Guido's keynote from this year's PyCon he mentioned some tentative plans for adding variable type declarations to the Python syntax in one of the next major releases. How much of that idea was inspired by Mypy? - Tobias
- Type theory is a large and complex problem domain. Can you explain where Mypy falls in this space? - Tobias
- Which language(s) had the biggest influence on the particular syntax and semantics used in Mypy? - Tobias
- What kinds of type definitions and guarantees can be encoded using Mypy? - Tobias
- Can you talk a bit about user defined types as implemented in Mypy? - Chris
- How has the inclusion of the typing module in the Python standard libary influenced the evolution of Mypy? - Tobias
- Did the inclusion of multiple inheritance add any implementation complexity to Mypy? - Chris
- Do you know of any formal studies that have been performed to research the ergonomics or efficiency gains of static or gradual type systems? - Tobias
- What does the future roadmap for Mypy look like? - Tobias

### Keep In Touch
- David
    - [GitHub](https://github.com/ddfisher)
- Greg
    - [web page](http://web.mit.edu/price/)
    - [GitHub](https://github.com/gnprice)

$ pip3 install mypy-lang

Bug reports, feature requests, questions welcome on issue tracker: github.com/python/mypy


### Picks
- Tobias
    - [Functional Geekery - Andreas Stefik](https://www.functionalgeekery.com/episode-55-andreas-stefik/) episode about studies performed on the human factors of development
    - [Soft Skills Engineering Podcast](https://twitter.com/softskillseng)
- Chris
    - [Grimm Artisenal Ales Lucky Cloud](http://grimmales.com/luckycloud/)
    - [jq - json swiss army knife](https://stedolan.github.io/jq/)
- David
    - [fzf - a fuzzy finder](https://github.com/junegunn/fzf)
    - [Thinking, Fast And Slow](http://amzn.to/28YHvYc) by Daniel Kahneman
    - [Ringworld](http://amzn.to/28YHi7c)
- Greg
    - [On Proof and Progress in Mathematics](http://www.ams.org/journals/bull/1994-30-02/S0273-0979-1994-00502-6/S0273-0979-1994-00502-6.pdf), essay by Bill Thurston
    - [Axiomatic](http://amzn.to/28Nr0x9) by Greg Egan

### Links
- GitHub [repo](https://github.com/python/mypy), and [CONTRIBUTING file](https://github.com/python/mypy/blob/master/CONTRIBUTING.md)
- [PEP 484](https://www.python.org/dev/peps/pep-0484/)
- [PyCon 2016 workshop slides](https://dl.dropboxusercontent.com/content_link/CzGrw5JyeBy2m2yGXgYckx25C5F1SISDYueX8f7nXxEuDJO1aCmcNN6kfgHEdzUf/file?dl=1)
- [Typeshed](https://github.com/python/typeshed) shared repo for stubs
- [Other tools (PyCharm, pylint, pytype, ...) using PEP 484 types](https://github.com/python/typing/issues/200)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
