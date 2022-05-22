import os
from pytube import YouTube
import re
import sqlite3
from opencage.geocoder import OpenCageGeocode
from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup
import mechanize
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.config import Config
from kivymd.uix.button import MDFloatingBottomButton
from kivy_garden.mapview import MapView
from kivy_garden.mapview import MapMarker
from kivy.uix.button import Button
from kivy.utils import platform




if platform not in ["android", "ios"]:
    Window.size = (340,650)

if platform == 'android':
    import android
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
    from android.storage import primary_external_storage_path
    dir = primary_external_storage_path()
    download_dir_path = os.path.join(dir, 'Download')

Config.set('graphics', 'resizable', True)


EMAIL_REGEX = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')


class WelcomeScreen(Screen):
    
    def on_enter(self, *args):
        if os.path.exists("userProfilelog.json"):
            Clock.schedule_once(self.switch_to_home, 5)        
        else:
            Clock.schedule_once(self.switch_to_home, 5)

    def switch_to_home(self, dt):
        if os.path.exists("userProfilelog.json"):
            self.manager.current = 'homescreen'
            self.manager.transition.direction = 'left'
        else:
            self.manager.current = 'loginscreen'
            self.manager.transition.direction = 'left'
    
class HomeScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class SignUpScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class InfoTable(Screen):
    # Creating Table For Information
    def add_datatable(self):
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint ={'center_x':0.5, 'center_y':0.55},
            size_hint=(0.9, 0.57),
            column_data=[
                ("", dp(30)),
                ("", dp(10)),
                ("", dp(30)),
            ],
            row_data=[
                (
                    "Phone Number",
                    ":", 
                    M1,
                    
                ),
                (
                    "Location",
                    ":",
                    L1,
                ),
                (
                    "Network Operator",
                    ":",
                    N1,
                ),
                (
                    "Signaling",
                    ":",
                    S1,
                ),
                (
                    "Connection Status",
                    ":",
                    C1,
                ),
            ]
        )
        self.add_widget(self.data_tables)
        return layout

    def on_enter(self):
        self.add_datatable()

