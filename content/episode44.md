Title: Episode 44 - Airflow with Maxime Beauchemin
Date: 2016-02-02
Category: Episodes
Tags: Big Data, Workflows, Data Science
url: maxime-beauchemin-airflow.html
save_as: maxime-beauchemin-airflow.html

### Summary
Are you struggling with trying to manage a series of related, interdependent batch jobs? Then you should check out [Airflow](https://github.com/airbnb/airflow). In this episode we spoke with the project's creator Maxime Beauchemin about what inspired him to create it, how it works, and why you might want to use it. Airflow is a data pipeline management tool that will simplify how you build, deploy, and monitor your complex data processing tasks so that you can focus on getting the insights you need from your data.

<iframe id="audio_iframe" src="http://www.podbean.com/media/player/sxy4j-5ca0db?from=yiiadmin&skin=103&postId=6070491&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- Subscribe on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Stitcher](http://www.stitcher.com/s?fid=64838&refid=stpr), [TuneIn](http://tunein.com/embed/follow/p726240/#) or [RSS](http://podcastinit.podbean.com/feed/)
- Follow us on [Twitter](https://twitter.com/Podcast__init__) or [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Give us feedback! Leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Tweet](https://twitter.com/Podcast__init__) to us, send us an [email](mailto:hosts@podcastinit.com) or leave us a message on [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) for your opportunity to find out about upcoming guests, suggest questions, and propose show ideas.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)
- Linode is sponsoring us this week. Check them out at [linode.com/podcastinit](https://linode.com/podcastinit/?utm_source=podcastinit&utm_medium=podcast&utm_content=20%20dollar&utm_campaign=podcastinit20) and get a $20 credit to try out their fast and reliable Linux virtual servers for your next project
- I would also like to thank Hired, a job marketplace for developers and designers, for sponsoring this episode of Podcast.\_\_init\_\_. Use the link [hired.com/podcastinit](https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit) to double your signing bonus.
- Your hosts as usual are Tobias Macey and Chris Patti
- Today we are interviewing Maxime Beauchemin about his work on the Airflow project.

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

### Interview with Maxime Beauchemin
- Introductions
- How did you get introduced to Python? - Chris
- What is Airflow and what are some of the kinds of problems it can be used to solve? - Chris
- What are some of the biggest challenges that you have seen when implementing a data pipeline with a workflow engine? - Tobias
- What are some of the signs that a workflow engine is needed? - Tobias
- Can you share some of the design and architecture of Airflow and how you arrived at those decisions? - Tobias
- How does Airflow compare to other workflow management solutions, and why did you choose to write your own? - Chris
- One of the features of Airflow that is emphasized in the documentation is the ability to dynamically generate pipelines. Can you describe how that works and why it is useful? - Tobias
- For anyone who wants to get started with using Airflow, what are the infrastructure requirements? - Tobias
- Airflow, like a number of the other tools in the space, support interoperability with Hadoop and its ecosystem. Can you elaborate on why JVM technologies have become so prevalent in the big data space and how Python fits into that overall problem domain? - Tobias
- Airflow comes with a web UI for visualizing workflows, as do a few of the other Python workflow engines. Why is that an important feature for this kind of tool and what are some of the tasks and use cases that are supported in the Airflow web portal? - Tobias
- One problem with data management is tracking the provenance of data as it is manipulated and shuttled between different systems. Does Airflow have any support for maintaining that kind of information and if not do you have recommendations for how practitioners can approach the issue? - Tobias
- What other kinds of metadata can Airflow track as it executes tasks and what are some of the interesting uses you have seen or created for that information? - Tobias
- With all the other languages competing for mindshare, what made you choose Python when you built Airflow? - Chris
- I notice that Airflow supports Kerberos. It's an incredibly capable security model but that comes at a high price in terms of complexity. What were the challenges and was it worth the additional implementation effort? - Chris
- When does the data pipeline/workflow management paradigm break down and what other approaches or tools can be used in those cases? - Tobias
- So, you wrote another tool recently called Panoramix. Can you describe what it is and maybe explain how it fits in the data management domain in relation to Airflow? - Tobias

### Keep In Touch
- [Google Group](https://groups.google.com/forum/#!forum/airbnb_airflow)
- [Gitter](https://gitter.im/airbnb/airflow)
- [GitHub](https://github.com/airbnb/airflow)

### Picks
- Tobias
    - [Empire of the East](http://www.anrdoezrs.net/jk122gv30v2IQROJQSOIKLMOLQMJIKNNQJSQJJJJJJ?url=http%3A%2F%2Fwww.thriftbooks.com%2Fw%2Fempire-of-the-east_fred-saberhagen%2F563595%2F%23isbn%3D0765307421&cjsku=4537235) by Fred Saberhagen
    - [The Book of Swords](http://www.anrdoezrs.net/f281nmvsmu9HIFAHJF9BCDFCHDA9BEEHAJHAAAAAA?url=http%3A%2F%2Fwww.thriftbooks.com%2Fw%2Fbook-of-swords-books-1-to-3_fred-saberhagen%2F308963%2F%23isbn%3D1568650094&cjsku=1993429) by Fred Saberhagen
- Chris
    - [Buraka Son Sistema](https://en.wikipedia.org/wiki/Buraka_Som_Sistema)
    - [Star Wars - Despecialized Edition](http://originaltrilogy.com/topic/Harmys-STAR-WARS-Despecialized-Edition-HD-V25-MKV-IS-OUT-NOW/id/12713)
    - [The Iron Druid Chronicles](http://www.anrdoezrs.net/links/7850795/type/dlg/http://www.thriftbooks.com/series/the-iron-druid-chronicles/38373)
- Maxime
    - [Flask App Builder](http://flask-appbuilder.readthedocs.org/en/latest/)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
