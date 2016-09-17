Title: Episode 74 - Sandstorm.io with Asheesh Laroia
Date: 2016-09-17
Category: Episodes
Tags: User Experience, Security, Consumer Producs
url: asheesh-laroia-sandstorm.html
save_as: asheesh-laroia-sandstorm.html

### Summary
Sandstorm.io is an innovative platform that aims to make self-hosting applications easier and more maintainable for the average individual. This week we spoke with Asheesh Laroia about why running your own services is desirable, how they have made security a first priority, how Sandstorm is architected, and what the installation process looks like.

<iframe src="https://www.podbean.com/media/player/2tfuv-62bb9a?from=yiiadmin&skin=103&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)
- Linode is sponsoring us this week. Check them out at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $20 credit to try out their fast and reliable Linux virtual servers for your next project
- We are also sponsored by Rollbar. Rollbar is a service for tracking and aggregating your application errors so that you can find and fix the bugs in your application before your users notice they exist. Use the link [rollbar.com/podcastinit](https://rollbar.com/podcastinit) to get 90 days and 300,000 errors for free on their bootstrap plan.
- Hired has also returned as a sponsor this week. If you're looking for a job as a developer or designer then Hired will bring the opportunities to you. Sign up at [hired.com/podcastinit](https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit) to double your signing bonus.
- Visit our site to subscribe to our show, sign up for our newsletter, read the show notes, and get in touch.
- To help other people find the show you can leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), or [Google Play Music](https://play.google.com/music/m/I7ogju4xv6adasgqz6545jndgsy?t=Podcastinit_-_Python_and_the_people_who_make_it_great), and tell your friends and co-workers
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) for your opportunity to find out about upcoming guests, suggest questions, and propose show ideas.
- I would also like to mention that the organizers of PyCon Zimbabwe are looking to the global Python community for help in supporting their event. If you would like to donate the [link](https://onepercentclub.com/en/projects/pyzim/plan) will be in the show notes.
- Your hosts as usual are Tobias Macey and Chris Patti
- Today we're interviewing Asheesh Laroia about Sandstorm.io, a project that is trying to make self-hosted applications easy and secure for everyone.

<div class="well">
<a href="http://linode.com/podcastinit"><img src="/images/linode-banner-sponsor-large.png" alt="Linode Sponsor Banner" style="width: 100%;"></img></a><br/>
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

<div class="well">
<a href="https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit"><img src="/images/hired-logo-dark-padding.png" alt="Hired Logo" style="float: left; width: 20%; margin-right: 20px;"></a>
<p>
On Hired software engineers & designers can get 5+ interview requests in a week and each offer has salary and equity upfront. With full time and contract opportunities available, users can view the offers and accept or reject them before talking to any company. Work with over 2,500 companies from startups to large public companies hailing from 12 major tech hubs in North America and Europe.  Hired is totally free for users and If you get a job you’ll get a $2,000 “thank you” bonus. If you use our <a href="https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit">special link</a> to signup, then that bonus will double to $4,000 when you accept a job. If you’re not looking for a job but know someone who is, you can refer them to Hired and get a $1,337 bonus when they accept a job.
</p>
</div>

### Interview with Asheesh Laroia
- Introductions
- How did you get introduced to Python? - Tobias
- Can you start by telling everyone about the Sandstorm project and how you got involved with it? - Tobias
- What are some of the reasons that an individual would want to self-host their own applications rather than using comparable services available through third parties? - Tobias
- How does Sandstorm try to make the experience of hosting these various applications simple and enjoyable for the broadest variety of people? - Tobias
- What does the system architecture for Sandstorm look like? - Tobias
- I notice that Sandstorm requires a very recent Linux kernel version. What motivated that choice and how does it affect adoption? - Chris
- One of the notable aspects of Sandstorm is the security model that it uses. Can you explain the capability-based authorization model and how it enables Sandstorm to ensure privacy for your users? - Tobias
- What are some of the most difficult challenges facing you in terms of software architecture and design? - Tobias
- What is involved in setting up your own server to run Sandstorm and what kinds of resources are required for different use cases? - Tobias
- You have a number of different applications available for users to install. What is involved in making a project compatible with the Sandstorm runtime environment? Are there any limitations in terms of languages or application architecture for people who are targeting your platform? - Tobias
- How much of Sandstorm is written in Python and what other languages does it use? - Tobias

### Keep In Touch
- [Twitter](https://twitter.com/asheeshlaroia)
- [Blog](http://www.asheesh.org/)
- [Email](asheesh@sandstorm.io)

### Picks
- Tobias
    - [OpsGenie](https://www.opsgenie.com)
- Chris
    - [Viking Godfather Safety Razor](http://amzn.to/2cS8V3x)
    - [Who Killed Sherlock Holmes?](http://amzn.to/2cTefGA) by Paul Cornell
    - [Petrus Aged Red](http://petrussourbeer.com/en)
- Asheesh
    - [Amtrak](https://www.amtrak.com/home)
    - [The Master Switch](http://amzn.to/2d97PT7) by Tim Wu
    - [Rocket Chat](https://rocket.chat/)

### Links
- [North Star Post](http://nstarpost.com/)
- [Contact Otter](https://www.contactotter.com/)
- [Hacker Slides](https://github.com/jacksingleton/hacker-slides)
- [Permanote](https://github.com/keybits/permanote)
- [Radicale](http://radicale.org/)
- [Media Goblin](http://mediagoblin.org/)
- [IPython Notebook](http://jupyter.org/)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
