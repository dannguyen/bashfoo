
## Entries that need to be polished

Todos:
- figure out `output_md` feature...?

```yaml

"`youtube-dl` with -g/--get-url flag to extract actual URL of a video":
  date: 2021-08-03
  code: |
    youtube-dl -g 'https://twitter.com/ScottSeiss/status/1384517698307121153'

    # With YouTube URLs, the --get-url option will print URLs for the related "manifests",
    # and also the audio URL. To omit the former, use --youtube-skip-dash-manifest;
    # for the latter, use -f/--format to specify a video format
    youtube-dl -g --youtube-skip-dash-manifest 'https://www.youtube.com/watch?v=zDFP8Q69yhg' -f mp4


    ffmpeg -ss 10 -i $(youtube-dl -g --youtube-skip-dash-manifest 'https://www.youtube.com/watch?v=zDFP8Q69yhg' -f mp4) -t 1.4 parasite.gif
  output: |
    https://video.twimg.com/ext_tw_video/1384517264368623616/pu/vid/720x1280/x_lNPxc8WED_H5e6.mp4?tag=12

  output_md: |
    TKTK
```
