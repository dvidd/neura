# Pandora     

This is a projec made in summer of 2019, I put around 20 arounds into it while playing with a EEG that i made with some sensor that i bought, the propouse of the projects was making a open source devices that take the brain waves and picks in a graf and detect patrons.
If you want to contribute feel free to do it. :) 

Example uses :
  - If user with interface concentrate into something twice in a period of 2 seconds, a function is activate like : pause music

<img src="https://neura8.github.io/images/1photo.png">

## Brain waves 
I try to center in brain waves BETA and ALPHA <a href="https://en.wikipedia.org/wiki/Morse_code"> morse </a>

<img src="https://www.paranormal-explore.com/images/brain-waves.png">


<dl>
  <dt>Diferents brain waves</dt>

</dl>

Directory structure
------
    .
    ├── assets              # Utility for UI and desing 
    ├── desing              # 3d models for the pandora
    ├── docs                # Docs for the pandora
    ├── headset             # Scripts for parser the data from the headset
    ├── patrons             # Libary of patrons and examples
    ├── server              # Server for the pandora and W3RY
    └── controls            # Controls of the pandora to the iot
        ├── bluetooth       # Controls of server to conection
        ├── chromecast      # Allows communication with the chromecast
        ├── testing         # Testing stuff and playgrounds
        ├── controls.py     # Main file of the hardware of the pandora
     


Database conect to the pandoras with each info

## Hardware of pandora

<img src="https://github.com/neura8/pandora/blob/master/assets/pandora.png?raw=true">


# TODO

Make a model that get some kind of patrons from the brain waves, add an interface to add new reactive patrons, selct function to the patrons and make more functions.



## Patrons Pandora

| Patrons made  | Developing    | Future  |  2.0 |
| ------------- | ------------- |---------| -----|
| Conect to device  | Get calls | Alpha waves | Precise patrons |
| Controls of audio in device  | Controls of pause and continue  | Next / before | 
| Chromecats control | Volume control  | IOT Plug



### Licence 

<img src="http://seawisphunter.com/minibuffer/api/MIT-License-transparent.png">

MIT Licence - Neura8 2019
