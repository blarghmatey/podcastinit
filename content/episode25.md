Title: Episode 25 - uWSGI Core Developers
Date: 2015-09-22
Category: Episodes
Tags: Servers, Microservices, Deployment
url: uwsgi-developers.html
save_as: uwsgi-developers.html

### Summary
uWSGI is one of the most versatile application servers available. It was originally written for running Python applications and has since gained functionality to support Perl, Ruby, PHP, and more in addition to the incredible feature set. In this episode Tobias got to interview three of the core developers of this project and find out more about how the different pieces of it fit together and what its future holds.

<iframe id="audio_iframe" src="http://www.podbean.com/media/player/8gaby-593157?from=yiiadmin&skin=103&postId=5845335&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- Subscribe on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Stitcher](http://www.stitcher.com/s?fid=64838&refid=stpr), [TuneIn](http://tunein.com/embed/follow/p726240/#) or [RSS](http://podcastinit.podbean.com/feed/)
- Follow us on [Twitter](https://twitter.com/Podcast__init__) or [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Give us feedback! Leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Tweet](https://twitter.com/Podcast__init__) to us, send us an [email](mailto:hosts@podcastinit.com) or leave us a message on [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)
- I would also like to thank Hired, a job marketplace for developers, for sponsoring this episode of Podcast.\_\_init\_\_. Sign up at hired.com/podcastinit to double your signing bonus.
- We are recording today on September 22nd, 2015 and your hosts as usual are Tobias Macey and Chris Patti
- Today we are interviewing the core developers of uWSGI (Adriano Di Luzio, Riccardo Magliocchetti, and Roberto De Ioris)

### Interview with uWSGI core developers
- Introductions
- How did you get introduced to Python?
- For anyone who hasn't come across the project before, can you explain what uWSGI is and what makes it unique?
- How did you architect uWSGI in order to allow for supporting so many different languages?
- The feature set of uWSGI is truly incredible. Does this make the code complicated to understand and modify?
- Can you describe some of your favorite features in uWSGI?
- What have you found to be the most overlooked or underutilized features of uWSGI?
- Can you briefly describe how Emperor mode works and how that can be used to handle routing between microservices?
- Could you discuss some of the particular features UWSGI provides around load balancing?
    - Is connection draining supported?
    - Can nodes be dynamically added and removed from the pool or does the config need to be rewritten and UWSGI restarted?
- The configuration syntax looks like it provides a very rich set of capabilities. Is it based on a general purpose programming language or is it a DSL?
- What might be some common use cases for using UWSGI in tandem with another web server like NGINX?
- I have read that WSGI does not get along with http/2. Are there any plans to look towards supporting that protocol in some way?
- What new capabilities can we look forward to in the future of uWSGI?

### Picks
- Tobias
    - [Manjaro Linux](https://manjaro.github.io/)
    - [Kontact](https://www.kde.org/applications/office/kontact/)
    - [Blackhat](http://amzn.to/1Fs2pvl)
- Riccardo
    - [Building Microservices book](http://www.jdoqocy.com/p1115tenkem19A729B71334823BA13652977A99222?url=http%3A%2F%2Fshop.oreilly.com%2Fproduct%2F0636920033158.do%3Fcmp%3Daf-prog-books-videos-product_cj_9781491950357_%2525zp&cjsku=0636920033158)
    - [Django-Denis](https://github.com/xrmx/django-denis)
- Adriano
    - [Paxos Algorithm](http://research.microsoft.com/en-us/um/people/lamport/pubs/lamport-paxos.pdf)
- Roberto
    - [The Brink](https://en.wikipedia.org/wiki/The_Brink)

### Keep In Touch
- [Mailing List](http://lists.unbit.it/cgi-bin/mailman/listinfo/uwsgi)
- #uWSGI on IRC
- [GitHub](https://github.com/unbit/uwsgi)
- [latest docs](http://uwsgi-docs.readthedocs.org/en/latest/)
- Roberto
    - [Twitter](https://twitter.com/unbit)
    - [GitHub](https://github.com/unbit/)
- Adriano
    - [GitHub](https://github.com/aldur/)
    - [Twitter](https://twitter.com/AdrianoDiLuzio)
- Riccardo
    - [GitHub](https://github.com/xrmx)
    - [Twitter](https://twitter.com/rmistaken)
