# PullTube
Sometimes I am lazy and I need to quickly download videos from YouTube from the terminal. This repository does exaclty that...a simple
terminal CLI-based app. I utilize python and `pytube` library to download the videos

# Installation

```sh
git clone https://github.com/Aavache/pulltube.git
cd pulltube
pip install .
```

# Download a video

1. Get the video link!, in order to get the correct URL, click the button `share` below the video and copy the link.

2. Go to your terminal and pull the video with the following command. Feel free to add multiple videos. Don't forget to wrap the URL with quotes as there could be special characters.

```sh
pulltube 'http://youtube.com/watch?v=9bZkp7q19f0'
```

# Download only the audio
```sh
pulltube --only-audio 'http://youtube.com/watch?v=9bZkp7q19f0'
```

# Checkout available options

```sh
$ pulltube --help

Usage: pulltube [OPTIONS] [URLS]...

  Pull a videos from YouTube

Options:
  -p, --save-path TEXT  Path where video will be saved  [default: ./]
  --only-audio          Only audio track
  -e, --extension TEXT  File extension  [default: mp4]
  --help                Show this message and exit.
```

# Create issues
Feel free to create issues or contribute!
