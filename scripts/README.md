# scripts

### I keep all my scripts as executable files in a `.scripts` folder that I've added to my Path. If you use them; you may need to tinker.
<br>

**column-checker**: A script I built to find any columns in a SQL database that are reserved keywords. I used this when migrating
a database from MySQL 5 to MySQL 8 to find which areas of the codebase could possibly be referencing a reserved keyword without
proper mitigation and crashing the application. It uses a SQL backup of the database to determine which columns are reserved.
If you need this for something simliar; you can use the `sql_file` variable to point to your SQL backup and may need to look
at the `re.compile` and `line.strip` to ensure it follows the patterning of your SQL backup file.
<br><br>

**youtube-downloader**: Script that uses the `yt-dlp` library to download videos from YouTube. It downloads the highest video
resolution the video has to an .MP4 file. It also supports just downloading the audio to an .MP3 file. The `--output` flag allows you 
to choose what to name the file. Use it to download tech stuff, memes, or both - _the primeagen_. No warranty explicit or implied. Use
at your own risk. I take no responsibility if used for nefarious purposes. These are not the droids you are looking for.
<br><br>