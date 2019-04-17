# Raspberry Pi Execution And Installation Steps
## PUTTY:
PuTTY is a free and open-source terminal emulator, serial console and network file transfer application. It supports several network protocols, including SCP, SSH, Telnet, rlogin, and raw socket connection. It can also connect to a serial port.
Here we are using putty to connect to our Raspberry Pi and control it.

### DOWNLOAD INSTALLATION PACKAGE
One can download latest version of putty from the site https://www.ssh.com/ssh/putty/download .The only need is to select the appropriate version of the installer compatible with the computer and operating system.
### STARTING THE INSTALLER
Once the download is finished, just click on the installer and start the installation.
### CONFIGURING AND INSTALLING
![The home page image is not found](https://github.com/cw-rashmi/AISCMM/blob/master/src/Raspberry_Pi/pics/putty1.png)

Just hit next to start the installation.
The installer then asks for the Destination folder in which to install the software. Almost always it is best to use the default value. Just click Next.
![The home page image is not found](https://github.com/cw-rashmi/AISCMM/blob/master/src/Raspberry_Pi/pics/putty2.png)

Then, the installer asks to select product features to install. You probably want to add a shortcut on the desktop if you expect to use the software frequently. All the other options generally should be enabled. When ready, click Install.
![The home page image is not found](https://github.com/cw-rashmi/AISCMM/blob/master/src/Raspberry_Pi/pics/putty3.png)

When the installation has completed successfully, it should show a Completed screen. Click Finish to exit the installer.
![The home page image is not found](https://github.com/cw-rashmi/AISCMM/blob/master/src/Raspberry_Pi/pics/putty4.png)

## VNC server
### DOWNLOAD INSTALLATION PACKAGE
One can download latest version of putty from the site https://www.realvnc.com/en/connect/download/vnc/windows/ .The only need is to select the appropriate version of the installer compatible with the computer and operating system.
### CONFIGURING AND INSTALLING
Double-click the executable to start the graphical Install Wizard, and follow the instructions.

## Installation of Raspbian on Raspberry pi 3. 
To install raspbian on the SD card refer this video  https://www.youtube.com/watch?v=B5wkXu6tmb4 .

The raspbian is installed on 8 GB memory card. To install raspbian first step is to format the memory card in order to make it suitable for installation. To format memory card SD Memory card format tool 5.0 is used. Steps to format the memory card are as follows:

* Download SD Memory card format tool from www.sdcard.org\downloads\.
* Install the memory card formatting tool.
* Format memory card as FAT.
* Once formatting is completed, memory card is ready for use.

Once the memory card is formatted, it is ready for use. The next step is to download the operating system either raspbian or noobs from official website https://www.raspberrypi.org/downloads/. After downloading the system image of raspbian extract the zip file to some folder. Next step is to write this downloaded system image to memory card. For this purpose Etcher tool is used. Steps to write system image to memory card are as follows:

* Download Etcher and install it from https://etcher.io/.
* Connect an SD card reader with the SD card inside.
* Open Etcher and select from your hard drive the Raspberry Pi .img or .zip file you wish to write to       the SD card.
* Select the SD card you wish to write your image to.
* Review your selections and click 'Flash!' to begin writing data to the SD card.

Once the system image is written to memory card, insert that memory card into raspberry pi and power on the raspberry pi. On the first boot it will take you through all the normal installation steps. Once you are done with that raspberry pi is ready for use.

## Running Raspberry Pi GUI:-
![The home page image is not found](https://github.com/cw-rashmi/AISCMM/blob/master/src/Raspberry_Pi/pics/5.png)
* Run putty and enter the ip address of raspberry pi, choose connection type as SSH and hit open.
* Once the raspberry pi is detected the putty will ask for the username and password for the raspberry pi. Once the raspberry login is successful the raspberry pi terminal will get opened.
* To start the vcn server from the putty terminal, type the command vncserver. Then vcn server will generate the number for the the raspberry pi.
* Open the VCN Viewer application and select the corresponding window number. Then the user need to fill the username and password and then raspberry pi GUI will get open.







