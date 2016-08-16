Title: Episode 28 - Kay Hayen on Nuitka
Date: 2015-10-06
Category: Episodes
Tags: Compilers, Performance
url:kay-hayen-nuitka.html
save_as: kay-hayen-nuitka.html

### Summary
Kay Hayen is a systems engineer from Germany who has dedicated his spare time to the creation of Nuitka, a library that will compile your Python project to C++. In this episode we talked to Kay about what inspired him to create the project, how it operates, and some of the challenges he has faced. It is a very interesting project and it has the potential to let you run your Python code in a whole new way!

<iframe id="audio_iframe" src="https://www.podbean.com/media/player/k629c-59b2ac?from=yiiadmin&skin=103&postId=5878444&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Hello and welcome to Podcast.\_\_init\_\_, the podcast about Python and the people who make it great.
- Subscribe on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Stitcher](http://www.stitcher.com/s?fid=64838&refid=stpr), [TuneIn](http://tunein.com/embed/follow/p726240/#) or [RSS](http://podcastinit.podbean.com/feed/)
- Follow us on [Twitter](https://twitter.com/Podcast__init__) or [Google+](https://plus.google.com/+Podcastinit-the-python-podcast)
- Give us feedback! Leave a review on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Tweet](https://twitter.com/Podcast__init__) to us, send us an [email](mailto:hosts@podcastinit.com), leave us a message on [Google+](https://plus.google.com/+Podcastinit-the-python-podcast), or leave a comment on our [show notes](http://pythonpodcast.com/kay-hayen-nuitka.html)
- I would like to thank everyone who has donated to the show. Your contributions help us make the show sustainable. For details on how to support the show you can visit our site at [pythonpodcast.com](http://pythonpodcast.com)
- I would also like to thank Hired, a job marketplace for developers, for sponsoring this episode of Podcast.\_\_init\_\_. Use the link [hired.com/podcastinit](http://hired.com/podcastinit) to double your signing bonus. Linode has also sponsored this episode and you can get a $10 credit using the link linode.com/podcastinit to try out their fast and reliable linux virtual servers.
- We are recording today on October 6th, 2015 and your hosts as usual are Tobias Macey and Chris Patti
- Today we are interviewing Kay Hayen about the Nuitka project

<div class="well">
<a href="https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit"><img src="/images/hired-logo-dark-padding.png" alt="Hired Logo" style="float: left; width: 20%; margin-right: 20px;"></a>
<p>
On Hired software engineers & designers can get 5+ interview requests in a week and each offer has salary and equity upfront. With full time and contract opportunities available, users can view the offers and accept or reject them before talking to any company. Work with over 2,500 companies from startups to large public companies hailing from 12 major tech hubs in North America and Europe.  Hired is totally free for users and If you get a job you’ll get a $2,000 “thank you” bonus. If you use our <a href="https://hired.com/?utm_content=shownotes-4k&utm_medium=podcast&utm_source=podcastinit">special link</a> to signup, then that bonus will double to $4,000 when you accept a job. If you’re not looking for a job but know someone who is, you can refer them to Hired and get a $1,337 bonus when they accept a job.
</p>
</div>

<div class="well">
<a href="http://linode.com/podcastinit"><img src="/images/linode-banner-sponsor-large.png" alt="Linode Sponsor Banner"style="width: 100%;"></img></a><br/>
<p>Use the promo code <strong>podcastinit10</strong> to get a $10 credit when you sign up!</p>
</div>

### Interview with Kay Hayen
- Introductions
    - German, family with 2 kids, one cat
    - Working in ATM (Air Traffic Management), tracker product
    - Systems Engineer
    - Nuitka as a hobbyist
- How did you get introduced to Python?
    - Once was Perl "Guru".
    - Python was getting a lot of positive press
    - Team decision to want to use readable stuff
    - CPAN was still more complete, but Python was making inroads
- Can you describe how to pronounce the name of your project?
     - Wife Anna, Russian, Annuitka -> Nuitka
- Can you briefly describe what Nuitka is and what your motivation was for creating it?
    - I was thinking a fully integrated and compatible compiler should be possible.
    - Why is nobody doing it?
    - I can do it.
    - I am doing it.
    - Take Python beyond current use cases.
        - Everbody currently using Python needs no compiler, or wouldn't use it
        - Less need for time consuming C++/Python hybrid coding
        - Simple code should compile to fast code by default
        - Complex code should still work
- On the project web site it says that Nuitka does a lot of clever things after being fed a Python project. Can you provide some details as to what some of that cleverness is?
    - Re-formulations of Python into simpler Python
        - No "class"
        - No "assert"
        - No complex assignments
    - SSA tracing
        - Attaching uses to assignments properly
            - Despite try/finally
            - Loops
        - Avoids checks for known defined/undefined values
    - Function inlining (coming)
    - Constant propagation
    - Closure variable removal
- What is libpython and how is it used in both Nuitka and CPython?
    - Core of the Python interpreter
    - With Python VM and C interface
    - Nuitka can fall back to it
    - Avoiding it as often as we can, key to performance
- Is there any way to provide hints to Nuitka to generate more optimized output?
    - Nuitka is yet to make a difference based on type information
    - Not yet there, but coming soonish. SSA was pre-requisite
    - PEP 484 will be unreliable type information, mostly useless
    - I want type hints that are checked at Python run time
- What are some of the biggest challenges in generating statically compiled code from a language as dynamic as Python?
    - Python is compiled to .pyc files
    - Compatible Frame stack, cached
    - Exception handling of Python is terrible
    - CPython type system designed to be extensible
        - Extension types for functions, bound/unbound methods, generators, etc.
    - Many details to get right
- Are there any particular Python constructs that Nuitka is unable to translate and as a corollary to that is the compilation step lossy at all or do you have some way of ensuring that the functionality of the program remains unaltered?
    - Big point, no price attached
    - Except for not having bytecode, there is nothing missing
    - No pdb support
    - Edit / run cycle is not accelerated
    - That said: PyQt (integrated), PySide (available, unmerged), wxPython (available, maybe merged) needed patches to take compiled function/method objects for function objects too
- Are there any particular types of programs that benefit the most from Nuitka's compilation?
    - Bindings with ctypes of cffi compile into zero overhead C calls (planned)
    - Scientific programs are the most obvious goal (float type inference)
    - CPU bound or low latency programs
- Is it possible to feed an entire project with multiple modules into Nuitka all at once or is the standard use to perform compilation one source file or submodule at a time?
    - You give it the main program and it recurses imports according to "PYTHONPATH"
    - nuitka --recurse-all "/usr/bin/hg" supposed to work
    - Might have to give directories with program plug-ins
- I'm curious about what led you to choose compilation to C++ for Nuitka rather than making Nuitka an LLVM back end like Numba?
    - When I started Nuitka, I was using C++0x and variadic templates
    - Wanted to make a proof of concept that compatibility and integration is feasible
    - From there, code generation got less high level to goto ridden C
- How does Nuitka compare to projects like Numba or Cython?
    - Graceful degradation goal
    - Complete compatibility with Python whole stack
- How does Nuitka compare to PyPy? - Kay
    - PyPy is the coolest project ever
    - Pure Python goals shared
- How can users evaluate the performance of Nuitka - Kay
    - They currently cannot
    - Developing a tool to compare CPython and Nuitka runs
        - Based on vmprof from PyPy people
        - Identify parts of program where Nuitka is slower
        - Links to source code
    - To be done, help needed.
    - Nuitka is only starting to get to serious performance
        - Compatibility is such a high bar to take
        - C++ to C took a year (avoiding C++ exceptions)
        - SSA literally took forever

### Picks
- Tobias
    - [Forbidden Island](http://amzn.to/1MbCskV)
    - [Forbidden Desert](http://amzn.to/1MbCycj)
    - [Otto Project](https://ottoproject.io)
- Chris
    - [Grimm Super Symmetry](http://grimmales.com/supersymmetry/)
    - [Are You Listening To?: Boston](http://youarelistening.to/boston)
    - [Ripple](https://ripple.com/)
- Kay
    - [Learn being skeptic, Atheist Experience](http://www.atheist-experience.com/)
    - [MicroPython](https://micropython.org/)

### Keep In Touch
- [Nuitka Homepage](http://nuitka.net)
- [Google+](https://plus.google.com/+KayHayen)
- [Email](mailto:kay.hayen@gmail.com)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
