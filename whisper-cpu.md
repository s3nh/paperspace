%%bash
sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
source run.sh
git clone https://github.com/MiscellaneousStuff/openai-whisper-cpu.git
cd openai-whisper-cpu/
git submodule init
git submodule update
%%bash
yt-dlp   https://www.youtube.com/watch?v=HXbhS9bevqU -x --audio-format "mp3"
pip install -e whisper
