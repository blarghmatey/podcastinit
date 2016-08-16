Title: Episode 15 - Damien George of Micro Python
save_as: damien-george-micropython.html
url: damien-george-micropython.html
Date: 2015-06-29
Category: Episodes
Tags: Hardware, Embedded, IoT, Micro Python

### Summary
We talked to Damien George about his work on the Micro Python interpreter and the PyBoard SOC (Systom On a Chip). The combination of the interpreter and SOC allows Python developers to get involved in hardware hacking, as well as letting electronics afficionados try their hand at development. Damien explained to us where this fits in with the expanding landscape of low cost embedded devices and why you should get one to start playing with it.

<iframe id="audio_iframe" src="https://www.podbean.com/media/player/qvjxr-5767e0?from=wp&skin=103&postId=5728224&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
* Date of recording - June 29th, 2015
* Hosts - Tobias Macey and Chris Patti
* Follow us on iTunes, Stitcher or TuneIn
* Give us feedback on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Twitter](https://twitter.com/Podcast__init__), [email](mailto:hosts@podcastinit.com) or [Disqus](http://podcastinit.com)
* You can donate (if you want)!
* Overview - Interview with Damien George from the Micro Python project

### Interview with Damien George
* Introductions
   * Postdoc in Theoretical Physics
* How did you get introduced to Python?
* What problem were you trying to solve when you first had the idea to create the Micro Python board and interpreter?
   * Not really :)
   * Python lets you get things done quickly
   * Abstracts the hardware really well
* In the Kickstarter video you mention that Micro Python is a complete re-implementation of Python optimized to run on a micro-controller. How hard was it to create an alternative Python implementation? Did you have hard decisions to make as to what to include given the limitations of the hardware?
   * To start with, was it even possible?
     * Proof of Concept: Get a REPL running on the board
   * Lots of tricks to get things to fit into RAM
      * Stuffing integers into pointers
      * Optimizing RAM at various points
      * Runs the parser 4 times, looking for different things each time
      * Lots of things are stored in ROM in the built-in Flash
   * Very fine efficiency trade off between code size, memory usage, speed.
   * REPL runs in 1K of RAM!
      * Most of this is the parse tree
   * 20 line script might take ~5K RAM
   * 128K RAM on the Micro Python board
   * Not 100% Python - but 90% - the most useful parts
* I know that people who have developed alternative Ruby implementations have run into issues due to the lack of a formal specification. Has the fact that there _is_ a specification for Python made your job easier?
   * Definitely, Python is very well defined
   * Well documented
   * Already multiple implementations
* The WiPy chip seems like an interesting device. What are some ways in which it could be put to use? A Micro Python cluster for instance?
   * Small, cheap, low power little wireless chip that also runs Python
   * You can telnet in and have a Python REPL
   * Part of the Internet of Things
* What changes did you have to make to get the Python interpreter to run without an underlying operating system?
* When you were designing the hardware, what were some of the requirements that you were targeting in terms of performance or peripherals?
   * Wanted the best chip for the least money
   * Didn't know ahead of time how many resources were required
* What level of hardware knowledge is required to start working with the Micro Python board?
   * Virtually none
   * Just need to plug into USB and login with a terminal program to get a Python prompt
   * Can change frequency of CPU, turn on/off LEDs, etc.
   * Connecting peripherals requires some hardware knowledge
   * Module namespace to make hardware management easier
* For anyone who is interested in writing libraries, what kinds of restrictions do they need to be aware of?
   * Be aware of RAM size limitations
   * Prety much anything that will fit will work
   * Libraries with C extensions won't work because they rely on the CPython API
* What license is used for the Micro Python interpreter and the PyBoard? Are the compatible with commercial uses?
   * MIT License
   * Hardware schematics are open source as well, open and accessible design
* What are some of the most interesting/innovative projects that you have seen people make with the Micro Python board or runtime?
   * Damien attempted to make a quadcopter - not completely finished
   * Micro Python controlled guitar - PyBoard connected to actuators to play guitar
* How does the experience of using Micro Python compare to some of the other hardware projects that are popular right now such as Arduino, Raspberry Pi or Tessel?
   * PyBoard in between Arduino and Raspberry Pi
      * More approachable than Arduino
      * Not a full OS like Raspberry Pi
   * Tessel similar to Micro Python but runs Javascript
* EU Space Agency (Europe's version of NASA) interested in Micro Python
   * Prepared to fund Micro Python development to explore possibilities of space based applications
      * Code needs to be well written and with few bugs
      * See if it can be used for real-time systems

### Picks
* Tobias
   * [Machine Gun Preacher](http://www.imdb.com/title/tt1586752/) - Real life story of Sam Childers' work in Southern Sudan
   * [Pocket Book Android App](https://play.google.com/store/apps/details?id=com.obreey.reader&hl=en) - E-Book app with good UI/UX and solid feature set
   *  Online access to digital media through local library memberships
      * [Hoopla Digital](https://www.hoopladigital.com/home;jsessionid=BA909933ECAB99A033C57A5620A272E4)
      * [Overdrive](http://app.overdrive.com/)
* Chris
   * [Real Ramen](https://en.wikipedia.org/wiki/Ramen)
   * [RedHat Summit](http://www.redhat.com/summit/)
   * [The SELinux Coloring Book](https://github.com/mairin/selinux-coloring-book/blob/master/PDF/en/selinux-coloring-book_USLetter-Stapled.pdf)
* Damien
   * [MOSH](http://mosh.mit.edu) - Mobile shell, resilient SSH that allows for resuming sessions across networks, computer sleeps, etc.

### Keep in Touch
* Twitter
  - [@micropython](https://twitter.com/micropython)
  - [@damienpgeorge](https://twitter.com/damienpgeorge)
* GitHub - [micropython](https://github.com/micropython)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
