Title: Episode 45 - Cython with Craig Citro and Robert Bradshaw
Date: 2016-02-18
Category: Episodes
Tags: Performance, Compilation
url: cython-developers.html
save_as: cython-developers.html

### Summary
Do you find yourself reaching for a different language when you need some extra speed? With Cython you can get the best of both worlds by writing your code in Python and executing it as compiled code. In this episode we were joined by Craig Citro and Robert Bradshaw from the Cython project to discuss how and when you might want to incorporate it into your applications.

<iframe id="audio_iframe" src="http://www.podbean.com/media/player/n8m48-5ccbbc?from=yiiadmin&skin=103&postId=6081468&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- Subscribe on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Stitcher](http://www.stitcher.com/s?fid=64838&refid=stpr), [TuneIn](http://tunein.com/embed/follow/p726240/#) or [RSS](http://podcastinit.podbean.com/feed/)
- Follow us on [Twitter](https://twitter.com/Podcast__init__) or [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Give us feedback! Leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Tweet](https://twitter.com/Podcast__init__) to us, send us an [email](mailto:hosts@podcastinit.com) or leave us a message on [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) for your opportunity to find out about upcoming guests, suggest questions, and propose show ideas.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)
- Linode is sponsoring us this week. Check them out at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $20 credit to try out their fast and reliable Linux virtual servers for your next project
- I would also like to thank Hired, a job marketplace for developers, for sponsoring this episode of Podcast.\_\_init\_\_. Use the link [hired.com/podcastinit](http://hired.com/podcastinit) to double your signing bonus.
- Your host is Tobias Macey
- Today we are interviewing Craig Citro and Robert Bradshaw

<div class="well">
<a href="https://linode.com/podcastinit/?utm_source=podcastinit&utm_medium=podcast&utm_content=20%20dollar&utm_campaign=podcastinit20"><img src="/images/linode-banner-sponsor-large.png" alt="Linode Sponsor Banner"style="width: 100%;"></img></a><br/>
<p>Use the promo code <strong>podcastinit20</strong> to get a $20 credit when you sign up!</p>
</div>

<div class="well">
<a href="https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit"><img src="/images/hired-logo-dark-padding.png" alt="Hired Logo" style="float: left; width: 20%; margin-right: 20px;"></a>
<p>
On Hired software engineers & designers can get 5+ interview requests in a week and each offer has salary and equity upfront. With full time and contract opportunities available, users can view the offers and accept or reject them before talking to any company. Work with over 2,500 companies from startups to large public companies hailing from 12 major tech hubs in North America and Europe.  Hired is totally free for users and If you get a job you’ll get a $2,000 “thank you” bonus. If you use our <a href="https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit">special link</a> to signup, then that bonus will double to $4,000 when you accept a job. If you’re not looking for a job but know someone who is, you can refer them to Hired and get a $1,337 bonus when they accept a job.
</p>
</div>

### Interview with Craig Citro and Robert Bradshaw
- Introductions
- How did you get introduced to Python? - Chris
- What is Cython and how did the project get started? - Tobias
- My understanding is that Cython can improve the performance of a Python program without even having to provide any type annotations. How does it manage to do that? - Tobias
- Can a Cython module be used as a way to sidestep the GIL? What are some of the pitfalls that can be caused by doing so? - Tobias
- Can you give some examples of how Cython can be used to improve the perfomance of Python programs? - Tobias
- How does Cython work under the covers? - Tobias
- What were some of the challenges during the creation of Cython and what design decisions were made to overcome them? - Tobias
- Does Python's cross platform nature create any unique challenges when compiling down to the C level? - Chris
- What processor and system architectures does Cython support and are there plans to expand that support? - Tobias
- How do generators and list comprehensions map to C, and did those higher level language constructs pose any special challenges in Cython's design? - Chris
- Would Rust ever be a potential compile target for performance and safety optimized modules? - Tobias

### Keep In Touch
- Craig
    - [Twitter](https://twitter.com/craigcitro)
    - [GitHub](https://github.com/craigcitro)
    - [Website](http://www.craigcitro.org/)
- Robert
    - [Email](mailto:robertwb@gmail.com)

### Picks
- Tobias
    - [Certificates, Reputation, and the Blockchain](https://medium.com/mit-media-lab/certificates-reputation-and-the-blockchain-aee03622426f#.ctvv32ymo)
- Craig
    - [Curious Kids Science Book](http://amzn.to/1oNSmtc) by Asia Citro
    - [dplyr](https://github.com/hadley/dplyr)
    - [magrittr](https://github.com/smbache/magrittr)
    - [Everything Is Obvious: How Common Sense Fails Us](http://amzn.to/1PUMYLE) by Duncan Watts
- Robert
    - [Mo Willems](http://www.mowillems.com/)
    - [Philips Hue Lights](http://amzn.to/1Rbenvc)
    - [Sage Math Cloud](http://cloud.sagemath.org/)

### Links
- [Sage](http://www.sagemath.org/) (Math)
- [Pyrex](https://en.wikipedia.org/wiki/Pyrex_\(programming_language\))

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
