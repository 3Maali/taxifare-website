import streamlit as st
import requests

import random
import folium
from streamlit_folium import st_folium
import numpy as np


'''
# Welcom to TaxiFareModel
'''
st.write("✨ Discover an exciting activity to enjoy your day in Riyadh — then calculate the taxi fare for your journey in just one click.")

st.logo(
    "https://imgs.search.brave.com/2_4Oh5PaVSzkunQOzsbyejsJGoRt66m2selCZnIoS0s/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzL2Y5L2Rj/L2Q0L2Y5ZGNkNGIz/YjUxN2JhZmZlZDgx/OWVkNzQ4MzdmMWYy/LmpwZw",
    link="https://streamlit.io/gallery",
    size="large",
    icon_image=None,
)

st.sidebar.markdown(f"Hey there! Join our community and connect with awesome people ready to dive into epic adventures together — let the journey begin!")


image_urls = [
    "https://cdn-icons-png.flaticon.com/512/3075/3075977.png",
    "https://cdn-icons-png.flaticon.com/512/3081/3081559.png",
    "https://cdn-icons-png.flaticon.com/512/869/869636.png",
    "https://cdn-icons-png.flaticon.com/512/2920/2920322.png",
    "https://cdn-icons-png.flaticon.com/512/809/809957.png",
    "https://cdn-icons-png.flaticon.com/512/3208/3208758.png"
]

titles = [
    "Eat", "Shopping", "Museums",
    "Sports", "Relaxing", "Adventure"
]


row1 = st.columns(3)
row2 = st.columns(3)

all_columns = row1 + row2

for i, col in enumerate(all_columns):
    with col.container(height=140):
        st.image(image_urls[i], width=60)
        st.markdown(f"**{titles[i]}**", unsafe_allow_html=True)




popover = st.popover("what kind of activity you like ?")
Eat = popover.checkbox("Eat", False)
Shopping = popover.checkbox("Shopping", False)
Museum = popover.checkbox("Museums", False)
Sports = popover.checkbox("Sports", False)
Relaxing = popover.checkbox("Relaxing", False)
Adventure = popover.checkbox("New Adventure", False)


if Eat:
    # st.write(":red[This is a red item.]")
    container = st.container(border=True)
    container.write("🍽️ Eat")
    container.write("Takya – Modern Saudi fusion cuisine located in Bujairi Terrace, offering a contemporary twist on traditional dishes. [24.7370, 46.5762]")
    container.write("LPM Riyadh – A renowned French-Mediterranean restaurant known for its elegant ambiance and exquisite menu. [24.6903, 46.6839]")
    container.write("Zafran Indian Bistro – Popular for its flavorful Indian dishes, with branches in The View Mall and Nakheel Mall. [24.7740, 46.6620]")
    st.write("This is outside the container")
if Shopping:
    # st.write(":blue[This is a blue item.]")
    container = st.container(border=True)
    container.write("🛍️ Shopping")
    container.write("Riyadh Park Mall – A favorite among locals, offering a variety of brands and a pleasant shopping environment. ")
    container.write("Kingdom Centre Tower – An iconic skyscraper housing luxury boutiques and offering panoramic city views")
    container.write("Al Nakheel Mall – Features a wide range of international brands and dining options, suitable for families and groups.")
    st.write("This is outside the container")
if Museum:
    # st.write(":green[This is a green item.]")
    container = st.container(border=True)
    container.write("🖼️ Museums")
    container.write("National Museum of Saudi Arabia – The kingdom's largest museum, showcasing Arabian history, culture, and art. ")
    container.write("Al Masmak Palace Museum – A historic fortress turned museum, offering insights into Riyadh's heritage. ")
    container.write("Saqer-Aljazirah Aviation Museum – Exhibits the evolution of aviation in Saudi Arabia, featuring aircraft displays and interactive exhibits. ")
    st.write("This is outside the container")
if Sports:
    # st.write(":white[This is a white item.]")
    container = st.container(border=True)
    container.write("🏋️ Sports")
    container.write("Padel Clubs – Padel is gaining popularity in Riyadh, with various clubs offering facilities and group sessions.")
    container.write("Kingdom Arena – A premier venue hosting major sporting events, including boxing matches and tennis tournaments.")

    st.write("This is outside the container")
