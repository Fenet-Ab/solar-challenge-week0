import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, summary_table

# Load data
df = load_data()

# Streamlit page config
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

st.title("🌞 Solar Data Dashboard")
st.write("Interactive dashboard to explore solar metrics across Benin, Togo, and Sierra Leone")

# Sidebar for country selection
countries = st.sidebar.multiselect(
    "Select countries to display",
    options=df['Country'].unique(),
    default=list(df['Country'].unique())
)

# Sidebar for metric selection
metric = st.sidebar.selectbox(
    "Select metric to visualize",
    options=['GHI','DNI','DHI']
)

# Filter data based on selection
filtered_df = df[df['Country'].isin(countries)]

# Boxplot
st.subheader(f"{metric} Distribution by Country")
plt.figure(figsize=(8,5))
sns.boxplot(x='Country', y=metric, data=filtered_df)
plt.title(f"{metric} Distribution")
st.pyplot(plt)

# Summary Table
st.subheader(f"{metric} Summary Table")
table = summary_table(filtered_df, metric)
st.dataframe(table)

# Optional: Scatter plot with WS
if st.checkbox("Show Wind Speed vs. Metric scatter plot"):
    st.subheader(f"{metric} vs WS")
    plt.figure(figsize=(8,5))
    sns.scatterplot(x='WS', y=metric, hue='Country', data=filtered_df)
    st.pyplot(plt)
