Title: Episode 52 - Hypothesis with David MacIver
Date: 2016-04-09
Category: Episodes
Tags: Testing, Automation
url: david-maciver-hypothesis.html
save_as: david-maciver-hypothesis.html

### Summary
Writing tests is important for the stability of our projects and our confidence when making changes. One issue that we must all contend with when crafting these tests is whether or not we are properly exercising all of the edge cases. Property based testing is a method that attempts to find all of those edge cases by generating randomized inputs to your functions until a failing combination is found. This approach has been popularized by libraries such as Quickcheck in Haskell, but now Python has an offering in this space in the form of Hypothesis. This week, the creator and maintainer of Hypothesis, David MacIver, joins us to tell us about his work on it and how it works to improve our confidence in the stability of our code.

<iframe id="audio_iframe" src="https://www.podbean.com/media/player/8ib9d-5e4371?from=yiiadmin&skin=103&postId=6177649&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- Subscribe on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Stitcher](http://www.stitcher.com/s?fid=64838&refid=stpr), [TuneIn](http://tunein.com/embed/follow/p726240/#) or [RSS](http://podcastinit.podbean.com/feed/)
- Follow us on [Twitter](https://twitter.com/Podcast__init__) or [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Give us feedback! Leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Tweet](https://twitter.com/Podcast__init__) to us, send us an [email](mailto:hosts@podcastinit.com) or leave us a message on [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) for your opportunity to find out about upcoming guests, suggest questions, and propose show ideas.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)
- Linode is sponsoring us this week. Check them out at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $20 credit to try out their fast and reliable Linux virtual servers for your next project
- Open Data Science Conference on May 21-22nd in Boston. 20%
- Your hosts as usual are Tobias Macey and Chris Patti
- Today we are interviewing David MacIver about the Hypothesis project which is an advanced Quickcheck implementation for Python.

<div class="well">
<a href="http://linode.com/podcastinit"><img src="/images/linode-banner-sponsor-large.png" alt="Linode Sponsor Banner"style="width: 100%;"></img></a><br/>
<p>Use the promo code <strong>podcastinit20</strong> to get a $20 credit when you sign up!</p>
</div>

### Interview with David MacIver
- Introductions
- How did you get introduced to Python? - Chris
- Can you provide some background on what Quickcheck is and what inspired you to write an implementation in Python? - Tobias
- Are there any ways in which Hypothesis improves on the original design of Quickcheck? - Tobias
- Can you walk us through the execution of a simple Hypothesis test to give our listeners a better sense for what Hypothesis does? - Chris
- Have you had trouble getting people to use Hypothesis? How has adoption been? - David
- What does this sort of testing get you that conventional testing doesn't? - David
- Why do you think this sort of testing hasn't caught on in the Python world before? - David
- Are there any facilities of the Python language that make your job easier? Are there aspects of the language that make this style of testing more difficult? - Tobias
- What are some of the design challenges that you have been presented with while working on Hypothesis and how did you overcome them? - Tobias
- Given that testing is an important part of the development process for ensuring the reliability and correctness of the system under test, how do you make sure that Hypothesis doesn't introduce uncertainty into this step? - Tobias
- Given the sophisticated nature of the internals of Hypothesis, do you find it difficult to attract contributors to the project? - Tobias
- A few months ago you went through some public burnout with regards to open source and Hypothesis in particular, but circumstances have brought you back to it with a more focused plan for making it sustainable. Can you provide some background and detail about your experiences and reasoning? - Tobias
- What's next for Hypothesis? - Chris

### Keep In Touch
- [Twitter](https://twitter.com/drmaciver)
- [Blog](http://drmaciver.com)
- [NewsLetter](http://tinyletter.com/drmaciver)

### Picks
- Tobias
    - [TypeForm](http://typeform.io)
    - [Listener Survey](https://podcastinit.typeform.com/to/gCdmf7)
    - [CI Survey](https://tobiasmacey.typeform.com/to/kq6rwd)
- Chris
    - [Seashine](http://seashinegame.com/)
    - [CheckIO](https://www.checkio.org/)
    - [Mike Coutermarsh's Jr. Developer series](https://medium.com/@mscccc/jr-developers-0-hello-world-dd1d4a2a098c#.bual8m633)
- David
    - [Make It Stick by Peter Brown](http://makeitstick.net/) 
    - [Beeminder](https://www.beeminder.com/)
    - [Vorkosigan Saga by Lois McMaster Bujold ](https://en.wikipedia.org/wiki/Vorkosigan_Saga)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
