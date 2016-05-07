Title: Episode 55 - Apache LibCloud with Anthony Shaw
Date: 2016-04-30
Category: Episodes
Tags: Cloud, Automation, DevOps
url: apache-libcloud.html
save_as: apache-libcloud.html

### Summary
More and more of our applications are running in the cloud and there are increasingly more providers to choose from. The LibCloud project is a Python library to help us manage the complexity of our environments from a uniform and pleasant API. In this episode Anthony Shaw joins us to explain how LibCloud works, the community that builds and supports it, and the myriad ways in which it can be used. We also got a peek at some of the plans for the future of the project.

<iframe src="https://www.podbean.com/media/player/k68uq-5ee871?from=yiiadmin&skin=103&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- Subscribe on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Stitcher](http://www.stitcher.com/s?fid=64838&refid=stpr), [TuneIn](http://tunein.com/embed/follow/p726240/#) or [RSS](http://podcastinit.podbean.com/feed/)
- Follow us on [Twitter](https://twitter.com/Podcast__init__) or [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Give us feedback! Leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Tweet](https://twitter.com/Podcast__init__) to us, send us an [email](mailto:hosts@podcastinit.com) or leave us a message on [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) for your opportunity to find out about upcoming guests, suggest questions, and propose show ideas.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)nnn
- Linode is sponsoring us this week. Check them out at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $20 credit to try out their fast and reliable Linux virtual servers for your next project
- The Open Data Science Conference in Boston is happening on May 21st and 22nd. If you use the code EP during registration you will save 20% off of the ticket price. If you decide to attend then let us know, we'll see you there!
- Your hosts as usual are Tobias Macey and Chris Patti
- Today we are interviewing Anthony Shaw about the Apache LibCloud project

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

### Interview with Anthony Shaw
- Introductions
- How did you get introduced to Python? - Chris
- What is LibCloud and how did it get started? - Tobias
- How much overhead does using libcloud impose versus native SDKs for performance sensitive APIs like block storage? - Chris
- What are some of the design patterns and abstractions in the library that allow for supporting such a large number of cloud providers with a mostly uniform API? - Tobias
- Given that there are such differing services provided by the different cloud platforms, do you face any difficulties in exposing those capabilities? - Tobias
- How does LibCloud compare to similar projects such as the Fog gem in Ruby? - Tobias
- What inspired the choice of Python as the language for creating the LibCloud project? Would you make the same choice again? - Tobias
- Which versions of Python are supported and what challenges has that created? - Tobias
- What is your opinion on the state of PyPI as a package maintainer? What statistics are most useful to you and what else do you wish you could track? - Tobias
- Could you walk our listeners through the under the cover process details of instantiating a computer instance in say, Azure using libcloud? - Chris
- Does LibCloud have any native support for parallelization, such as for the purpose of launching a large number of compute instances simultaneously? - Tobias
- What does it mean to be an Apache project and what benefits does it provide? - Tobias
- What are some of the most notable projects that leverage LibCloud for interacting with platform and infrastructure service providers? - Tobias
- Could you describe how libcloud could be extended to abstract away a new type of service that's not yet supported - e.g. a database? - Chris
- Would you suggest that libcloud users extend libcloud to cover 'native' services they might use like AWS Lambda, or should they mix libcloud and 'native' SDKs in cases like this? - Chris
- Could you talk a little bit about the cloud oriented network services that libcloud supports? Is it possible to create AWS VPCs, subnets, etc using libcloud? - Chris
- Do you know if people use LibCloud for abstracting the APIs of a single cloud provider, even if they don't have any intention of using a different platform? - Tobias
- Do you think that people are more likely to use LibCloud for bridging across muliple public cloud platforms, or is it more commonly used in a hybrid cloud type of environment? - Tobias
- What is on the roadmap for LibCloud that people should keep an eye out for? - Tobias

### Keep In Touch
- [Twitter](https://twitter.com/anthonypjshaw)
- [GitHub](https://github.com/tonybalogne)
- [GitHub](https://github.com/apache/libcloud)

### Picks
- Tobias
    - [Blue Yeti Microphone](http://amzn.to/26FAxhK)
    - [Diablo Swing Orchestra](http://www.diabloswing.com/)
- Chris
    - [Rosewill RK Keycaps](http://amzn.to/1pTPHhy)
    - [Enki](https://www.enki.com/)
    - [Catch 22](http://amzn.to/1pTPKKr)
- Anthony
    - [Hidden Brain Podcast](http://www.npr.org/podcasts/510308/hidden-brain)
    - [PyKwalify](http://pykwalify.readthedocs.org/en/unstable/)
    - Doing Nothing

### Links
- [Dimension Data](http://www.dimensiondata.com/en-US/Pages/NewHomePage1.aspx)
- [Austin Bingham and Robert Smallshire Pluralsight Python Training](https://www.pluralsight.com/courses/python-fundamentals)
- [CloudKick](https://www.rackspace.com/cloud/monitoring)
- [PyPI Ranking website](http://pypi-ranking.info/alltime)
- [Apache JClouds](https://jclouds.apache.org/)
- [SaltStack](https://www.saltstack.com)
- [Scalr](http://www.scalr.com/)
- [Apache Software Foundation](http://www.apache.org/)
- [Mist.io](https://mist.io/)
- [StackStorm](https://stackstorm.com/)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
