Title: Episode 74 - Python and Open Source at Zalando
Date: 2016-09-10
Category: Episodes
Tags: Open Source, Business
url: python-at-zalando.html
save_as: python-at-zalando.html

### Summary
Open source has proven its value in many ways over the years. In many companies that value is purely in terms of consuming available projects and platforms. In this episode Zalando describes their recent move to creating and releasing a number of their internal projects as open source and how that has benefited their business. We also discussed how they are leveraging Python and a couple of the libraries that they have published.

<iframe src="https://www.podbean.com/media/player/9gcuy-6289bd?from=yiiadmin&skin=103&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)
- Linode is sponsoring us this week. Check them out at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $20 credit to try out their fast and reliable Linux virtual servers for your next project
- Rollbar is also sponsoring us this week. Rollbar is a service for tracking and aggregating your application errors so that you can find and fix the bugs in your application before your users notice they exist. Use the link [rollbar.com/podcastinit](https://rollbar.com/podcastinit) to get 90 days and 300,000 errors for free on their bootstrap plan.
- Hired has also returned as a sponsor this week. If you're looking for a job as a developer or designer then Hired will bring the opportunities to you. Sign up at [hired.com/podcastinit](https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit) to double your signing bonus.
- Visit our site to subscribe to our show, sign up for our newsletter, read the show notes, and get in touch.
- To help other people find the show you can leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), or [Google Play Music](https://play.google.com/music/m/I7ogju4xv6adasgqz6545jndgsy?t=Podcastinit_-_Python_and_the_people_who_make_it_great), and tell your friends and co-workers
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) for your opportunity to find out about upcoming guests, suggest questions, and propose show ideas.
- Your hosts as usual are Tobias Macey and Chris Patti
- Today we're interviewing Jie Bao and João Santos about their use of Python at Zalando

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

### Interview with Zalando
- Introductions
- How did you get introduced to Python? - Tobias
- Can you start by telling us a bit about what Zalando does and some of the technologies that you use? - Tobias
- What role does Python play in your environment? - Tobias
- Is the use of Python for a particular project governed by any particular operational guidelines or is it largely a matter of developer choice? - Tobias
- Given that you have such a variety of platforms to support, how do you architect your systems to keep them easy to maintain and reason about? - Tobias
- One of the projects that you have open sourced is Connexion. Can you explain a bit about what that is and what it is used for at Zalando? - Tobias
- What made you choose to standardize on Swagger/OpenAPI vs RAML or some of the other API standards? - Tobias
- Did Connexion start its life as open source or was it extracted from another project? - Tobias
- ExpAn is another one of your projects that is written in Python. What do you use that for? - Tobias
- Can you describe the internal implementation of ExpAn and what it takes to get it set up? - Tobias
- Given the potential complexity of and the need for statistical significance in the data for proper A/B testing, how did you design ExpAn to satisfy those requirements? - Tobias
- Given the laws in Germany around digital privacy, were there any special considerations that needed to be made in the collection strategy for the data that gets used in ExpAn? - Tobias

### Keep In Touch
- João
    - [Twitter](https://twitter.com/joaomcsantos)
- Jie
    - [Twitter](https://twitter.com/jiebao)
- Laurie
    - [Twitter](https://twitter.com/LauritaApplez)

### Picks
- Tobias
    - [Hacker's Keyboard](https://play.google.com/store/apps/details?id=org.pocketworkstation.pckeyboard&hl=en)
- Jie
    - [Shah of Shahs](http://amzn.to/2cmu7zI) by Ryszard Kapuściński
- João
    - [Serendipity](https://en.wikipedia.org/wiki/Serendipity)
- Laurie
    - [Flow](https://en.wikipedia.org/wiki/Flow_(psychology))

### Links

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
