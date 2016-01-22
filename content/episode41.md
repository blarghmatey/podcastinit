Title: Episode 41 - Maciej Fijalkowski on RPython
Date: 2015-12-17
Category: Episodes
Tags: JIT, Interpreters
url: maciej-fijalkowski-rpython.html
save_as: maciej-fijalkowski-rpython.html

### Summary
RPython is a subset of Python that is used for writing high performance interpreters for dynamic languages. The most well-known product of this tooling is the PyPy interpreter. In this episode we had the pleasure of speaking with Maciej Fijalkowski about what RPython is, what it isn't, what kinds of projects it has been used for, and what makes it so interesting.

<iframe id="audio_iframe" src="http://www.podbean.com/media/player/rkszj-5bf87f?from=yiiadmin&skin=103&postId=6027391&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- Subscribe on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Stitcher](http://www.stitcher.com/s?fid=64838&refid=stpr), [TuneIn](http://tunein.com/embed/follow/p726240/#) or [RSS](http://podcastinit.podbean.com/feed/)
- Follow us on [Twitter](https://twitter.com/Podcast__init__) or [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Give us feedback! Leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Tweet](https://twitter.com/Podcast__init__) to us, send us an [email](mailto:hosts@podcastinit.com) or leave us a message on [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) for your opportunity to find out about upcoming guests, suggest questions, and propose show ideas.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)
- Linode is sponsoring us this week. Check them out at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $20 credit to try out their fast and reliable Linux virtual servers for your next project
- I would also like to thank Hired, a job marketplace for developers, for sponsoring this episode of Podcast.\_\_init\_\_. Use the link [hired.com/podcastinit](http://hired.com/podcastinit) to double your signing bonus.
- We are recording today on December 17th, 2015 and your hosts as usual are Tobias Macey and Chris Patti
- Today we are interviewing Maciej Fijalkowski on RPython

<div class="well">
<a href="http://linode.com/podcastinit"><img src="/images/linode-banner-sponsor-large.png" alt="Linode Sponsor Banner"style="width: 100%;"></img></a><br/>
<p>Use the promo code <strong>podcastinit20</strong> to get a $20 credit when you sign up!</p>
</div>

<div class="well">
<a href="https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit"><img src="/images/hired-logo-dark-padding.png" alt="Hired Logo" style="float: left; width: 20%; margin-right: 20px;"></a>
<p>
On Hired software engineers & designers can get 5+ interview requests in a week and each offer has salary and equity upfront. With full time and contract opportunities available, users can view the offers and accept or reject them before talking to any company. Work with over 2,500 companies from startups to large public companies hailing from 12 major tech hubs in North America and Europe.  Hired is totally free for users and If you get a job you’ll get a $2,000 “thank you” bonus. If you use our <a href="https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit">special link</a> to signup, then that bonus will double to $4,000 when you accept a job. If you’re not looking for a job but know someone who is, you can refer them to Hired and get a $1,337 bonus when they accept a job.
</p>
</div>

### Interview with Maciej Fijalkowski
- Introductions
- How did you get introduced to Python? - Chris
- What is RPython and how does it differ from CPython? - Tobias
- Can you share some of the history of RPython in terms of the major improvements and design choices? - Tobias
- In the documentation it says that RPython is able to generate a Just In Time compiler for dynamic languages. Can you explain why that is significant and some of the ways that it does that? - Tobias
- The most well-known use of RPython is the PyPy interpreter for Python. Can you share some of the other languages that have been ported to the RPython runtime and how their performance has been improved or altered in the process? - Tobias
- Are there any languages that have been designed entirely for use with RPython, rather than translating an existing language to run on it? - Tobias
- Do you know of any cases where an application has been written to run directly on RPython? - Tobias
- What are the computer architecture and operating system platforms that RPython supports and do you have any plans to expand that support? - Tobias
- Are there any minimum hardware specifications that are necessary to be able to effectively run a language written against the RPython platform? - Tobias
- Is RPython similar in concept to other efforts like Parrot in the Perl world? - Chris
- Are there any particular areas of the project that you need help with and how can people get involved with the project? - Tobias

### Picks
- Tobias
    - [PyCoders 2015 Recap](http://us4.campaign-archive2.com/?u=9735795484d2e4c204da82a29&id=22fde1c28d&e=b0190ae72d)
    - [Shape Up](http://amzn.to/1TPJNaY)
    - [Xbox One](http://amzn.to/1TPJVY5)
    - [Xbox One Kinect](http://amzn.to/1IYVyLN)
    - [Selfless](http://amzn.to/1IYVBHt)
- Chris
    - [Skunk Bear](http://skunkbear.tumblr.com/)
    - [Category 6](https://en.wikipedia.org/wiki/6_Nimmt!)
    - [Environments](https://en.wikipedia.org/wiki/Environments_(album_series))
- Maciej
    - [PyCon South Africa](https://za.pycon.org/)

### Keep In Touch
- [IRC](https://botbot.me/freenode/pypy/)
- [Mailing List](https://mail.python.org/mailman/listinfo/pypy-dev)
- [PyPy consultancy](http://baroquesoftware.com/)

### Links
- [Psyco](http://psyco.sourceforge.net/) (Python JIT)
- [Truffle](https://bitbucket.org/ssllab/zippy)
- [HippyVM](http://hippyvm.com/)
- [Topaz](https://github.com/topazproject/topaz)
- [Pycket](https://github.com/samth/pycket)
- [Pyxie-lang](http://www.sparkslabs.com/pyxie/)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
