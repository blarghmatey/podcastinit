Title: Episode 27 - Trent Nelson on Pyparallels
Date: 2015-09-07
Category: Episodes
Tags: Implementations, Concurrency, Parallelism, The GIL
url: trent-nelson-pyparallel.html
save_as: trent-nelson-pyparallel.html

### Summary
Trent Nelson is a software engineer working with Continuum Analytics and a core contributor to CPython. He started experimenting with a way to sidestep the restrictions of the Global Interpreter Lock without discarding its benefits and that has become the PyParallel project. We had the privilege of discussing the details around this innovative experiment with Trent and learning more about the challenges he has experienced, what motivated him to start the project, and what it can offer to the community.

<iframe id="audio_iframe" src="http://www.podbean.com/media/player/v2rjn-59787d?from=yiiadmin&skin=103&postId=5863549&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- Subscribe on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Stitcher](http://www.stitcher.com/s?fid=64838&refid=stpr), [TuneIn](http://tunein.com/embed/follow/p726240/#) or [RSS](http://podcastinit.podbean.com/feed/)
- Follow us on [Twitter](https://twitter.com/Podcast__init__) or [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Give us feedback! Leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Tweet](https://twitter.com/Podcast__init__) to us, send us an [email](mailto:hosts@podcastinit.com) or leave us a message on [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at <pythonpodcast.com>
- I would also like to thank Hired, a job marketplace for developers, for sponsoring this episode of Podcast.\_\_init\_\_. Use the link [hired.com/podcastinit](https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit) to double your signing bonus.
- We are recording today on September 7th, 2015 and your hosts as usual are Tobias Macey and Chris Patti
- Today we are interviewing Trent Nelson about PyParallel

<div class="well">
<a href="https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit"><img src="/images/hired-logo-dark-padding.png" alt="Hired Logo" style="float: left; width: 20%; margin-right: 20px;"></a>
<p>
On Hired software engineers & designers can get 5+ interview requests in a week and each offer has salary and equity upfront. With full time and contract opportunities available, users can view the offers and accept or reject them before talking to any company. Work with over 2,500 companies from startups to large public companies hailing from 12 major tech hubs in North America and Europe.  Hired is totally free for users and If you get a job you’ll get a $2,000 “thank you” bonus. If you use our <a href="https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit">special link</a> to signup, then that bonus will double to $4,000 when you accept a job. If you’re not looking for a job but know someone who is, you can refer them to Hired and get a $1,337 bonus when they accept a job.
</p>
</div>

### Interview with Trent Nelson
- Introductions
- How did you get introduced to Python?
- For our listeners who may not be aware, can you give us an overview of what Pyparallel is and what makes it different from other Python implementations?
- How did PyParallel come about?
- What are some of the biggest technical hurdles that you have been faced with during your work on PyParallel?
- I understand that PyParallel currently only works on Windows. What was the motivation for that and what would be required for enabling PyParallel to run on a Linux or BSD style operating system?
- How does Pyparallel get around the limitations of the global interpreter lock without removing it?
- Is there any special syntax required to take advantage of the parallelism offered by PyParallel? How does it interact with the threading module in the standard library?
- In the abstract for the Pyparallel paper, you cite a simple rule - "Don't persist parallel objects" - how easy is this to do with currently available concurrency paradigms and APIs, and would it make sense to add such support?
  - For instance, how would one be sure to follow this rule when using Twisted or asyncio?
- Are there any operations that are not supported in parallel threads?
- What drove the decision to fork Python 3.3 as opposed to the 2.X series?
- In the documentation you mention that the long term goal for PyParallel is to merge it back into Python mainline, possibly within 5 years. Has anything changed with that goal or timeline? What milestones do you need to hit before that becomes a realistic possibility?
- Can you compare PyParallel to PyPy-STM and Go with Goroutines in terms of performance and user implementation?
- What are some particular problem areas that you are looking for help with?
- Assuming that it does get merged in as Python 4, how do you think that would affect the features and experiments that went into Python 5?
- To be continued...

### Picks
- Tobias
  - [Testinfra](http://testinfra.readthedocs.org/en/latest/)
  - [Software Engineering Daily](http://softwareengineeringdaily.com/)
- Chris
  - [Hello Webapp - Intermediate Concepts](https://www.kickstarter.com/projects/1868398473/hello-web-app-intermediate-concepts)
  - [Grimm Rainbow Dome](http://grimmales.com/rainbowdome/)
  - [PBS Idea Channel](https://www.youtube.com/user/pbsideachannel) 
- Trent
  - [Show Stopper](http://amzn.to/1UxJExs) by G. Pascal Zachary

### Keep In Touch
- [GitHub](https://github.com/pyparallel/pyparallel)
- Twitter
  - [@PyParallel](https://twitter.com/pyparallel)
  - [@TrentNelson](https://twitter.com/trentnelson)
