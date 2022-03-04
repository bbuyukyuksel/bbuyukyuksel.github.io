### [Xmrig on Raspberrypi OS 32-bit](https://www.raspberrypi.org/forums/viewtopic.php?t=305983#p1830626)

https://www.raspberrypi.org/forums/viewtopic.php?p=1830626&sid=7ab25f40ff77140d374b5131b61f371c#p1830626)

Steps to install Xmrig XMR miner on your raspberypi OS 32-bit.

\1. sudo apt update && sudo apt full-upgrade
\2. sudo apt-get clean
\3. sudo shutdown -r now (system will reboot)
\4. sudo apt-get install -y raspbian-nspawn-64
\5. ds64-shell
\6. sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
\7. git clone https://github.com/xmrig/xmrig.git
\8. cd xmrig
\9. mkdir build
\10. cd build
\11. cmake ..
\12. make

This process will take some time so please be paitent. Once completed visit https://xmrig.com/wizard to create your config.json file.

\13. place your config.json file in /xmrig/build

Now lets start your miner using your config.json settings
./xmrig -c

or to start manually...

\14. ./xmrig --donate-level 1 -o xmrpool.eu:5555 -u 46792AW3DDgQAbVVS3jj4ZLFRqrGwAGGJ91Y9QSmjCCQ122BxBBa51ke1W9284auBcjS438ZdLD8ebDfpo7tk3M71wCfi7t -p YourWorkerName

You miner should now be running!

If like me you like automation, then the below instructions will be of interest to you..

The steps provided in this post as of 4th March 2021 still work very well.

I've been fiddling for 2 hours with this and finally achieved "Automine on boot". (may be useful to some)

Assumptions, the "xmrig" executable is in /home/pi/xmrig/build/, and you have a correct config.json file.

\1. Follow this article to install and build everything.
\2. In terminal run "chmod +x /home/pi/xmrig/build/xmrig"
\3. In terminal run "touch /home/pi/xmrig.log"
\4. In terminal run "sudo nano /lib/systemd/system/xmrig.service"
\5. Paste:
[Unit]
Description=PiMiner
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/ds64-run /home/pi/xmrig/build/xmrig -c -B --log-file="/home/pi/xmrig.log"

[Install]
WantedBy=multi-user.target

\6. In terminal run "sudo systemctl daemon-reload"
\7. In terminal run "sudo systemctl enable xmrig"
\8. Either reboot the pi ("sudo reboot now") or in terminal run "sudo systemctl start xmrig"

The only issue is that you no longer see the mining console. You can run in terminal "tail /home/pi/xmrig.log" or view the entire log file. No nice GUI, but all the same logs are there. (I personally would welcome any suggestion with instruction, for how to do this if at all possible. i would then add such detail to this post)