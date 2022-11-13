# AudioCensor 🎵#️⃣
Censor portions of audio using ffmpeg

> 💡 This script is the  baseline for what will eventually become a tool for censoring out curse words in audio or video files. 


```
ffmpeg -i jbp.m4a -i Censoredbeep.m4a -filter_complex "[0]adelay=0001|0001[s0];[1]adelay=2000|2000[s1];[2]adelay=10000|10000[s2];[3]adelay=14250|14250[s3]; [s1][s2][s3][s4]amix=4" -preset ultrafast output.mp3
```

## Use cases
- The first use case I imagined was a tool that would automatically ingest an mp3 file from a podcast feed and perform all actions in the script to transcribe the audio, parse out all curse words, replace audio where curse words are present with a bleep.mp3 sound effect, and spit out the new mp3 with the title "censored_INPUT.mp3. The audio could then be reuploaded by the Podcaster to have as a non-explicit version of any episode. This could be useful for a podcast like Joe Rogan when he has an educator on the show but swear words are peppered througout as sentence enhancers but could benefit someone in a younger audience that wouldn't necessarily appreciate listening to swearing. 
- Another use case would be a teacher that wants to show an educational video that may have a swear word somewhere in an important portion of said video and the audience would again be in a younger, school environment.

# Go to the link below to see an example of the code in action
[Example Code README.md](https://claudchereji.github.io/AudioCensor/exampleCode/)

## Steps to build
-Build dictionary with list of all English swear words 

- learn whisperAI

- Transcribe with whisperAI

- reference swear words dictionary to filter out swear words 

- Get time codes for swear words with whisperAI 

- Save time codes to JSON file

- Overlay input mp3 with bleep.mp3 at every time code

- Export new mp3

## Future Features
1. Filter for levels of explicitness
  - G
  - Pg
  - Pg-13
  - R
  - Unrated

2. Multiple options for censored sound effects 

3. Custom censored sound effects

## Colaborations
> I could use some help setting a custom Jekyll theme cause I'm all thumbs with implementing that on the static site
🤷🏻‍♂️ +1


PLEASE HELP!! I'm a script kiddie and I'm just cobbling together random code I find on the internet and it's all CLI based. I want to streamline this and make it into either a webapp or something that can be launched on any PC with a simple pip install or GIT Clone. Any help is appreciated!
