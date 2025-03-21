import yt_dlp


def check_url(url):
    print(url)
    if 'youtube.com/watch?v=' in url or 'youtu.be/' in url:
        return 'video'
    elif 'youtube.com/playlist?list=' in url:
        return 'playlist'
    elif 'youtube.com/@' in url:
        return 'channel'
    else:
        print("Error in URL")
        return 'error'

def youtube_video_url_cleaner(url):
    ret = ""
    for i in url:
        if i == '&':
            break
        ret += i
    return ret

def downloader(url, quality_choice, audio_only, subtitle, type):

    # Define options based on user selection
    ydl_opts = {
        'download_archive': 'downloaded_videos.txt'
    }

    if type == 'playlist':
        ydl_opts['outtmpl'] = '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s'
    elif type == 'channel':
        ydl_opts['outtmpl'] = '%(uploader)s/%(title)s.%(ext)s'
    else:
        ydl_opts['outtmpl'] = '%(title)s.%(ext)s'

    if audio_only == "y" or audio_only == "Y":
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]
        })
    else:
        # Video format with quality limit
        if quality_choice == "best":
            video_format = "bestvideo+bestaudio/best"
        else:
            video_format = f"bestvideo[height<={quality_choice}]+bestaudio/best"
        
        ydl_opts['format'] = video_format
        ydl_opts['merge_output_format'] = 'mp4'  # Ensure MP4 format

    # Download with yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_manager(url, quality_choice, audio_only, subtitle):
    if check_url(url) == 'video':
        url = youtube_video_url_cleaner(url)
        print('video: ', url)
        downloader(url, quality_choice, audio_only, subtitle, 'video')
    elif check_url(url) == 'playlist':
        print('playlist: ', url)
        downloader(url, quality_choice, audio_only, subtitle, 'playlist')
    elif check_url(url) == 'channel':
        print('channel: ', url)
        downloader(url, quality_choice, audio_only, subtitle, 'channel')
    else:
         print("Error unexpected")
    

url = input("Enter URL: ")
quality_choice = input("Enter max resolution: ")
audio_only = input("Audio only (y/n): ")
subtitle = input("Subtitle (y/n): ")
download_manager(url, quality_choice, audio_only, subtitle)
