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

selected_country = st.sidebar.selectbox("Select a Country:", ['All'] + df['Location'].unique().tolist())

if selected_country == 'All':
# Filter the data based on the selected country
    filtered_df = df
else:
    filtered_df = df[df['Location'] == selected_country]

# Set the page title
st.title('University Ranking Dataset Dashboard')

######################################################################
df2 = filtered_df.head(100)
# Count the number of universities in each country
country_counts = df2['Location'].value_counts().reset_index()
country_counts.columns = ['Country', 'Count']

##################################World Map#############################
st.title("top 100 university distribution around the World")

fig = px.choropleth(
    data_frame = country_counts,
    locations='Country',  # Column containing the country names
    locationmode='country names',
    color='Count',  # Column to determine the color of the regions
    hover_name='Country',  # Column to display on hover
    color_continuous_scale='Viridis',  # Choose a color scale
    projection='natural earth'  # Choose a map projection
)

# Format hover data
fig.update_traces(hovertemplate='<b>%{hovertext}</b><br>' +
                                'Cases: %{customdata[0]}<br>' +
                                'Deaths: %{customdata[1]}<br>' +
                                'Death Rate: %{customdata[2]:.2f}%'
                 )

# Set customdata for hover details
fig.data[0].customdata = country_counts[['Country', 'Count']]


fig.update_layout(
    width=1000,  # Set the width of the figure in pixels
    height=600  # Set the height of the figure in pixels
)

st.plotly_chart(fig)

st.markdown("A worldmap showing the distribution of top 100 universities around the world")
st.markdown("As you can see most of top notch universities are located in developed countries such as USA, UK, Canada and France")
##########################################################################

# Add a slider to filter the number of universities to display
num_universities_to_display = st.slider("Select Number of Universities to Display", min_value=1, max_value=100, value=0)

# Filter the data based on the selected number of universities
filtered_data2 = country_counts[country_counts['Count'] >= num_universities_to_display]

# Create a bar chart to display the count of top 100 universities in each country
st.title("Count of Top 100 Universities by Country")
fig = px.bar(filtered_data2, x='Country', y='Count', color='Count', labels={'Count': 'Number of Universities'})

# Customize the bar chart appearance
fig.update_layout(xaxis_title='Country', yaxis_title='Number of Universities')
st.plotly_chart(fig)

st.markdown("A bar chart showing the number of universities in each country")
st.markdown("USA is leading with 34 universities which is predictable since most ivy school are located in the states")
st.markdown("A slicer was added to filter based on the number of universities")
####################################################################3


# Convert 'No of student' column to a numeric data type (assuming it contains numbers)
st.title("Top 10 Universities with Highest Number of Students")
##filtered_df['No of student'] = pd.to_numeric(filtered_df['No of student'], errors='coerce')  # 'coerce' converts non-numeric values to NaN

# Remove commas from the 'No of student' column and then convert it to a numeric data type
filtered_df['No of student'] = pd.to_numeric(filtered_df['No of student'].str.replace(',', ''), errors='coerce')

# Keep only valid numeric values
filtered_df = filtered_df[pd.to_numeric(filtered_df['No of student'], errors='coerce').notna()]

# Sort the DataFrame by 'No of student' column in descending order to get the top 10
df1 = filtered_df.sort_values(by='No of student', ascending=False).head(10)


# Create a bar chart using Streamlit's native charting capabilities
st.bar_chart(df1.set_index('Name of University')['No of student'])

st.markdown("A bar chart showing top 10 univerisities with the most number of students around the world")
st.markdown("Tribhuvan university is ranked number 1 with more than 400,000 students")
st.markdown("the number of students is not specific whether those students are enrolled on or off campus")
st.markdown("A filter was added in order to specify the top 10 universities in a specific country")
####################################################################

st.title("University Data")
st.dataframe(df1)

