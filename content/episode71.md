Title: Episode 71 - Gensim with Radim Řehůřek
Date: 2016-08-20
Category: Episodes
Tags: NLP, Semantic Analysis, Topic Modeling
url: radim-rehurek-gensim.html
save_as: radim-rehurek-gensim.html

### Summary
Being able to understand the context of a piece of text is generally thought to be the domain of human intelligence. However, topic modeling and semantic analysis can be used to allow a computer to determine whether different messages and articles are about the same thing. This week we spoke with Radim Řehůřek about his work on GenSim, which is a Python library for performing unsupervised analysis of unstructured text and applying machine learning models to the problem of natural language understanding.

<iframe src="https://www.podbean.com/media/player/fye29-61f534?from=yiiadmin&skin=103&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)
- Linode is sponsoring us this week. Check them out at [linode.com/podcastinit](http://linode.com/podcastinit) and get a $20 credit to try out their fast and reliable Linux virtual servers for your next project
- We are also sponsored by Sentry this week. Stop hoping your users will report bugs. Sentry's real-time tracking gives you insight into production deployments and information to reproduce and fix crashes. Check them out at [getsentry.com](https://getsentry.com/welcome/) and use the code *podcastinit* at [signup](https://getsentry.com/welcome/?utm_source=podcastinit&utm_medium=podcast&utm_campaign=sponsored&code=podcastinit) to get a $50 credit on your account.
- Visit our site to subscribe to our show, sign up for our newsletter, read the show notes, and get in touch.
- To help other people find the show you can leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), or [Google Play Music](https://play.google.com/music/m/I7ogju4xv6adasgqz6545jndgsy?t=Podcastinit_-_Python_and_the_people_who_make_it_great), and tell your friends and co-workers
- Join our community! Visit [discourse.pythonpodcast.com](https://discourse.pythonpodcast.com) for your opportunity to find out about upcoming guests, suggest questions, and propose show ideas.
- Your hosts as usual are Tobias Macey and Chris Patti
- Today we're interviewing Radim Řehůřek about Gensim, a library for topic modeling and semantic analysis of natural language.

<div class="well">
<a href="http://linode.com/podcastinit"><img src="/images/linode-banner-sponsor-large.png" alt="Linode Sponsor Banner" style="width: 100%;"></img></a><br/>
<p>Use the promo code <strong>podcastinit20</strong> to get a $20 credit when you sign up!</p>
</div>

<div class="well">
<a href="https://getsentry.com/welcome/?utm_source=podcastinit&utm_medium=podcast&utm_campaign=sponsored&code=podcastinit"><img src="/images/sentry-horizontal-black.png" style="background: white; margin: auto; display: block; padding: 10px; width: 90%;"/></a><br/>
<p>Stop hoping your users will report bugs. Sentry's real-time tracking gives you insight into production deployments and information to reproduce and fix crashes. Use the code <b>podcastinit</b> at <a href="https://www.getsentry.com/signup/?code=podcastinit&utm_source=podcastinit&utm_medium=podcast&utm_campaign=sponsored">signup</a> to get a $50 credit!</p>
</div>

### Interview with Radim Řehůřek
- Introductions
- How did you get introduced to Python? - Chris
- Can you start by giving us an explanation of topic modeling and semantic analysis? - Tobias
- What is Gensim and what inspired you to create it? - Tobias
- What facilities does Gensim provide to simplify the work of this kind of language analysis? - Tobias
- Can you describe the features that set it apart from other projects such as the NLTK or Spacy? - Tobias
- What are some of the practical applications that Gensim can be used for? - Tobias
- One of the features that stuck out to me is the fact that Gensim can process corpora on disk that would be too large to fit into memory. Can you explain some of the algorithmic work that was necessary to allow for this streaming process to be possible? - Tobias
    - Given that it can handle streams of data, could it also be used in the context of something like Spark? - Tobias
- Gensim also supports unsupervised model building. What kinds of limitations does this have and when would you need a human in the loop? - Tobias
    - Once a model has been trained, how does it get saved and reloaded for subsequent use? - Tobias
- What are some of the more unorthodox or interesting uses people have put Gensim to that you've heard about? - Chris
- In addition to your work on Gensim, and partly due to its popularity, you have started a consultancy for customers who are interested in improving their data analysis capabilities. How does that feed back into Gensim? - Tobias
- Are there any improvements in Gensim or other libraries that you have made available as a result of issues that have come up during client engagements? - Tobias
- Is it difficult to find contributors to Gensim because of its advanced nature? - Tobias
- Are there any resources you'd like to recommend our listeners explore to get a more in depth understanding of topic modeling and related techniques? - Chris

### Keep In Touch
- [RaRe Technologies](http://rare-technologies.com/)
- [Twitter](https://twitter.com/RadimRehurek)
- [Email](radim@rare-technologies.com)
- [Github](https://github.com/piskvorky)
- [Mailing List](https://groups.google.com/group/gensim)

### Picks
- Tobias
    - [Dark Matter and the Dinosaurs](http://amzn.to/2bvESj1) by Lisa Randall
- Chris
    - [m-cli](https://github.com/rgcr/m-cli)
- Radim
    - [1177 BC: The Year Civilization Collapsed](http://press.princeton.edu/titles/10185.html)

### Links
- [Nadia Eghbal](https://medium.com/@nayafia/)
- [Gensim](https://radimrehurek.com/gensim/)
- [SQL Addict](http://sqladdict.com/)
- [NLTK](http://www.nltk.org/)
- [Spacy](http://spacy.io/)
- [Latent Dirichlet Allocation (LDA)](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation)
- [LSI](https://www.researchgate.net/publication/298210256_LSI_Latent_Semantic_Inference_for_Natural_Image_Segmentation)
- [Keynote in Italy on distributed processing](https://www.youtube.com/watch?v=Og1r5heUmOo)
- [Google Scholar references for Gensim](https://scholar.google.com/scholar?hl=en&q=gensim&btnG=&as_sdt=1%2C22&as_sdtp=)
- [Stylometric analysis](https://en.wikipedia.org/wiki/Stylometry)
- [On Writing Well](http://amzn.to/2b6tIlc)
- [Student Incubator](https://rare-technologies.com/incubator/)
- [Wikipedia on topic modeling](https://en.wikipedia.org/wiki/Topic_model)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
