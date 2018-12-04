# Simple commits reports

## Install

Download into your home/bin directory and add execution permissions
`wget -O ~/bin/commits https://raw.githubusercontent.com/fmgarate/commits/master/commits.py`
`chmod +x ~/bin/commits`

## Usage

`commits [-h] [-p PATH] [-d DATE] [-a AUTHOR]`

## Optional arguments

-h, --help: show a help message and exit
-p PATH, --path PATH: run as if git was started in PATH instead of the current working directory
-d DATE, --date DATE: filter commits for DATE
-a AUTHOR, --author AUTHOR: filter commits by AUTHOR

## Examples

Today's commits from current directory
`commits`

Today's commits from a specific directory
`commits --path ~/src/myapp`

Commits from a specific directory and date
`commits --path ~/src/myapp --date 2018-10-10`

Commits from a specific directory, date and author
`commits --path ~/src/myapp --date 2018-10-10 --author john`

Using shot options
`commits -p ~/src/myapp -d 2018-10-10 -a john`
`commits -p ~/src/myapp`
`commits -p ~/src/myapp -d 2018-10-10`
