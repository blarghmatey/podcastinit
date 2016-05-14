Title: Episode 57 - Buildbot with Pierre Tardy
Date: 2016-05-14
Category: Episodes
Tags: DevOps, Automation, Continuous Integration
url: pierre-tardy-buildbot.html
save_as: pierre-tardy-buildbot.html

### Summary
As technology professionals, we need to make sure that the software we write is reliably bug free and the best way to do that is with a continuous integration and continuous deployment pipeline. This week we spoke with Pierre Tardy about Buildbot, which is a Python framework for building and maintaining CI/CD workflows to keep our software projects on track.

<iframe src="https://www.podbean.com/media/player/9fnbx-5f4e11?from=yiiadmin&skin=103&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show, subscribe, join our newsletter, check out the show notes, and get in touch you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)
- Linode is sponsoring us this week. Check them out at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $20 credit to try out their fast and reliable Linux virtual servers for your next project
- We are also sponsored by Rollbar this week. Rollbar is a service for tracking and aggregating your application errors so that you can find and fix the bugs in your application before your users notice they exist. Use the link [rollbar.com/podcastinit](https://rollbar.com/podcastinit) to get 90 days and 300,000 errors for free on their bootstrap plan.
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) for your opportunity to find out about upcoming guests, suggest questions, and propose show ideas.
- Your hosts as usual are Tobias Macey and Chris Patti
- Today we are interviewing Pierre Tardy about the Buildbot continuous integration system.

<div class="well">
<a href="http://linode.com/podcastinit"><img src="/images/linode-banner-sponsor-large.png" alt="Linode Sponsor Banner"style="width: 100%;"></img></a><br/>
<p>Use the promo code <strong>podcastinit20</strong> to get a $20 credit when you sign up!</p>
</div>

<div class="well">
<a href="https://rollbar.com/podcastinit"><img src="/images/rollbar-large-logo.png" alt="Rollbar Logo"/></a><br/>
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

### Interview with Pierre Tardy
- Introductions
- How did you get introduced to Python? - Chris
- For anyone who isn't familiar with it can you explain what Buildbot is? - Tobias
- What was the original inspiration for creating the project? - Tobias
- How did you get involved in the project? - Tobias
- Can you describe the internal architecture of Buildbot and outline how a typical workflow would look? - Tobias
- There are a number of packages out on PyPI for doing subprocess invocation and control, in addition to the functions in the standard library. Which does buildbot use and why? - Chris
- What makes Buildbot stand out from other CI/CD options that are available today? - Tobias
- Scaling a large CI/CD system can become a challenge. What are some of the limiting factors in the Buildbot architecture and in what ways have you seen people work to overcome them? - Tobias
- Are there any design or architecture choices that you would change in the project if you were to start it over? - Tobias
- If you were starting from scratch on implementing buildbot today, would you still use Python? Why? - Chris
- What are some of the most difficult challenges that have been faced in the creation and evolution of the project? - Tobias
- What are some of the most notable uses of Buildbot and how do they uniquely leverage the capabilities of the framework? - Tobias
- What are some of the biggest challenges that people face when beginning to implement Buildbot in their architecture? - Tobias
- Does buildbot support the use of docker or public clouds as a part of the build process? - Chris
- I know that the execution engine for Buildbot is written in Twisted. What benefits does that provide and how has that influenced any efforts for providing Python 3 support? - Tobias
- Does buildbot support build parallelization at all? For instance splitting one very long test run up into 3 instances each running a section of tests to cut build time? - Chris
- What are some of the most requested features for the project and are there any that would be unreasonably difficult to implement due to the current design of the project? - Tobias
- Does buildbot offer a plugin system like Jenkins does, or is there some other approach it uses for custom extensions to the base buildbot functionality? - Chris
- Managing a reliable build pipeline can be operationally challenging. What are some of the thorniest problems for Buildbot in this regard and what are some of the mechanisms that are built in to simplify the operational characteristics? - Tobias
- What were some of the challenges around supporting slaves running on platforms with very different environmental characteristics like Microsoft Windows? - Chris
- What is on the roadmap for Buildbot? - Tobias

### Keep In Touch
- [Buildbot Website](http://buildbot.net)
- [GitHub](https://github.com/buildbot)

### Picks
- Tobias
    - [Viking Safety Razor](http://amzn.to/1p0rjui)
- Chris
    - [Lifeline](http://3mingames.com/2015/04/lifeline/)
    - [Suzaku Sake](http://www.gekkeikan-sake.com/?method=products.productDrilldown&productID=6266EC82-C94E-DFD2-92AB-3DA7B622660C&originalMarketingURL=product/Suzaku)


### Links
- [Crossbar.io](http://crossbar.io/)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
