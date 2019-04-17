# Flask Server
## Flask Server Set Up:-
To install flask the prerequisites are to have python installed on the computer. The flask can be installed the terminal using the pip installer using the command:-
```
pip install Flask
```
### To run the Flask server:-
The flask server first need to be configured for a IP address and port number. It is the identifier for the applications which wants to send requests to the flask server.

The flask IP address is same as that of the ip address of local machine. And the port number can be any one open port.
The user needs to open the command prompt and just run the command
```
Python App.js 
```
Once the flask server is ready the mobile application as well as the raspberry pi can send requests to and receive reply from the same.

* The flask server interacts with SQLite Database.
* The flask server keeps on running in the background. And keeps on listening was the user request. The mobile application or the raspberry pi can query the particular method of flask server by the ip address, port number, method to be invoked and passing the parameters in the form of JSON parameters.
* An example of flask API request URL is:
```
http://192.168.43.104:5010/get_data
```
Here 192.168.43.104 is the ip address of the flask server which is same as that of the local machine on which flask is running.
And 5010 is port number. get_data is the name of route specified in the flask. 

The flask server listen to all the request on the ip address and port number. The requests can be identified by the route specified in the route. Each route need to be distinct. And the corresponding queries specified on the route are executed and response is sent back to the user.
