from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.boxlayout import BoxLayout
from urllib import parse
from kivy.network.urlrequest import UrlRequest
from datetime import datetime
from disaster_reminders import reminders
from weather_builder import weather_helper
from kivymd.toast import toast
import calendar
import api # make your own `api` file then create a variable for api key there.
from kivy.uix.screenmanager import ScreenManager, Screen
import webbrowser
from kivy.uix.image import Image

# Article Navigation
class MainScreen(Screen):
    pass

class ArticleOneScreen(Screen):
    pass

class ArticleTwoScreen(Screen):
    pass
   
class ArticleThreeScreen(Screen):
	pass

class ArticleFourScreen(Screen):
	pass

class ArticleFiveScreen(Screen):
	pass

class ArticleSixScreen(Screen):
	pass

class ArticleSevenScreen(Screen):
	pass

class ArticleEightScreen(Screen):
	pass

class FullImage(Image):
    pass
	
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(ArticleOneScreen(name='article_one'))
sm.add_widget(ArticleTwoScreen(name='article_two'))
sm.add_widget(ArticleThreeScreen(name='article_three'))
sm.add_widget(ArticleFourScreen(name='article_four'))
sm.add_widget(ArticleFiveScreen(name='article_five'))
sm.add_widget(ArticleSixScreen(name='article_six'))
sm.add_widget(ArticleSevenScreen(name='article_seven'))
sm.add_widget(ArticleEightScreen(name='article_eight'))

class Content(BoxLayout):
	pass

class About(BoxLayout):
	pass

class Version(BoxLayout):
	pass
	
