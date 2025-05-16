import requests
import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGraphicsDropShadowEffect)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPixmap,QPalette, QBrush, QLinearGradient, QColor)
from dotenv import load_dotenv
import random


class Page1(QWidget):
 
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.weather_label = QLabel(self)
        self.weatherdesc = QLabel("HOT",self)
        self.weather_emooji = QLabel("HOTEMOJI",self)
        self.get_movie_button = QPushButton("Get a Movie For this Weather",self)
        
        self.UI1()


    def UI1(self):
        

        vbox = QVBoxLayout()
        vbox.addWidget(self.weather_label)
        vbox.addWidget(self.weatherdesc)
        vbox.addWidget(self.weather_emooji)
        vbox.addWidget(self.get_movie_button)
        
        self.setLayout(vbox)
        self.weather_label.setAlignment(Qt.AlignCenter)
        self.weatherdesc.setAlignment(Qt.AlignCenter)
        self.weather_emooji.setAlignment(Qt.AlignCenter)

        self.weather_label.setObjectName("WeatherLabel")
        self.weatherdesc.setObjectName("weatherdesc")
        self.weather_emooji.setObjectName("emoji")
        self.get_movie_button.setObjectName("GetButton")
        
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(25)
        shadow.setXOffset(0)
        shadow.setYOffset(4)
        shadow.setColor(QColor(0,0,0,150))
        
        self.weather_label.setGraphicsEffect(shadow)
        self.weatherdesc.setGraphicsEffect(shadow)
        self.weather_emooji.setGraphicsEffect(shadow)
        self.get_movie_button.setGraphicsEffect(shadow)
        

        self.setStyleSheet("""  
            QLabel, QPushButton {
                font-family: Helvetica Neue;
                           }

            QLabel#WeatherLabel {
                font-size: 62px;
                font-style: bold;
                color: #2c3e50;
                           }
            
            QLabel#weatherdesc {
                font-size: 58px;
                font-weight: Demi bold;
                color: #2c3e50;
                           }

            QLabel#emoji {
                font-size: 60px;
                font-family: Noto Color Emoji;
                           }

            QPushButton#GetButton {
    background: qlineargradient(
        x1:0, y1:0, x2:0, y2:1,
        stop:0 #00b894,
        stop:1 #019875);
    color: white;
    border-radius: 10px;
    padding: 12px 25px;
    font-size: 16px;
    font-weight: 600;
    border: none;

}

QPushButton#GetButton:hover {
    background: qlineargradient(
        x1:0, y1:0, x2:0, y2:1,
        stop:0 #019875,
        stop:1 #00b894);

}

QPushButton#GetButton:pressed {
    background: #01775c;

}


""") #ADD DROP SHADOW, Better Front, Better Background 
        
        self.get_movie_button.clicked.connect(self.go_to_page2)
        self.get_weather()
        self.setMinimumSize(400,300)
        self.resize(500,400)

    def Location(self):                                   #ERROR Handling is pending
        res = requests.get("https://ipinfo.io/json")
        data = res.json()
        city = data.get("city")
        return city

    def get_weather(self):                         #Error handling is pending
        load_dotenv()
        api_key = os.getenv("api_key")
        city = self.Location()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"


        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["cod"]==200:
            self.display_weather(data)

    def go_to_page2(self):
        self.stacked_widget.setCurrentIndex(1)

    def display_weather(self,data):
        temp = data["main"]["temp"]
        real_temp = temp - 273
        desc = data["weather"][0]["description"]
        weather_id  = data["weather"][0]["id"]
        print(data)

        self.weather_label.setText(f"{round(real_temp)}°C {self.Location()}")
        self.weatherdesc.setText(f"{desc}")
        self.weather_emooji.setText(f"{self.get_emoji(weather_id)}")

    
    #Another function to display errors

    @staticmethod
    def get_emoji(weather_id):
        if weather_id >= 200:
            return "⛈️"
        elif weather_id >= 300:
            return "🌧️"
        elif weather_id >= 500:
            return "🌧️"
        elif weather_id >= 600:
            return "❄️"
        elif weather_id >= 700:
            return "🌫️"
        elif weather_id == 800:
            return "☀️"
        elif weather_id > 800:
            return "☁️"
        


