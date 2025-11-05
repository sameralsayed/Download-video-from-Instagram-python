from yt_dlp import YoutubeDL  # pip install yt-dlp

def download_instagram_video(url, output_path='./downloads'):
    """
    Download an Instagram video (best quality MP4).
    
    Args:
    url (str): Instagram video URL (e.g., 'https://www.instagram.com/p/POST_ID/' or Reel link).
    output_path (str): Directory to save the video (default: './downloads').
    
    Returns:
    dict: Info about the downloaded video if successful, None otherwise.
    """
    try:
        # Configure options for video download
        ydl_opts = {
            'format': 'best[ext=mp4]/best',  # Prefer MP4, fallback to best
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Output filename template
            'noplaylist': True,  # Download single video, not multiple
        }
        
        # Download the video
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f"Video downloaded successfully to {output_path}!")
        return ydl.extract_info(url, download=False)  # Return metadata
        
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None

# Example usage
if __name__ == "__main__":
    VIDEO_URL = "https://www.instagram.com/reel/ABC123def/"  # Replace with your public Instagram video URL
    download_instagram_video(VIDEO_URL)