class CodeTable(Screen):
    def add_codetable(self):
        layout = AnchorLayout()
        self.IDEA = MDDataTable(
            pos_hint ={'center_x':0.5, 'center_y':0.45},
            size_hint=(0.9, 0.60),
            rows_num = 15,
            column_data=[
                ("", dp(50)),
                ("", dp(10)),
                ("", dp(50)),
            ],
            row_data=[
                (
                    "Balance Check",
                    ":",
                    "*199*2*1#",

                ),
                (
                    "Check Vi Recharge Offers",
                    ":",
                    "*199*1*7#",
                ),
                (
                    "Deactivate Vi DND Service",
                    ":",
                    "*STOP 0 To 1909",
                ),
                (
                    "Activate Vi DND Service",
                    ":",
                    "1909",
                ),
                (
                    "Vi Data Balance Check Code",
                    ":",
                    "*199*2*2#",
                ),
                (
                    "Vi 2G/3G/4GData Offers Check Code",
                    ":",
                    "*199*1*3#",

                ),
                (
                    "Vi Mobile Number Check Code",
                    ":",
                    "*111*2# | *131*1#",

                ),
                (
                    "Download Vi Mobile App	",
                    ":",
                    "*199*4#",

                ),
                (
                    "Vi APN Settings",
                    ":",
                    "*199*2*2#",

                ),
                (
                    "Vi Customer Care Number",
                    ":",
                    "199",

                ),
                (
                    "Start Vi Value Added Service (VAS)",
                    ":",
                    "*199*3*1#",

                ),
                (
                    "Check Vi Voice, SMS, Roaming Offers",
                    ":",
                    "*199*1*8#",

                )

            ]
        )
        self.add_widget(self.IDEA)
        return layout
    def add_codetable1(self):
        layout = AnchorLayout()
        self.RELIANCE = MDDataTable(
            pos_hint ={'center_x':0.5,'center_y':0.45},
            size_hint=(0.9, 0.60),
            elevation = dp(20),
            rows_num = 15,
            column_data=[
                ("", dp(50)),
                ("", dp(10)),
                ("", dp(50)),
            ],
            row_data=[
                (
                    "Know balance/Talktime",
                    ":",
                    "*333#",

                ),
                (
                    "Know Number",
                    ":",
                    "Dial *1#",
                ),
                (
                    "Check 4G data usage",
                    ":",
                    "MBAL to 55333",
                ),
                (
                    "Check prepaid balance & validity",
                    ":",
                    "SMS BAL to 199",
                ),
                (
                    "Know bill amount",
                    ":",
                    "SMS BILL to 199",
                ),
                (
                    "Check the current tariff plan",
                    ":",
                    "SMS MYPLAN to 199",
                ),
                (
                    "Activate 4G data",
                    ":",
                    "Call 1925 or SMS START to 1925",
                ),
                (
                    "Check net balance",
                    ":",
                    "use MyJio app",
                ),
                (
                    "Deactivate Jio Caller Tune",
                    ":",
                    "*333*3*1*2#",
                ),
                (
                    "Know Jio number of JioFi device",
                    ":",
                    "SMS JIO to 199",
                ),
                (
                    "Postpaid Main Menu",
                    ":",
                    "*111# or *222#",
                ),
                (
                    "Start Jio Postpaid Miss Call Alert Service	",
                    ":",
                    "*123*30#",
                )
            ]
        )
        self.add_widget(self.RELIANCE)
        return layout
    def add_codetable2(self):
        layout = AnchorLayout()
        self.AIRTEL = MDDataTable(
            pos_hint ={'center_x':0.5, 'center_y':0.45},
            size_hint=(0.9, 0.60),
            rows_num = 15,
            column_data=[
                ("", dp(50)),
                ("", dp(10)),
                ("", dp(50)),
            ],
            row_data=[
                (
                    "Balance Check USSD Code",
                    ":",
                    "*123#",
                ),
                (
                    "Number Check USSD Code	",
                    ":",
                    "*282#",
                ),
                (
                    "4G Data Balance Check Code	",
                    ":",
                    "*121*2# & Reply With ”1”",
                ),
                (
                    "Airtel Customer Care Number",
                    ":",
                    "198",
                ),
                (
                    "Complain Number",
                    ":",
                    "121",
                ),
                (
                    "Check Airtel Unlimited Packs",
                    ":",
                    "*121*1#",
                ),
                (
                    "Offers Check Code",
                    ":",
                    "*121#",
                ),
                (
                    "Plan Validity Check Code",
                    ":",
                    "*123#",
                ),
                (
                    "Data Charges Check Code",
                    ":",
                    "*121*7*5#",
                ),
                (
                    "Postpaid Current Bill Plan Check",
                    ":",
                    "SMS “”BP”” To 121",
                ),
                (
                    "Postpaid Due/Pending Amount Check",
                    ":",
                    "SMS “”OT”” To 121",
                ),
                (
                    "Airtel Postpaid Bill Payment Check	",
                    ":",
                    "SMS “”PMT”” To 121",
                ),
                (
                    "Postpaid Current Plan Usage Check	",
                    ":",
                    "SMS “”UNB”” To 121",
                ),
            ]
        )
        self.add_widget(self.AIRTEL)
        return layout
    def add_codetabl3(self):
        layout = AnchorLayout()
        self.BSNL = MDDataTable(
            pos_hint ={'center_x':0.5, 'center_y':0.45},
            size_hint=(0.9, 0.60),
            rows_num = 15,
            column_data=[
                ("", dp(50)),
                ("", dp(10)),
                ("", dp(50)),
            ],
            row_data=[
                (
                    "BSNL Net Balance Code",
                    ":",
                    "*124#",
                ),
                (
                    "BSNL Balance Check	",
                    ":",
                    "*123#",
                ),
                (
                    "BSNL 3G Net Balance Check ",
                    ":",
                    "*112#",
                ),
                (
                    "BSNL 2G Net Balance Check",
                    ":",
                    "*123*6# And *123*10#",
                ),
                (
                    "BSNL SMS Check	",
                    ":",
                    "*123*1#",
                ),
                (
                    "BSNL Night Data Balance Check Code	",
                    ":",
                    "*123*8#",
                ),
                (
                    "BSNL Internet Enquiry Numer",
                    ":",
                    "*234#",
                ),
                (
                    "BSNL Video Call Balance Check Code	",
                    ":",
                    "*123*9#",
                ),
                (
                    "4G data Balance Check",
                    ":",
                    "*124*2#",
                )
            ]
        )
        self.add_widget(self.BSNL)
        return layout
    def add_codetable4(self):
        layout = AnchorLayout()
        self.VI = MDDataTable(
            pos_hint ={'center_x':0.5, 'center_y':0.45},
            size_hint=(0.9, 0.60),
            rows_num = 15,
            column_data=[
                ("", dp(50)),
                ("", dp(10)),
                ("", dp(50)),
            ],
            row_data=[
                (
                    "Balance Check",
                    ":",
                    "*199*2*1#",

                ),
                (
                    "Check Vi Recharge Offers",
                    ":",
                    "*199*1*7#",
                ),
                (
                    "Deactivate Vi DND Service",
                    ":",
                    "*STOP 0 To 1909",
                ),
                (
                    "Activate Vi DND Service",
                    ":",
                    "1909",
                ),
                (
                    "Vi Data Balance Check Code",
                    ":",
                    "*199*2*2#",
                ),
                (
                    "Vi 2G/3G/4GData Offers Check Code",
                    ":",
                    "*199*1*3#",

                ),
                (
                    "Vi Mobile Number Check Code",
                    ":",
                    "*111*2# | *131*1#",

                ),
                (
                    "Download Vi Mobile App	",
                    ":",
                    "*199*4#",

                ),
                (
                    "Vi APN Settings",
                    ":",
                    "*199*2*2#",

                ),
                (
                    "Vi Customer Care Number",
                    ":",
                    "199",

                ),
                (
                    "Start Vi Value Added Service (VAS)",
                    ":",
                    "*199*3*1#",

                ),
                (
                    "Check Vi Voice, SMS, Roaming Offers",
                    ":",
                    "*199*1*8#",

                )

            ]
        )
        self.add_widget(self.VI)
        return layout
    def add_codetable5(self):
        layout = AnchorLayout()
        self.VODAFONE = MDDataTable(
            pos_hint ={'center_x':0.5, 'center_y':0.45},
            size_hint=(0.9, 0.60),
            rows_num = 15,
            column_data=[
                ("", dp(50)),
                ("", dp(10)),
                ("", dp(50)),
            ],
            row_data=[
                (
                    "Balance Check",
                    ":",
                    "*199*2*1#",

                ),
                (
                    "Check Vi Recharge Offers",
                    ":",
                    "*199*1*7#",
                ),
                (
                    "Deactivate Vi DND Service",
                    ":",
                    "*STOP 0 To 1909",
                ),
                (
                    "Activate Vi DND Service",
                    ":",
                    "1909",
                ),
                (
                    "Vi Data Balance Check Code",
                    ":",
                    "*199*2*2#",
                ),
                (
                    "Vi 2G/3G/4GData Offers Check Code",
                    ":",
                    "*199*1*3#",

                ),
                (
                    "Vi Mobile Number Check Code",
                    ":",
                    "*111*2# | *131*1#",

                ),
                (
                    "Download Vi Mobile App	",
                    ":",
                    "*199*4#",

                ),
                (
                    "Vi APN Settings",
                    ":",
                    "*199*2*2#",

                ),
                (
                    "Vi Customer Care Number",
                    ":",
                    "199",

                ),
                (
                    "Start Vi Value Added Service (VAS)",
                    ":",
                    "*199*3*1#",

                ),
                (
                    "Check Vi Voice, SMS, Roaming Offers",
                    ":",
                    "*199*1*8#",

                )

            ]
        )
        self.add_widget(self.VODAFONE)
        return layout
    def add_codetable6(self):
        layout = AnchorLayout()
        self.RELIANCEJIO = MDDataTable(
            pos_hint ={'center_x':0.5,'center_y':0.45},
            size_hint=(0.9, 0.60),
            elevation = dp(20),
            rows_num = 15,
            column_data=[
                ("", dp(50)),
                ("", dp(10)),
                ("", dp(50)),
            ],
            row_data=[
                (
                    "Know balance/Talktime",
                    ":",
                    "*333#",

                ),
                (
                    "Know Number",
                    ":",
                    "Dial *1#",
                ),
                (
                    "Check 4G data usage",
                    ":",
                    "MBAL to 55333",
                ),
                (
                    "Check prepaid balance & validity",
                    ":",
                    "SMS BAL to 199",
                ),
                (
                    "Know bill amount",
                    ":",
                    "SMS BILL to 199",
                ),
                (
                    "Check the current tariff plan",
                    ":",
                    "SMS MYPLAN to 199",
                ),
                (
                    "Activate 4G data",
                    ":",
                    "Call 1925 or SMS START to 1925",
                ),
                (
                    "Check net balance",
                    ":",
                    "use MyJio app",
                ),
                (
                    "Deactivate Jio Caller Tune",
                    ":",
                    "*333*3*1*2#",
                ),
                (
                    "Know Jio number of JioFi device",
                    ":",
                    "SMS JIO to 199",
                ),
                (
                    "Postpaid Main Menu",
                    ":",
                    "*111# or *222#",
                ),
                (
                    "Start Jio Postpaid Miss Call Alert Service	",
                    ":",
                    "*123*30#",
                )
            ]
        )
        self.add_widget(self.RELIANCEJIO)
        return layout
    def add_codetable7(self):
        layout = AnchorLayout()
        self.JIO = MDDataTable(
            pos_hint ={'center_x':0.5,'center_y':0.45},
            size_hint=(0.9, 0.60),
            elevation = dp(20),
            rows_num = 15,
            column_data=[
                ("", dp(50)),
                ("", dp(10)),
                ("", dp(50)),
            ],
            row_data=[
                (
                    "Know balance/Talktime",
                    ":",
                    "*333#",

                ),
                (
                    "Know Number",
                    ":",
                    "Dial *1#",
                ),
                (
                    "Check 4G data usage",
                    ":",
                    "MBAL to 55333",
                ),
                (
                    "Check prepaid balance & validity",
                    ":",
                    "SMS BAL to 199",
                ),
                (
                    "Know bill amount",
                    ":",
                    "SMS BILL to 199",
                ),
                (
                    "Check the current tariff plan",
                    ":",
                    "SMS MYPLAN to 199",
                ),
                (
                    "Activate 4G data",
                    ":",
                    "Call 1925 or SMS START to 1925",
                ),
                (
                    "Check net balance",
                    ":",
                    "use MyJio app",
                ),
                (
                    "Deactivate Jio Caller Tune",
                    ":",
                    "*333*3*1*2#",
                ),
                (
                    "Know Jio number of JioFi device",
                    ":",
                    "SMS JIO to 199",
                ),
                (
                    "Postpaid Main Menu",
                    ":",
                    "*111# or *222#",
                ),
                (
                    "Start Jio Postpaid Miss Call Alert Service	",
                    ":",
                    "*123*30#",
                )
            ]
        )
        self.add_widget(self.JIO)
        return layout
    def on_enter(self):
        if N1 == "RELIANCE":
            self.add_codetable1()
        elif N1 == "IDEA":
            self.add_codetable()
        elif N1 == "AIRTEL":
            self.add_codetable2()
        elif N1 == "BSNL":
            self.add_codetable3()
        elif N1 == "VI":
            self.add_codetable4()
        elif N1 == "VODAFONE":
            self.add_codetable3()
        elif N1 == "RELIANCEJIO":
            self.add_codetable6()
        elif N1 == "JIO":
            self.add_codetable6()
        else:
            pass

