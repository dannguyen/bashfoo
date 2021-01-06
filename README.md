
# bashfoo.yaml

[https://github.com/dannguyen/bashfoo](https://github.com/dannguyen/bashfoo)

Dan Nguyen's personally curated list of bash/command-line commands and snippets
  that are useful but yet he keeps forgetting


## TOC

- [`ffmpeg` encode .mkv video to .mp4](#manifest--ffmpeg-encode-mkv-video-to-mp4)
- [`find` and execute command on each file](#manifest--find-and-execute-command-on-each-file)
- [`find` directory name recursively](#manifest--find-directory-name-recursively)
- [`find` file by name](#manifest--find-file-by-name)
- [`magick` convert image to favicon.ico](#manifest--magick-convert-image-to-favicon-ico)
- [`pgrep` and get all process info](#manifest--pgrep-and-get-all-process-info)
- [`pkill` using a file pattern](#manifest--pkill-using-a-file-pattern)
- [`printf` to stderr](#manifest--printf-to-stderr)
- [`pygmentize` a code snippet into highlighted rich text that I can paste into GMail](#manifest--pygmentize-a-code-snippet-into-highlighted-rich-text-that-i-can-paste-into-gmail)
- [`rsync` the contents of one directory into another](#manifest--rsync-the-contents-of-one-directory-into-another)
- ['stem' a filename, i.e. get filename sans path or extension](#manifest--stem-a-filename-i-e-get-filename-sans-path-or-extension)
- [`tar` extraction, verbose](#manifest--tar-extraction-verbose)
- [`unzip` only an archive's CSV files and pipe to stdout](#manifest--unzip-only-an-archive-s-csv-files-and-pipe-to-stdout)
- [`xargs` (BSD) to pipe results into another command, one at a time](#manifest--xargs-bsd-to-pipe-results-into-another-command-one-at-a-time)
- [Calculate total kilobytes of hard disk space for files with given extension(s)](#manifest-calculate-total-kilobytes-of-hard-disk-space-for-files-with-given-extension-s-)
- [List the top 10 subdirectories in order of most recently modified](#manifest-list-the-top-10-subdirectories-in-order-of-most-recently-modified)






-------------------------------
<a name="manifest--ffmpeg-encode-mkv-video-to-mp4" id="manifest--ffmpeg-encode-mkv-video-to-mp4"></a>

### `ffmpeg` encode .mkv video to .mp4

```sh
# Example
ffmpeg -i input.mkv -acodec aac -vcodec libx264 output.mp4
```

**Reference**: [How can I convert an m4v video to a widely viewable format using ffmpeg?](https://superuser.com/a/462112/512499)


-------------------------------
<a name="manifest--find-and-execute-command-on-each-file" id="manifest--find-and-execute-command-on-each-file"></a>

### `find` and execute command on each file

```sh
# Example
find ./PATTERN -exec FOO BAR {} \;

find PlainText/*.md -exec wc -l {} \;
```

**Reference**: [How to run find -exec?](https://unix.stackexchange.com/questions/12902/how-to-run-find-exec)


-------------------------------
<a name="manifest--find-directory-name-recursively" id="manifest--find-directory-name-recursively"></a>

### `find` directory name recursively

```sh
# Example
find START_DIR -type d -name "PATTERN"
```

**Reference**: [How can I recursively search for directory names with a particular string where the string is only part of the directory name](https://askubuntu.com/questions/153144/how-can-i-recursively-search-for-directory-names-with-a-particular-string-where)


-------------------------------
<a name="manifest--find-file-by-name" id="manifest--find-file-by-name"></a>

### `find` file by name

```sh
# Example
find . -name "foo*"
```

**Reference**: [How can I recursively find all files in current and subfolders based on wildcard matching?](https://stackoverflow.com/questions/5905054/how-can-i-recursively-find-all-files-in-current-and-subfolders-based-on-wildcard)


-------------------------------
<a name="manifest--magick-convert-image-to-favicon-ico" id="manifest--magick-convert-image-to-favicon-ico"></a>

### `magick` convert image to favicon.ico

```sh
# Example
magick /tmp/testimage.png -background none -resize 128x128 -density 128x128 favicon.ico
```

**Reference**: [Convert PNG to ICO](https://imagemagick.org/discourse-server/viewtopic.php?t=36031)


-------------------------------
<a name="manifest--pgrep-and-get-all-process-info" id="manifest--pgrep-and-get-all-process-info"></a>

### `pgrep` and get all process info

```sh
# Example
# MacOS
pgrep -fil 'rails'

# Linux
pgrep -af 'rails'
```

Output:

```

47502 rails master RBENV_VERSION=2.5.1 TERMINAL_FONT=Monaco
47517 rails worker[0] RBENV_VERSION=2.5.1 TERMINAL_FONT=Monaco
```

**Reference**: [How to get pgrep to display full process info](https://serverfault.com/questions/77162/how-to-get-pgrep-to-display-full-process-info)


-------------------------------
<a name="manifest--pkill-using-a-file-pattern" id="manifest--pkill-using-a-file-pattern"></a>

### `pkill` using a file pattern

```sh
# Example
pkill -fil ipython
```

Output:

```
kill -15 90396
kill -15 90523
```

**Reference**: [How to kill all processes with a given partial name?](https://stackoverflow.com/questions/8987037/how-to-kill-all-processes-with-a-given-partial-name)


-------------------------------
<a name="manifest--printf-to-stderr" id="manifest--printf-to-stderr"></a>

### `printf` to stderr

```sh
# Example
>&2 printf 'Error: %s\n' 'There was a problem' 'And another problem'
```

Output:

```
Error: There was a problem
Error: And another problem
```

**Reference**: [print output to stderr, not stdout](https://stackoverflow.com/questions/2990414/echo-that-outputs-to-stderr)


-------------------------------
<a name="manifest--pygmentize-a-code-snippet-into-highlighted-rich-text-that-i-can-paste-into-gmail" id="manifest--pygmentize-a-code-snippet-into-highlighted-rich-text-that-i-can-paste-into-gmail"></a>

### `pygmentize` a code snippet into highlighted rich text that I can paste into GMail

```sh
# Example
printf "SELECT name, id\n FROM datatable AS tx WHERE id > 100\n ORDER BY id ASC;" \
  | pygmentize -f rtf -l sql -O style=solarized-light \
  | pbcopy
```

**Reference**: [Pygments Command Line Interface](https://pygments.org/docs/cmdline/)

**Notes**: 


- Use `-L` to list all styles, formatters, and lexers
- Use `-o` to output to file


-------------------------------
<a name="manifest--rsync-the-contents-of-one-directory-into-another" id="manifest--rsync-the-contents-of-one-directory-into-another"></a>

### `rsync` the contents of one directory into another

```sh
# Example
rsync -av src_dir/ target_dir
```

Output:

```
building file list ... done
created directory /target_dir
./
.gitignore
README.md
static/media/
static/media/demos/
static/media/demos/find.mp4

sent 452477 bytes  received 2378 bytes  50909710.00 bytes/sec
total size is 472016  speedup is 1.00
```

**Reference**: [How To Use Rsync to Sync Local and Remote Directories on a VPS](https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories-on-a-vps)

**Notes**: 


- only the source directory should have a trailing slash
- the `-v` flag makes for verbose output
- the `-n` flag does a dry run


-------------------------------
<a name="manifest--stem-a-filename-i-e-get-filename-sans-path-or-extension" id="manifest--stem-a-filename-i-e-get-filename-sans-path-or-extension"></a>

### 'stem' a filename, i.e. get filename sans path or extension

```sh
# Example
fullname=/tmp/hello/world.txt
newname="a_whole_new_$(basename ${fullname%.*})"
echo $newname
```

Output:

```
a_whole_new_world
```

**Reference**: [Extract filename and extension in Bash](https://stackoverflow.com/questions/965053/extract-filename-and-extension-in-bash)


-------------------------------
<a name="manifest--tar-extraction-verbose" id="manifest--tar-extraction-verbose"></a>

### `tar` extraction, verbose

```sh
# Example
tar xzfv ARCHIVE.TAR.GZ
```

**Reference**: [The tar command explained](https://www.howtoforge.com/tutorial/linux-tar-command/)


-------------------------------
<a name="manifest--unzip-only-an-archive-s-csv-files-and-pipe-to-stdout" id="manifest--unzip-only-an-archive-s-csv-files-and-pipe-to-stdout"></a>

### `unzip` only an archive's CSV files and pipe to stdout

```sh
# Example
unzip -p schools.zip "*.csv" > schools.csv
```


-------------------------------
<a name="manifest--xargs-bsd-to-pipe-results-into-another-command-one-at-a-time" id="manifest--xargs-bsd-to-pipe-results-into-another-command-one-at-a-time"></a>

### `xargs` (BSD) to pipe results into another command, one at a time

```sh
# Example
echo Alice Bob Charlie | xargs -I{} -n1 echo 'Hey, {} is a great name!'
```

Output:

```
Hey, Alice is a great name!
Hey, Bob is a great name!
Hey, Charlie is a great name!
```

**Reference**: [Execute a command once per line of piped input?](https://unix.stackexchange.com/questions/7558/execute-a-command-once-per-line-of-piped-input)


-------------------------------
<a name="manifest-calculate-total-kilobytes-of-hard-disk-space-for-files-with-given-extension-s-" id="manifest-calculate-total-kilobytes-of-hard-disk-space-for-files-with-given-extension-s-"></a>

### Calculate total kilobytes of hard disk space for files with given extension(s)

```sh
# Example
echo $(find . -type f \
        \( -iname "*.csv" -o -iname '*.xls*' \) \
        -printf "(%k/1024)+" \
        2>/dev/null; \
        echo 0;) | bc
```

Output:

```
15732
```

**Reference**: [Find the total size of certain files within a directory branch](https://unix.stackexchange.com/questions/41550/find-the-total-size-of-certain-files-within-a-directory-branch/148472)

**Notes**: 



- Requires the use of gnu-find (gfind on my MacOS)
- use `-printf "%s+"` to print size by bytes
- `2>/dev/null` hides error messages
- `-iname` is case-insensitive


-------------------------------
<a name="manifest-list-the-top-10-subdirectories-in-order-of-most-recently-modified" id="manifest-list-the-top-10-subdirectories-in-order-of-most-recently-modified"></a>

### List the top 10 subdirectories in order of most recently modified

```sh
# Example
find ~/a -mindepth 1 -maxdepth 2 -type d \
    -not -name '_*' -not -name '.*' \
    -print0
  | xargs -0 -n1 -I{} \
      stat  -f '%Sm %N' -t '%Y-%m-%d %H:%M:%S' {} \
  | sort -rn | head -n10

# GNU variant, e.g. with gnu-coretools on macOS
gfind . -mindepth 1 -maxdepth 2 -type d \
    -not -name '_*' -not -name '.*'  \
    -printf '%T+ %p\n'  \
  | sort -rn \
  | head -n 10
```

Output:

```
2020-11-27 14:05:45 /Users/dan/Downloads/r-book
2020-09-25 11:39:45 /Users/dan/Desktop/sf-shelter-data
2020-06-18 22:45:15 /Users/dan/Downloads/journalism-syllabi
2020-08-26 20:16:55 /Users/dan/Desktop/vocal-samples
2020-07-09 14:48:38 /Users/dan/Downloads/svelte-project
2020-07-09 14:29:43 /Users/dan/Desktop/matplotlibguide
2020-05-29 22:00:28 /Users/dan/Downloads/buzzfeed-archives
2020-03-18 14:57:03 /Users/dan/Downloads/transcribe-texts
2020-01-18 05:55:32 /Users/dan/Desktop/oldstuff
2020-01-17 16:43:39 /Users/dan/Desktop/random_images
```

**Reference**: [How to recursively find and list the latest modified files in a directory with subdirectories and times (my answer](https://stackoverflow.com/questions/5566310/how-to-recursively-find-and-list-the-latest-modified-files-in-a-directory-with-s/65588958#65588958)
