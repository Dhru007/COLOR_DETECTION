# COLOR_DETECTION

This repository hosts the Color Detection App, a web-based tool for identifying colors in an uploaded image. Built using Python and Streamlit, the app provides a user-friendly interface for exploring RGB values, color names, and corresponding hexadecimal codes by selecting specific points in an image.

## Technology Stack

- Python Libraries:
  - pandas: For handling CSV files.
  - numpy: For image processing.
  - streamlit: For creating the web interface.
  - Pillow: For handling image uploads.
  - plotly.express: For interactive image rendering.

## Features

Upload Images: Supports image formats like .jpg, .jpeg, and .png.
Color Detection: Identifies the closest color name based on RGB values.
Hex Code Display: Shows the hex code of the detected color.
Interactive Visualization: Uses Plotly for rendering the uploaded image interactively.
User Inputs: Allows users to provide coordinates to detect specific colors in the image.
Live Color Preview: Displays a visual representation of the detected color.

## Usage

1. Launch the App: Open the app in your browser after running the Streamlit command.
2. Upload an Image: Use the Upload Image button to load your image.
3. Provide Coordinates: Enter the X and Y coordinates to select a pixel from the image.
4. Detect Color: Click the Detect Color button to view the detected color name, RGB values, and hex code.
5. Visual Feedback: The app displays a live color preview for better visualization.

## Dataset

The script uses a dataset (`colors.csv`) containing a list of color names and their corresponding RGB values. You can modify or expand this dataset as per your requirements. The dataset should follow the structure: color, color_name, hex, R, G, B.


## Sample Output

<img width="524" alt="image" src="https://github.com/Dhru007/COLOR_DETECTION/blob/main/Color-Detection-System-/img1.png">
<img width="524" alt="image" src="https://github.com/Dhru007/COLOR_DETECTION/blob/main/Color-Detection-System-/img2.png">


## Contribution
1. Fork the repository.
2. Create a new feature branch:
  - git checkout -b feature-name
3. Commit your changes:
  - git commit -m "Add feature description"
4. Push to the branch:
  - git push origin feature-name
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


## Feel free to contribute by reporting issues, suggesting improvements, or submitting pull requests.



