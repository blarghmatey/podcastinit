Title: Episode 80 - Python for GIS with Sean Gillies
Date: 2016-10-22
Category: Episodes
Tags: GIS, Mapping
url: sean-gillies-python-gis.html
save_as: sean-gillies-python-gis.html

### Summary
Location is an increasingly relevant aspect of software systems as we have more internet connected devices with GPS capabilities. GIS (Geographic Information Systems) are used for processing and analyzing this data, and fortunately Python has a suite of libraries to facilitate these endeavors. This week Sean Gillies, an author and contributor of many of these tools, shares the story of his career and contributions, and the work that he is doing at MapBox.

<iframe src="https://www.podbean.com/media/player/d4vtf-63cf1a?from=yiiadmin&skin=103&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

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

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable.
- When you're ready to launch your next project you'll need somewhere to deploy it. Check out Linode at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $20 credit to try out their fast and reliable Linux virtual servers for running your awesome app.
- You'll want to make sure that your users don't have to put up with bugs, so you should use Rollbar for tracking and aggregating your application errors to find and fix the bugs in your application before your users notice they exist. Use the link [rollbar.com/podcastinit](https://rollbar.com/podcastinit) to get 90 days and 300,000 errors for free on their bootstrap plan.
- Visit our site to subscribe to our show, sign up for our newsletter, read the show notes, and get in touch.
- To help other people find the show you can leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), or [Google Play Music](https://play.google.com/music/m/I7ogju4xv6adasgqz6545jndgsy?t=Podcastinit_-_Python_and_the_people_who_make_it_great), and tell your friends and co-workers
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) for your opportunity to find out about upcoming guests, suggest questions, and propose show ideas.
- Your host as usual is Tobias Macey
- Today I'm interviewing Sean Gillies about writing Geographic Information Systems in Python.

### Interview with Firstname Lastname
- Introductions
- How did you get introduced to Python?
- Can you start by describing what Geographic Information Systems are and what kinds of projects might take advantage of them?
- How did you first get involved in the area of GIS and location-based computation?
- What was the state of the Python ecosystem like for writing these kinds of applications?
- You have created and contributed to a number of the canonical tools for building GIS systems in Python. Can you list at least some of them and describe how they fit together for different applications?
- What are some of the unique challenges associated with trying to model geographical features in a manner that allows for effective computation?
  - How does the complexity of modeling and computation scale with increasing land area?
- Mapping and cartography have an incredibly long history with an ever-evolving set of tools. What does our digital age bring to this time-honored discipline that was previously impossible or impractical?
- To build accurate and effective representations of our physical world there are a number of domains involved, such as geometry and geography. What advice do you have for someone who is interested in getting started in this particular niche?
- What level of expertise would you advise for someone who simply wants to add some location-aware features to their application?
- I know that you joined Mapbox a little while ago. Which parts of their stack are written in Python?
- What are the areas where Python still falls short and which languages or tools do you turn to in those cases?

### Keep In Touch
- [Email](mailto:sean.gillies@gmail.com)
- [Twitter](https://twitter.com/sgillies)

### Picks
- Tobias
  - [Roku Streaming Stick](http://amzn.to/2ehZiNs)
- Sean
  - [The Tacopedia](http://amzn.to/2f3wysS)
  - [Stromé](https://en.wikipedia.org/wiki/Stromae)

### Links
- [GDAL](http://www.gdal.org/)
- [SWIG](http://www.swig.org/)
- [QGIS](http://www.qgis.org/en/site/)
- [Shapefiles](https://en.wikipedia.org/wiki/Shapefile)
- [Shapely](http://toblerity.org/shapely/manual.html)
- [Fiona](http://toblerity.org/fiona/manual.html)
- [Raster File](https://en.wikipedia.org/wiki/GIS_file_formats#Raster_formats)
- [GEOS](https://trac.osgeo.org/geos/)
- [Rasterio](https://mapbox.github.io/rasterio/)
- [PostGIS](http://www.postgis.net/)
- [RTree](http://toblerity.org/rtree/)
- [GeoPandas](http://geopandas.org/)
- [GeoJSON](http://geojson.org/)
- [Orthorectification](https://trac.osgeo.org/ossim/wiki/orthorectification)
- [Mapbox](https://www.mapbox.com/)
- [SCONS](http://scons.org/)
- [Mapnik](http://mapnik.org/)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