class MusicScreen(Screen):
    pass

class PopupScreen(Screen):
    pass


class MapScreen(Screen):
    def map_views(self):
        layout = BoxLayout ()
        self.map_view = MapView(lat= lat, lon= lng, zoom=13)
        self.map_marker=MapMarker()
        self.map_marker.lat=lat
        self.map_marker.lon=lng
        self.map_marker.source="Image/Map-Marker.png"
        self.map_view.add_marker(self.map_marker)
        self.add_widget(self.map_view)
        touchBarbtn1 = Button(text='Back', size_hint=(0.4, 0.05),pos =(100, 50),background_color =(0, 0, 128, 255))
        touchBarbtn1.bind(on_press=lambda x: self.window_close())
        self.add_widget(touchBarbtn1)

        return layout
    def on_enter(self):
        self.map_views()

    def window_close(self):
        self.manager.current = 'mainscreen'


sm = ScreenManager()
sm.add_widget(WelcomeScreen(name = 'welcomescreen'))
sm.add_widget(HomeScreen(name = "homescreen"))
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(SignUpScreen(name = 'signupscreen'))
sm.add_widget(MainScreen(name = 'mainscreen'))
sm.add_widget(InfoTable(name='infotable'))
sm.add_widget(CodeTable(name = 'codetable'))
sm.add_widget(MusicScreen(name = 'musicscreen'))
sm.add_widget(MapScreen(name = 'mapscreen'))
sm.add_widget(PopupScreen(name = 'popup'))

