What I want to to here
======================

I want to code a scheduler that
1. Based on a provided list of videos
2. With feed a play_video(item) one video at a time
3. When a video is playing in the player the next video should wait till it is finished.

Once that step is achieved, based on an interrupt from the server say on changes in the new playlist,
the scheduler should be fed as next the new playlist and start looping that from the beginning to the end.
