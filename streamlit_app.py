import streamlit
import pandas
import requests

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')

streamlit.text('Blueberry Oatmeal')

streamlit.text('Bacon Egg and Cheese')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

fruite_selected = streamlit.multiselect("Pick Some Fruit:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruite_selected]

streamlit.dataframe(fruits_to_show)

fruit_choice = streamlit.text_inut('What fruit would you like information about?','Kiwi')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

streamlit.header('Fruityvice Fruit Advice')

streamlit.write('The user entered ', fruit_choice)

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)