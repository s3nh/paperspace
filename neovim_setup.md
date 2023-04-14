Because I always forgot how to install this shit. 
Tested on fresh Linux Mint desktop. 


```bash

curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim.appimage
chmod u+x nvim.appimage
./nvim.appimage

```


In case of ./nvim.appimage failed, then go straight to 


```bash
./nvim.appimage --appimage-extract
./squashfs-root/AppRun --version

# Optional: exposing nvim globally.
sudo mv squashfs-root /
sudo ln -s /squashfs-root/AppRun /usr/bin/nvim
nvim
```



