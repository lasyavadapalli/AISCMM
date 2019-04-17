#  NODEMCU
## Arduino IDE
Download the Arduino Software (IDE)
Get the latest version from the https://www.arduino.cc/en/Main/Software. You can choose between the Installer (.exe) and the Zip packages. 
When the download finishes, proceed with the installation and please allow the driver installation process when you get a warning from the operating system.
Choose the components to be installed.

* Choose the installation directory (we suggest to keep the default one)

* The process will extract and install all the required files to execute properly the Arduino Software (IDE)

Once the installation is finished just hit the finish button.

## Steps to Setup Arduino IDE for NODEMCU ESP8266
* Install Arduino IDE software from the link http://www.arduino.cc/en/main/software.
* Open File ->Preferences
* Adding ESP8266 Board ManagerIn the Additional Boards Manager enter below URL.
http://arduino.esp8266.com/stable/package_esp8266com_index.json

The Boards Manager window opens, scroll the window page to bottom till you see the module with the name ESP8266. Once we get it, select that module and select version and click on the Install button. When it is installed it shows Installed in the module as shown in the figure and then close the window.

* Selecting ESP8266 Arduino Board

* To run the esp8266 with Arduino we have to select the Board: “Arduino/Genuino Uno” and then change it to NodeMCU 1.0 (ESP-12E Module) or other esp8266 modules. This can be done by scrolling down, as shown in the figure.

* Connecting ESP8266 to the PC

*  Let’s connect the ESP8266 module to your computer through USB cable as shown in the figure. When module is connected to the USB, COM port is detected eg: here COM5 is shown in the figure.

* Selecting COM Port

* Upload the program to NodeMCU and check the output on the Serial Monitor

### Connecting Temperature Sensor to the Node MCU

DS18B20 is used for measuring the soil temperature. It is one wire interface sensor, very common in PCB embedded electrical circuits. Its unique one wire protocol requires only one port pin for communication and needs no other external components to work. It is waterproof sensor hence it can be used in humid and wet environmental conditions. It can operate on 3.3v and 5.5v.
This sensor has 3 pins.
Vcc - 5V
Gnd - Gnd
Data

### Connecting Moisture Sensor to the Node MCU
 
KG003 soil moisture sensor is used to measure the soil moisture. This is a simple water sensor that can be used to detect soil moisture. Module output is high level when the soil moisture deficit or output is low. The sensitivity can be adjusted by using the digital potentiometer. The output is available in both analog and digital format. In the project analog interfacing is used for accurate output. The soil moisture sensor consists of two probes. The two probes allow the current to pass through the soil and then it gets the resistance value to measure the moisture value. When there is more water, the soil will conduct more electricity which means that there will be less resistance. Therefore, the moisture level will be higher. Dry soil conducts electricity poorly, so when there will be less water, the soil will conduct less electricity which means that there will be more resistance. Therefore, the moisture level will be lower. The sensor has 4 pins. First two pins are Vcc and GND. The next two pins are output pins.A0 pin is giving analog output and D0 pin is giving digital output. We are using analog output of sensor to get readings. As raspberry pi does not have any analog pin, we have to use an ADC to convert analog output of sensor into digital. The ADC used here is ADS1115.

**NOTE**: Before running the  scripts  for create a csv file containing the ip addresses of all the nodemcus installed in the farm with the name: “nmcu_ip.csv”. Create another csv file with the name “ping_ip_list.csv”.
