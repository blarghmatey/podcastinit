Title: Episode 20 - Static Site Generators
Date: 2015-08-03
Category: Episodes
Tags: websites, blogging
url: static-site-generators.html
save_as: static-site-generators.html

### Summary
In this episode we had the opportunity to discuss the world of static site generators with Roberto Alsina of the Nikola project and Justin Mayer of the Pelican project. They explained what static site generators are and why you might want to use one. We asked about why you should choose a Python based static site generator, theming and markup support as well as metadata formats and documentation. We also debated what makes Pelican and Nikola so popular compared to other projects.

<iframe id="audio_iframe" src="http://www.podbean.com/media/player/w5e6f-583e3b?from=wp&skin=103&postId=5783099&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Welcome to Podcast.\_\_init\_\_ the podcast about Python and the people who make it great
- Follow us on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Stitcher](http://www.stitcher.com/s?fid=64838&refid=stpr) or [TuneIn](http://tunein.com/radio/Podcast\_\_init\_\_-p726240/)
- Give us feedback on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Twitter](https://twitter.com/Podcast__init__), [email](mailto:hosts@podcastinit.com) or [Disqus](http://podcastinit.com)
- We donate our time to you because we love Python and its community. If you would like to return the favor you can send us a [donation](\url{http://podcastinit.com/our-plans-for-your-donations.html)}. Everything that we don't spend on producing the show will be donated to the PSF to keep the community alive.
- Date of recording - August 08, 2015
- Hosts Tobias Macey and Chris Patti
- Today we are interviewing the core developers of Nikola and Pelican about static site generators

### Interview
- Introductions
    - Monitorial.net <- Justin
    - Upriise <- Justin
    - Works for Canonical <- Roberto
- How did you get introduced to Python?
    - Justin:
        - Needed a way to get order data to payment processor for commerce company
    - Roberto:
        - 1996 got involved with Linux
        - Found XForms
        - Wrote Python bindings
- For our listeners who might not know, what are static site generators and what are some of the advantages they bring to the table over other similar systems that perform the same function?
    - Roberto
        - Remove all the effort from the computer that serves the website
        - Server runs no code
        - Smaller ssurface area for security purposes
    - Justin
        - Better performance - important for responsiveness and uptime
        - Easier deployment and maintenance
        - Easier versioning and migration
        - Can version both input and output
- There are a number of static site generators available in virtually every language. Why would a user want to leverage a Python solution vs Ruby, javascript, Go, etc.?
    - ReStructured TeXT is best supported in Python
    - Good language for supporting various markup syntaxes
- Most static site generators seem to have a primary focus on blogging. What is it about these tools that lend themselves so well to that use case?
    - The author of the tools shape the purpose of the tool
    - Most popular among programmers which is a demographic that is likely to have a blog
        - Workflow is similar to what programmers are used to
    - Still useful for non-chronological pages due to templating system
- Something that struck me comparing the two systems is that they have largely the same kinds of data going into the metadata block for each post, but it's expressed in a different / incompatible way in each. Have you ever considered agreeing on a standard and even advertising it as such so all static site generators could make use of it?
- Challenging because of the idiosyncratic way problems are solved in each system
- Wouldn't end up with the same site even if metadata were identical
- Roberto & Justin are talking, this may happen!
- The themes in Pelican and Nikola have very different feels and one of the things that initially drew me to Pelican is the larger catalog of themes available. What are some of the challenges involved in creating a theme for a static site generator?
- Many programmers who write SSGs aren't amazing at HTML
- Pelican and Nikola seem to be the most widely used projects for creating static sites using Python. What do you think is the key to that popularity?
    - Frequent updates, good documentation and large community
    - Easy to get up and running
        - Need to be productive inside of 2 minutes
    - Good first impressions are key
    - Importance of extensibility
    - Core modularity and availability of plugins
- A lot of people have written about the importance (and difficulty) of writing and maintaining good documentation in open source projects. Nikola's documentation is excellent. How did Nikola manage this in its development process and what can other open source projects learn from this?
    - No secrets - just do it and keep it updated.
    - Need to look at the tool as if using it for the first time
- What are some specific examples of unique and interesting uses your site generators have been put to?
    - Justin:
        - kernel.org, Debian, Chicago Linux Users, TransFX (translation house) all use Pelican
        - Embedding Jupyter notebooks and MathML rendering in posts
        - Site search plugin
    - Nikola:
        - Big adoption in the sciences (Jupyter notebook embedding supported in core)
        - Output is forever
        - Plugin to trigger internet archive to reindex site
- Nikola's flexible deployment architecture (e.g. the use of doit tasks) seems to lend itself to some interesting use cases. What was the inspiration for this?
    - Build was taking 1 1/2 hours, doit allowed for incremental generation
    - Doit is a generic task system. Nikola has no "main" it's a collection of doit tasks.
- Is there any specific help that you would like to ask of the audience?
    - Contribute themes
    - Help with reviewing issues and pull requests

### Picks
- Tobias
    - [Termux](http://termux.com/)
    - [Magic Wormhole](https://github.com/warner/magic-wormhole)
    - [Arrow](http://crsmithdev.com/arrow/)
- Chris
    - [Emacs Lisp Introduction](https://www.gnu.org/software/emacs/manual/eintr.html)
    - [3D Cellular Automata in Minecraft](https://www.youtube.com/watch?v=wNypW-aSCmE)
    - [Prompt 2](https://panic.com/prompt/)
- Justin
    - [Monitorial.net](http://monitorial.net)
    - [Upriise](http://upriise.com)
    - [Ergodox](http://ergodox.org/)
    - [Jarvis Bamboo Sit/Stand Desk](http://www.ergodepot.com/Jarvis_Desk_Bamboo_p/jrv-b.htm)
    - [Talky.io](https://talky.io)
    - [Fish shell](http://fishshell.com/)
        - [Tacklebox](https://github.com/justinmayer/tacklebox)
    - [iTerm v3.0 beta](https://www.iterm2.com/)
    - [Brother Thelonious Belgian Ale](http://www.beeradvocate.com/beer/profile/112/30282/)
    - [Frog's Leap Winery](http://www.frogsleap.com/)
    - [PyCon Italia](https://www.pycon.it/en/) and Italy in general
- Roberto
    - [Neal Stephenson](http://www.nealstephenson.com/)
    - [Docopt](http://docopt.org/)
    - [Fried Pickles](https://en.wikipedia.org/wiki/Fried_pickle)
    - [PyAr](http://python.org.ar/) Python Argentina User Group
    - [PyCon Argentina](http://ar.pycon.org/) in Mendosa
    - [PyCamp](http://python.org.ar/wiki/PyCamp)

### Keep In Touch
- Justin
    - [Personal](http://justinmayer.com)
    - [Pelican](http://getpelican.com)
- Roberto
    - [Nikola](http://getnikola.com)
        - Forums and mailing list
