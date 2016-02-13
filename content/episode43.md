Title: Episode 43 - WSGI 2.0
Date: 2016-01-25
Category: Episodes
Tags: WSGI, Web, Standards
url: wsgi-2.html
save_as: wsgi-2.html

### Summary
The Web Server Gateway Interface, or WSGI for short, is a long-standing pillar of the Python ecosystem. It has enabled a vast number of web frameworks to proliferate by not having to worry about how exactly to interact with the HTTP protocol and focus instead on building a library that is robust, extensible, and easy to use. With recent evolutions to how we interact with the web, it appears that WSGI may be in need of an update and that is what our guests on this episode came to discuss. Cory Benfield is leading an effort to determine what if any modifications should be made to the WSGI standard or if it is time to retire it in favor of something new. Andrew Godwin has been hard at work building the Channels framework for Django to allow for interoperability with websockets. They bring their unique perspectives to bear on how and why we may want to consider bringing WSGI into the current state of the web.

<iframe id="audio_iframe" src="http://www.podbean.com/media/player/25wxt-5c6f25?from=yiiadmin&skin=103&postId=6057765&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- Subscribe on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Stitcher](http://www.stitcher.com/s?fid=64838&refid=stpr), [TuneIn](http://tunein.com/embed/follow/p726240/#) or [RSS](http://podcastinit.podbean.com/feed/)
- Follow us on [Twitter](https://twitter.com/Podcast__init__) or [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Give us feedback! Leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Tweet](https://twitter.com/Podcast__init__) to us, send us an [email](mailto:hosts@podcastinit.com) or leave us a message on [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) for your opportunity to find out about upcoming guests, suggest questions, and propose show ideas.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)
- Linode is sponsoring us this week. Check them out at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $20 credit to try out their fast and reliable Linux virtual servers for your next project
- I would also like to thank Hired, a job marketplace for developers, for sponsoring this episode of Podcast.\_\_init\_\_. Use the link [hired.com/podcastinit](http://hired.com/podcastinit) to double your signing bonus.
- Your hosts as usual are Tobias Macey and Chris Patti
- Today we are interviewing Cory Benfield and Andrew Godwin about a proposed update to the WSGI specification.

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

### Interview with Cory Benfield and Andrew Godwin
- Introductions
- How did you get introduced to Python? - Chris
- First off, what is WSGI? - Tobias
- What are some of the ways the current WSGI spec has fallen out of step with the needs of the modern developer? - Chris
- How did you come to be involved with the new WSGI specification? What brought you into this process? - Chris
- Do you think the WSGI name itself brings a lot of expectation, or is it good to keep it as a well-recognised Python landmark? - Tobias
- Would it be better to make a clean break and implement an entirely new set of APIs and style of interaction? - Tobias
- What kind of compatibility guarantees should be made between the current spec and the proposed upgrade? What would the impact be if the new specification was incompatible? - Tobias
- How has the response been to your call for comments? What are some of the most frequently raised concerns or suggestions? - Tobias
- What are some of the proposed changes to the specification? - Tobias
- Are there any future directions you think WSGI should take that perhaps haven't been considered yet? - Chris
- Has your opinion or vision of the proposed update changed as you reviewed responses to the conversation on the mailing list? - Tobias
- Do you have any ideas of how to design the new specification in order to avoid a similar situation of needing to deprecate the current standards in order to accomodate new web protocols? - Tobias
- What are some of the points of contention or rigorous debate that have kept previous WSGI 2 attempts from succeeding? - Chris

### Keep In Touch
- Andrew
    - [Twitter](https://twitter.com/andrewgodwin)
    - [GitHub](https://github.com/andrewgodwin)
- Cory
    - [Twitter](https://twitter.com/lukasaoz)
    - [GitHub](https://github.com/lukasa)

### Picks
- Tobias
    - [Discourse](http://www.discourse.org/)
- Chris
    - [The Expanse](http://www.syfy.com/theexpanse)
    - [Puerto Rico for IOS](https://itunes.apple.com/us/app/puerto-rico-hd/id438437326?mt%3D8)
    - [Dominion for IOS](https://itunes.apple.com/us/app/dominion/id948405722?mt%3D8)
    - [Splendor for IOS](https://itunes.apple.com/us/app/splendor/id971215921?mt%3D8)
- Cory
    - [Wusthof Knives](http://www.wusthof.com/usa/index.jsp)
    - [Australian Football](https://en.wikipedia.org/wiki/Australian_rules_football)
    - [XCOM 2](https://xcom.com/agegate/)
- Andrew
    - [Archery](https://en.wikipedia.org/wiki/Archery)
    - [Tromsø Norway](https://en.wikipedia.org/wiki/Troms%C3%B8)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
