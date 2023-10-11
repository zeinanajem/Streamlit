####################################################### LIBRARIES ########################################################
import pandas as pd
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit import components
#########################################################################################################################

######################################################### LOAD THE MALARIA DATASET #################################################
#file_url = 'https://github.com/AhmadBakkar/Malaria/blob/master/Malaria.csv'
#df = pd.read_csv(file_url)

df = pd.read_csv('World University Rankings 2023(1).csv')

st.set_page_config(page_title = 'University Ranking',
                    page_icon = 'bar_chart:',
                    layout = 'wide'
)

st.set_option('deprecation.showPyplotGlobalUse', False)


######################################################### TABS AND SESSIONS #################################################
# Create a dictionary to store the session state
session_state = st.session_state


# Create a selectbox widget in the sidebar to allow the user to choose a specific country
selected_country = st.sidebar.selectbox("Select a Country:", df['Location'].unique())


# Filter the data based on the selected country
filtered_df = df[df['Location'] == selected_country]


# Set the page title
st.title('University Ranking Dataset Dashboard')

######################################################################
df2 = df.head(100)
# Count the number of universities in each country
country_counts = df2['Location'].value_counts().reset_index()
country_counts.columns = ['Country', 'Count']

# Create a bar chart to display the count of top 100 universities in each country
st.title("Count of Top 100 Universities by Country")
fig = px.bar(country_counts, x='Country', y='Count', color='Count', labels={'Count': 'Number of Universities'})

# Customize the bar chart appearance
fig.update_layout(xaxis_title='Country', yaxis_title='Number of Universities')
st.plotly_chart(fig)
####################################################################3



# Convert 'No of student' column to a numeric data type (assuming it contains numbers)
st.title("Top 10 Universities with Highest Number of Students")
filtered_df['No of student'] = pd.to_numeric(filtered_df['No of student'], errors='coerce')  # 'coerce' converts non-numeric values to NaN

# Sort the DataFrame by 'No of student' column in descending order to get the top 10
df1 = filtered_df.sort_values(by='No of student', ascending=False).head(10)

# Create a bar chart using Streamlit's native charting capabilities
st.bar_chart(df1.set_index('Name of University')['No of student'])





####################################################################3

