
# bashfoo.yaml

[https://github.com/dannguyen/bashfoo](https://github.com/dannguyen/bashfoo)

Dan Nguyen's personally curated list of bash/command-line commands and snippets
  that are useful but yet he keeps forgetting


## TOC

- [`xargs` (BSD) to pipe results into another command, one at a time](#manifest--xargs-bsd-to-pipe-results-into-another-command-one-at-a-time)
- [`magick` convert image to favicon.ico](#manifest--magick-convert-image-to-favicon-ico)
- [calculate total kilobytes of hard disk space for files with given extension(s)](#manifest-calculate-total-kilobytes-of-hard-disk-space-for-files-with-given-extension-s-)
- [`printf` to stderr](#manifest--printf-to-stderr)
- [Stem filename, i.e. get filename sans path or extension](#manifest-stem-filename-i-e-get-filename-sans-path-or-extension)
- [`pkill` using a file pattern](#manifest--pkill-using-a-file-pattern)
- [`pgrep` and get all process info](#manifest--pgrep-and-get-all-process-info)
- [`tar` extraction, verbose](#manifest--tar-extraction-verbose)
- [`find` file by name](#manifest--find-file-by-name)
- [`find` directory name recursively](#manifest--find-directory-name-recursively)
- [`find` and execute command on each file](#manifest--find-and-execute-command-on-each-file)

------



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


<a name="manifest--magick-convert-image-to-favicon-ico" id="manifest--magick-convert-image-to-favicon-ico"></a>

### `magick` convert image to favicon.ico

```sh
# Example

magick /tmp/testimage.png -background none -resize 128x128 -density 128x128 favicon.ico
```

**Reference**: [Convert PNG to ICO](https://imagemagick.org/discourse-server/viewtopic.php?t=36031)


<a name="manifest-calculate-total-kilobytes-of-hard-disk-space-for-files-with-given-extension-s-" id="manifest-calculate-total-kilobytes-of-hard-disk-space-for-files-with-given-extension-s-"></a>

### calculate total kilobytes of hard disk space for files with given extension(s)

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


<a name="manifest-stem-filename-i-e-get-filename-sans-path-or-extension" id="manifest-stem-filename-i-e-get-filename-sans-path-or-extension"></a>

### Stem filename, i.e. get filename sans path or extension

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


<a name="manifest--tar-extraction-verbose" id="manifest--tar-extraction-verbose"></a>

### `tar` extraction, verbose

```sh
# Example

tar xzfv ARCHIVE.TAR.GZ
```

**Reference**: [The tar command explained](https://www.howtoforge.com/tutorial/linux-tar-command/)


<a name="manifest--find-file-by-name" id="manifest--find-file-by-name"></a>

### `find` file by name

```sh
# Example

find . -name "foo*"
```

**Reference**: [How can I recursively find all files in current and subfolders based on wildcard matching?](https://stackoverflow.com/questions/5905054/how-can-i-recursively-find-all-files-in-current-and-subfolders-based-on-wildcard)


<a name="manifest--find-directory-name-recursively" id="manifest--find-directory-name-recursively"></a>

### `find` directory name recursively

```sh
# Example

find START_DIR -type d -name "PATTERN"
```

**Reference**: [How can I recursively search for directory names with a particular string where the string is only part of the directory name](https://askubuntu.com/questions/153144/how-can-i-recursively-search-for-directory-names-with-a-particular-string-where)


<a name="manifest--find-and-execute-command-on-each-file" id="manifest--find-and-execute-command-on-each-file"></a>

### `find` and execute command on each file

```sh
# Example

find ./PATTERN -exec FOO BAR {} \;

find PlainText/*.md -exec wc -l {} \;
```

**Reference**: [How to run find -exec?](https://unix.stackexchange.com/questions/12902/how-to-run-find-exec)
