Title: Episode 6 - Jonathan Slenders Talks About Prompt Toolkit
Date: 2015-05-17
Category: Episodes
Tags: prompt-toolkit, ptpython, command line, readline, open source

<iframe id="audio_iframe" src="http://www.podbean.com/media/player/5xs8w-561e18?from=wp&skin=103&postId=5643800&download=0&share=1&fonts=Helvetica&auto=0" height="100" width="100%" frameborder="0" scrolling="no" data-name="pb-iframe-player"></iframe>

#Brief Introduction
- Date of recording - May 17th, 2015
- Hosts - Tobias Macey and Chris Patti
- Follow us on iTunes, Stitcher or TuneIn
- Give us feedback! (iTunes, Twitter, email, Disqus comments)
- Overview - Interview with Jonathan Slenders
#Interview with Jonathan Slenders
- Introductions
- How were you first introduced to Python? -Chris
- What inspired you to create the python-prompt-toolkit?
- What are some design considerations that you made when building prompt-toolkit?
    - Make minimal use of inheritance
        - Overly strong coupling
        - Better clarity for the API of your library
        - Completely event driven / asynchronous
        - No global state
    - ptpython completion benefits from asynchrony - The jedi completion library is too slow - completion happens in its own thread
- You have built a number of projects that use the prompt-toolkit as a core component, did you have them in mind from the beginning, or are they experiments to test the capabilities of the toolkit?
    - tmux rewrite in Python, abandoned, original motivation for prompt-toolkit
    - [ptpython](https://github.com/jonathanslenders/ptpython)
    - [pgcli](https://github.com/dbcli/pgcli)
    - [ptpdb](https://github.com/jonathanslenders/ptpdb)
    - [pyvim](https://github.com/jonathanslenders/pyvim)
- Do you intend to bring PyVim to feature parity with Vim, or is it just intended for experimentation?
    - Short answer: Don't know - but will probably never be in full parity with Vim
- What inspired you to create ptpython and why did you choose to make it a stand-along project rather than extending iPython?
- How difficult was it to integrate with IPython and what were the benefits?
    - IPython has its own event loop - this presented difficulties as prompt-toolkit has its own as well
- What are some of the most interesting uses that you have seen of the prompt-toolkit?
    - PyVim - really challenged the design
    - pgcli
#Picks
- Tobias
    - [vimsert](https://github.com/gabesullice/vimsert)
    - [Johnny Cash Project](http://www.thejohnnycashproject.com/)
    - [Interstellar](http://www.imdb.com/title/tt0816692/)
- Chris
    - [Grimm Telekinesis](http://grimmales.com/telekinesis/)
    - [pandoc](http://pandoc.org/)
    - [vimpager](https://github.com/rkitover/vimpager)
    - [Homebrew Cask](https://github.com/caskroom/homebrew-cask)
- Jonathan Slenders
    - Belgian Beer
      - Rochefort
    - Western European Folk Dancing
#Keep in touch
- Twitter - [@jonathan\_s](https://twitter.com/jonathan\_s)
- GitHub - [jonathanslenders](https://github.com/jonathanslenders)