class NewApp(MDApp):
    data ={
        'Logout': 'logout',
        'Feedback': 'book-arrow-right',
    }



    def callback(self,instance):
        icon = instance.icon
        if isinstance(instance, MDFloatingBottomButton):
            if icon == 'logout':
                if os.path.exists("userProfilelog.json"):
                    os.remove("userProfilelog.json")
                self.strng.get_screen('loginscreen').manager.current = 'loginscreen'
                self.strng.get_screen('loginscreen').ids.logpassword_text_fied.text=''
                self.strng.get_screen('loginscreen').ids.logemail_text_fied.text=''
            elif icon == 'book-arrow-right':
                print('Open folder')

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.strng = Builder.load_string("ScreenManager")
        return self.strng

    def check_signup(self):
        self.username_text = self.strng.get_screen('signupscreen').ids.username_text_fied.text
        self.password_text = self.strng.get_screen('signupscreen').ids.password_text_fied.text
        self.repassword_text = self.strng.get_screen('signupscreen').ids.repassword_text_fied.text
        self.email_text = self.strng.get_screen('signupscreen').ids.email_text_fied.text

        if self.password_text.split() == [] or self.repassword_text.split() == [] or self.email_text.split() == [] or self.username_text.split() == []:
            cancel_btn_emptyentry_dialogue = MDFlatButton(text='Retry', on_release = self.close_entry_dialogue)
            self.dialog = MDDialog(title = 'Requied',text = "Fill all requied entries", size_hint = (0.7,0.2), buttons = [cancel_btn_emptyentry_dialogue])
            self.dialog.open()

        elif not EMAIL_REGEX.match(self.email_text):
            cancel_btn_emptyentry_dialogue = MDFlatButton(text='Retry', on_release = self.close_entry_dialogue)
            self.dialog = MDDialog(title = 'Invalid Email',text = "Enter a vaild email with characters and @", size_hint = (0.7,0.2), buttons = [cancel_btn_emptyentry_dialogue])
            self.dialog.open()


        elif len(self.password_text) <= 7:
            cancel_btn_password_dialogue = MDFlatButton(text = "Retry", on_release = self.close_entry_dialogue)
            self.dialog = MDDialog(title = 'Too short password',text = "password should have minimum 8 characters ", size_hint = (0.7,0.2), buttons = [cancel_btn_password_dialogue])
            self.dialog.open()

        elif self.password_text != self.repassword_text :
            cancel_btn_password_dialogue = MDFlatButton(text = "Retry", on_release = self.close_entry_dialogue)
            self.dialog = MDDialog(title = 'Invalid Pasword',text = "Password & confirmpassword must be same", size_hint = (0.7,0.2), buttons = [cancel_btn_password_dialogue])
            self.dialog.open()

        else:
            conn = sqlite3.connect('Database.db')

            #Creating cursor
            with conn:
                cursor = conn.cursor()

                # Making table if not exist
                cursor.execute('CREATE TABLE IF NOT EXISTS Users (Username TEXT NOT NULL, Email TEXT NOT NULL, Password TEXT NOT NULL, RePassword TEXT NOT NULL)')
                # Inserting Data into Table
                cursor.execute('INSERT INTO Users (Username, Email, Password, RePassword) VALUES (?,?,?,?)', (self.username_text, self.email_text, self.password_text, self.repassword_text))
                conn.commit()

            self.strng.get_screen('signupscreen').ids.disabled_button.disabled = False

    def close_entry_dialogue(self,obj):
        self.dialog.dismiss()

    def clearentry(self):
        self.strng.get_screen('signupscreen').ids.username_text_fied.text=''
        self.strng.get_screen('signupscreen').ids.password_text_fied.text=''
        self.strng.get_screen('signupscreen').ids.repassword_text_fied.text=''
        self.strng.get_screen('signupscreen').ids.email_text_fied.text=''

    def clearentry_s(self):
        self.strng.get_screen('loginscreen').ids.logpassword_text_fied.text=''
        self.strng.get_screen('loginscreen').ids.logemail_text_fied.text=''

    def disbutton(self):
        self.strng.get_screen('signupscreen').ids.disabled_button.disabled = True

    def disbutton_s(self):
        self.strng.get_screen('loginscreen').ids.disabled_button.disabled = True


    def username_changer(self):
        pass

    def check_login(self):

        self.logemail_text = self.strng.get_screen('loginscreen').ids.logemail_text_fied.text
        self.logpassword_text = self.strng.get_screen('loginscreen').ids.logpassword_text_fied.text

        if self.logpassword_text.split() == [] or self.logemail_text.split() == [] :
            cancel_btn_emptyentry_dialogue = MDFlatButton(text='Retry', on_release = self.close_entry_dialogue)
            self.dialog = MDDialog(title = 'Requied',text = "Fill all requied entries", size_hint = (0.7,0.2), buttons = [cancel_btn_emptyentry_dialogue])
            self.dialog.open()

        elif os.path.exists("Database.db") == False:
            cancel_btn_emptyentry_dialogue = MDFlatButton(text='Retry', on_release = self.close_entry_dialogue)
            self.dialog = MDDialog(title = 'Wrong credentials',text = "Invalid email or password, user not found try to signup first", size_hint = (0.7,0.2), buttons = [cancel_btn_emptyentry_dialogue])
            self.dialog.open()

        else:
            conn = sqlite3.connect('Database.db')

            # Creating cursor
            with conn:
                cursor = conn.cursor()

                # Searching for users
                find_user = ('SELECT * FROM users WHERE Email = ? AND Password = ?')
                cursor.execute(find_user,(self.logemail_text, self.logpassword_text))
                results = cursor.fetchall()

                if results :
                    self.strng.get_screen('loginscreen').ids.disabled_button.disabled = False
                    self.store.put('UserInfo', email = self.logemail_text, password = self.logpassword_text)
                    self.username_changer_log()
                else:
                    cancel_btn_emptyentry_dialogue = MDFlatButton(text='Retry', on_release = self.close_entry_dialogue)
                    self.dialog = MDDialog(title = 'Wrong credentials',text = "Invalid email or password, user not found try to signup first", size_hint = (0.7,0.2), buttons = [cancel_btn_emptyentry_dialogue])
                    self.dialog.open()

    def username_changer_log(self):
        pass

    def on_start(self):
        self.store = JsonStore("userProfilelog.json")
        try:
            if self.store.get('UserInfo') != "":
                self.username_changer_log()
                self.strng.get_screen('welcomescreen').manager.current = 'welcomescreen'

        except KeyError:
            self.strng.get_screen('welcomescreen').manager.current = 'welcomescreen'

    def delete_josn(self):
        if os.path.exists("userProfilelog.json"):
            os.remove("userProfilelog.json")
        else:
            pass

    def find_info(self):

        self.number_text = self.strng.get_screen('mainscreen').ids.number_text_fied.text

        self.mc = mechanize.Browser()

        self.mc.set_handle_robots(False)

        self.url = 'https://www.findandtrace.com/trace-mobile-number-location'

        self.mc.open(self.url)

        self.mc.select_form(name ='trace')

        self.mc['mobilenumber'] = self.number_text # Enter a targeted mobile number

        self.res = self.mc.submit().read()

        self.soup = BeautifulSoup(self.res,'html.parser')

        self.tbl = self.soup.find_all('table',class_='shop_table')

        self.data = self.tbl[0].find_all("td")

        self.M1 = self.data[0].get_text()
        global M1
        M1 = self.M1

        self.L1 = self.data[1].get_text()
        global L1
        L1 = self.L1

        self.N1=self.data[2].get_text()
        global N1
        N1 = self.N1

        self.S1=self.data[4].get_text()
        global S1
        S1 = self.S1

        self.C1=self.data[5].get_text()
        global C1
        C1 = self.C1

        self.mylocation = self.data[1].get_text()
        global lat
        global lng
        if self. mylocation == "Madhya Pradesh And Chhatisgarh":
            lat = 23.473324
            lng = 77.947998
        elif self.mylocation == "Bihar & Jharkhand":
            lat = 23.778540
            lng = 86.791760

        elif self.mylocation == "Jammu and Kashmir":
            lat = 33.2778
            lng = 75.3412

        elif self.mylocation == "Kerala & Lakshadweep":
            lat = 10.486799
            lng = 75.986746

        elif self.mylocation == "Bihar & Jharkhand":
            lat = 16.912640
            lng = 73.986775
        else:
            self.key = "6f7bbae2ad564ebeaa8c10af8f86744c"

            self.locator = Nominatim(user_agent="loction")

            self.location = self.locator.geocode(self.mylocation)

            self.geocoder = OpenCageGeocode(self.key)

            self.query = str(self.location)

            self.result = self.geocoder.geocode(self.query)

            self.lat = self.result[0]['geometry']['lat']


            lat = self.lat

            self.lng = self.result[0]['geometry']['lng']
            lng = self.lng

    def check_number(self):
        self.number_text = self.strng.get_screen('mainscreen').ids.number_text_fied.text
        if self.number_text.split() == []:
            cancel_btn_emptyentry_dialogue = MDFlatButton(text='Retry', on_release = self.close_entry_dialogue)
            self.dialog = MDDialog(title = 'Requied',text = "Fill all requied entries", size_hint = (0.7,0.2), buttons = [cancel_btn_emptyentry_dialogue])
            self.dialog.open()
        elif len(self.number_text)!=10:
            cancel_btn_emptyentry_dialogue = MDFlatButton(text='Retry', on_release = self.close_entry_dialogue)
            self.dialog = MDDialog(title = 'Requied',text = "Enter 10 Digits Number", size_hint = (0.7,0.2), buttons = [cancel_btn_emptyentry_dialogue])
            self.dialog.open()
        else:
            self.strng.get_screen('mainscreen').ids.third_disabled.disabled = False

    def downloadsong(self):

        self.link_text = self.strng.get_screen('musicscreen').ids.link_text_fied.text        

        if self.link_text.split() == []:
            cancel_btn_emptyentry_dialogue = MDFlatButton(text='Retry', on_release = self.close_entry_dialogue)
            self.dialog = MDDialog(title = 'Requied',text = "Enter Youtube url link", size_hint = (0.7,0.2), buttons = [cancel_btn_emptyentry_dialogue])
            self.dialog.open()
        else:
            self.strng.get_screen('popup').manager.current = 'popup'
            try:
                if self.strng.get_screen('popup').manager.current:
                    yt = YouTube(self.link_text)
                    # extract only audio
                    video = yt.streams.filter(only_audio=True).first()
                    destination = download_dir_path






























                    # download the file
                    out_file = video.download(output_path=destination)
                    print(yt.title, '~ viewed', yt.views,'times.')
                    # save the fileSS
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)
                    # result of success
                    print(yt.title + " has been successfully downloaded.")
                    self.progressbarEvent = Clock.schedule_interval(self.updateprogressbar, 0.2)
                else:
                    pass
            except:
                pass
        
    def updateprogressbar(self,value):
        self.progressbar = self.strng.get_screen('popup').ids.download_progress_bar
        if self.progressbar.value <100:
            self.progressbar.value +=1


    def back_home(self):
        self.strng.get_screen('homescreen').manager.current = 'homescreen'



if __name__ == "__main__":
    NewApp().run()
                                   
