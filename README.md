# plug_connect
A utility package for check the connection of plug and socket

# hardware

# software
- ubuntu mate (20.04) for raspberry pi 4
- [ROS Noetic](http://wiki.ros.org/noetic/Installation/Ubuntu) (install ROS-Base)
- enable SPI interface ```sudo raspi-config```
- install wiringPi ```sudo apt-get install wiringpi```
- install GPIO
  ```
    sudo apt-get install python3-pip
    sudo pip install RPi-GPIO spidev
  ```

# setup service
1. create a service /etc/systemd/system/connection-check.service

```
[Unit]
Description="Connection Check ROS Node"
After=multi-user.target

[Service]
Type=simple
User=ubuntu
Group=ubuntu
ExecStart=/home/ubuntu/catkin_ws/src/plug_connect/auto_start.sh

[Install]
WantedBy=multi-user.target

```
2. make scripts executable
```
sudo chmod +x auto_start.sh
sudo chmod +x scripts/connection_check.py
```
3. enable service
```
sudo systemctl enable connection-check.service
```
4. enable sudo no password ```sudo visudo``` and add line after group sudo ```${ubuntu} ALL=(ALL:ALL) NOPASSWD:ALL```
5. add ```auth sufficient pam_permit.so``` line to ```/etc/pam.d/sudo``` file to fix error "pam_unit auth could not identify password for ..."
