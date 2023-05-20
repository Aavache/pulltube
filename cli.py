import sys
import click
from pytube import YouTube
import exceptions


@click.command()
@click.argument('urls', type=str, nargs=-1)
@click.option('-p', '--save-path', help='Path where video will be saved', type=str,
              default='./', show_default=True)
@click.option('--only-audio', help='Only audio track', is_flag=True)
@click.option('-e', '--extension', help='File extension', type=str,
              default='mp4', show_default=True)
def cli(urls, save_path, only_audio, extension):
    """Pull a videos from YouTube"""

    if not len(urls):
        click.echo('URL is not provided')
        sys.exit(1)

    for url in urls:
        print(url)
        yt = YouTube(url)
        click.echo(f'Title of the video {yt.title}')

        if only_audio:
            streams = yt.streams.filter(only_audio=True)
            if not len(streams):
                raise exceptions.SteamNotFoundError
            steam = streams[0]
        else:
            streams = yt.streams.filter(file_extension=extension)
            if not len(streams):
                raise exceptions.SteamNotFoundError
            steam = streams[0]

        click.echo(f"Downloading {url}...")
        steam.download()


if __name__ == '__main__':
    cli()
