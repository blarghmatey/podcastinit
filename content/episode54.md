Title: Episode 54 - Pip and the Python Packaging Authority with Donald Stufft
Date: 2016-04-22
Category: Episodes
Tags: Packaging, Community
url: donald-stufft-pip.html
save_as: donald-stufft-pip.html

### Summary
As Python developers we have all used pip to install the different libraries and projects that we need for our work, but have you ever wondered about who works on pip and how the package archive we all know and love is maintained? In this episode we interviewed Donald Stufft who is the primary maintainer of pip and the Python Package Index about how he got involved with the projects, what kind of work is involved, and what is on the roadmap. Give it a listen and then give him a big thank you for all of his hard work!

<iframe id="audio_iframe" src="https://www.podbean.com/media/player/bejq7-5eafc4?from=yiiadmin&skin=103&postId=6205380&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- Subscribe on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Stitcher](http://www.stitcher.com/s?fid=64838&refid=stpr), [TuneIn](http://tunein.com/embed/follow/p726240/#) or [RSS](http://podcastinit.podbean.com/feed/)
- Google Play Music just launched support for podcasts, so now you can check us out there and [subscribe to the show](https://play.google.com/music/m/I7ogju4xv6adasgqz6545jndgsy?t=Podcastinit_-_Python_and_the_people_who_make_it_great).
- Follow us on [Twitter](https://twitter.com/Podcast__init__) or [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Give us feedback! Leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Tweet](https://twitter.com/Podcast__init__) to us, send us an [email](mailto:hosts@podcastinit.com) or leave us a message on [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) for your opportunity to find out about upcoming guests, suggest questions, and propose show ideas.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)
- Linode is sponsoring us this week. Check them out at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $20 credit to try out their fast and reliable Linux virtual servers for your next project
- We also have a new sponsor this week. Rollbar is a service for tracking and aggregating your application errors so that you can fix the bugs in your application before your users notice they exist. Use the link [rollbar.com/podcatinit](https://rollbar.com/podcastinit) to get 90 days and 300,000 errors for free on their bootstrap plan.
- The Open Data Science Conference in Boston is happening on May 21st and 22nd. If you use the code EP during registration you will save 20% off of the ticket price. If you decide to attend then let us know, we'll see you there!
- Your hosts as usual are Tobias Macey and Chris Patti
- Today we are interviewing Donald Stufft about Pip and the Python Packaging Authority

<div class="well">
<a href="https://rollbar.com/podcastinit"><img src="/images/rollbar-large-logo.png" alt="Rollbar Logo" /></a><br/>
<p>I’m excited to tell you about a new sponsor of the show, Rollbar.</p>

<p>
One of the frustrating things about being a developer, is dealing with errors… <i>(sigh)</i>

<ul>
<li>Relying on users to report errors</li>
<li>Digging thru log files trying to debug issues</li>
<li>A million alerts flooding your inbox ruining your day...</li>
</ul>

With Rollbar’s full-stack error monitoring, you get the context, insights and control you need to find and fix bugs faster. It's easy to get started tracking the errors and exceptions in your stack.
You can start tracking production errors and deployments in 8 minutes - or less, and Rollbar works with all major languages and frameworks, including Ruby, Python, Javascript, PHP, Node, iOS, Android and more.
You can integrate Rollbar into your existing workflow such as sending error alerts to Slack or Hipchat, or automatically create new issues in Github, JIRA, Pivotal Tracker etc.
</p>
<p>
We have a special offer for Podcast.__init__ listeners. Go to <a href="https://rollbar.com/podcastinit">rollbar.com/podcastinit</a>, signup, and get the Bootstrap Plan free for 90 days. That's 300,000 errors tracked for free.
Loved by developers at awesome companies like Heroku, Twilio, Kayak, Instacart, Zendesk, Twitch and more. Help support Podcast.__init__ and give Rollbar a try a today. Go to <a href="https://rollbar.com/podcastinit">rollbar.com/podcastinit</a>
</p>
</div>

<div class="well">
<a href="http://linode.com/podcastinit"><img src="/images/linode-banner-sponsor-large.png" alt="Linode Sponsor Banner"style="width: 100%;"></img></a><br/>
<p>Use the promo code <strong>podcastinit20</strong> to get a $20 credit when you sign up!</p>
</div>

### Interview with Donald Stufft
- Introductions
- How did you get introduced to Python? - Chris
- How did you get involved with the Pip project? - Tobias
- What is the Python Packaging Authority and what does it do? - Tobias
- How is PyPi / the Python Packaging Authority funded? - Chris
- What is your opinion on the current state of Python packaging? Are there lessons from other languages and package managers that you think should be adopted by Python? - Tobias
- What was involved in getting pip into the standard Python distribution? Was there any controversy around this? - Chris
- Can you describe some of the mechanics of Pip and how it differs from the other packaging systems that Python has used in the past? - Tobias
- Does pip interact at all with virtualenv, pyenv and the like? - Chris
- The newest package format for Python is the wheel system. Can you describe what that is and what its benefits are? - Tobias
- What are the biggest challenges that you have encountered while working on Pip? - Tobias
- What does the infrastructure for the Python Package Index look like? - Tobias
- What have been some of the challenges around scaling Pypi's infrastructure to meet demand? - Chris
- You're currently working on a replacement for the PyPI site with the Warehouse project. Can you explain your motivation for that and how it improves on the current system? - Tobias
- Where do you see the future of dependency management in Python headed? - Chris
- A few days ago there was a big story about how an NPM library was removed from the index, breaking a large number of dependent projects and applications. Do you think that anything like that could happen in the Python ecosystem? - Tobias
- What's on the roadmap for Pip? - Tobias

### Keep In Touch
- [GitHub](https://github.com/pypa)
- [DistUtils Special Interest Group]()
- [Email](donald@stufft.io)
- [Twitter](@dstufft)
- [IRC](dstufft)

### Picks
- Tobias
    - [Xiki](http://xiki.org/)
- Chris
    - [Agar.io](http://agar.io/)
    - [Culprate](https://culprate.bandcamp.com/)
    - [TCP/IP Illustrated Volume I: The Protocols](http://www.kohala.com/start/tcpipiv1.html)
- Donald
    - [Linux on Windows 10](http://www.hanselman.com/blog/DevelopersCanRunBashShellAndUsermodeUbuntuLinuxBinariesOnWindows10.aspx)

### Links
- Bandersnatch
- Wheel
- Warehouse pypa/warehouse
- [PyPI Sponsors](https://warehouse.python.org)56
- [DevPI]()

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
