# app/myweatherpy.py

import os
import requests
import json
import re
import datetime

from dotenv import load_dotenv

load_dotenv()

api_key =os.environ.get("openweather_API") # to obtain API_KEY from env file. 
#
#
#
#
def get_response(symbol):  #> To define and return the result after user input. 
    request_url = f"api.openweathermap.org/data/2.5/weather?q=London,uk&APPID={api_key}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    #print(response.status_code) #> 200

    try:
        parsed_response["Time Series (Daily)"]
    except: #> "OOPS" will generate below error message
        print("-------------------------")
        print("ERROR MESSAGE:")
        print("SORRY. WE COULD NOT FIND ANY TRADING DATA FOR THE ENTERED STOCK SYMBOL.\n"+
        "PLEASE CHECK THE SYMBOL AND TRY IT AGAIN")
        exit()

    return parsed_response

if __name__ == "__main__":
    # Welcome message.

    print("Welcome to MyWeatherPy. We are here to help you to provide information\n"
            "about your curiosity in the weather condition anywhere")

    confirmation = input("Are you ready to explore MyWeatherPy? Please press n to exit.\n"
                "Otherwise, please press any button if you would like to proceed:  ")
    while True:
        if confirmation == "n":
            print("Thank you for considering, MyWeatherPy. We hope you visit us again in the future!")
            exit()

        else:
            user_input = input("Awesome choice ! Please enter zip code, or city name and state to start\n"
                                "For example, you can input 10004 or New York, NY: ")

        










                                
    # Decide whether we want to do command line style application or pop up screen, clickable type or HTML web application


    # Ask User Input


    # Request weather, condition, forecast etc using API credentials through HTML request

    # Ask wheather user wants to see historical data or forecast

    # Once result is showing, ask whether the user lives in the city, plans for trip or curious


    #if live in the city, advise things like take umbrella, be careful icy weather, use sunblock etc
    #if plan for trip, show other results - website to tripadvisor, priceline, avis car, marriott.com etc. then link it
    # if just curious, put a link to wikipedia to learn more about the city.


    # Search for more city, zip code, etc. 



    # Ask if user want to save the result? and store up to 5?



    # Ask if user wants to receive the information in the email. Weather they want to receive alert daily/weekly in the email.



