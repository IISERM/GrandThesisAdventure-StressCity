# GTA - Stress City

The game binaries can be found on the [website for the game](https://iiserm.github.io/GTA-Stress-City). This repository is only for posterity.


This is a Virtual Treasure Hunt game hosted by the Turing Club, made using a custom terminal-based engine, [Tetra](https://github.com/DhruvaSambrani/turing-hunt-engine).

# Objectives

## Primary

- [X] Build the world with maps of all areas
    - [X] Link maps via transitions
    - [ ] ~~Make mini-map tool to see current location relative to the entire world~~
- [X] Collate a list of clue-essential items
    - [X] Create media files for clue items
    - [X] Code the behaviour and location of items
- [X] Sample playtest to debug

## Secondary 

- [X] Collate a list of non-essential fluff (world-building) items/NPCs
    - [X] Code the behaviour and location of items
- [ ] ~~Bug [Dhruva](https://github.com/DhruvaSambrani) to implement save states~~

## Misc. - not sure if necessary

- [ ] ~~Implement diagonal player movement~~

# Developing

1. Clone this repo and [Tetra](https://github.com/DhruvaSambrani/turing-hunt-engine) as sibling directories.
2. cd into this repo
3. Run `sh make` for linux/mac. For windows, read `./make` and follow the same steps.
4. Run `./dist/main-$(ldd --version)`
