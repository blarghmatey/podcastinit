Title: Episode 70 - Python on Windows with Steve Dower
Date: 2016-08-02
Category: Episodes
Tags: Windows, Microsoft
url: steve-dower-python-on-windows.html
save_as: steve-dower-python-on-windows.html

### Summary
In order for Python to continue to attract new users, we need to have an easy way for people to get started with it, and Windows is still the most widely used operating system among computers. Steve Dower is the build maintainer for the Windows installers of Python and this week we spoke with him about his work in that role. He told us about the changes that he has made to the installer to make it easier for new users to get started and how modern updates to the packaging ecosystem for libraries has simplified dependency management. He also told us about how the Visual Studio team is building a set of tools to make development of Python code more enjoyable and how Microsoft's adoption of open source is making Windows a more attractive platform for developers.

<iframe src="https://www.podbean.com/media/player/g59fd-61c505?from=yiiadmin&skin=103&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable.
- Linode is sponsoring us this week. Check them out at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $20 credit to try out their fast and reliable Linux virtual servers for your next project
- We are also sponsored by Sentry this week. Stop hoping your users will report bugs. Sentry's real-time tracking gives you insight into production deployments and information to reproduce and fix crashes. Check them out at [getsentry.com](https://getsentry.com/welcome/) and use the code *podcastinit* at signup to get a $50 credit on your account!
- Visit our site to subscribe to our show, sign up for our newsletter, read the show notes, and get in touch.
- To help other people find the show you can leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), or [Google Play Music](https://play.google.com/music/m/I7ogju4xv6adasgqz6545jndgsy?t=Podcastinit_-_Python_and_the_people_who_make_it_great), and tell your friends and co-workers
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) for your opportunity to find out about upcoming guests, suggest questions, and propose show ideas.
- Your hosts as usual are Tobias Macey and Chris Patti
- Today we're interviewing Steve Dower about Python on Windows

<div class="well">
<a href="http://linode.com/podcastinit"><img src="/images/linode-banner-sponsor-large.png" alt="Linode Sponsor Banner" style="width: 100%;"></img></a><br/>
<p>Use the promo code <strong>podcastinit20</strong> to get a $20 credit when you sign up!</p>
</div>

<div class="well">
<a href="https://getsentry.com/welcome/?utm_source=podcastinit&utm_medium=podcast&utm_campaign=sponsored&code=podcastinit"><img src="/images/sentry-horizontal-black.png" style="background: white; margin: auto; display: block; padding: 10px; width: 90%;"/></a><br/>
<p>Stop hoping your users will report bugs. Sentry's real-time tracking gives you insight into production deployments and information to reproduce and fix crashes. Use the code <b>podcastinit</b> at <a href="https://www.getsentry.com/signup/?code=podcastinit&utm_source=podcastinit&utm_medium=podcast&utm_campaign=sponsored">signup</a> to get a $50 credit!</p>
</div>

### Interview with Steve Dower
- Introductions
- How did you get introduced to Python? - Chris
- You are currently the release manager for Python on Windows. How did you end up with that responsibility? - Tobias
- While Python has supported Windows for a long time, the overall experience has historically been rather poor. Can you give a bit of the background of why that was and tell us about some of the work that you and others have been doing to make it better? - Tobias
- Given that a large percentage of users are still on Windows, having a good story for getting started with Python on that platform is important for adoption of the language. What are some of the areas where the current situation needs to be improved? - Tobias
- What is the most difficult part of building a distribution of Python for a Windows environment? Has it gotten easier in recent years? - Tobias
- When we were speaking at PyCon you mentioned that the most frequently downloaded version of Python from the [python.org](https://www.python.org/downloads/) site is the 32 bit version for Windows. Do you think that is an accurate and useful metric? What other statistics do you wish you could capture or improve? - Tobias
- How does Python Tools for Visual Studio compare with other Python IDEs like Pycharm? - Chris
- What are some unique features that Python Tools for Visual Studio offers that other tools don't? - Chris
- Are there any compelling aspects of developing Python on Windows that could convince users on other platforms to make the switch? - Tobias
- Could you give our listeners a whirlwind tour of the underlying implementation of PTVS? How does Visual Studio provide such in depth introspection for your Python code? - Chris

### Keep In Touch
- [Twitter](https://twitter.com/zooba)
- Github
  - [Microsoft](https://github.com/microsoft)
  - [Azure](https://github.com/azure)
- steve.dower

### Picks
- Tobias
    - [Kdiff3](http://kdiff3.sourceforge.net/)
    - [SpyderCo Triangle Sharpmaker](http://amzn.to/2aPpGcm)
- Chris
    - [Audible](http://www.audible.com/)
- Steve
    - [Sandisk Extreme Portable SSD](http://amzn.to/2bdtjgf)
    - [SMBC](http://smbc-comics.com)
    - [Random Encounters](https://youtube.com/randomencountersent)

### Links
- Windows compilers
    - [Visual C++ Build Tools](http://landinghub.visualstudio.com/visual-cpp-build-tools) (for Python 3.5 and later)
    - [Visual C++ Compiler for Python 2.7](http://aka.ms/vcpython27)
- [PEP 514](https://www.python.org/dev/peps/pep-0514/)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
