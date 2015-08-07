Title: Episode 16 - Holger Krekel on Pytest
url: holger-krekel-pytest.html
save_as: holger-krekel-pytest.html
Date: 2015-07-08
Category: Episodes
Tags: testing, tools, packaging, deployment

### Summary
In this episode we talked to Holger Krekel about the py.test library. We discussed the various styles of testing that it supports, the plugin system and how it compares to the unittest library. We also reviewed some of the challenges around packaging and releasing Python software and our thoughts on some ways that they can be improved.

<iframe id="audio_iframe" src="http://www.podbean.com/media/player/hyqam-578c2d?from=wp&skin=103&postId=5737517&download=1&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

### Brief Introduction
- Welcome to Podcast.\_\_init\_\_ the podcast about Python and the people who make it great
- Date of recording - July 8th, 2015
- Hosts Tobias Macey and Chris Patti
- Follow us on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Stitcher](http://www.stitcher.com/s?fid=64838&refid=stpr) or [TuneIn](http://tunein.com/radio/Podcast\_\_init\_\_-p726240/)
- Give us feedback on [iTunes](https://itunes.apple.com/us/podcast/podcast.-init/id981834425?mt=2&uo=6&at=&ct=), [Twitter](https://twitter.com/Podcast__init__), [email](mailto:hosts@podcastinit.com) or [Disqus](http://podcastinit.com)
- We donate our time to you because we love Python and its community. If you would like to return the favor you can send us a [donation](\url{http://podcastinit.com/our-plans-for-your-donations.html)}. Everything that we don't spend on producing the show will be donated to the PSF to keep the community alive.
- Overview - Interview with Holger Krekel about his work on Pytest

### Interview with Holger Krekel
- Introductions
    - Programming for 25 years
    - Runs a consultancy
    - Been to almost every EuroPyCon and PyCon US
- How did you get introduced to Python? - Chris
    - Wanted to write an HTTP proxy and Java I/O was too confusing. Jython took less than a day to get it working after 2-3 days on it with Java.
- What inspired you to create Pytest, and how did the existing unittest framework play into the story?
    - Introduced to agile methods through the Zope community
    - Zope used unittest - didn't like the boiler plate
    - Not in the spirit of Python
    - Only took ~200 lines of code to get a testing tool working
    - Original name was 'utest' - 2003
    - Pytest name came in 2004 on [Pypy project](http://pypy.org/)
    - Huge number of tests on that project (20,000) - distributed test runner - xdist helped solve this.
- There are many different styles of testing, such as BDD, unit testing, integration testing, functional testing, what attributes of py.test make it suitable or unsuitable for these different approaches?
    - What are your views on black box testing and how would someone use py.test to implement this approach?
        - Pytest's plugin architecture enables you to hook into the various phases of test execution enabling you to extend Pytest in all kinds of ways beyond the original design.
    - I have been hearing a lot about property based testing which was popularized by the Quickcheck module in Haskell. Does py.test support anything like that?
        - [hypothesis-pytest](https://pypi.python.org/pypi/hypothesis-pytest/0.11.0)
- Do you think the characteristics and nature of the unit testing framework being used have any effect on the number and quality of the tests developers write?
    - Developers find writing tests in Pytest to be fun compared to unittest
    - Which will help people write better tests
    - Encourages refactoring
- Is there ever a time when you would advice \_against\_ writing tests?
    - When exploring a problem, writing tests first doesn't make sense
    - When getting feedback on a potential approach, writing tests first can be a waste of time
- What are some signs that you watch out for when writing tests that tell you that a particular feature needs to be refactored?
    - When the test code is fragile it should be refactored
    - Requires experience to really understand when to refactor
    - When it's not fun anymore or the tests are repetitive
- For someone who is converting their existing unit tests from UnitTest/Nose style to use py.test in an idiomatic manner, what are some of the biggest differences to be aware of?
    - Generator/yield based testing should move to property based testing
    - If py.test can't run a UnitTest/Nose style test it is considered a bug and gets fixed
- Has the strict backwards compatibility policy presented any interesting technical challenges thus far?
    - Yes it definitely makes more work
    - However breaking the API in a large project like this will cause too many problems for users
- py.test supports execution of tests written with other frameworks, how much ongoing maintenance does this feature require as changes are made to the other implementations?
- The web page says that Pytest is designed to work with domain specific and non Python tests, and in fact a coworker is using it to test a node.js project - how did Pytest's design enable this?
    - Pytest uses a collection tree model to represent your project
        - This is not Python specific
        - All classes and functions are just mapped into this tree, not directly on the Python function
    - There are few Python specific hooks for fixtures etc.
    - People have written plugins so they can express their tests in YAML, Microsoft Excel
    - Tests are represented as items
    - All plugins are written in Python
- What are some of the most interesting applications of py.test that you have seen?
    - Plugins!
        - Pytest-BDD
        - Pytest-C++
        - Pytest-sugar
    - [Py.test plugin list](http://pytest.org/latest/plugins\_index/index.html)
- Speaking about adoption, do you have any sense of the relative adoption of Pytest versus unitest or other tools?
    - Very hard to actually know
    - Download numbers are not a clear indicator due to robots, CI systems, etc.
    - Quantifying market share is hard to do
    - Popularity is not a useful heuristic in determining a good fot for technology adoption
        - But popularity is an indicator for the level of support you might receive
        - Tech can be popular but very poorly maintained
- Are there any features of py.test that would make it suitable for use with configuration management tools and infrastructure testing?
    - Example driven testing
    - Run py.test from a blackbox approach
    - Largest benefit would be from having one testing tool used across the organization
- Where do you see Pytest and more generally test frameworks headed in the future?
    - No big changes for Pytest - lots of incremental things
    - Plugins will add functionality
    - Holger is also the author of [Tox](https://bitbucket.org/hpk42/tox)
    - Integration testing and testing in more complex environments are a direction that test management tools will likely go
    - Tools like Jenkins can be a real headache in trying to have a good testing story for your company
    - <https://devpi.net/hpk/dev/devpi-server/2.2.0/+toxresults/devpi-server-2.2.0.tar.gz>
- Any questions we didn't ask?
    - Pytest is a very healthy project! There are 10 regular contributors - this is exceptional among OSS projects

### Picks
- Tobias
    - [python-future](http://python-future.org)
    - [six](http://pythonhosted.org/six/)
    - [The Way Back](http://www.imdb.com/title/tt1023114/?ref\_=nv\_sr\_1)
    - [Rosewill BK-500A](http://amzn.to/1J42d0M)} or [BK-500i](\url{http://amzn.to/1LRZfl6)
    - [pipdeptree](https://github.com/naiquevin/pipdeptree)
    - [pundler](https://github.com/steder/pundler)
- Chris
    - [Crop Bavarian Weizen](https://untappd.com/b/crop-bistro-and-brewery-bavarian-weizen/330954)
    - [Dutch Pancakes](https://en.wikipedia.org/wiki/Pannekoek)
    - [Prophet](http://comicsalliance.com/prophet-the-barbarian-space-opera-you-should-already-be-readi/)
- Holger
    - [The Utopia of Rules](http://amzn.to/1fnhVgt)
    - [IPFS.io](http://ipfs.io/) - The interplanetary file system
    - [A New Way to Look at Networking](https://www.youtube.com/watch?v=oCZMoY3q2uM)

### Keep In Touch
- [Twitter](https://twitter.com/hpk42)
- [Blog](http://holgerkrekel.net)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
