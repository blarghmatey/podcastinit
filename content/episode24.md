Title: Episode 24 - Trent Nelson on Pyparallels
Date: 2015-09-07
Category: Episodes
Tags: implementations, concurrency

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- Subscribe on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Stitcher](http://www.stitcher.com/s?fid=64838&refid=stpr), [TuneIn](http://tunein.com/embed/follow/p726240/#) or [RSS](http://podcastinit.podbean.com/feed/)
- Follow us on [Twitter](https://twitter.com/Podcast__init__) or [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Give us feedback! Leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Tweet](https://twitter.com/Podcast__init__) to us, send us an [email](mailto:hosts@podcastinit.com) or leave us a message on [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at <pythonpodcast.com>
- We are recording today on September 7th, 2015 and your hosts as usual are Tobias Macey and Chris Patti
- Today we are interviewing Trent Nelson about PyParallel

### Interview with Trent Nelson
* Introductions
* How did you get introduced to Python? - Chris
* For our listeners who may not be aware, can you give us an overview of what Pyparallel is and what makes it different from other Python implementations? - Chris
* How did PyParallel come about? - Tobias
* What are some of the biggest technical hurdles that you have been faced with during your work on PyParallel? - Tobias
* I understand that PyParallel currently only works on Windows. What was the motivation for that and what would be required for enabling PyParallel to run on a Linux or BSD style operating system? - Tobias
* How does Pyparallel get around the limitations of the global interpreter lock without removing it? - Chris
* Is there any special syntax required to take advantage of the parallelism offered by PyParallel? How does it interact with the threading module in the standard library? - Tobias
* In the abstract for the Pyparallel paper, you cite a simple rule - "Don't persist parallel objects" - how easy is this to do with currently available concurrency paradigms and APIs, and would it make sense to add such support? - Chris
  * For instance, how would one be sure to follow this rule when using Twisted or asyncio? - Chris
* Are there any operations that are not supported in parallel threads? - Tobias
* What drove the decision to fork Python 3.3 as opposed to the 2.X series? - Chris
* In the documentation you mention that the long term goal for PyParallel is to merge it back into Python mainline, possibly within 5 years. Has anything changed with that goal or timeline? What milestones do you need to hit before that becomes a realistic possibility? - Tobias
* Can you compare PyParallel to PyPy-STM and Go with Goroutines in terms of performance and user implementation? - Tobias
* What are some particular problem areas that you are looking for help with? - Tobias
* Assuming that it does get merged in as Python 4, how do you think that would affect the features and experiments that went into Python 5? - Tobias
* To be continued...

### Picks
* Tobias
    * Testinfra
    * Software Engineering Daily
    * Morcheeba
* Chris
* [Hello Webapp - Intermediate Concepts](https://www.kickstarter.com/projects/1868398473/hello-web-app-intermediate-concepts)
* [Grimm Rainbow Dome](http://grimmales.com/rainbowdome/)
* [PBS Idea Channel](https://www.youtube.com/user/pbsideachannel) 
* Trent
    * [Show Stopper](http://amzn.to/1UxJExs) by G. Pascal Zachary

### Keep In Touch
* github.com/pyparallel/pyparallel
* @pyparallel
* @trentnelson


### Links
* PEP XXXX (to be added later)
