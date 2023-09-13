import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

st.title('Startup India website data')

# loading the CSV file name
df= pd.read_csv('startup_data.csv')
st.dataframe(df)

df_indu = df['Industry'].value_counts()
df_ind = {'Category': df_indu.index, 'Frequency': df_indu.values}
df_ind = pd.DataFrame(df_ind)

df_ind['Percentage'] = (df_ind['Frequency'] / df_ind['Frequency'].sum()) * 100
sampl = df_ind.head(10)

st.header('Distribution of top 10 Categories')

# Create a pie chart
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(sampl['Frequency'], labels=sampl['Category'], autopct='%1.1f%%', startangle=140)
ax.axis('off') 

# Display the pie chart using Streamlit
st.pyplot(fig)

# Preparing for state count
dfl=df['Location']
location_frequency = dfl.value_counts()
# Create a DataFrame from the location_frequency data
data = {'Location': location_frequency.index, 'Frequency': location_frequency.values}
df_co = pd.DataFrame(data)
# Split the "Location" column into two columns using a comma as the separator
df_co[['City', 'State/UT']] = df_co['Location'].str.split(',', expand=True)
states_freq= df_co['State/UT'].value_counts() 
state_df = states_freq.to_frame()
state_df.reset_index(level=0, inplace=True)
state_df.columns = ['State', 'Count'] 


st.header ('states wise heat map')
# Load the geoJson into a GeoDataFrame
gdf_states = gpd.read_file('Indiamap.geojson')

#Merging the data
merged = gdf_states.set_index('STNAME').join(state_df.set_index('State'))
merged.reset_index(level=0, inplace=True)
merged['Count'] = merged['Count'].replace(np.nan, 0)

# Create figure and axes for Matplotlib and set the title
fig1, ax1 = plt.subplots(1, figsize=(10, 10))
ax1.axis('off')
ax1.set_title('Indian state-wise startups from Startup.gov.in', fontsize=16, fontweight='bold'  )

# Plot the figure
merged.plot(column='Count', cmap='YlOrRd', linewidth=0.8, ax=ax1, edgecolor='0', legend=True,
            legend_kwds={'label': "Number of Startups"})

# Display the Matplotlib plot using Streamlit
st.pyplot(fig1)

