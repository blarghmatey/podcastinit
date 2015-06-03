Title: Episode 8 - Mark Baggett on Python's Role in Information Security
Date: 2015-05-28
Category: Episodes
Tags: InfoSec, Penetration Testing, Security,

### Brief Introduction
*  Date of recording - May 28th, 2015
*  Hosts - Tobias Macey and Chris Patti
*  Overview - Interview with Mark Bagett
*  Follow us on iTunes, Stitcher or TuneIn
*  Give us feedback! (iTunes, Twitter, email, Disqus comments)
*  You can donate (if you want)!

### Interview with Mark Bagett
*  Introductions
*  How were you first introduced to Python? - Chris
    *  Started using it for automating tasks while working as a sysadmin
    *  Found code that launched an attack on FTP server - in Python
*  What are some of the tasks in your job that you use Python for? -Tobias
    *  Trusted command & control backdoor for Windows
        *  Mostly not used by malware authors - thus far (at least Mark  hasn't seen it used that way)
        *  Flame virus - 5MB payload - incredibly advanced
            *  Lua interpreter bundled along with the scripts
        *  Vale framework - Python framework that takes payloads out of penetration testing executables
*  What is it about Python that makes it useful for penetration testing and other information security tasks?
    *  Same thing that makes it useful for anything else
    *  mpacket from core security
*  What are some of the more useful Python penetration testing tools?
    *  OFFENSE
        *  [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)
        *  [scapy](http://www.secdev.org/projects/scapy/)
        *  [Volatility](https://code.google.com/p/volatility/)
    *  DEFENSE
        *  [Counter dictionary from collections](https://docs.python.org/2/library/collections.html#collections.Counter)
        *  Pandas
        *  iPython
        *  matplotlib
*  We've noticed that a lot of the literature around information security and penetration testing focuses on targeting Windows. Can you enlighten us as to why that is?
    *  Windows event tracing
        *  logman
        *  event trace providers - implement packet sniffing (Can turn every browser into a key logger)
    *  Primary attack surface - Where most attacks are targeted
    *  Fewer purely Linux systems
        *  Very few ports open - maybe 80, 22
        *  Very likely no user just sitting there waiting to run an executable you send
    *  More freedom on Linux - less formalized patching process, more variable tools = more exploits
    *  Will write code to only use built in modules for Python that will run in customer target environments
*  What are some of the legal considerations that you have to deal with on a regular basis as a penetration tester?
*  There have recently been a number of attacks based on hijacking the TCP/IP stack. Is Python being used for any of these exploits or tools to defend against them?
    *  Data analytics
    *  Detect repeated sequence numbers - Man in the Middle Attack
        *  As simple as 5 lines of Python code
        *  import scapy, start sniffing packets, pull together all packets - make list of associated packets
        *  Can pull together all packets inside of stream
        *  Time spefic source communicates with specific destination
        *  Bro - intrusion detection suite
            * Built into Security Onion - Doug Berks
            * FLOSS Weekly episode 296 with [Bro developers](http://twit.tv/show/floss-weekly/296)
*  What are some activities that you do on a regular basis for which you would turn to another language or toolchain, rather than using Python?
    *  Powershell - The Python of windows
        *  Whitelisted and ubiquitous
    *  Password cracking - compiled language like C or assembly
* For anyone who is interested in getting involved in the security industry, and penetration testing in particular, what resources or tools would you recommend?
    *  Developers make the best InfoSec professionals
        *  Lots of jobs and opportunities
    *  Developer -\> Systems Administration -\> Information Security
    *  Security conferences - BSides, Defcon, Black Hat
    *  Online capture the flag challenges (google it) - good practice for critical thinking and using code for security exercises
    *  Get involved in the industry - Meetups, etc.
    *  SANS institute course, Python for Penetration Testers, SEC573 by  Mark Baggett - sans.org
    *  Lots of free online resources
    *  [Violent Python](http://shop.oreilly.com/product/978159749957*do)
    *  [PicoCTF](https://picoctf.com/)
    *  [Counter Hack Challenges](https://www.counterhackchallenges.com/)

### Picks
*  Tobias
    *  [Authy](https://www.authy.com/)
    *  [OpenWRT](https://openwrt.org/)
    *  [TP-Link Archer C7](http://amzn.to/1FR46Ac)
    *  [Schemas For The Real World by Carina C. Zona](https://www.youtube.com/watch?v=PYYfVqtcWQY)
    *  [The Soul of Software by Avdi Grimm](https://youtu.be/IgbHzFb1hGw)
    *  [China Mieville](http://en.wikipedia.org/wiki/China\_Mi%C3%A9ville)
*  Chris
    *  [Rapscallion Munich Dark](http://www.beeradvocate.com/beer/profile/18639/121363/)
    *  [Write](http://writeapp.net/mac/)
    *  [Marginal Way](http://marginalwayfund.org/)
    *  [Frankie and Johnny's](http://frankie-johnnys.com/)
    *  [pyenv](https://github.com/yyuu/pyenv)
*  Mark Bagett
    *  [Corelabs impacket](http://corelabs.coresecurity.com/index.php?module=Wiki&action=view&type=tool&name=Impacket)
    *  [Google Labs - Rekall](http://www.rekall-forensic.com/)
    *  [Adams peanut butter cup fudge ripple cheesecake](http://www.thecheesecakefactory.com/menu/desserts/cheesecakes/adams-peanut-butter-cup-fudge-ripple-cheesecake/)
    *  [BSides security conference](http://www.securitybsides.com/w/page/12194156/FrontPage)

### Keep in Touch
*  Twitter: [@markbaggett](https://twitter.com/markbaggett)
*  [In Depth Defense](http://www.indepthdefense.com/)

The intro and outro music is from Requiem for a Fish [The Freak Fandango Orchestra](http://freemusicarchive.org/music/The_Freak_Fandango_Orchestra/)  / [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)
