"""
    Created By  : itsparser
    Created On  : 25/01/22
"""
from datetime import datetime


def process():
    start = datetime.now()
    import ffmpeg
    ffmpeg.input('out720from4k.mp4').output('out320from720.mp4', vf="scale=-1:320").run()
    # out, err = (
    #     ffmpeg.input('input.mp4').output('out.mp4', **{'qscale:v': 3}).run()
    # )
    # return out
    # stream = ffmpeg.input('input.mp4')
    # stream = ffmpeg.hflip(stream)
    # stream = ffmpeg.output(stream, 'output.mp4')
    # ffmpeg.run(stream)
    end = datetime.now()
    print(f"start - {start}, end - {end}, diff - {end - start}")


if __name__ == '__main__':
    process()
