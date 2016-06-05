Title: Episode 60 - Mercurial with Augie Fackler
Date: 2016-06-04
Category: Episodes
Tags: Version Control, Developer Tools
url: augie-fackler-mercurial.html
save_as: augie-fackler-mercurial.html

### Summary
As developers, one of the most important tools that we use daily is our version control system. Mercurial is one such tool that is written in Python, making it eminently flexible, customizable, and incredibly powerful. This week we spoke with Augie Fackler to learn about the history, features, and future of Mercurial.

<iframe src="https://www.podbean.com/media/player/hagfr-5fe0a1?from=yiiadmin&skin=103&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)
- Linode is sponsoring us this week. Check them out at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $20 credit to try out their fast and reliable Linux virtual servers for your next project
- We are also sponsored by Sentry this week. Stop hoping your users will report bugs. Sentry's real-time tracking gives you insight into production deployments and information to reproduce and fix crashes. Check them out at [getsentry.com](https://getsentry.com/welcome/)
- Visit our site to subscribe to our show, sign up for our newsletter, read the show notes, and get in touch.
- To help other people find the show you can leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), or [Google Play Music](https://play.google.com/music/m/I7ogju4xv6adasgqz6545jndgsy?t=Podcastinit_-_Python_and_the_people_who_make_it_great), and tell your friends and co-workers
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) for your opportunity to find out about upcoming guests, suggest questions, and propose show ideas.
- Your hosts as usual are Tobias Macey and Chris Patti
- Today we're interviewing Augie Fackler about the Mercurial version control system

<div class="well">
<a href="http://linode.com/podcastinit"><img src="/images/linode-banner-sponsor-large.png" alt="Linode Sponsor Banner"style="width: 100%;"></img></a><br/>
<p>Use the promo code <strong>podcastinit20</strong> to get a $20 credit when you sign up!</p>
</div>

<div class="well">
<a href="http://getsentry.com"><img src="/images/sentry-horizontal-black.png" style="background: white;"/></a>
<p>Stop hoping your users will report bugs. Sentry's real-time tracking gives you insight into production deployments and information to reproduce and fix crashes.</p>
</div>

### Interview with Augie Fackler
- Introductions
- How did you get introduced to Python? - Chris
- Can you describe what Mercurial is and how the project got started? - Tobias
- How did you get involved with working on Mercurial? - Tobias
- What are some of the features that can be found in Mercurial which are lacking in similar tools such as Git or Bazaar? - Tobias
- One  of the common complaints with Git is that its human interface could use  some work. How is Mercurial's UX an improvement over Git? - Chris
- For someone who is using Mercurial to work with a Git or other VCS repository, what are some of the edge cases that they should watch out for? Are there certain operations that could be performed in Mercurial which would break that compatibility layer? - Tobias
- How is Mercurial architected and what are some of the design choices that allow for it to be so flexible and extensible? - Tobias
- One of the core goals of Mercurial is for it to be safe. Can you explain what safety means in this context and how it is architected to achieve that goal? - Tobias
- One of the noteworthy aspects of Mercurial is the strong focus on making extensions a first-class concern in the project, so much so that a number of the core functions are written as extensions. Can you describe why that is and how the extensions plug into the core execution engine? - Tobias
- What are some of the most notable extensions that are available for use with Mercurial? - Tobias
- For someone who is familiar with Git, what are some of the concepts that they would need to learn about in order to use Mercurial in an idiomatic way? - Tobias
- A large part of the reason that Git has seen such large adoption is due to the prevalence of GitHub. There is the option of using BitBucket when using Mercurial. Are there any other noteworthy Mercurial hosting options? Do you think that the dearth of open source mercurial servers is partially due to the fact that Mercurial ships with a functional server built in? - Tobias
- Can you share some of the most recent features that have been added to Mercurial? - Tobias
- What do you have planned for the future of Mercurial? - Tobias
- How do you think current day DVCS systems like Mercurial, Git and Darcs might evolve in the future? - Chris

### Keep In Touch
- [Twitter](https://twitter.com/durin42)

### Picks
- Tobias
    - [Sapiens: A Brief History of Humankind](http://amzn.to/1ZabGwO) by Yuval Noah Harrari
    - [Cultures of Continuous Learning](https://www.youtube.com/watch?v=vr-qlXhj0HM) Keynote by Vanessa Hurst
- Chris
    - [Intro to Django Video Series](http://shop.oreilly.com/product/0636920045533.do)
    - [Transistor Podcast](http://transistor.prx.org/)
    - [Embedded Podcast](http://www.npr.org/podcasts/510311/embedded)
- Augie
    - [Leviathan Wakes]( http://www.amazon.com/Leviathan-Wakes-James-S-Corey/dp/0316129089)
    - [Three Body Problem](http://www.amazon.com/Three-Body-Problem-Cixin-Liu/dp/0765382032)
    - [Prometheus](https://prometheus.io/)

### Links
- Mercurial: The Definitive Guide
    - [Online](http://hgbook.red-bean.com/)
    - [Print](http://www.anrdoezrs.net/rm72wktqks7FGD8FHD799AE89HG79CCGAHAA8H888?url=http%3A%2F%2Fshop.oreilly.com%2Fproduct%2F9780596801311.do%3Fcmp%3Daf-prog-books-videos-product_cj_9780596800673_%2525zp&cjsku=SKU-KIT-9780596801311-IP-BUNDLE)
- [Revsets](https://selenic.com/hg/help/revsets)
- [Git Pickaxe](http://www.philandstuff.com/2014/02/09/git-pickaxe.html)
- [Facebook Mercurial Post](https://code.facebook.com/posts/218678814984400/scaling-mercurial-at-facebook/)
- [Remote File Log](https://bitbucket.org/facebook/remotefilelog)
- [Gerrit](https://www.gerritcodereview.com/)
- [Kallithea](https://kallithea-scm.org/)
- [Reviewboard](https://www.reviewboard.org/)
- [Mozilla Review Board](https://reviewboard.mozilla.org/r/)
- [A Case of Computational Thinking: The Subtle Effect of
Hidden Dependencies on the User Experience of Version
Control](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/42942.pdf)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/) / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
