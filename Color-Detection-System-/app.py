import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
import plotly.express as px

# Title for the web app
st.title('Color Detection App')

# Load the CSV file with color information
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

# Function to get color name by matching RGB values
def getColorName(R, G, B):
    minimum = 10000
    cname = ""
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d < minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

# Upload image using Streamlit file uploader
uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Convert the uploaded image into a numpy array
    image = Image.open(uploaded_file)
    img_rgb = np.array(image)

    # Plotly expects an RGB image for rendering
    fig = px.imshow(img_rgb)

    # Display the image in the app using Plotly
    st.plotly_chart(fig, use_container_width=True)

    # Input fields for user to provide coordinates
    x = st.number_input("Enter X coordinate", min_value=0, max_value=img_rgb.shape[1]-1, step=1)
    y = st.number_input("Enter Y coordinate", min_value=0, max_value=img_rgb.shape[0]-1, step=1)

    if st.button("Detect Color"):
        # Get the RGB values at the user-provided coordinate
        r, g, b = img_rgb[int(y), int(x)]

        # Get the color name
        color_name = getColorName(r, g, b)

        # Display color information
        st.write(f"Detected Color: {color_name}")
        st.write(f"RGB Values: R={r}, G={g}, B={b}")
        st.write(f"Hex Code: #{'{:02x}{:02x}{:02x}'.format(r, g, b).upper()}")

        # Display the color visually
        st.write("Detected Color:")
        st.markdown(
            f'<div style="width:100px;height:50px;background-color:rgb({r},{g},{b});"></div>',
            unsafe_allow_html=True
        )
