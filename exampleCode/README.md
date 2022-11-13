# What is this?
This folder contains an .srt file of a podcast episode of mine that I downloaded and transcribed using WhisperAI. I then used the cmd+f function to find a cussword in the audio file.
there are two cusswords but i focused on the first one since ffmpegs' amix function has certain limitations when attempting to run two audio filters that require muting. Put simply, amix will normalize the audio of all the audio files used in a given command instead of muting the predefined sections of audio. Given that fact, I decided to creat an MVP and simply perform the desired functions on one of the occurances of said cuss words.

# what code did you run?

```
ffmpeg -i Recording9.mp3 -af "volume=enable='between(t,1542.5,1544)':volume=0" r9Muted.mp3 && ffmpeg -i r9Muted.mp3 -i Censoredbeep.m4a -filter_complex "[0]adelay=0001|0001[s0];[1]adelay=1542500|1542500[s1]; [s0][s1]amix=2" -preset ultrafast -async 1 output.mp3
```

# What about everything else?
- The audio file titled "Recording9.mp3" is the original podcast episode.
- r9muted.mp3 is the output of the initial script that mutes the section of audio that we predefined as containing a cussword
- Censoredbeep.m4a is the sound effect were using to cover up the section 
that got muted
- output.mp3 is the final product

# What time in the audio file is the cuss word?
The first cussword is at the 25m42s mark.

# How did you convert the time into something that ffmpeg understands?
 

 
