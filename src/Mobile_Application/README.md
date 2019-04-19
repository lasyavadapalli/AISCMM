# Mobile Application Code Execution
## Visual Studio Installation in Windows OS:-
* Install latest version of visual studio from website https://visualstudio.microsoft.com/downloads/?utm_medium=microsoft&utm_source=docs.microsoft.com&utm_campaign=button+cta&utm_content=download+vs2017 . Make sure your system requirements and then install community version.


* Once the installer in installed it will ask for the different frameworks that one can install with visual studio. For our project following frameworks are necessary.
- .NET Desktop Environment
- Universal Windows Platform deveploment  
- ASP.NET and Web Deveploment
- Mobile development with .NET

Install these all components.
Once the visual studio is installed the project can be installed.

## Installation of mobile application on the Visual studio:
After successful installation of visual studio open the project via the file-> Open project menu. Then browse through the folder and select the sln file. 
Once the project is open the next step is to install the packages required for the application. For that open the NuGet package manager and then search for the following set of packages and install the same.
* OxyPlot.Core
* OxyPlot.Xamarin.Forms 
* CarouselView.FormsPlugin
* Syncfusion.Xamarin.SfChart
* Xamarin.Forms

## Google+ login:
* The mobile application requires the google sign in. When the mobile application requests the google api for google credential google need to authenticate that the request is coming from authenticated user and then only permission will be granted.
* So in order to access the google sign in api:
- Go to https://console.developers.google.com ->Create a new project->In that project click on Enable Api and services from dashboard-> Enable Google+ api 
- Go to credentials-> Create Credentials-> OAuth client ID


- Select Android and then create a new OAuth Client ID by entering SHA-1 key of your visual studio and package name of our project.


- For SHA-1 key refer this video https://www.youtube.com/watch?v=A59Oy_2yFIQ 


## To run the Mobile application there are two methods:-
### Using the Emulator :-
One can select the appropriate emulator and run it to deploy the mobile application on the emulator.

### Deploying the mobile application in the mobile phones :- 
One can connect the mobile phones to the computer via USB cable. 
To allow deployment in the mobile phones one need to enable the developer option in the setting and allow the installation of the apps via USB debugging. 

Once the mobile is ready for allowing the installations the visual studio shows the option for deploying the application in the connected device. The user can click on the same and get the application in the mobile
