Title: Project Sword Devlog: First Thoughts
Date: 2022-02-28 10:20
status: published
Category: Wordz
Tags: devlog, project-sword, project-sword-devlog
Slug: sword-update-01
Authors: josh
Summary: A public declaration of "I'm making a game, deh"
showkofi: false

My first _serious_ foray into game development is underway. I'm developing a small
topdown action game that will feel like an old action RPG - e.g. Secret of Evermore -
with minimal combat. It's inspired by this tweet:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">NYE parties are both wackand dangerous rn. So<br><br>On New Years Eve, everyone write down a mythical weapon they want to wield in 2022. Create the legend behind it, what it looks like, what power it possesses, etc<br><br>Then, tomorrow, you start your 365 day quest to find or forge it.</p>&mdash; 🎃Aaron Catano-Saez🇵🇷 (@AaronCatanoSaez) <a href="https://twitter.com/AaronCatanoSaez/status/1476909963217969163?ref_src=twsrc%5Etfw">December 31, 2021</a></blockquote>

It's light in scope - more of a learning experiment than a full game, but it will
have a story and some combat and some weird stuff in it. It's got a sword in it. Hence... Project Sword.

My tech stack is as follows:

- Unity - as an engine with the following packages
    - Ink Unity Integration
    - Auto Importer for Aseprite Pro
    - ScriptableObjects-Architechture
- VS Code - as C# editor
- [Aseprite](https://www.aseprite.org/) - for all pixel art assets & animation
- [Inky](https://github.com/inkle/inky) - for editing [Ink Dialogues](https://www.inklestudios.com/ink/)

Rather than take a programming heavy approach, I'm trying _really hard_ to keep
things decoupled and pass around events and make use of ScriptableObjects. To this
end, I've aleady coded some pretty cool things, including:

- ScriptableObject World Variables
- A WorldVariable Manager to save / load world variable configurations
- A ScriptableObject Condition system, allowing you to create logical statements
    involving the state of the world / the player's inventory / etc. to drive
    other behavior (e.g. a locked door that only opens if the player has a key or
    has passed some other milestone)

I'll share how I've implemented each idea in future tutorials. I've got a huge list
of things I want to talk about and I'm hoping that I'm not talking into the void.
That's okay too, though!
