@powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
choco install teamviewer -fy
choco install filezilla -fy
choco install firefox -fy
choco install googlechrome -fy
choco install skype -fy
choco install thunderbird -fy
choco install adobereader -fy
choco install openoffice -fy
choco install libreoffice-fresh -fy
choco install notepadplusplus -fy
choco install gimp -fy
choco install vlc -fy
choco install adobereader -fy
choco install hpsupportassistant -fy
choco install openvpn -fy
choco install wget -fy
choco install python3 -fy
choco install cutepdf -fy

REM Python script
python LDAPmover.py
