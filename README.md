# GDBrowserPy
A simple library for user GDBrowsers API!
## Importing
```python
from GDBrowserPy import GD
```
## Level Object
```python
from GDBrowserPy import GD

level = GD.Level(id=128,download=False)

level.name # Get name of Level
level.id # Get id of Level
level.description # Get description of Level
level.author # Get author of Level
level.playerID # Get playerID of Author
level.accountID # Get accountID of Author
level.difficulty # Get difficulty of Level
level.downloads # Get downloads of Level
level.likes # Get likes of Level
level.disliked # Get disliked of Level
level.length # Get length of Level
level.stars # Get stars of Level
level.orbs # Get orbs of Level
level.diamonds # Get diamonds of Level
level.featured # Get featured of Level
level.epic # Get epic of Level
level.gameVersion # Get gameVersion of Level
level.editorTime # Get editorTime of Level
level.totalEditorTime # Get totalEditorTime of Level
level.version # Get version of Level
level.copiedID # Get copiedID of Level
level.twoPlayer # Get if Level is twoPlayer
level.officialSong # Get officialSong of Level (0 if it's an Custom Song)
level.customSong # Get customSong of Level (0 if it's an Official Song)
level.coins # Get coins of Level
level.verifiedCoins # Get verifiedCoins of Level
level.starsRequested # Get starsRequested of Level
level.ldm # Get if Level has ldm 
level.objects # Get object count of Level
level.large # Get if Level is large
level.cp # Get cp of Level
level.difficultyFace # Get difficultyFace of Level
level.songName # Get songName of Level
level.songAuthor # Get songAuthor of Level
level.songSize # Get songSize of Level
level.songID # Get songID of Level

level.leaderboard(count=100,weekly=False) # Returns Level Leaderboard. 
# count is the amount leaderboard players to get. 
# weekly is weather to get the weekly leaderboard or not
level.like(username="username",password="password") # Like the level
```

