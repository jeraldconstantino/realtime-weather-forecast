![banner](https://github.com/jeraldconstantino/realtime-weather-forecast/blob/master/banner.png)
<h1 align="center">Real-Time Weather Forecast</h1>
A Python-based mobile application that utilized OpenWeatherMap API to acquire and display the current weather information for a specific location inputted by the user.

## Features
- Displays information about the current weather condition, including weather description (like clear sky, moderate rain, and overcast clouds), humidity, cloudiness, air pressure, and temperature.
- Predicts and display the next four days weather conditions with a weather description in every 3 hours.
- Provides dynamic weather reminder (that changes every time the user refresh the App or tap the search button), as well as preparation tips.
- Can search weather information globally.
- Provides Philippine emergency hotlines in case of emergency.
- Provides some helpful information about Disaster management.

## Usage
To use this project, make sure that you have [Git](https://git-scm.com/) and [Python](https://www.python.org/downloads/) (which includes PIP) installed in your machine. 

> **NOTE:** At the time I wrote this document (January 2, 2023), Python 3.10 (and below) is the only compatible version with the required dependencies. The latest Python version can't run this application due to incompatibility with the Kivy package. 

Kindly follow the instructions below:    
* Use `cd` command to go to your desired directory where you want to save the repository.
1. Clone this repository
```
$ git clone https://github.com/jeraldconstantino/realtime-weather-forecast
```
2. Create a [virtual environment](https://docs.python.org/3/library/venv.html).
```
$ python -m venv [your desired name]
$ path\to\venv\Scripts\Activate.ps1      # This will activate your environment.
```
3. Install dependencies within your environment.
```
$ pip install -r requirements.txt
```
4. Create an account with the [OpenWeatherMap](https://openweathermap.org/) website.
5. From that website, generate and copy the API key which can be found in your account logo.
> **NOTE:** API key is unique to every users and must not be shared with the others. 
6. Paste the API key within the [api.py](https://github.com/jeraldconstantino/realtime-weather-forecast/blob/master/api.py) file.
7. Run the App.

## Open for Contribution
1. Clone repository and create a new branch: 
```
$ git clone https://github.com/jeraldconstantino/realtime-weather-forecast
$ git checkout https://github.com/jeraldconstantino/realtime-weather-forecast -b name_for_new_branch
```
2. Make changes and test.
3. Submit [Pull Request](https://github.com/jeraldconstantino/realtime-weather-forecast/pulls) with comprehensive description of changes.

### Bug Reports & Feature Requests
Kindly use the [issue tracker](https://github.com/jeraldconstantino/realtime-weather-forecast/issues) to report any bugs or file feature requests.

## Personal Note:
This App was created since 2020 (although I made it available in GitHub on December, 2022) using my Android device (because I have no Laptop or PC that time) using [PyDroid 3 IDE](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3&hl=en&gl=US) which can be downloaded from the Google Play Store. The App might not be responsive with various screen size and the UI might not be the same as shown in [banner](https://github.com/jeraldconstantino/realtime-weather-forecast/blob/master/banner.png) above. However, the main functionality of this App to request weather data from the OpenWeatherMap via API is working, as well as its features mentioned above. 
