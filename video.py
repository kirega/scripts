
import subprocess
import os
import ffmpeg
# file  = "/home/kirega/Documents/Projects/proxertise/ad/2018/07/26/Ariana_Grande_-_No_Tears_Left_To_Cry-ffxKSjUwKdU.mp4"
# def getLength(filename):
#     # result = subprocess.Popen(['ffmpeg','-i' ,file, '-f', 'null'],
#     #  stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell=True)

#     result = subprocess.Popen(['ffmpeg','-i',file,'-f', 'null','-o','/file.txt'])
#     # return [x for x in result.stdout.readlines() if "Duration" in x]
#     # os.ffmpeg()
#     return result


# getLength(file)

file = '/home/kirega/Pictures/Screenshot from 2018-07-16 11-07-03.png'
file1 = '/home/kirega/Music/Ella Henderson - Missed (Official Studio Version) Lyrics on Screen [Full Length] New-yA5Z39aB8PI.mp4'
time = '15'
# ffmpeg -loop 1 -i image.png -c:v libx264 -t 15 -pix_fmt yuv420p -vf scale=320:240 out.mp4

# def make_video(file,time):
#     subprocess.Popen(['ffmpeg','-loop','1','-i',file,'-c:v', 'libx264','-t',time,'-pix_fmt','yuv420p','-vf','scale=1280:1024','-y','out.mp4'])

# # make_video(file,time)#
# time=time + '.mp4'
# print(time)

# probe = ffmpeg.probe(file1)
# video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
# width = int(video_stream['width'])
# height = int(video_stream['height'])
file3 = 'http://localhost:8000/media/ad/Demi_Lovato_-_Sober_Lyrics-A-_9VonfUko_XeeEMYY.mp4'
out_string = 'other6.jpg'
ffmpeg.input(file3, ss=time) \
.filter('scale', 300, -1) \
.output(out_string, vframes=1) \
.run()
