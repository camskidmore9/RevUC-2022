# RevUC-2022
Repository for RevolutionUC 2022 Hackathon. Collaboration with Bolt-Lyd


This was supposed to end up as a Discord bot to control and implement Spotify directly into Discord however, we could not find a way to make the audio stream into voice channels.

What we accomplished in the 24 hours:
 -Create a Python based Discord bot
 -Give bot ability to perform reactive text tasks in Discord
 -Allow bot to join Discord voice channel and play local files
 -Understand the Spotify API and learn how to allow a python program to access your spotify account and control what music is being listened to through various commands
 -Create a python program that takes in user input, finds the relevant song they wanted, and play it on your Spotify account on whatever device Spotify is playing on
 -Play, queue, skip, pause, and play spotify audio all through python program

What was not finished in 24 hours:
 -Finding a way to actively stream Spotify audio through Discord voice channels
 -Implement Spotify controls into the Discord bot (This would be quite simple to accomplish, we just spent a large amount of time trying to solve the streaming problem and did not focus on this)
 
Next steps/ideas:
 -Implement the spotify controls into the discord bot
 -Solve the streaming problem:
  
*Ideas for solving the streaming problem*:    
IDEA 1:
    -Create a React server that acts as a web player which Spotifys web sdk can easily stream the music on. Have this run in the same local file as the source code for the bot itself.
    -Find a way to pipe this audio from the React page into the bot to create a streaming environment. This could be accomplished by treating the bot as a live mic and allowing it to "talk" in the channel as the spotify stream
    
IDEA 2:
    -Create a second bot that is a regular Spotify user account that takes in spotify audio as its mic and have that output the audio to the voice channel.
    -This would require users to have both the control bot and the streaming bot in their server.
    -Discord bot sends commands to the "user" streaming bot for when to join. If this cannot be accomplished on one device, a Raspberry Pi could be used to run the spotify part of the code.
 
What we tried that didn't work:
  -Use a live capturing audio software in Python to capture and save audio in tiny mp3 fragments
  -Save this audio as the same mp3 file, overwriting it every time
  -Have the discord bot running simaultaneously to play that single mp3 file in a while loop and stream that audio
  -This worked (kinds) you would only get audio in bits and not an actual stream so it was just clipping horribly and was not an effective solution
For more informaiton about our Hackathon submission, please visit: https://devpost.com/software/rick-the-discord-bot

  ~Cam
