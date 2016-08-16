Title: Episode 13 - Jacob Kovac on KivEnt
URL: jacob-kovac-kivent.html
save_as: jacob-kovac-kivent.html
Category: Episodes
Date: 2015-06-17
Tags: Game Development, Kivy

### Summary
In this episode we talked to Jacob Kovac, creator of the KivEnt game engine and one of the Kivy core developers. He told us about what inspired him to create the KivEnt project, some of the ways that he has managed to optimize rendering time and some of the problems that he has encountered as part of his work on the project. We also discussed what the use cases and limitations of the KivEnt engine are and he shared some of the projects that have been made with it.

<iframe id="audio_iframe" src="https://www.podbean.com/media/player/sztiw-571853?from=wp&skin=103&postId=5707859&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
*  Date of recording - June 17th, 2015
*  Hosts - Tobias Macey and Chris Patti
*  Follow us on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Stitcher](http://www.stitcher.com/s?fid=64838&refid=stpr) or [TuneIn](http://tunein.com/radio/Podcast\_\_init\_\_-p726240/)
*  Give us feedback on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Twitter](https://twitter.com/Podcast\_\_init\_\_), [email](mailto:hosts@podcastinit.com) or [Disqus](http://podcastinit.com)
*  We don't have any corporate sponsorship or advertisements in the show because we are making it for the community and we respect our listeners and value your time. If you would like to help support the show and keep it ad-free you can find out how by visiting our [website](http://podcastinit.com/our-plans-for-your-donations.html)
*  Overview - Interview with Jacob Kovac about the KivEnt Game Engine, based off of Kivy

### Interview with Jacob Kovac
*  Introductions
*  How did you get introduced to Python? - Chris
*  Could you please give us a high level overview of KivEnt and how it differs from other game builder frameworks like Unity or Unreal?
    *  Manages memory for game objects and stores them contiguously in memory for greater efficiency
    *  Real-time focused rendering engine for Kivy
    *  Cython interface to provide performant game objects with Python API
    *  Increased speed of main render loop by 38X by removing a single Python list lookup
    *  Kivent is mainly 2D focused, vs 3D for Unity/Unreal
    *  Python all the way down
        *  Cython and pointer magic for optimization purposes
    *  Made to be familiar to Pythonistas
    *  Aiming for "A" level games
    *  Bringing modern advancements in making games to Python - GPU awareness
    * Built with constraints in mind
    * The Pacman Dossier
*  What inspired you to create the KivEnt engine?
    *  Tried to create an Android infinite runner in Kivy, performance was unacceptable
    *  Looking for how to build games in Python with large amounts of data
*  Is there a particular kind of game KivEnt is particularly suited for versus any of the other popular frameworks?
    *  Focuses mainly on 2D, agnostic as to 'type' of game
    *  Jacob's interests largely focused on procedurally generated environments
*  Could KivEnt be used to create networked multiplayer games and what challenges might that bring to the table for the aspiring KivEnt game developer?
    *  Multiplayer thought to be largely out of scope
        *  This doesn't mean KivEnt is bad for multiplayer games, but that KivEnt in and of itself doesn't wholly solve this problem.
        *  Plenty of other frameworks to draw on for handling the multi-player server or pulling data from it, KivEnt solves the client side problems germane to making a game in Python
*  Does the fact that KivEnt games need to run on so many platforms present any unique difficulties in KivEnt's development?
    *  Kivy has solved most of the cross-platform problems
    *  Difference in GPU vendors has proved the most difficult
*  I hear game developers talk a lot about assets and asset formats. What kinds of assets can be used with KivEnt?
    *  2D assets are simple - especially as compared to 3D
    *  KivEnt supports any image format that Kivvy does for your platform
    *  Coming next release - you can specify the vertex format for your model
    *  https://youtu.be/qe9fWC-2e3M
*  I have heard that unit testing games is difficult and rarely done for reasons of time pressure, as well as lack of determinism in the interactions. Does KivEnt provide any utilities to make this easier?
    *  Not currently well tested, but targeting that for next release
    *  Trying to add tooling to make testing games easier, though still somewhat difficult
    *  Platform Biased Podcast - by a bunch of Microsoft Studios SDETs
*  How does KivEnt handle input and what kids of input devices are supported?
    *  Input handled entirely by Kivy, so any inputs supported by Kivy are accessible in KivEnt
    *  Rumors of using Kinect camera with Kivy/KivEnt applications
* Is there a built in physics engine or is that something that is pluggable?
    *  Mostly pluggable
    *  Chipmunk 2D integration provided via a module
    *  Particle Panda - one of the major inspirations for KivEnt
    *  New Particle engine coming in the next version of KivEnt
* How does KivEnt handle collision tracking?
    *  Mathematically difficult, very hard to get right
    *  Don't do it! Use the physics engine - Chipmunk 2D is also a collision detection engine
    *  Kivy enables devs to use C, C++, Java and Objective C code in their games
    *  Game development has been democratized
    *  Entity / Component architecture enables great modularity
    *  Game objects that appear on the screen (Gun, ball, etc.) are not represented as such in the system
* Can you tell us about some of the projects that you have seen built in KivEnt which you are most excited by?
    *  https://github.com/chozabu/KivEntEd
    *  https://play.google.com/store/apps/details?id=org.chozabu.boardzfree&hl=en
* What are some ways in which our listeners could help contribute to the project?
    *  Would like to see more people build games in KivEnt
        *  Give feedback about the experience and what can be improved
    *  If you have Apple hardware, try out KivEnt and file issues with any errors that occur

### Picks
*  Tobias
    *  [EIN (Emacs IPython Notebook)](https://github.com/tkf/emacs-ipython-notebook)
    *  [Pip 7.x](https://pip.pypa.io/en/latest/news.html)
    *  [RESTful Web APIs](http://www.tkqlhce.com/click-7841235-11260198-1430755877000?url=http%3A%2F%2Fshop.oreilly.com%2Fproduct%2F0636920028468.*do%3Fcmp%3Daf-webplatform-books-videos-product\_cj\_9781449358068\_%2525zp&cjsku=0636920028468*)
*  Chris
    *  [The Killing](http://www.imdb.com/title/tt1637727/)
    *  [Data Science on the iPad with RethinkDB](http://rethinkdb.com/blog/pythonista/)
    *  [Left Hand Nitro Milk Stout](http://lefthandbrewing.com/beers/milk-stout-nitro/)
*  Jacob
    *  [Pelican Static Site Generator](http://getpelican.com)
    *  [Terraria 1.3](https://terraria.org/)
    *  Amorone Homemade Red Wine

### Keep in Touch
*  E-Mail - kovac
*  Blog - chaosbuffalogames.com/blog
*  IRC - \#kivy

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The\_Freak\_Fandango\_Orchestra/) / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
