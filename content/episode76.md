Title: Episode 76 - PsychoPy with Jonathan Peirce
Date: 2016-09-07
Category: Episodes
Tags: Science
url: jonathan-peirce-psychopy.html
save_as: jonathan-peirce-psychopy.html

### Summary
We're delving into the complex workings of your mind this week on Podcast.\_\_init\_\_ with Jonathan Peirce. He tells us about how he started the PsychoPy project and how it has grown in utility and popularity over the years. We discussed the ways that it has been put to use in myriad psychological experiments, the inner workings of how to design and execute those experiments, and what is in store for its future.

<iframe src="https://www.podbean.com/media/player/9fm8a-62f5e4?from=yiiadmin&skin=103&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable.
- Hired is sponsoring us this week. If you're looking for a job as a developer or designer then Hired will bring the opportunities to you. Sign up at [hired.com/podcastinit](https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit) to double your signing bonus.
- Once you land a job you can check out our other sponsor Linode for running your awesome new Python apps. Check them out at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $20 credit to try out their fast and reliable Linux virtual servers for your next project
- You want to make sure your apps are error-free so give our last sponsor, Rollbar, a look. Rollbar is a service for tracking and aggregating your application errors so that you can find and fix the bugs in your application before your users notice they exist. Use the link [rollbar.com/podcastinit](https://rollbar.com/podcastinit) to get 90 days and 300,000 errors for free on their bootstrap plan.
- Visit our [site](http://pythonpodcast.com) to subscribe to our show, sign up for our newsletter, read the show notes, and get in touch.
- By leaving a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), or [Google Play Music](https://play.google.com/music/m/I7ogju4xv6adasgqz6545jndgsy?t=Podcastinit_-_Python_and_the_people_who_make_it_great) it becomes easier for other people to find us.
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) to help us grow and connect our wonderful audience.
- Your hosts as usual are Tobias Macey and Chris Patti
- Today we're interviewing Jonathan Peirce about PsychoPy, an open source application for the presentation and collection of stimuli for psychological experimentation

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
On Hired software engineers & designers can get 5+ interview requests in a week and each offer has salary and equity upfront. With full time and contract opportunities available, users can view the offers and accept or reject them before talking to any company. Work with over 2,500 companies from startups to large public companies hailing from 12 major tech hubs in North America and Europe. Hired is totally free for users and If you get a job you’ll get a $2,000 “thank you” bonus. If you use our <a href="https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit">special link</a> to signup, then that bonus will double to $4,000 when you accept a job. If you’re not looking for a job but know someone who is, you can refer them to Hired and get a $1,337 bonus when they accept a job.
</p>
</div>


### Interview with Jonathan Peirce
- Introductions
- How did you get introduced to Python? - Chris
- Can you start by telling us what PsychoPy is and how the project got started? - Tobias
- How does PsychoPy compare feature wise against some of the proprietary alternatives? - Chris
- In the documentation you mention that this project is useful for the fields of psychophysics, cognitive neuroscience and experimental psychology. Can you provide some insight into how those disciplines differ and what constitutes an experiment? - Tobias
- Do you find that your users who have no previous formal programming training come up to speed with PsychoPy quickly? What are some of the challenges there? -Chris
- Can you describe the internal architecture of PsychoPy and how you approached the design? - Tobias
- How easy is it to extend PsychoPy with new types of stimulus? - Chris
- What are some interesting challenges you faced when implementing PsychoPy? - Chris
- I noticed that you support a number of output data formats, including pickle. What are some of the most popular analysis tools for users of PsychoPy? - Tobias
    - Have you investigated the use of the new Feather library? - Tobias
- How is data input typically managed? Does PsychoPy support automated readings from test equipment or is that the responsibility of those conducting the experiment? - Tobias
- What are some of the most interesting experiments that you are aware of having been conducted using PsychoPy? - Chris
- While reading the docs I found the page describing the integration with the OSF (Open Science Framework) for sharing and validating an experiment and the collected data with other members of the field. Can you explain why that is beneficial to the researchers and compare it with other options such as GitHub for use within the sciences? - Tobias
- Do you have a roadmap of features that you would like to add to PsychoPy or is it largely driven by contributions from practitioners who are extending it to suit their needs? - Tobias

### Keep In Touch
- [PsychoPy Discourse Forum](http://discourse.psychopy.org/)

### Picks
- Tobias
    - [Hackers: Heroes of the Computer Revolution](http://www.stevenlevy.com/index.php/books/hackers) by Steven Levy
- Chris
    - [Castro 2](http://supertop.co/castro/)
- Jon
    - [Discourse](discourse.org)

### Links
- [Feather](https://blog.rstudio.org/2016/03/29/feather/)
- [Pyglet](https://bitbucket.org/pyglet/pyglet/wiki/Home)
- [HDF5](http://hortonworks.com/apache/hdfs/)
- [Open Science Framework](https://osf.io/)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/) / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
