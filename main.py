import streamlit as st
import snowflake.connector as snow
import pandas



st.title('Zena\'s Amazing Athleisure Catalog')

my_cnx = snow.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),CURRENT_REGION()")
my_data_row = my_cur.fetchone()

st.info("Hello from Snowflake:")
st.info(my_data_row)

# run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()
df = pandas.DataFrame(my_catalog)
color_list = df[0].values.tolist()
option = st.selectbox('Pick a sweatsuit color or style:', list(color_list))
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'

my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '" + option + "';")
df2 = my_cur.fetchone()
st.image(df2[0],width=400,caption= product_caption)
st.warning('Price: ', df2[1])
st.write('Sizes Available: ',df2[2])
st.write(df2[3])

