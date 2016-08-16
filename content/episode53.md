Title: Episode 53 - StackStorm2 with Tomaž Muraus and Patrick Hoolboom
Date: 2016-04-16
Category: Episodes
Tags: Automation, DevOps
url: stackstorm.html
save_as: stackstorm.html

### Summary
If you are responsible for managing any amount of servers, then you know that automation is critical for maintaining your sanity. This week we spoke with Tomaž Muraus and Patrick Hoolboom about their work on StackStorm, which is a platform for tracking and reacting to events in your infrastructure. By allowing you to register actions with event triggers it frees you from having to worry about a whole class of concerns so that you can focus on building new capabilities rather than babysitting what you already have.

<iframe id="audio_iframe" src="https://www.podbean.com/media/player/w78w9-5e778e?from=yiiadmin&skin=103&postId=6190990&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- Subscribe on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Stitcher](http://www.stitcher.com/s?fid=64838&refid=stpr), [TuneIn](http://tunein.com/embed/follow/p726240/#) or [RSS](http://podcastinit.podbean.com/feed/)
- Follow us on [Twitter](https://twitter.com/Podcast__init__) or [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Give us feedback! Leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Tweet](https://twitter.com/Podcast__init__) to us, send us an [email](mailto:hosts@podcastinit.com) or leave us a message on [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) for your opportunity to find out about upcoming guests, suggest questions, and propose show ideas.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)
- Linode is sponsoring us this week. Check them out at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $20 credit to try out their fast and reliable Linux virtual servers for your next project
- I would also like to thank Hired, a job marketplace for developers and designers, for sponsoring this episode of Podcast.\_\_init\_\_. Use the link [hired.com/podcastinit](http://hired.com/podcastinit) to double your signing bonus.
- ODSC East in Boston is happening on May 21st - 22nd. Use the discount code EP for 20% off when you [register](https://odsceast.eventbrite.com/?discount=EP)
- Your hosts as usual are Tobias Macey and Chris Patti
- Today we are interviewing Tomaž Muraus and Patrick Hoolboom about the StackStorm project, which is an event-driven system automation framework.

<div class="well">
<a href="http://linode.com/podcastinit"><img src="/images/linode-banner-sponsor-large.png" alt="Linode Sponsor Banner"style="width: 100%;"></img></a><br/>
<p>Use the promo code <strong>podcastinit20</strong> to get a $20 credit when you sign up!</p>
</div>

### Interview
- Introductions
- How did you get introduced to Python? - Chris
- What is StackStorm and what problems does it solve? - Tobias
- What was your inspiration for creating StackStorm and what were some of the biggest architectural and design challenges? - Tobias
- What made you choose Python for StackStorm's implementation rather than another language like Go? - Chris
- Can you describe the architecture of StackStorm and what the setup looks like? - Tobias
- Other than chat driven events, what types of event sources does StackStorm support, and what use cases do those alternate event streams enable? - Chris
- The home page describes StackStorm as being an event-driven framework for automating the users infrastructure. What kinds of capabilities are made possible by this and do you think that it simplifies or complicates the work of operations engineers? - Tobias
- Is there a minimum or maximum size of infrastructure for which it would make sense to use StackStorm? - Tobias
- It looks like StackStorm is made up of a number of discrete components. What do the components use to communicate, and how did those choices influence the design of StackStorm's overall architecture? - Chris
- I use SaltStack in my work which is a tool that also focuses on event-driven architecture. Can you compare and contrast the capabilities and focus of StackStorm with the features of SaltStack? Would it make sense to use both frameworks in the same infrastructure? - Tobias
- One of the advertised features of StackStorm is a strong focus on ChatOps. Can you explain that concept for people who might not be familiar with it and describe why it is such a useful paradigm? - Tobias
- Extensibility is a critical capability for an operations platform due to the wide variety of environments that people are inclined to build. In StackStorm the unit of extensibility is a pack. Can you describe what a pack is and how you arrived at that abstraction? - Tobias
    - Have you encountered any situations in which the concept of a pack has been the wrong abstraction and made something more difficult than it may have been otherwise? - Tobias
- In very large scale environments like Netflix, how would one build a StackStorm cluster to handle the immense load. More specifically, how does one determine what kinds of machine resources each component needs? - Chris
- Management of credentials is always a difficult problem in operations. Does StackStorm attempt to tackle that issue or does it defer that responsibility to other systems, such as the user's configuration management platform? - Tobias
- Does StackStorm interface with Kibana, Splunk or other log / metric aggregation packages? - Chris
- What are some of the most surprising uses that you have heard of from people using the platform? - Tobias

### Keep In Touch
- Tomaž
    - [Twitter](https://twitter.com/kamislo)
    - [website/blog](https://www.tomaz.me/)
- Patrick
    - [Twitter](https://twitter.com/doriftoshoes)

### Picks
- Tobias
    - [SAWS](https://github.com/donnemartin/saws)
    - [Bill Peet](http://amzn.to/1qOoz4B)
- Chris
    - [Grimm Brewing Subliminal Message Sour Red Ale](http://grimmales.com/subliminal/)
    - [Lobste.rs](https://lobste.rs/)
    - [Medium](https://medium.com/)
- Tomaž
    - [Understanding Air France 447](http://amzn.to/1r2WUxt)
    - [Aviation Herald](http://avherald.com/)
- Patrick
    - [True Nutrition](http://truenutrition.com)
    - [JP Cycles](http://www.jpcycles.com/)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
