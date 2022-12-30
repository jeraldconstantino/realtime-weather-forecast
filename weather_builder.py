weather_helper = """
Screen:
	BoxLayout:
		orientation: 'vertical'
		MDFloatLayout:
			id: top_bar
			size_hint: 1, 0.085
			pos_hint: {'center_x':0.5, 'center_y':0.5}
			md_bg_color: 1, 1, 1, 1
			MDIconButton:
				id: magnify_icon
				icon: 'magnify'
				pos_hint: {'center_x': 0.935, 'center_y': 0.5}
				theme_text_color: 'Custom'
				text_color: app.theme_cls.primary_dark	
				on_release: app.show_data()
				
			Image:
				id: forecast_logo
				source: 'logo/forecast_light_logo.png'
				pos_hint: {'center_x': 0.1, 'center_y': 0.45}
				size_hint: 1.5, 1.5
				
			MDLabel:
				id: country
				text: 'Real-Time Weather Forecast'
				halign: 'center'
				pos_hint: {'center_y': 0.5}
				font_style: 'H3'
				font_size: sp(20)
				theme_text_color: 'Custom'
				text_color: app.theme_cls.primary_dark
		
		MDBottomNavigation:
			id: botnav_bg
			text_color_active: app.theme_cls.primary_dark
			text_color_normal: (160/255, 167/255, 172/255, 1)
			
			MDBottomNavigationItem:
				text: "HOME"
				name: "Home Button"
				icon: 'weather-partly-cloudy'
				text_color: app.theme_cls.primary_dark
				
				FullImage:
					id: nav1bg_home
					source: 'bg_canvas/white.png'
					
				ScrollView:
					BoxLayout:
						orientation: 'vertical'
						MDCard:
							id: img_temp
							pos_hint: {'center_x':0.5,'center_y':0.80}
							size_hint: 1,0.42
							elevation: 0
							radius: [15,]
							background: 'weather_pictures/main.jpeg'
							
							ScrollView:
								MDFloatLayout:
									Image:
										source: "weather_pictures/shadow_elevation.png"
										allow_stretch: True
										keep_ratio: False
								
									MDFloatLayout:
										orientation: 'vertical'
										MDLabel:
											id: temperature
											text: '°C'
											pos_hint: {'center_x': 0.52,'center_y': 0.22}			
											font_style: 'H3'
											font_size: sp(50)
											theme_text_color: 'Custom'
											text_color: (1,1,1,1)
															
										MDLabel:	
											id: description
											text: 'Description'
											pos_hint: {'center_x': 0.52,'center_y': 0.08}
											font_style: 'Overline'
											font_size: sp(13)
											theme_text_color: 'Custom'
											text_color: (1,1,1,1)
																	
						BoxLayout:
							MDFloatLayout:	
								MDCard:
									id: other_info_bg
									pos_hint: {'center_x':0.5,'center_y':0.892}
									size_hint_x: 0.95
									size_hint_y: 0.165
									elevation: 8
									radius: [15,]
									md_bg_color: (216/255, 233/255, 243/255, 1)
								
								ScrollView:
									BoxLayout:
										pos_hint: {'center_x': 0.5, 'center_y': 0.88}
										MDFloatLayout:
											orientation: 'vertical'
											MDLabel:
												id: humidity
												text: '--%'
												pos_hint: {'center_x': 0.88, 'center_y': 0.875}
												theme_text_color: 'Custom'
												text_color: app.theme_cls.primary_dark
												font_style: 'Subtitle2'
												font_size: sp(18)
														
											MDLabel:
												id: humidity_text
												text: 'HUMIDITY'
												pos_hint: {'center_x': 0.853, 'center_y': 0.845}
												theme_text_color: 'Custom'
												text_color: app.theme_cls.primary_dark
												font_style: 'Overline'
												font_size: sp(8)			
											MDIcon:
												id: humidity_icon
												icon: 'water-percent'
												theme_text_color: 'Custom'
												pos_hint: {'center_x': 0.87,'center_y': 0.9235}
												text_color: app.theme_cls.primary_dark	
													
										MDFloatLayout:
											orientation: 'vertical'
											MDLabel:
												id: visibility
												text: '--km'
												pos_hint: {'center_x': 0.65, 'center_y': 0.875}
												theme_text_color: 'Custom'
												text_color: app.theme_cls.primary_dark
												font_style: 'Subtitle2'
												font_size: sp(18)
														
											MDLabel:
												id: visibility_text
												text: 'VISIBILITY'
												pos_hint: {'center_x': 0.82, 'center_y': 0.845}
												theme_text_color: 'Custom'
												text_color: app.theme_cls.primary_dark
												font_style: 'Overline'
												font_size: sp(8)		
													
											MDIcon:
												id: visibility_icon
												icon: 'weather-fog'
												theme_text_color: 'Custom'
												pos_hint: {'center_x': 0.863,'center_y': 0.9235}
												text_color: app.theme_cls.primary_dark
											
										MDFloatLayout:
											orientation: 'vertical'
											MDLabel:
												id: wind
												text: '--mps'
												pos_hint: {'center_x': 0.62, 'center_y': 0.875}
												theme_text_color: 'Custom'
												text_color: app.theme_cls.primary_dark
												font_style: 'Subtitle2'
												font_size: sp(18)
														
											MDLabel:
												id: wind_text
												text: 'WIND SPEED'
												pos_hint: {'center_x': 0.774, 'center_y': 0.845}
												theme_text_color: 'Custom'
												text_color: app.theme_cls.primary_dark
												font_style: 'Overline'
												font_size: sp(8)		
													
											MDIcon:
												id: wind_icon
												icon: 'weather-windy-variant'
												theme_text_color: 'Custom'
												pos_hint: {'center_x': 0.8665,'center_y': 0.9235}
												text_color: app.theme_cls.primary_dark	
											
										MDFloatLayout:
											orientation: 'vertical'
											MDLabel:
												id: clouds
												text: '--%'
												pos_hint: {'center_x': 0.87, 'center_y': 0.875}
												theme_text_color: 'Custom'
												text_color: app.theme_cls.primary_dark
												font_style: 'Subtitle2'
												font_size: sp(18)
														
											MDLabel:
												id: clouds_text
												text: 'CLOUDINESS'
												pos_hint: {'center_x': 0.8, 'center_y': 0.845}
												theme_text_color: 'Custom'
												text_color: app.theme_cls.primary_dark
												font_style: 'Overline'
												font_size: sp(8)
																
											MDIcon:
												id: clouds_icon
												icon: 'weather-cloudy'
												theme_text_color: 'Custom'	
												pos_hint: {'center_x': 0.864,'center_y': 0.9235}
												text_color: app.theme_cls.primary_dark
											
										MDFloatLayout:
											orientation: 'vertical'
											MDLabel:
												id: pressure
												text: '--hPa'
												pos_hint: {'center_x': 0.5, 'center_y': 0.875}
												theme_text_color: 'Custom'
												text_color: app.theme_cls.primary_dark
												font_style: 'Subtitle2'
												font_size: sp(18)
														
											MDLabel:
												id: pressure_text
												text: 'PRESSURE'	
												pos_hint: {'center_x': 0.705, 'center_y': 0.845}
												theme_text_color: 'Custom'
												text_color: app.theme_cls.primary_dark
												font_style: 'Overline'
												font_size: sp(8)
																
											MDIcon:
												id: pressure_icon
												icon: 'gauge'
												theme_text_color: 'Custom'
												pos_hint: {'center_x': 0.7275,'center_y': 0.9235}
												text_color: app.theme_cls.primary_dark
						
				ScrollView:
					MDFloatLayout:
						pos_hint: {'center_x':0.5,'center_y':0.1}
						MDFloatLayout:
							MDCard:
								id: feels_like_bg
								pos_hint: {'center_x':0.5,'center_y':0.285}
								size_hint_x: 0.96
								size_hint_y: 0.531
								elevation: 8
								radius: [15,]
								md_bg_color: (216/255, 233/255, 243/255, 1)
						
						MDFloatLayout:
							MDCard:
								id: reminder_bg
								pos_hint: {'center_x':0.5,'center_y':0.173}
								size_hint_x: 0.96
								size_hint_y: 0.3
								elevation: 2
								radius: [30,30, 15, 15]
								md_bg_color: (178/255, 211/255, 230/255, 1)
								
						ScrollView:
							pos_hint: {'center_x': 0.5, 'center_y': 0.2945}
							BoxLayout: 
								orientation: 'vertical'
								pos_hint: {'center_x': 0.5, 'center_y': 0.1}
								size_hint_x: 0.95
								MDFloatLayout:
									orientation: 'vertical'
									pos_hint: {'center_x': 0.5, 'center_y': 0.2945}
									
									MDLabel:
										id: feels_like_text_bg
										text: 'IT FEELS LIKE ...'
										pos_hint: {'center_x': 0.65,'center_y': 0.718}
										theme_text_color: 'Custom'
										text_color: app.theme_cls.primary_dark
										font_style: 'H1'
										font_size: sp(25)
										
									MDLabel:
										id: feels_like
										halign: 'center'
										text: '--°C'
										pos_hint: {'center_y': 0.62}
										theme_text_color: 'Custom'
										text_color: app.theme_cls.primary_dark
										font_style: 'H2'
										font_size: sp(60)
						
									MDIcon:
										id: leaf_bg
										icon: 'leaf'
										theme_text_color: 'Custom'
										pos_hint: {'center_x': 0.581,'center_y': 0.718}
										text_color: app.theme_cls.primary_dark
							
						
						MDFloatLayout:
							orientation: 'vertical'
							MDIcon:
								id: alert_icon
								icon: 'alert-circle-outline'
								text_size: [dp(24), dp(24)]
								theme_text_color: 'Custom'
								pos_hint: {'center_x': 0.55,'center_y': 0.275}
								text_color: app.theme_cls.primary_dark
								
							MDLabel:
								id: reminder_text_bg
								text: 'REMINDER:'
								pos_hint: {'center_x': 0.62, 'center_y': 0.275}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H3'
								font_size: sp(23)
							
							MDLabel:
								id: reminder
								text: 'If anyone in your family has a disability or special needs, adjust your plan accordingly.'
								halign: 'center'
								pos_hint: {'center_x': 0.5, 'center_y': 0.15}
								size_hint_x: 0.85
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(18)			
											
			MDBottomNavigationItem:
				text: "WEEK"
				name: "Week Button"
				icon: 'calendar-outline'
				FullImage:
					id: nav2bg_week
					source: 'bg_canvas/white.png'
				
				BoxLayout:
					orientation: 'vertical'
					MDFloatLayout:
						MDFloatLayout:
							MDCard:
								id: hourly_bg
								pos_hint: {'center_x':0.5,'center_y':0.81}
								size_hint_x: 0.95
								size_hint_y: 0.2
								elevation: 0
								radius: [15,]
								md_bg_color: (216/255, 233/255, 243/255, 1)
						
						MDFloatLayout:
							MDCard:
								id: today_bg
								pos_hint: {'center_x':0.5,'center_y':0.947}
								size_hint_x: 0.95
								size_hint_y: 0.1
								elevation: 8
								radius: [30,30, 15, 15]
								md_bg_color: (178/255, 211/255, 230/255, 1)
							
						MDFloatLayout:
							orientation: 'vertical'
							MDLabel:
								id: today_text
								text: 'TODAY'
								halign: 'center'
								pos_hint: {'center_y': 0.945}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'Overline'
								font_size: sp(45)
						
						MDFloatLayout:
							orientation: 'vertical'		
							Image:
								id: first_hour_D1_img
								source: 'weather_icons/01d.png'
								pos_hint: {'center_x': 0.125, 'center_y': 0.8}
							
							MDLabel:
								id: first_hour
								text: '-:--'
								pos_hint: {'center_x': 0.555, 'center_y': 0.85}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H3'
								font_size: sp(15)
							
							MDLabel:
								id: first_hour_temperature
								text: '--°C'
								halign: 'center'
								pos_hint: {'center_x': 0.115, 'center_y': 0.75}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H3'
								font_size: sp(18)
						
						MDFloatLayout:
							orientation: 'vertical'		
							Image:
								id: second_hour_D1_img
								source: 'weather_icons/01d.png'
								pos_hint: {'center_x': 0.325, 'center_y': 0.8}
							
							MDLabel:
								id: second_hour
								text: '-:--'
								pos_hint: {'center_x': 0.755, 'center_y': 0.85}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H3'
								font_size: sp(15)
							
							MDLabel:
								id: second_hour_temperature
								text: '--°C'
								halign: 'center'
								pos_hint: {'center_x': 0.315, 'center_y': 0.75}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H3'
								font_size: sp(18)
						
						MDFloatLayout:
							orientation: 'vertical'		
							Image:
								id: third_hour_D1_img
								source: 'weather_icons/01d.png'
								halign: 'center'
								pos_hint: {'center_y': 0.8}
							
							MDLabel:
								id: third_hour
								text: '-:--'
								halign: 'center'
								pos_hint: {'center_y': 0.85}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H3'
								font_size: sp(15)
							
							MDLabel:
								id: third_hour_temperature
								text: '--°C'
								halign: 'center'
								pos_hint: {'center_y': 0.75}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H3'
								font_size: sp(18)
						
						MDFloatLayout:
							orientation: 'vertical'		
							Image:
								id: fourth_hour_D1_img
								source: 'weather_icons/01d.png'
								pos_hint: {'center_x': 0.675, 'center_y': 0.8}
							
							MDLabel:
								id: fourth_hour
								text: '-:--'
								pos_hint: {'center_x': 1.1085, 'center_y': 0.85}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H3'
								font_size: sp(15)
							
							MDLabel:
								id: fourth_hour_temperature
								text: '--°C'
								halign: 'center'
								pos_hint: {'center_x': 0.6855, 'center_y': 0.75}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H3'
								font_size: sp(18)
						
						MDFloatLayout:
							orientation: 'vertical'		
							Image:
								id: fifth_hour_D1_img
								source: 'weather_icons/01d.png'
								pos_hint: {'center_x': 0.875, 'center_y': 0.8}
							
							MDLabel:
								id: fifth_hour
								text: '-:--'
								pos_hint: {'center_x': 1.3085, 'center_y': 0.85}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H3'
								font_size: sp(15)
							
							MDLabel:
								id: fifth_hour_temperature
								text: '--°C'
								halign: 'center'
								pos_hint: {'center_x': 0.8855, 'center_y': 0.75}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H3'
								font_size: sp(18)
								
						MDFloatLayout:
							MDCard:
								id: weekly_bg
								pos_hint: {'center_x':0.5,'center_y':0.463}
								size_hint_x: 0.95
								size_hint_y: 0.445
								elevation: 0
								radius: [15,]
								md_bg_color: (216/255, 233/255, 243/255, 1)
						
						MDFloatLayout:
							orientation: 'vertical'		
							Image:
								id: tomorrow_img
								source: 'weather_icons/01d.png'
								pos_hint: {'center_x': 0.35, 'center_y': 0.613}
								
							MDLabel:
								id: tomorrow_text
								text: 'TOMORROW'
								pos_hint: {'center_x': 0.58, 'center_y': 0.653}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H3'
								font_size: sp(18)
							
							MDLabel:
								id: min_text
								text: 'Min.'
								pos_hint: {'center_x': .962, 'center_y': 0.653}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(14)
							
							MDLabel:
								id: desc_text
								text: 'Description'
								pos_hint: {'center_x': 1.25, 'center_y': 0.653}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(14)
							
							MDLabel:
								id: max_text
								text: 'Max.'
								pos_hint: {'center_x': 1.105, 'center_y': 0.653}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(14)
							
							MDLabel:
								id: week_display_tomorrow
								text: 'day'
								pos_hint: {'center_x': 0.6, 'center_y': 0.613}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(16)
							
							MDLabel:
								id: min_temp_tomorrow
								text: '--°C'
								pos_hint: {'center_x': .95, 'center_y': 0.613}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(16)
							
							MDLabel:
								id: max_temp_tomorrow
								text: '--°C'
								pos_hint: {'center_x': 1.1, 'center_y': 0.613}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(16)
							
							MDLabel:
								id: desc_temp_tomorrow
								text: ' '
								pos_hint: {'center_x': 1.25, 'center_y': 0.613}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(16)
						
						MDFloatLayout:
							orientation: 'vertical'		
							Image:
								id: third_week_img
								source: 'weather_icons/01d.png'
								pos_hint: {'center_x': 0.35, 'center_y': 0.503}
								
							MDLabel:
								id: id_third_week
								text: 'date'
								pos_hint: {'center_x': 0.58, 'center_y': 0.543}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H3'
								font_size: sp(18)
							
							MDLabel:
								id: week_display_third
								text: 'day'
								pos_hint: {'center_x': 0.6, 'center_y': 0.503}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(16)
							
							MDLabel:
								id: min_temp_third
								text: '--°C'
								pos_hint: {'center_x': .95, 'center_y': 0.503}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(16)
							
							MDLabel:
								id: max_temp_third
								text: '--°C'
								pos_hint: {'center_x': 1.1, 'center_y': 0.503}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(16)
							
							MDLabel:
								id: desc_temp_third
								text: ' '
								pos_hint: {'center_x': 1.25, 'center_y': 0.503}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(16)
							
						MDFloatLayout:
							orientation: 'vertical'		
							Image:
								id: fourth_week_img
								source: 'weather_icons/01d.png'
								pos_hint: {'center_x': 0.35, 'center_y': 0.393}
								
							MDLabel:
								id: id_fourth_week
								text: 'date'
								pos_hint: {'center_x': 0.58, 'center_y': 0.433}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H3'
								font_size: sp(18)
							
							MDLabel:
								id: week_display_fourth
								text: 'day'
								pos_hint: {'center_x': 0.6, 'center_y': 0.393}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(16)
							
							MDLabel:
								id: min_temp_fourth
								text: '--°C'
								pos_hint: {'center_x': .95, 'center_y': 0.393}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(16)
							
							MDLabel:
								id: max_temp_fourth
								text: '--°C'
								pos_hint: {'center_x': 1.1, 'center_y': 0.393}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(16)
							
							MDLabel:
								id: desc_temp_fourth
								text: ' '
								pos_hint: {'center_x': 1.25, 'center_y': 0.393}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(16)
						
						MDFloatLayout:
							orientation: 'vertical'		
							Image:
								id: fifth_week_img
								source: 'weather_icons/01d.png'
								pos_hint: {'center_x': 0.35, 'center_y': 0.283}
								
							MDLabel:
								id: id_fifth_week
								text: 'date'
								pos_hint: {'center_x': 0.58, 'center_y': 0.323}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H3'
								font_size: sp(18)
							
							MDLabel:
								id: week_display_fifth
								text: 'day'
								pos_hint: {'center_x': 0.6, 'center_y': 0.283}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(16)
							
							MDLabel:
								id: min_temp_fifth
								text: '--°C'
								pos_hint: {'center_x': .95, 'center_y': 0.283}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(16)
							
							MDLabel:
								id: max_temp_fifth
								text: '--°C'
								pos_hint: {'center_x': 1.1, 'center_y': 0.283}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(16)
							
							MDLabel:
								id: desc_temp_fifth
								text: ' '
								pos_hint: {'center_x': 1.25, 'center_y': 0.283}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H2'
								font_size: sp(16)
								
						MDFloatLayout:
							MDCard:
								id: hotline_bg
								pos_hint: {'center_x':0.5,'center_y':0.115}
								size_hint_x: 0.95
								size_hint_y: 0.21
								elevation: 0
								radius: [15,]
								md_bg_color: (216/255, 233/255, 243/255, 1)
							
							MDFloatLayout:
								orientation: 'vertical'	
								MDLabel:
									id: hotline_text
									text: 'Looking for Philippine Government Emergency Hotlines?'
									halign: 'center'
									pos_hint: {'center_y': 0.155}
									theme_text_color: 'Custom'
									text_color: app.theme_cls.primary_dark
									font_style: 'Overline'
									font_size: sp(20)
								
								MDFillRoundFlatButton:
									id: hotline_button
									text: 'Click Me!'
									pos_hint: {'center_x': 0.5, 'center_y': 0.074}
									md_bg_color: app.theme_cls.primary_dark
									text_color: (1, 1, 1, 1)
									on_release: app.government_hotlines()
									
			MDBottomNavigationItem:
				text: "ARTICLE"
				name: "Article"
				icon: 'newspaper-variant-outline'
				
				FullImage:
					id: nav3bg_article
					source: 'bg_canvas/white.png'
				
				MDFloatLayout:
					MDFloatLayout:
						MDCard:
							id: article_buttons_bg
							pos_hint: {'center_x':0.5,'center_y':0.43}
							size_hint_y: 0.92
							elevation: 0
							radius: [30,]
							md_bg_color: (216/255, 233/255, 243/255, 1)
				
					MDFloatLayout:
						MDCard:
							id: disaster_management_bg
							pos_hint: {'center_x':0.5,'center_y':0.947}
							size_hint_x: 0.95
							size_hint_y: 0.1
							elevation: 8
							radius: [30,30, 15, 15]
							md_bg_color: (178/255, 211/255, 230/255, 1)
					
						MDFloatLayout:
							orientation: 'vertical'
							MDLabel:
								id: disaster_management
								text: 'Disaster Management'
								halign: 'center'
								pos_hint: {'center_y': 0.945}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'Overline'
								font_size: sp(35)
						
						MDFloatLayout:
							orientation: 'vertical'
							MDIcon:
								id: alert_circle_outline_bg
								icon: 'alert-circle-outline'
								text_size: [dp(24), dp(24)]
								theme_text_color: 'Custom'
								pos_hint: {'center_x': 0.538,'center_y': 0.845}
								text_color: app.theme_cls.primary_dark
								
							MDLabel:
								id: know_more
								text: 'Know More About Disaster?'
								pos_hint: {'center_x': 0.6, 'center_y': 0.845}
								theme_text_color: 'Custom'
								text_color: app.theme_cls.primary_dark
								font_style: 'H3'
								font_size: sp(23)
							
						MDFloatLayout:
							ScreenManager:
								MainScreen:
								ArticleOneScreen:
								ArticleTwoScreen:
								ArticleThreeScreen:
								ArticleFourScreen:
								ArticleFiveScreen:
								ArticleSixScreen:
								ArticleSevenScreen:
								ArticleEightScreen:
				
			MDBottomNavigationItem:
				text: "SETTING"
				name: "Settings Button"
				icon: 'tune'
				
				FullImage:
					id: nav4bg_setting
					source: 'bg_canvas/white.png'
				
				MDFloatLayout:
					MDCard:
						id: setting_bg
						pos_hint: {'center_x':0.5,'center_y':0.95}
						size_hint_x: 0.95
						size_hint_y: 0.1
						elevation: 0
						radius: [30,]
						md_bg_color: (216/255, 233/255, 243/255, 1)
					
					MDSwitch:
						id: switch
						pos_hint: {'center_x': 0.85, 'center_y': 0.95}
						on_active: app.check(*args)
						thumb_color: app.theme_cls.primary_dark
					
					MDLabel:
						id: dark_mode_text
						text: 'Dark Mode'
						pos_hint: {'center_x': 0.57, 'center_y': 0.95}
						theme_text_color: 'Custom'
						text_color: app.theme_cls.primary_dark
						font_style: 'H3'
						font_size: sp(20)	
			
				MDFloatLayout:
					MDCard:
						id: about_developer_bg
						pos_hint: {'center_x':0.5,'center_y':0.83}
						size_hint_x: 0.95
						size_hint_y: 0.1
						elevation: 0
						radius: [30,]
						md_bg_color: (216/255, 233/255, 243/255, 1)
					
					MDLabel:
						id: about_developer_text
						text: 'About Developer'
						pos_hint: {'center_x': 0.57, 'center_y': 0.83}
						theme_text_color: 'Custom'
						text_color: app.theme_cls.primary_dark
						font_style: 'H3'
						font_size: sp(20)	
					
					MDIconButton:
						id: information_variant_icon
						icon: 'information-variant'
						pos_hint: {'center_x': 0.85, 'center_y': 0.83}
						theme_text_color: 'Custom'
						text_color: app.theme_cls.primary_dark
						user_font_size: sp(35)
						on_release: app.show_details()
				
				MDFloatLayout:
					MDCard:
						id: about_app_bg
						pos_hint: {'center_x':0.5,'center_y':0.71}
						size_hint_x: 0.95
						size_hint_y: 0.1
						elevation: 0
						radius: [30,]
						md_bg_color: (216/255, 233/255, 243/255, 1)
					
					MDLabel:
						id: about_app_text
						text: 'About Real-Time Weather Forecast'
						pos_hint: {'center_x': 0.57, 'center_y': 0.72}
						theme_text_color: 'Custom'
						text_color: app.theme_cls.primary_dark
						font_style: 'H3'
						font_size: sp(20)	
					
					MDLabel:
						id: version_text
						text: 'Version: 1.0.0 beta'
						pos_hint: {'center_x': 0.63, 'center_y': 0.69}
						theme_text_color: 'Custom'
						text_color: app.theme_cls.primary_dark
						font_style: 'H2'
						font_size: sp(15)	
					
					MDIconButton:
						id: about_app_logo
						icon: 'logo/forecast_light_logo.png'
						pos_hint: {'center_x': 0.85, 'center_y': 0.71}
						theme_text_color: 'Custom'
						text_color: app.theme_cls.primary_dark
						user_font_size: sp(35)
						on_release: app.show_version()
						
<Content>
	BoxLayout:
		orientation: 'vertical'
		MDTextField:
			id: search
			hint_text: 'Search Location'
			icon_right: 'map-marker'
			helper_text: 'Provide a valid location'
			helper_text_mode: 'on_focus'
			color_mode: 'primary'
			icon_right_color: app.theme_cls.primary_dark
			multiline: False
			pos_hint: {'center_x': 0.5, 'center_y': 0.1}

<MainScreen>:
    name: 'main'
    MDRectangleFlatButton:
        text: 'What is a Disaster?'
        size_hint: 1, 0.1
        pos_hint: {'center_x':0.5,'center_y':0.75}
        theme_text_color: 'Custom'
		line_color: app.theme_cls.primary_dark
        on_press: root.manager.current = 'article_one'
       
	MDRectangleFlatButton:
		text: 'What is Hazard? How is it Classified?'
		size_hint: 1, 0.1
		pos_hint: {'center_x': 0.5, 'center_y': 0.65}
		theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		on_press: root.manager.current = 'article_two'
	
	MDRectangleFlatButton:
		text: 'Tornadoes, Typhoons, Cyclones'
		size_hint: 1, 0.1
		pos_hint: {'center_x': 0.5, 'center_y': 0.55}
		theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		on_press: root.manager.current = 'article_three'
		
	MDRectangleFlatButton:
		text: 'Disaster Preparedness'
		size_hint: 1, 0.1
		pos_hint: {'center_x': 0.5, 'center_y': 0.45}
		theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		on_press: root.manager.current = 'article_four'
	
	MDRectangleFlatButton:
		text: 'Donating Money or Supplies'
		size_hint: 1, 0.1
		pos_hint: {'center_x': 0.5, 'center_y': 0.35}
		theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		on_press: root.manager.current = 'article_five'
	
	MDRectangleFlatButton:
		text: 'Disaster Prevention'
		size_hint: 1, 0.1
		pos_hint: {'center_x': 0.5, 'center_y': 0.25}
		theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		on_press: root.manager.current = 'article_six'
	
	MDRectangleFlatButton:
		text: 'Disaster Recovery'
		size_hint: 1, 0.1
		pos_hint: {'center_x': 0.5, 'center_y': 0.15}
		theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		on_press: root.manager.current = 'article_seven'
	
	MDRectangleFlatButton:
		text: 'What is Vulnerability?'
		size_hint: 1, 0.1
		pos_hint: {'center_x': 0.5, 'center_y': 0.05}
		theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		on_press: root.manager.current = 'article_eight'

<ArticleOneScreen>:
    name: 'article_one'
	MDFloatLayout:
		MDCard:
			pos_hint: {'center_x':0.5,'center_y':0.43}
			size_hint_y: 0.92
			elevation: 0
			radius: [30,]
			md_bg_color: (216/255, 233/255, 243/255, 1)
	   
		MDIcon:
			icon: 'alert-circle-outline'
			text_size: [dp(24), dp(24)]
			theme_text_color: 'Custom'
			pos_hint: {'center_x': 0.538,'center_y': 0.834}
			text_color: app.theme_cls.primary_dark
								
		MDLabel:
			text: 'What Is a Disaster?'
			pos_hint: {'center_x': 0.6, 'center_y': 0.834}
			theme_text_color: 'Custom'
			text_color: app.theme_cls.primary_dark
			font_style: 'H3'
			font_size: sp(23)
			
    MDLabel:
        text: 'Newspapers, radio and television networks carry accounts of disasters striking many parts of the world almost every day. So what is a disaster? The term disaster owes its roots to the French word DESASTRE which is a mixture of the two terms DES meaning bad and ASTER meaning star. The term thus applies to BAD or EVIL STAR. A disaster can be defined as a serious disruption in the functioning of the community or society that causes extensive material, economic, social or environmental losses that exceed the ability of the affected society to use its own resources to cope.'
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.90, 1
		pos_hint: {'center_x': 0.5, 'center_y': 0.63}
		line_height: 1.5
	
	MDLabel:
        text: 'A disaster is a product from the combination of danger, vulnerability and inadequate capacity or steps to minimize the possible chances of risk.'
        halign: ('justify')
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.90, 1
		pos_hint: {'center_x': 0.5, 'center_y': 0.405}
		line_height: 1.5
	
	MDLabel:
        text: 'A disaster occurs when the vulnerable population is impacted by a disaster and causes damage, casualties and disruption. Any flood, earthquake or cyclone threat that is a triggering event along with greater vulnerability (insufficient access to services, sick and elderly people, lack of knowledge, etc) will result in a disaster that causes greater loss of life and property. For instance, an earthquake in an uninhabited desert, no matter how high the intensity produced, may not be considered as disaster.'
        halign: ('justify')
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.90, 1
		pos_hint: {'center_x': 0.5, 'center_y': 0.192}
		line_height: 1.5
		
    MDFillRoundFlatIconButton:
        icon: 'arrow-left-circle'
        pos_hint: {'center_x':0.87,'center_y':0.84}
        md_bg_color: app.theme_cls.primary_dark
        on_press: root.manager.current = 'main'

<ArticleTwoScreen>:
    name: 'article_two'
	MDFloatLayout:
    	pos_hint: {'center_x': 0.5, 'center_y': 0.385}		
		canvas:
			Color:
				rgb: (216/255, 233/255, 243/255, 200/255)
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: [30,]
						
		MDIcon:
			icon: 'alert-circle-outline'
			text_size: [dp(24), dp(24)]
			theme_text_color: 'Custom'
			pos_hint: {'center_x': 0.538,'center_y': 0.96}
			text_color: app.theme_cls.primary_dark
								
		MDLabel:
			text: 'What is Hazard? How is it Classified?'
			pos_hint: {'center_x': 0.6, 'center_y': 0.958}
			theme_text_color: 'Custom'
			text_color: app.theme_cls.primary_dark
			font_style: 'H3'
			font_size: sp(19)
			
    MDLabel:
        text: 'Hazard can be described as a dangerous condition or event that threatens or has the potential to cause injury to life or damage to property or the environment. The word hazard originates from the word HASARD in old French and AZ-ZAHR in Arabic, meaning CHANCE or LUCK. It is possible to group hazards into two broad categories, namely natural and manmade.'
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.90, 1
		pos_hint: {'center_x': 0.5, 'center_y': 0.68}
		line_height: 1.5
	
	MDLabel:
        text: '1. Natural hazards are hazards caused by natural occurrences that are (hazards with meteorological, geological or even biological origin). Cyclones, tsunamis, earthquakes and volcanic eruptions, which are exclusively natural, are examples of natural hazards. Landslides, floods, drought, fires, as their causes are both natural and man-made, are socio-natural hazards. For example, flooding may be caused by heavy rainfall, landslides, or the obstruction of human waste drains.'
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.85, 1
		pos_hint: {'center_x': 0.53, 'center_y': 0.405}
		line_height: 1.5
	
	MDLabel:
        text: '2. Hazards that are caused by human error are manmade hazards. Industries or energy generation facilities are associated with manmade hazards that include fires, hazardous waste leakage, pollution, dam failure, wars or civil unrest, etc.'
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.85, 1
		pos_hint: {'center_x': 0.53, 'center_y': 0.1658}
		line_height: 1.5
		
	MDFillRoundFlatIconButton:
        icon: 'arrow-left-circle'
        pos_hint: {'center_x':0.87,'center_y':0.84}
        md_bg_color: app.theme_cls.primary_dark
        on_press: root.manager.current = 'main'

<ArticleThreeScreen>:
    name: 'article_three'
	MDFloatLayout:
    	pos_hint: {'center_x': 0.5, 'center_y': 0.385}		
		canvas:
			Color:
				rgb: (216/255, 233/255, 243/255, 200/255)
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: [30,]
						
		MDIcon:
			icon: 'alert-circle-outline'
			text_size: [dp(24), dp(24)]
			theme_text_color: 'Custom'
			pos_hint: {'center_x': 0.538,'center_y': 0.96}
			text_color: app.theme_cls.primary_dark
								
		MDLabel:
			text: 'Tornadoes, Typhoons, Cyclones'
			pos_hint: {'center_x': 0.6, 'center_y': 0.96}
			theme_text_color: 'Custom'
			text_color: app.theme_cls.primary_dark
			font_style: 'H3'
			font_size: sp(20)
			
    MDLabel:
        text: 'There are high-speed storms, followed several times by heavy rainfall. These cause structural damage, broken overhead cables, and flood potential.'
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.90, 1
		pos_hint: {'center_x': 0.5, 'center_y': 0.76}
		line_height: 1.5
	
	MDLabel:
        text: 'Utility services may be interrupted due to damage to the structure and overhead wires. Heavy rainfall may also cause flooding. Sometimes these could last for a couple of days. In such situations, before these few days when the operations begin to subsidize, any reconstruction and relief activities will not even begin.'
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.90, 1
		pos_hint: {'center_x': 0.5, 'center_y': 0.605}
		line_height: 1.5
	
	MDLabel:
        text: 'The only positive thing about these kinds of natural disasters is that, due to the progress of metrological research, they can be forecast to a fair degree. And in most situations, its possible to get an alert of up to several days. Typically at least some protective steps - during these few days of alert - can be taken. A preventive measure will in most situations, include:'
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.90, 1
		pos_hint: {'center_x': 0.5, 'center_y': 0.405}
		line_height: 1.5
	
	MDLabel:
        text: '- Moving to safer areas, such as structurally sound houses, which are not susceptible to flooding.'
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.85, 1
		pos_hint: {'center_x': 0.53, 'center_y': 0.27}
		line_height: 1.5
	
	MDLabel:
        text: '- Not venturing out to sea etc for sports, fishing etc.'
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.85, 1
		pos_hint: {'center_x': 0.53, 'center_y': 0.22}
		line_height: 1.5
		
	MDFillRoundFlatIconButton:
        icon: 'arrow-left-circle'
        pos_hint: {'center_x':0.87,'center_y':0.84}
        md_bg_color: app.theme_cls.primary_dark
        on_press: root.manager.current = 'main'

	MDLabel:
        text: 'However, despite these warnings, property loss can not be significantly mitigated, since it is not possible to relocate immovable objects. Another important thing about these kinds of strong winds and precipitation is that they do not entirely occur at will. There are well-defined geographical regions that appear to see typhoon and cyclone events.'
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.90, 1
		pos_hint: {'center_x': 0.5, 'center_y': 0.1}
		line_height: 1.5

<ArticleFourScreen>:
    name: 'article_four'
	MDFloatLayout:
    	pos_hint: {'center_x': 0.5, 'center_y': 0.385}		
		canvas:
			Color:
				rgb: (216/255, 233/255, 243/255, 200/255)
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: [30,]
						
		MDIcon:
			icon: 'alert-circle-outline'
			text_size: [dp(24), dp(24)]
			theme_text_color: 'Custom'
			pos_hint: {'center_x': 0.538,'center_y': 0.96}
			text_color: app.theme_cls.primary_dark
								
		MDLabel:
			text: 'Disaster Preparedness'
			pos_hint: {'center_x': 0.6, 'center_y': 0.96}
			theme_text_color: 'Custom'
			text_color: app.theme_cls.primary_dark
			font_style: 'H3'
			font_size: sp(20)
			
    MDLabel:
        text: 'These operations are designed to reduce loss of life and harm by extracting individuals and property from a threatened area for example, and encouraging prompt and efficient evacuation, relief and recovery. The best way of reducing the effects of disasters is preparedness. Community-based planning and management should be a high priority in the management of physical therapy practice.'
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.90, 1
		pos_hint: {'center_x': 0.5, 'center_y': 0.68}
		line_height: 1.5
	
	MDFillRoundFlatIconButton:
        icon: 'arrow-left-circle'
        pos_hint: {'center_x':0.87,'center_y':0.84}
        md_bg_color: app.theme_cls.primary_dark
        on_press: root.manager.current = 'main'
       
<ArticleFiveScreen>:
    name: 'article_five'
	MDFloatLayout:
    	pos_hint: {'center_x': 0.5, 'center_y': 0.385}		
		canvas:
			Color:
				rgb: (216/255, 233/255, 243/255, 200/255)
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: [30,]
						
		MDIcon:
			icon: 'alert-circle-outline'
			text_size: [dp(24), dp(24)]
			theme_text_color: 'Custom'
			pos_hint: {'center_x': 0.538,'center_y': 0.96}
			text_color: app.theme_cls.primary_dark
								
		MDLabel:
			text: 'Donating Money or Supplies'
			pos_hint: {'center_x': 0.6, 'center_y': 0.96}
			theme_text_color: 'Custom'
			text_color: app.theme_cls.primary_dark
			font_style: 'H3'
			font_size: sp(23)
			
    MDLabel:
        text: 'Donation of money to established non-governmental agencies is the most efficient way of responding to disasters. Financial contributions allow professional relief organisations to purchase exactly what is most urgently needed and pay for the transportation necessary to distribute these supplies. The supplies can often be purchased locally, reducing transport and storage costs, stimulating local economies, providing employment and ensuring that supplies arrive as quickly as possible.'
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.90, 1
		pos_hint: {'center_x': 0.5, 'center_y': 0.65}
		line_height: 1.5
	
	MDLabel:
        text: 'Donating equipment and supplies can be more complicated. Before organising collections of physical therapy equipment and assistive devices, it is important to confirm with the relief agencies that there is a need for the items. It is important to have an accurate analysis of need in the disaster-stricken area before determining the response.'
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.90, 1
		pos_hint: {'center_x': 0.5, 'center_y': 0.39}
		line_height: 1.5
	
	MDLabel:
        text: 'Many groups raise money for disaster relief. Many are reputable, but some may not be. Whenever you make a donation it is prudent to take steps to ensure the money you are giving will be used for the intended purpose.'
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.90, 1
		pos_hint: {'center_x': 0.5, 'center_y': 0.215}
		line_height: 1.5
	
	MDFillRoundFlatIconButton:
        icon: 'arrow-left-circle'
        pos_hint: {'center_x':0.87,'center_y':0.84}
        md_bg_color: app.theme_cls.primary_dark
        on_press: root.manager.current = 'main'

<ArticleSixScreen>:
    name: 'article_six'
	MDFloatLayout:
    	pos_hint: {'center_x': 0.5, 'center_y': 0.385}		
		canvas:
			Color:
				rgb: (216/255, 233/255, 243/255, 200/255)
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: [30,]
						
		MDIcon:
			icon: 'alert-circle-outline'
			text_size: [dp(24), dp(24)]
			theme_text_color: 'Custom'
			pos_hint: {'center_x': 0.538,'center_y': 0.96}
			text_color: app.theme_cls.primary_dark
								
		MDLabel:
			text: 'Disaster Relief'
			pos_hint: {'center_x': 0.6, 'center_y': 0.96}
			theme_text_color: 'Custom'
			text_color: app.theme_cls.primary_dark
			font_style: 'H3'
			font_size: sp(23)
			
    MDLabel:
        text: 'There are activities that are intended to provide permanent disaster protection. Not all disasters, especially natural disasters, can be avoided, but good evacuation plans, environmental preparation and design standards can reduce the risk of loss of life and injury. In January 2005, 168 governments implemented the Hyogo System, a 10-year global strategy for natural disaster risk reduction. It offers guiding principles, priorities for action, and practical means for achieving disaster resilience for vulnerable communities.'
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.90, 1
		pos_hint: {'center_x': 0.5, 'center_y': 0.65}
		line_height: 1.5
	
	MDFillRoundFlatIconButton:
        icon: 'arrow-left-circle'
        pos_hint: {'center_x':0.87,'center_y':0.84}
        md_bg_color: app.theme_cls.primary_dark
        on_press: root.manager.current = 'main'

<ArticleSevenScreen>:
    name: 'article_seven'
	MDFloatLayout:
    	pos_hint: {'center_x': 0.5, 'center_y': 0.385}		
		canvas:
			Color:
				rgb: (216/255, 233/255, 243/255, 200/255)
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: [30,]
						
		MDIcon:
			icon: 'alert-circle-outline'
			text_size: [dp(24), dp(24)]
			theme_text_color: 'Custom'
			pos_hint: {'center_x': 0.538,'center_y': 0.96}
			text_color: app.theme_cls.primary_dark
								
		MDLabel:
			text: 'Disaster Relief'
			pos_hint: {'center_x': 0.6, 'center_y': 0.96}
			theme_text_color: 'Custom'
			text_color: app.theme_cls.primary_dark
			font_style: 'H3'
			font_size: sp(23)
			
    MDLabel:
        text: 'The people affected and the societies that help them are still vulnerable after emergency needs have been addressed and the initial crisis is over. Activities for recovery include infrastructure repair, health care and rehabilitation. These should be coupled with development activities such as the creation of human capital for health, and the development of policies and practices to prevent any similar situations.'
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.90, 1
		pos_hint: {'center_x': 0.5, 'center_y': 0.69}
		line_height: 1.5
	
	MDFillRoundFlatIconButton:
        icon: 'arrow-left-circle'
        pos_hint: {'center_x':0.87,'center_y':0.84}
        md_bg_color: app.theme_cls.primary_dark
        on_press: root.manager.current = 'main'

<ArticleEightScreen>:
    name: 'article_eight'
	MDFloatLayout:
    	pos_hint: {'center_x': 0.5, 'center_y': 0.385}		
		canvas:
			Color:
				rgb: (216/255, 233/255, 243/255, 200/255)
			RoundedRectangle:
				size: self.size
				pos: self.pos
				radius: [30,]
						
		MDIcon:
			icon: 'alert-circle-outline'
			text_size: [dp(24), dp(24)]
			theme_text_color: 'Custom'
			pos_hint: {'center_x': 0.538,'center_y': 0.96}
			text_color: app.theme_cls.primary_dark
								
		MDLabel:
			text: 'What is Vulnerability?'
			pos_hint: {'center_x': 0.6, 'center_y': 0.96}
			theme_text_color: 'Custom'
			text_color: app.theme_cls.primary_dark
			font_style: 'H3'
			font_size: sp(23)
			
    MDLabel:
        text: 'Vulnerability can be characterized as the extent to which, because of its nature, construction and proximity to hazardous terrain or a disaster-prone area, a community, structure, services or geographic area is likely to be damaged or disrupted by the impact of a specific hazard." Vulnerabilities can be divided into physical and socio-economic vulnerability.'
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.90, 1
		pos_hint: {'center_x': 0.5, 'center_y': 0.69}
		line_height: 1.5
	
	MDLabel:
        text: 'Physical Vulnerability: It involves principles of who and what, such as earthquakes or floods, can be affected or destroyed by natural hazards. It is dependent on the physical state and proximity, location and design of the danger of individuals and items at risk, such as buildings, facilities etc. It also relates to the technical capacity of buildings and structures during a hazard event to withstand the forces acting on them.'
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.85, 1
		pos_hint: {'center_x': 0.53, 'center_y': 0.435}
		line_height: 1.5

	MDLabel:
        text: "Socio-economic vulnerability: The degree to which a threat affects a population would be based not only on the physical components of vulnerability, but also on socio-economic circumstances. The strength of the effect is also determined by the socio-economic status of the population. Whenever there is a strong wind or cyclone, they are normally at risk and lose their shelters."
        halign: 'justify'
        theme_text_color: 'Custom'
		text_color: app.theme_cls.primary_dark
		font_stle: 'H1'
		font_size: sp(15)
		size_hint: 0.85, 1
		pos_hint: {'center_x': 0.53, 'center_y': 0.175}
		line_height: 1.5

	MDFillRoundFlatIconButton:
        icon: 'arrow-left-circle'
        pos_hint: {'center_x':0.87,'center_y':0.84}
        md_bg_color: app.theme_cls.primary_dark
        on_press: root.manager.current = 'main'

<-FullImage>:
	canvas:
		Color:
			rgb: (1, 1, 1)
		Rectangle:
			texture: self.texture
			size: self.width + 20, self.height + 20
			pos: self.x - 10, self.y - 10

<About>
	BoxLayout:
		orientation: 'vertical'
		MDLabel:
			text: 'Jerald Constantino is a second-year Computer Engineering student at Batangas State University, The National Engineering University, and is interested in any computer hardware and software-related topics.'
			halign: 'center'

<Version>
	BoxLayout:
		size_hint: (0.8, 1)
		orientation: 'vertical'
		
		MDLabel:
			text: 'This application was inspired by the weather conditions in the Philippines which are yearly visited by an average of 20 tropical cyclones.'
			halign: 'justify'
"""	