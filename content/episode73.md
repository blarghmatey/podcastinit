Title: Episode 73 - Alex Martelli
Date: 2016-09-03
Category: Episodes
Tags: People
url: alex-martelli.html
save_as: alex-martelli.html

### Summary
Alex Martelli has dedicated a large part of his career to teaching others how to work with software. He has the highest number of Python questions answered on Stack Overflow, he has written and co-written a number of books on Python, and presented innumerable times at conferences in multiple countries. We spoke to him about how he got started in software, his work with Google, and the trends in development and design patterns that are shaping modern software engineering.

<iframe src="https://www.podbean.com/media/player/qi98f-6257a2?from=yiiadmin&skin=103&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)
- Linode is sponsoring us this week. Check them out at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $20 credit to try out their fast and reliable Linux virtual servers for your next project
- We also have a returning sponsor this week. Rollbar is a service for tracking and aggregating your application errors so that you can find and fix the bugs in your application before your users notice they exist. Use the link [rollbar.com/podcastinit](https://rollbar.com/podcastinit) to get 90 days and 300,000 errors for free on their bootstrap plan.
- Hired is sponsoring us this week. If you're looking for a job as a developer or designer then Hired will bring the opportunities to you. Sign up at [hired.com/podcastinit](https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit) to double your signing bonus.
- Visit our site to subscribe to our show, sign up for our newsletter, read the show notes, and get in touch.
- To help other people find the show you can leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), or [Google Play Music](https://play.google.com/music/m/I7ogju4xv6adasgqz6545jndgsy?t=Podcastinit_-_Python_and_the_people_who_make_it_great), and tell your friends and co-workers.
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) for your opportunity to find out about upcoming guests, suggest questions, and propose show ideas.
- Your hosts as usual are Tobias Macey and Chris Patti
- Today we're interviewing Alex Martelli

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

### Interview with Alex Martelli
- Introductions
- How did you get introduced to Python? - Chris
- You have achieved a number of honors and recognitions throughout your career for significant technical achievements. What kind of learning strategies do you use to enable you to achieve mastery of technical topics? - Tobias
- How do you keep the Python In A Nutshell book current as aspects of the core language and its libraries change? - Chris
- You are known for your prolific contributions to Stack Overflow, particularly on topics pertaining to Python. Was that a specific goal that you had set for yourself or did it happen organically? - Tobias
- When answering Stack Overflow questions, do you usually already know the answers or do you treat it as a learning opportunity? - Tobias
- What are some of the most difficult Python questions that you have been faced with? - Tobias
- You have presented quite a number of times at various Python conferences. What are some of your favorite talks? - Tobias
- Design patterns and idiomatic code are common themes in a number of your presentations. Why is it important for developers to understand these concepts and what are some of your favorite resources on the topic? - Tobias
- What do you see as the most influential trends in software development and design, both currently and heading into the future? - Tobias
- As a long-time computer engineer, are there any features or ideas from other languages that you would like to see incorporated into Python?

### Picks
- Tobias
    - [The Great Gatsby Movie](http://amzn.to/2bKAwW9)
- Chris
    - [Stone Ruination Double IPA](https://www.beeradvocate.com/beer/profile/147/4083/)
    - [Ghost Soldiers](https://smile.amazon.com/dp/B000FBJCJ4/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1#nav-subnav)
- Alex
    - [Alexander Hamilton](http://amzn.to/2bKAQUN) by Ron Chernow
    - [Hamilton Musical](http://www.hamiltonbroadway.com/)

### Links
- [Permission or Forgiveness](https://www.youtube.com/watch?v=AZDWveIdqjY)
- [Good enough is good enough](https://www.youtube.com/watch?v=gHG9FRSlPxw)
- [Modern Python Patterns and Idioms](https://www.youtube.com/watch?v=LeuChRCByZc)
- [Handling Errors and Exceptions in Modern Python](https://www.youtube.com/watch?v=frZrBgWHJdY)
- [Microservices](https://en.wikipedia.org/wiki/Microservices)
- [Google SRE Book](http://www.anrdoezrs.net/6d103wktqks7FGD8FHD799AE89HG79CCGAHAA8H888?url=http%3A%2F%2Fshop.oreilly.com%2Fproduct%2F0636920041528.do%3Fcmp%3Daf-velocity-books-videos-product_cj_9781491929124_%2525zp&cjsku=SKU-KIT-0636920041528-IP-BUNDLE)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