class Page2(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.movie_label = QLabel("Movie",self)
        self.movies_rating = QLabel("9.0", self)
        self.refresh_button = QPushButton("Reload", self)
        self.back_button = QPushButton("Back", self)    
    
        self.initUI()
    
    def initUI(self):   #Initial UI to be set, CSS, Get Pictures somehow
        
        vbox = QVBoxLayout()

        vbox.addWidget(self.movie_label)
        vbox.addWidget(self.movies_rating)
        vbox.addWidget(self.refresh_button)
        vbox.addWidget(self.back_button)

        self.setLayout(vbox)

        self.movie_label.setAlignment(Qt.AlignCenter)
        self.movies_rating.setAlignment(Qt.AlignCenter)

        self.movie_label.setObjectName("movieLabel")
        self.movies_rating.setObjectName("Rating")
        self.refresh_button.setObjectName("RefreshButton")
        self.back_button.setObjectName("BackButton")

        self.setStyleSheet("""

            QLabel, QPushButton {
                font-family: Helvetica Neue;
                           }

            QLabel#movieLabel {
                font-size: 62px;
                font-weight: 600;
                color: #2c3e50;
                           }
            
            QLabel#Rating {
                font-size: 45x;
                font-weight: 200;
                color: #2c3e50;
                           }


            QPushButton#RefreshButton {
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 #00b894,
                    stop:1 #019875);
                color: white;
                border-radius: 10px;
                padding: 12px 25px;
                font-size: 16px;
                font-weight: 600;
                border: none;

}

QPushButton#RefreshButton:hover {
    background: qlineargradient(
        x1:0, y1:0, x2:0, y2:1,
        stop:0 #019875,
        stop:1 #00b894);

}

QPushButton#RefreshButton:pressed {
    background: #01775c;
}

QPushButton#BackButton {
    background: qlineargradient(
        x1:0, y1:0, x2:0, y2:1,
        stop:0 #00b894,
        stop:1 #019875);
    color: white;
    border-radius: 10px;
    padding: 12px 25px;
    font-size: 16px;
    font-weight: 600;
    border: none;

}

QPushButton#BackButton:hover {
    background: qlineargradient(
        x1:0, y1:0, x2:0, y2:1,
        stop:0 #019875,
        stop:1 #00b894);

}

QPushButton#BackButton:pressed {
    background: #01775c;
}

                            """)
                
        self.back_button.clicked.connect(self.go_to_page1)
        self.refresh_button.clicked.connect(self.refresh)
        self.to_getMovie()

        
    def get_genre(self):
        load_dotenv()
        api_key = os.getenv("api_key")
        city = Page1.Location(self)
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"


        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        weather_id = data["weather"][0]["id"]
        
        if weather_id >= 200:
            return "53,27"
        elif weather_id >= 300:
            return "18,10749"
        elif weather_id >= 500:
            return "9648,80,18"
        elif weather_id >= 600:
            return "14,10751"
        elif weather_id >= 700:
            return "878,9648,36"
        elif weather_id == 800:
            return "12,35,28"
        elif weather_id > 800:
            return "99,10752,37"
        

    def to_getMovie(self):
        load_dotenv()
        api_key=os.getenv("api_key2")
        url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&vote_average.gte=6.0&with_genres={self.get_genre()}'

        response = requests.get(url)
        data = response.json()
        print(data)
        self.to_display_movie(data)
        
    def to_display_movie(self, data):
        self.data = data
        rand_movie = random.choice(data["results"])
        movie_name = rand_movie["title"]
        movie_rating = str(rand_movie["vote_average"])
        movie_rating_total = rand_movie["vote_count"]
        movie_desc = rand_movie["overview"]

        self.movie_label.setText(movie_name)
        self.movies_rating.setText(f"Rating: {movie_rating}")
        
    def refresh(self):
        
        data = self.data
        rand_movie = random.choice(data["results"])
        movie_name = rand_movie["title"]
        movie_rating = str(rand_movie["vote_average"])
        movie_rating_total = rand_movie["vote_count"]
        movie_desc = rand_movie["overview"]
        self.movie_label.setText(movie_name)
        self.movies_rating.setText(f"Rating: {movie_rating}")
    
    def to_displayError(self): #error handling
        pass

    #funtion to display error

    def go_to_page1(self):
        self.stacked_widget.setCurrentIndex(0)

class WeatherWatchlist(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget(self)
        self.page1 = Page1(self.stack)
        self.page2 = Page2(self.stack)

        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)
        
        self.setStyleSheet("background: linear-gradient(to right, #11998e, #38ef7d);")
        
        #gradient
        
        gradient = QLinearGradient(0, 0, self.width(), 0)  # Horizontal
        gradient.setColorAt(0.0, QColor("#d3d3d3"))  # Start
        gradient.setColorAt(1.0, QColor("#808080"))  # End

        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setAutoFillBackground(False)
        self.setPalette(palette)


        layout  = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)
        self.setWindowTitle("WeatherWatchlist")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_ = WeatherWatchlist()
    app_.show()
    sys.exit(app.exec_())