if Relaxing:
    # st.write(":yellow[This is a yellow item.]")
    container = st.container(border=True)
    container.write("🌿 Relaxing")
    container.write("Diplomatic Quarter (DQ) – Known for its serene parks and walking trails, ideal for a peaceful retreat within the city. ")
    container.write("Bujairi Terrace – Offers a blend of dining and relaxation with views of the historic At-Turaif district. ")
    st.write("This is outside the container")
if Adventure:
    # st.write(":yellow[This is a yellow item.]")
    container = st.container(border=True)
    container.write("🧗 New Adventure")
    container.write("Edge of the World – A breathtaking geological wonder offering hiking opportunities and panoramic desert views. ")
    container.write("Red Sand Dunes – Engage in thrilling activities like quad biking, camel rides, and sandboarding in the desert landscape.")

    st.write("This is outside the container")


suggestions = [
    "🕌 Explore Diriyah At-Turaif District – a historic UNESCO World Heritage Site.",
    "🎉 Check out a Riyadh Season event nearby – could be a concert, food fest, or something wild!",
    "🌌 Visit Al Masmak Fort at night – peaceful, lit up, and less crowded.",
    "🌆 Head to the Sky Bridge at Kingdom Centre for epic city views.",
    "☕ Chill at Camel Step Coffee Roasters – a hidden gem with amazing brews.",
    "🍰 Relax at Urth Caffé for cozy vibes, food, and great atmosphere.",
    "🚗 Take a mini road trip to Lake Kharrarah National Park and enjoy a scenic picnic.",
    "🌿 Drive along Wadi Hanifa – beautiful stops, cafes, and natural beauty.",
    "🧩 Try an Escape Room with friends – puzzles, mystery, and fun team vibes.",
    "🎮 Dive into a VR game session at VOX Cinemas or Sparkys."
]

st.divider()

st.write("Not Sure What To Do? 🎲")
st.write("Click the button below and get a random suggestion to enjoy your day in Riyadh!")

if st.button("Give me a surprise! ✨"):
    suggestion = random.choice(suggestions)
    st.success(suggestion)



st.divider()
st.title("Calculate the Taxi fare 💰")
st.write(" Welcome  to the Taxi Fare API, Enter the required data of the ride and we will provide you the Taxi fare for it !")




pickup_datetime = st.text_input("Date and time (YYYY-MM-DD HH:MM:SS)", "2013-07-06 17:18:00")
pickup_longitude = st.text_input("Pickup Longitude", "-73.950655")
pickup_latitude = st.text_input("Pickup Latitude", "40.783282")
dropoff_longitude = st.text_input("Dropoff Longitude", "-73.984365")
dropoff_latitude = st.text_input("Dropoff Latitude", "40.769802")
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=10, value=1)


# st.write(f"The current data you entered is : Date and Time {DateTime} , pickup longitude {pickup_log} , pickup latitude {pickup_lat} , dropoff longitude {dropoff_log} ,  dropoff latitude {dropoff_lat } ,passenger count {passenger_count} ")
st.write(f"Your pickup date and time: {pickup_datetime} ")
st.write(f"Pickup: ({pickup_latitude}, {pickup_longitude})")
st.write(f"Dropoff: ({dropoff_latitude}, {dropoff_longitude})")
st.write(f"Passengers: {passenger_count}")




m = folium.Map(location=[pickup_longitude, pickup_latitude], zoom_start=15 , width=50 , height= 50)
folium.Marker(
    [pickup_longitude, pickup_latitude], popup="Saudi Digital Academy", tooltip="Saudi Digital Academy"
).add_to(m)

folium.Marker(
    [dropoff_longitude, dropoff_latitude], popup="Ministry of education station", tooltip="Ministry of education station"
).add_to(m)

st_data = st_folium(m, width=725)



params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": float(pickup_longitude),
    "pickup_latitude": float(pickup_latitude),
    "dropoff_longitude": float(dropoff_longitude),
    "dropoff_latitude": float(dropoff_latitude),
    "passenger_count": int(passenger_count)
}




'''


##
🤔 Woundring what is the taxi fare between your location and your destination ?? click on the button below
'''


if st.button("Predict Fare 💡" , use_container_width = 100):

    url = 'https://taxifare-780091880701.europe-west1.run.app/predict'
    # url = 'https://taxifare.lewagon.ai/predict'
    response = requests.get(url, params=params )

    if response.status_code == 200:
        prediction = response.json().get("fare", "No fare returned.")
        st.success(f"Predicted Fare: ${prediction:.2f}")
    else:
        st.error("API call failed. Please check your input or try again later.")
