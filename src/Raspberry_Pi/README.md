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
![The home page image is not found](https://github.com/cw-rashmi/AISCMM/blob/master/src/Raspberry_Pi/pics/5.jpg)
* Run putty and enter the ip address of raspberry pi, choose connection type as SSH and hit open.
* Once the raspberry pi is detected the putty will ask for the username and password for the raspberry pi. Once the raspberry login is successful the raspberry pi terminal will get opened.
* To start the vcn server from the putty terminal, type the command vncserver. Then vcn server will generate the number for the the raspberry pi.
* Open the VCN Viewer application and select the corresponding window number. Then the user need to fill the username and password and then raspberry pi GUI will get open.



## Download and save the scripts final_script_fyp.py and alive_status_nmcu.py in a directory named AISCMM which is stored on the Desktop.(complete path: /home/pi/Desktop/AISCMM)
To connect the raspberry pi to network follow the steps:
 Run the following command in the terminal:
sudo nano /etc/nework/interfaces

Write the following lines and save:

      source-directory /etc/network/interfaces.d
      auto lo
      iface lo inet loopback
      iface eth0 inet dhcp
      auto wlan0
      allow-hotplug wlan0
      iface wlan0 inet dhcp
      wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
      iface default inet dhcp
      allow-hotplug wlan1
      iface wlan1 inet dhcp
        wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf


Save the file by Ctrl+x and then pess y. 
	
  b.    	Run the following command:
			sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
		Type the following lines:
			  country=IN
        ctrl_interface=DIR=/var/run/wpa_supplicant
        update_config=1
        network={
        			ssid="your ssid"
        			psk="your password"
        }
	c.  	Reboot the raspberry pi.

3.   	create a csv file with name : nmcu_ip.csv in the AISCMM directory.
	In this file enter the id and ip addesrres of the nodemcus installed in the farm.
	The format to store is:
		Eg. 	1_nmcu,192.168.43.240
          2_nmcu,192.168.43.86
          3_nmcu,192.168.43.119
          4_nmcu,192.168.43.100
          
          
4. Make the following changes in the script final_script_fyp.py
	
Line no 16,17 and 18: change the ip addresses in the variables of URL_get_data URL_update_mois_data and URL_delete_ip to the ip address of the flask server.

5. Make the following changes in the alive_status_nmcu.pi script:
Line 17. Change the ip address in the variable URL to the ip address of the flask server.

6. Steps to autorun the scripts on raspberry pi:
	Run the following command:
	Sudo nano /etc/profile
	
	append the following lines in the end:

sudo python /home/pi/Desktop/AISCMM/final_script_fyp.py &
sudo python /home/pi/Desktop/AISCMM/alive_status_nmcu.py &

 Now upon reboot the scripts will run on boot up.



## Connecting Ultrasonic sensor to raspberry pi 3.

HC-SR 04 ultrasonic distance sensor is used to measure water level in storage tank. This sensor operates on 5V. The maximum measuring distance is 200cm.The Ultrasonic transmitter transmits an ultrasonic wave, this wave travels in air and when it gets objected by water it gets reflected back toward the sensor this reflected wave is observed by the Ultrasonic receiver. Once the signal is received by receiver using time distance speed formula we can calculate the water level in the tank. A basic ultrasonic sensor consists of one or more ultrasonic transmitters (basically speakers), a receiver, and a control circuit. The transmitters emit a high frequency ultrasonic sound, which bounce off any nearby objects. Some of that ultrasonic noise is reflected and detected by the receiver on the sensor. That return signal is then processed by the control circuit to calculate the time difference between the signal being transmitted and received. This time can subsequently be used, along with some clever math, to calculate the distance between the sensor and the reflecting object.

### Connection with raspberry pi:

### Connecting Relay to raspberry pi3.

The single channel 5v relay is used to control the water pump. The operating voltage of the relay is 5v. This relay is connected to GPIO pin of raspberry pi. Whenever the moisture level is below threshold value water pump is switched on using the relay and also water pump is switched off once threshold level is reached.

### Connecting relay to raspberry pi3:

### Connecting Water pump to relay:

Run the final_script_fyp.py from the src/rpi folder .

NOTE: Before running the scripts create a csv file containing the ip addresses of all the nodemcus installed in the farm with the name: “nmcu_ip.csv”. Create another csv file with the name “ping_ip_list.csv”.







