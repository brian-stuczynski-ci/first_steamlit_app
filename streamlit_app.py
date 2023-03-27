import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

streamlit.header('Fruityvice Fruit Advice')

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

streamlit.write('The user entered ', fruit_choice)

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)

#dont not do anything past this line
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
# streamlit.text("The fruit load list contains:")
# streamlit.text(my_data_row)
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

fruit_choice_add = streamlit.text_input('What fruit would you like to add?','Jackfruit')

streamlit.write('The user added ', fruit_choice_add)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")