class WeatherApp(MDApp):
	#Main app
	def build(self):
		self.theme_cls.primary_palette = 'LightBlue'
		self.theme_cls.primary_hue = 'A700'
		self.theme_cls.theme_style = 'Light'
		self.realtime_weather = Builder.load_string(weather_helper)
		return self.realtime_weather
	
	def show_data(self):
		# the two buttons in the dialog
		search_button = MDFlatButton(text = 'Search', text_color = self.theme_cls.primary_dark, on_press = self.search_dialog)
		cancel_button = MDFlatButton(text = 'Cancel', text_color = self.theme_cls.primary_dark, on_release = self.close_dialog)
		
		#Pop up when search button press
		self.dialog = MDDialog(type = 'custom', content_cls = Content(), size_hint = [0.8, 0.5], buttons = [search_button, cancel_button], auto_dismiss = False)
		self.dialog.open()
	
	def search_dialog(self, obj):
		address = self.dialog.content_cls.ids.search.text
		self.open_weather_map_request(address)
		self.forecast_request(address)

	def close_dialog(self, obj):
		self.dialog.dismiss()
		
	# API Url Request
	def open_weather_map_request(self, address, *args):
		address = parse.quote(address)
		api_key = api.key # Kindly replace it with your own api key generated from OpenWeatherMap website
		url = "https://api.openweathermap.org/data/2.5/weather?q="+address+"&appid="+api_key		
		UrlRequest(url, on_success = self.success, on_failure = self.failure, on_error = self.error)
	
	# Home page 
	def success(self, urlrequest, result):
		weather_description = result['weather'][0]['description']
		main_description = result['weather'][0]['main']		
		weather_temperature = (result['main']['temp'] - 273.15)
		humidity_info = result['main']['humidity']
		pressure_info = result['main']['pressure']
		visibility_info = (result['visibility'] / 1000)
		wind_info = result['wind']['speed']
		cloudiness_info = result['clouds']['all']
		feels_like_info = (result['main']['feels_like'] - 273.15)
		city_name = result['name']
		country_name = result['sys']['country']
		
		self.root.ids.temperature.text = str("%0.0d°C" %weather_temperature)
		self.root.ids.description.text = str(weather_description)
		self.root.ids.humidity.text = str(f"{humidity_info}%")
		self.root.ids.pressure.text = str(f"{pressure_info}hPa")
		self.root.ids.visibility.text = str("%0.2fkm" %visibility_info)
		self.root.ids.wind.text = str(f"{wind_info}mps")
		self.root.ids.clouds.text = str(f'{cloudiness_info}%')
		self.root.ids.feels_like.text = str("%0.2d°C" %feels_like_info)
		self.root.ids.country.text = str(f'{city_name}, {country_name}')
		self.root.ids.reminder.text = str(reminders())
		
		# dynamic-time-based background picture of main card.
		current = self.current_time(datetime.now().hour)	
		if main_description == 'Clouds' and current == 'day':
			self.root.ids.img_temp.background = 'weather_pictures/cloudy_day.jpg'
		
		elif main_description == 'Clouds' and current == 'night':
			self.root.ids.img_temp.background = 'weather_pictures/cloudy_night.jpg'
		
		elif main_description == 'Rain' and current == 'day':
		
			self.root.ids.img_temp.background = 'weather_pictures/rainy_day.jpeg'
		
		elif main_description == 'Rain' and current == 'night':
		
			self.root.ids.img_temp.background = 'weather_pictures/rainy_night.jpeg'
		
		elif main_description == 'Snow' and current == 'day':
			self.root.ids.img_temp.background = 'weather_pictures/snow_night.jpeg'
		
		elif main_description == 'Snow' and current == 'night':
			self.root.ids.img_temp.background = 'weather_pictures/snow_night.jpeg'
		
		elif main_description == 'Thunderstorm' and current == 'day':
			self.root.ids.img_temp.background = 'weather_pictures/thunderstom_day.jpeg'
		
		elif main_description == 'Thunderstorm' and current == 'night':
			self.root.ids.img_temp.background = 'weather_pictures/thunderstorm_night.jpeg'
		
		elif main_description == 'Drizzle' and current == 'day':
			self.root.ids.img_temp.background = 'weather_pictures/drizzle_day.jpeg'
		
		elif main_description == 'Drizzle' and current == 'night':
		
			self.root.ids.img_temp.background = 'weather_pictures/drizzle_night.jpeg'
		
		elif main_description == 'Clear' and current == 'day':
			self.root.ids.img_temp.background = 'weather_pictures/clear_day.jpg'
		
		elif main_description == 'Clear' and current == 'night':
			self.root.ids.img_temp.background = 'weather_pictures/clear_night.jpg'
		
		elif main_description == 'Atmosphere' and current == 'day':
			self.root.ids.img_temp.background = 'weather_pictures/atmosphere_day.jpg'
		
		elif main_description == 'Atmosphere' and current == 'night':
			self.root.ids.img_temp.background = 'weather_pictures/atmosphere_night.jpg'
					
		else:
			self.root.ids.img_temp.background = 'weather_pictures/main.jpeg'
		
		self.dialog.dismiss()
	
	# Requesting five-day forecast
	def forecast_request(self, address, *args):
		api_key = api.key # Kindly replace it with your own api key generated from OpenWeatherMap website
		request = 'https://api.openweathermap.org/data/2.5/forecast?appid=' + api_key + '&q=' + address
		UrlRequest(request, on_success = self.weather_retrieved, on_failure = self.failure, on_error = self.error)
	
	# Retrieving five-day weather forecast
	def weather_retrieved(self, urlrequest, result):
		hour_datetime = []
		today_icons = []
		hourly_temp = []
		for a in range(0, 5):
			hour_datetime.append(result['list'][a]['dt_txt'])
			today_icons.append(result['list'][a]['weather'][0]['icon'])
			hourly_temp.append(result['list'][a]['main']['temp'] - 273.15)
		
		time_list = []
		for b in hour_datetime:
			meridiem = self.meridiem_identifier(b)
			time_list.append(meridiem)
		
		weekly_description = []
		weekly_datetime = []
		weekly_temp_max = []
		weekly_temp_min = []
		weekly_icons = []
		for c in range(8, len(result['list']), 8):
			weekly_icons.append(result['list'][c]['weather'][0]['icon'])
			weekly_temp_min.append(result['list'][c]['main']['temp_min'] - 273.15)
			weekly_temp_max.append(result['list'][c]['main']['temp_max'] - 273.15)
			weekly_datetime.append(result['list'][c]['dt_txt'])
			weekly_description.append(result['list'][c]['weather'][0]['description'])
			
		weekday_list = []
		for d in weekly_datetime:
			week = self.week_identifier(d)
			weekday_list.append(week)
		
		days = []
		for e in weekday_list:
			day = self.find_day(e)
			days.append(day)
		
		#To display the retrieved five-day forecast data 
		self.root.ids.first_hour.text = str(time_list[0])
		self.root.ids.second_hour.text = str(time_list[1])
		self.root.ids.third_hour.text = str(time_list[2])
		self.root.ids.fourth_hour.text = str(time_list[3])
		self.root.ids.fifth_hour.text = str(time_list[4])
		
		self.root.ids.first_hour_D1_img.source = str('weather_icons/{}.png'.format(today_icons[0]))
		self.root.ids.second_hour_D1_img.source = str('weather_icons/{}.png'.format(today_icons[1]))
		self.root.ids.third_hour_D1_img.source = str('weather_icons/{}.png'.format(today_icons[2]))
		self.root.ids.fourth_hour_D1_img.source = str('weather_icons/{}.png'.format(today_icons[3]))
		self.root.ids.fifth_hour_D1_img.source = str('weather_icons/{}.png'.format(today_icons[4]))
		
		self.root.ids.first_hour_temperature.text = str("%0.0d°C" %hourly_temp[0])
		self.root.ids.second_hour_temperature.text = str("%0.0d°C" %hourly_temp[1])
		self.root.ids.third_hour_temperature.text = str("%0.0d°C" %hourly_temp[2])
		self.root.ids.fourth_hour_temperature.text = str("%0.0d°C" %hourly_temp[3])
		self.root.ids.fifth_hour_temperature.text = str("%0.0d°C" %hourly_temp[4])
		
		self.root.ids.tomorrow_img.source = str('weather_icons/{}.png'.format(weekly_icons[0]))
		self.root.ids.third_week_img.source =  str('weather_icons/{}.png'.format(weekly_icons[1]))
		self.root.ids.fourth_week_img.source =  str('weather_icons/{}.png'.format(weekly_icons[2]))
		self.root.ids.fifth_week_img.source =  str('weather_icons/{}.png'.format(weekly_icons[3]))

		self.root.ids.min_temp_tomorrow.text = str("%0.0d°C" %weekly_temp_min[0])
		self.root.ids.min_temp_third.text = str("%0.0d°C" %weekly_temp_min[1])
		self.root.ids.min_temp_fourth.text = str("%0.0d°C" %weekly_temp_min[2])
		self.root.ids.min_temp_fifth.text = str("%0.0d°C" %weekly_temp_min[3])

		self.root.ids.max_temp_tomorrow.text = str("%0.0d°C" %weekly_temp_max[0])
		self.root.ids.max_temp_third.text = str("%0.0d°C" %weekly_temp_max[1])
		self.root.ids.max_temp_fourth.text = str("%0.0d°C" %weekly_temp_max[2])
		self.root.ids.max_temp_fifth.text = str("%0.0d°C" %weekly_temp_max[3])

		self.root.ids.id_third_week.text = str(weekday_list[1])
		self.root.ids.id_fourth_week.text = str(weekday_list[2])
		self.root.ids.id_fifth_week.text = str(weekday_list[3])

		self.root.ids.week_display_tomorrow.text = str(days[0])
		self.root.ids.week_display_third.text = str(days[1])
		self.root.ids.week_display_fourth.text = str(days[2])
		self.root.ids.week_display_fifth.text = str(days[3])

		self.root.ids.desc_temp_tomorrow.text = str(weekly_description[0])
		self.root.ids.desc_temp_third.text = str(weekly_description[1])
		self.root.ids.desc_temp_fourth.text = str(weekly_description[2])
		self.root.ids.desc_temp_fifth.text = str(weekly_description[3])

	# To determine 'AM' or 'PM'
	def meridiem_identifier(self, hour_datetime):
		next_data, hour = hour_datetime.split(' ')
		hour = int(hour[:2])
		
		meridiem = ' '
		if hour < 12:
			if hour == 0:
				hour = 12
			meridiem = 'AM'
		else:
			if hour > 12:
				hour -= 12
			meridiem = 'PM'
		return ('%i:00 %s' %(hour, meridiem))
	
	# To determine the week-day
	def week_identifier(self, week_datetime):
		current_date = ' '
		next_date, hour = week_datetime.split(' ')
		if current_date != next_date:
			current_date = next_date
			year, month, day = current_date.split('-')
			date = {'y': year, 'm': month, 'd': day}
			return ('{m}/{d}/{y}'.format(**date))
	
	def find_day(self, date):
		week_display = datetime.strptime(date, '%m/%d/%Y').weekday()
		return (calendar.day_name[week_display]) 
  
    #To determine day or night.
	def current_time(self, hour):
		if hour >= 5 and hour <= 17:
			time = 'day'
		else:
			time = 'night'
		return time
	
	# User input validation
	def failure(self, urlrequest, result):
		toast('Failed to find location. The location is neither existing nor you entered invalid value.')
	
	# User input validation
	def error(self, urlrequest, result):
		toast('ERROR: Please provide a valid value.')
	
	# Click Me! button
	def government_hotlines(self):
		return webbrowser.open("https://www.gov.ph/hotlines")
	
	# Dark mode setting
	def check(self, checkbox, value):
		# Dark Mode On
		if value:
			self.root.ids.switch.thumb_color_down = (43/255, 205/255, 252/255, 1)
			self.root.ids.country.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.magnify_icon.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.nav1bg_home.source = 'bg_canvas/arsenic.png'
			self.root.ids.nav2bg_week.source = 'bg_canvas/arsenic.png'
			self.root.ids.nav3bg_article.source = 'bg_canvas/arsenic.png'
			self.root.ids.nav4bg_setting.source = 'bg_canvas/arsenic.png'
			self.root.ids.top_bar.md_bg_color = (26/255, 37/255, 41/255, 1)
			self.root.ids.forecast_logo.source = 'logo/forecast_dark_logo.png'
			self.root.ids.about_app_logo.icon = 'logo/forecast_dark_logo.png'
			self.root.ids.botnav_bg.panel_color = (16/255, 27/255, 31/255, 1)
			self.root.ids.botnav_bg.text_color_active = (43/255, 205/255, 252/255, 1) 
			self.root.ids.reminder_bg.md_bg_color = (14/255, 76/255, 117/255, 1) 
			self.root.ids.feels_like_bg.md_bg_color = (33/255, 62/255, 70/255, 1) 
			self.root.ids.other_info_bg.md_bg_color = (33/255, 62/255, 70/255, 1)
			self.root.ids.hourly_bg.md_bg_color = (33/255, 62/255, 70/255, 1)
			self.root.ids.hotline_bg.md_bg_color = (33/255, 62/255, 70/255, 1)
			self.root.ids.weekly_bg.md_bg_color = (33/255, 62/255, 70/255, 1)
			self.root.ids.today_bg.md_bg_color = (14/255, 76/255, 117/255, 1)
			self.root.ids.setting_bg.md_bg_color = (33/255, 62/255, 70/255, 1)
			self.root.ids.about_developer_bg.md_bg_color = (33/255, 62/255, 70/255, 1)
			self.root.ids.about_app_bg.md_bg_color = (33/255, 62/255, 70/255, 1)
			self.root.ids.feels_like.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.feels_like_text_bg.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.leaf_bg.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.alert_circle_outline_bg.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.reminder_text_bg.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.reminder.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.humidity.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.humidity_text.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.humidity_icon.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.visibility.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.visibility_text.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.visibility_icon.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.wind.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.wind_text.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.wind_icon.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.clouds.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.clouds_text.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.clouds_icon.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.pressure.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.pressure_text.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.pressure_icon.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.article_buttons_bg.md_bg_color = (33/255, 62/255, 70/255, 1)
			self.root.ids.disaster_management_bg.md_bg_color = (14/255, 76/255, 117/255, 1) 
			self.root.ids.hotline_text.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.hotline_button.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.hotline_button.md_bg_color = (14/255, 76/255, 117/255, 1)
			self.root.ids.today_text.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.first_hour.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.first_hour_temperature.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.second_hour.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.second_hour_temperature.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.third_hour.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.third_hour_temperature.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.fourth_hour.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.fourth_hour_temperature.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.fifth_hour.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.fifth_hour_temperature.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.tomorrow_text.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.min_text.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.desc_text.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.max_text.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.week_display_tomorrow.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.min_temp_tomorrow.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.max_temp_tomorrow.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.desc_temp_tomorrow.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.id_third_week.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.week_display_third.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.min_temp_third.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.max_temp_third.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.desc_temp_third.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.id_fourth_week.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.week_display_fourth.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.min_temp_fourth.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.max_temp_fourth.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.desc_temp_fourth.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.id_fifth_week.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.week_display_fifth.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.min_temp_fifth.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.max_temp_fifth.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.desc_temp_fifth.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.disaster_management.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.alert_icon.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.know_more.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.dark_mode_text.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.about_developer_text.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.information_variant_icon.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.about_app_text.text_color = (43/255, 205/255, 252/255, 1)
			self.root.ids.version_text.text_color = (43/255, 205/255, 252/255, 1)
		
		# Dark Mode Off
		else:
			self.root.ids.switch.thumb_color_down = self.theme_cls.primary_dark
			self.root.ids.country.text_color = self.theme_cls.primary_dark
			self.root.ids.magnify_icon.text_color = self.theme_cls.primary_dark
			self.root.ids.nav1bg_home.source = 'bg_canvas/white.png'
			self.root.ids.nav2bg_week.source = 'bg_canvas/white.png'
			self.root.ids.nav3bg_article.source = 'bg_canvas/white.png'
			self.root.ids.nav4bg_setting.source = 'bg_canvas/white.png'
			self.root.ids.top_bar.md_bg_color = (1, 1, 1, 1)
			self.root.ids.forecast_logo.source = 'logo/forecast_light_logo.png'
			self.root.ids.about_app_logo.icon = 'logo/forecast_light_logo.png'
			self.root.ids.botnav_bg.panel_color = (245/255, 245/255, 245/255, 1)
			self.root.ids.botnav_bg.text_color_normal = (160/255, 167/255, 172/255, 1) 
			self.root.ids.botnav_bg.text_color_active = self.theme_cls.primary_dark
			self.root.ids.reminder_bg.md_bg_color = (178/255, 211/255, 230/255, 1) 
			self.root.ids.feels_like_bg.md_bg_color = (216/255, 233/255, 243/255, 1)
			self.root.ids.other_info_bg.md_bg_color = (216/255, 233/255, 243/255, 1)
			self.root.ids.hourly_bg.md_bg_color = (216/255, 233/255, 243/255, 1)
			self.root.ids.hotline_bg.md_bg_color = (216/255, 233/255, 243/255, 1)
			self.root.ids.weekly_bg.md_bg_color = (216/255, 233/255, 243/255, 1)
			self.root.ids.today_bg.md_bg_color = (178/255, 211/255, 230/255, 1)
			self.root.ids.article_buttons_bg.md_bg_color = (178/255, 211/255, 230/255, 1) 
			self.root.ids.disaster_management_bg.md_bg_color = (216/255, 233/255, 243/255, 1)
			self.root.ids.setting_bg.md_bg_color = (216/255, 233/255, 243/255, 1)
			self.root.ids.about_developer_bg.md_bg_color = (216/255, 233/255, 243/255, 1)
			self.root.ids.about_app_bg.md_bg_color = (216/255, 233/255, 243/255, 1)
			self.root.ids.feels_like.text_color = self.theme_cls.primary_dark
			self.root.ids.feels_like_text_bg.text_color = self.theme_cls.primary_dark
			self.root.ids.leaf_bg.text_color = self.theme_cls.primary_dark
			self.root.ids.alert_icon.text_color = self.theme_cls.primary_dark
			self.root.ids.reminder_text_bg.text_color = self.theme_cls.primary_dark
			self.root.ids.reminder.text_color = self.theme_cls.primary_dark
			self.root.ids.humidity.text_color = self.theme_cls.primary_dark
			self.root.ids.humidity_text.text_color = self.theme_cls.primary_dark
			self.root.ids.humidity_icon.text_color = self.theme_cls.primary_dark
			self.root.ids.visibility.text_color = self.theme_cls.primary_dark
			self.root.ids.visibility_text.text_color = self.theme_cls.primary_dark
			self.root.ids.visibility_icon.text_color = self.theme_cls.primary_dark
			self.root.ids.wind.text_color = self.theme_cls.primary_dark
			self.root.ids.wind_text.text_color = self.theme_cls.primary_dark
			self.root.ids.wind_icon.text_color = self.theme_cls.primary_dark
			self.root.ids.clouds.text_color = self.theme_cls.primary_dark
			self.root.ids.clouds_text.text_color = self.theme_cls.primary_dark
			self.root.ids.clouds_icon.text_color = self.theme_cls.primary_dark
			self.root.ids.pressure.text_color = self.theme_cls.primary_dark
			self.root.ids.pressure_text.text_color = self.theme_cls.primary_dark
			self.root.ids.pressure_icon.text_color = self.theme_cls.primary_dark
			self.root.ids.hotline_text.text_color = self.theme_cls.primary_dark
			self.root.ids.hotline_button.text_color = self.theme_cls.primary_dark
			self.root.ids.hotline_button.md_bg_color = (1, 1, 1, 1)
			self.root.ids.today_text.text_color = self.theme_cls.primary_dark
			self.root.ids.first_hour.text_color = self.theme_cls.primary_dark
			self.root.ids.first_hour_temperature.text_color = self.theme_cls.primary_dark
			self.root.ids.second_hour.text_color = self.theme_cls.primary_dark
			self.root.ids.second_hour_temperature.text_color = self.theme_cls.primary_dark
			self.root.ids.third_hour.text_color = self.theme_cls.primary_dark
			self.root.ids.third_hour_temperature.text_color = self.theme_cls.primary_dark
			self.root.ids.fourth_hour.text_color = self.theme_cls.primary_dark
			self.root.ids.fourth_hour_temperature.text_color = self.theme_cls.primary_dark
			self.root.ids.fifth_hour.text_color = self.theme_cls.primary_dark
			self.root.ids.fifth_hour_temperature.text_color = self.theme_cls.primary_dark
			self.root.ids.tomorrow_text.text_color = self.theme_cls.primary_dark
			self.root.ids.min_text.text_color = self.theme_cls.primary_dark
			self.root.ids.desc_text.text_color = self.theme_cls.primary_dark
			self.root.ids.max_text.text_color = self.theme_cls.primary_dark
			self.root.ids.week_display_tomorrow.text_color = self.theme_cls.primary_dark
			self.root.ids.min_temp_tomorrow.text_color = self.theme_cls.primary_dark
			self.root.ids.max_temp_tomorrow.text_color = self.theme_cls.primary_dark
			self.root.ids.desc_temp_tomorrow.text_color = self.theme_cls.primary_dark
			self.root.ids.id_third_week.text_color = self.theme_cls.primary_dark
			self.root.ids.week_display_third.text_color = self.theme_cls.primary_dark
			self.root.ids.min_temp_third.text_color = self.theme_cls.primary_dark
			self.root.ids.max_temp_third.text_color = self.theme_cls.primary_dark
			self.root.ids.desc_temp_third.text_color = self.theme_cls.primary_dark
			self.root.ids.id_fourth_week.text_color = self.theme_cls.primary_dark
			self.root.ids.week_display_fourth.text_color = self.theme_cls.primary_dark
			self.root.ids.min_temp_fourth.text_color = self.theme_cls.primary_dark
			self.root.ids.max_temp_fourth.text_color = self.theme_cls.primary_dark
			self.root.ids.desc_temp_fourth.text_color = self.theme_cls.primary_dark
			self.root.ids.id_fifth_week.text_color = self.theme_cls.primary_dark
			self.root.ids.week_display_fifth.text_color = self.theme_cls.primary_dark
			self.root.ids.min_temp_fifth.text_color = self.theme_cls.primary_dark
			self.root.ids.max_temp_fifth.text_color = self.theme_cls.primary_dark
			self.root.ids.desc_temp_fifth.text_color = self.theme_cls.primary_dark
			self.root.ids.disaster_management.text_color = self.theme_cls.primary_dark
			self.root.ids.know_more.text_color = self.theme_cls.primary_dark
			self.root.ids.dark_mode_text.text_color = self.theme_cls.primary_dark
			self.root.ids.alert_circle_outline_bg.text_color = self.theme_cls.primary_dark
			self.root.ids.about_developer_text.text_color = self.theme_cls.primary_dark
			self.root.ids.information_variant_icon.text_color = self.theme_cls.primary_dark
			self.root.ids.about_app_text.text_color = self.theme_cls.primary_dark
			self.root.ids.version_text.text_color = self.theme_cls.primary_dark
	
	# About Developers
	def show_details(self):
		cancel_button = MDFlatButton(text = 'Cancel', text_color = self.theme_cls.primary_dark, on_release = self.details_close_dialog)
		
		self.details_dialog = MDDialog(title = 'About Developers', type = 'custom', content_cls = About(), buttons = [cancel_button], size_hint = [0.8, 0.8], auto_dismiss = False)
		self.details_dialog.open()
	
	# About App
	def show_version(self):
		cancel_button = MDFlatButton(text = 'Cancel', text_color = self.theme_cls.primary_dark, on_release = self.app_close_dialog)
		self.app_dialog = MDDialog(title = 'About', type = 'custom', content_cls = Version(), buttons = [cancel_button], size_hint = [0.8,1], auto_dismiss = False)
		self.app_dialog.open()
	
	def details_close_dialog(self, obj):
		self.details_dialog.dismiss()
	
	def app_close_dialog(self, obj):
		self.app_dialog.dismiss()
		
WeatherApp().run()