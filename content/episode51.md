Title: Episode 51 - Pyjion with Brett Cannon and Dino Viehland
Date: 2016-03-31
Category: Episodes
Tags: Performance, CPython
url: pyjion-pluggable-jit.html
save_as: pyjion-pluggable-jit.html

### Summary
In an attempt to improve the performance characteristics of the CPython implementation, Dino Viehland began work on a patch to allow for a pluggable interface to a JIT (Just In Time) compiler. His employer, Microsoft, decided to sponsor his efforts and the result is the Pyjion project. In this episode we spoke with Dino Viehland and Brett Cannon about the goals of the project, the progress they have made so far, and the issues they have encountered along the way. We also made an interesting detour to discuss the general state of performance in the Python ecosystem and why the GIL isn't the bogeyman it's made out to be.

<iframe id="audio_iframe" src="http://www.podbean.com/media/player/4upnb-5e04af?from=yiiadmin&skin=103&postId=6161583&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- Subscribe on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Stitcher](http://www.stitcher.com/s?fid=64838&refid=stpr), [TuneIn](http://tunein.com/embed/follow/p726240/#) or [RSS](http://podcastinit.podbean.com/feed/)
- Follow us on [Twitter](https://twitter.com/Podcast__init__) or [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Give us feedback! Leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Tweet](https://twitter.com/Podcast__init__) to us, send us an [email](mailto:hosts@podcastinit.com) or leave us a message on [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) for your opportunity to find out about upcoming guests, suggest questions, and propose show ideas.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)
- Linode is sponsoring us this week. Check them out at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $20 credit to try out their fast and reliable Linux virtual servers for your next project
- I would also like to thank Hired, a job marketplace for developers and designers, for sponsoring this episode of Podcast.\_\_init\_\_. Use the link [hired.com/podcastinit](http://hired.com/podcastinit) to double your signing bonus.
- Your hosts as usual are Tobias Macey and Chris Patti
- Open Data Science Conference, Boston MA May 21st - 22nd
- PyCon US
- Today we are interviewing Brett Cannon and Dino Viehland about their work on Pyjion, a CPython extension that provides an API to allow for plugging a JIT compilation engine into the CPython runtime.

<div class="well">
<a href="http://linode.com/podcastinit"><img src="/images/linode-banner-sponsor-large.png" alt="Linode Sponsor Banner"style="width: 100%;"></img></a><br/>
<p>Use the promo code <strong>podcastinit20</strong> to get a $20 credit when you sign up!</p>
</div>

<div class="well">
<a href="https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit"><img src="/images/hired-logo-dark-padding.png" alt="Hired Logo" style="float: left; width: 20%; margin-right: 20px;"></a>
<p>
On Hired software engineers & designers can get 5+ interview requests in a week and each offer has salary and equity upfront. With full time and contract opportunities available, users can view the offers and accept or reject them before talking to any company. Work with over 2,500 companies from startups to large public companies hailing from 12 major tech hubs in North America and Europe.  Hired is totally free for users and If you get a job you’ll get a $2,000 “thank you” bonus. If you use our <a href="https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit">special link</a> to signup, then that bonus will double to $4,000 when you accept a job. If you’re not looking for a job but know someone who is, you can refer them to Hired and get a $1,337 bonus when they accept a job.
</p>
</div>

### Interview with Brett Cannon and Dino Viehland
- Introductions
- How did you get introduced to Python? - Chris
- What was the inspiration for the Pyjion project and what are its goals? - Tobias
- The FAQ mentions that Pyjion could easily be made cross platform, but this being a Microsoft project it was bootstrapped on Windows. Have any of the discrete tasks required to get Pyjion running under OSX or Linux been laid out even in outline form? - Chris
- Given that this is a Microsoft backed project it makes sense that the first JIT engine to be implemented is for the CoreCLR. What would an alternative implementation provide and in what ways can a JIT framework be tuned for particular workloads? - Tobias
- What kinds of use cases and problem domains that were previously impractical will be enabled by this? - Tobias
- Does Microsoft's recent acquisition of Xamarin and the Mono project change things for the Pyjion project at all? - Chris
- What are the challenges associated with your work on Pyjion? Are there certain aspects of the Python language and the CPython implementation that make the work more difficult than it might be otherwise? - Tobias
- When I think of Microsoft and programming languages I generally think of C++ and C#. Did your team have to go through an approval process in order to utilize Python, and further to open source your work on Pyjion? - Chris
- How does Pyjion hook into the CPython runtime and what kinds of primitives does it expose to JIT engines for them to be able to work with? - Tobias
- Would an entire project be run through the JIT engine during runtime or is it possible to target a subset of the code being executed? - Tobias
- In what ways can a JIT compiler implementation be purpose-built for a given workload and how would someone go about creating one? - Tobias
- Could a JIT plugin be designed with different trade-offs, like no C API compatibility, but that worked around the GIL to provide real concurrency in Python? - Chris
- One of the most notable benefits of having a JIT implementation for the CPython runtime is the fact that modules with C extensions can be used, such as NumPy. Does that pose any difficulties in the compilation methods used for optimizing the Python portion of the code? - Tobias
- What kinds of performance improvements have you seen in your experimentation? - Tobias
- Which release of Python do you hope to have Pyjion incorporated into? - Tobias
- Has any thought been given to making Python a first class citizen in Visual Studio Code? - Chris
- What areas of the project could use some help from our listeners? - Chris

### Keep In Touch
- Dino
    - [GitHub](https://github.com/DinoV)
- Brett
    - [Twitter](https://twitter.com/brettsky)
    - [Blog](http://snarky.ca)
    - [Python Engineering @ Microsoft Blog](https://blogs.msdn.microsoft.com/pythonengineering/)

### Picks
- Tobias
    - [Logitech Wave MK550](http://amzn.to/1SEokE2)
    - [SaltStack](https://saltstack.com)
    - [TestInfra](http://testinfra.readthedocs.org)
    - [SaltStack Formula Cookiecutter](https://github.com/mitodl/saltstack-formula-cookiecutter)
- Chris
    - [Anchor - Public Radio for the People](https://anchor.fm/)
    - [The Magicians](http://www.syfy.com/themagicians)
    - [Portal is a Feminist Masterpiece - PBS Gameshow](https://www.youtube.com/watch?v=JgnublE4dxU)
- Brett
    - [Breville Tea Maker](http://amzn.to/1SEorQe)
    - [Bodom Mugs](http://amzn.to/1TQu2UX)
    - [Alto's Adventure](http://altosadventure.com/)
- Dino
    - [Come Dine With Me](http://www.channel4.com/programmes/come-dine-with-me)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
