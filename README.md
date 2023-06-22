<img width="524" alt="image" src="https://github.com/Dhru007/COLOR_DETECTION/assets/103928261/b5878602-a863-4b34-9aba-44cee70ef856">
# COLOR_DETECTION

This Python script allows you to detect colors from an image by clicking on pixels and displaying the color information. The script uses a predefined color dataset to match the RGB values of the clicked pixel and determine the corresponding color name.

## Requirements

- Python 3.11.3
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)
- Pandas (`pip install pandas`)

## Usage

1. Clone the repository or download the Python script to your local machine.
2. Place an image file in the same directory as the script.
3. Run the script using the command: `python color_detection.py`.
4. Enter the path to the image when prompted.
5. A window will open displaying the image.
6. Double-click on any pixel in the image to detect the color.
7. The detected color, along with its RGB values, will be displayed on the image.
8. The color name will be shown in white if the color is dark, and in black if the color is light.

## Dataset

The script uses a dataset (`colors.csv`) containing a list of color names and their corresponding RGB values. You can modify or expand this dataset as per your requirements. The dataset should follow the structure: color, color_name, hex, R, G, B.


## Sample Output

![Sample Output](output.png)

## License

Feel free to contribute by reporting issues, suggesting improvements, or submitting pull requests.

# Color-Detection-System-

Color Detection System using Machine Learning Techniques- 
The system is based on supervised learning to determine the colour of objects in the image. It will detect the colour of an object from 
the given image using Convolutional Neural Network (CNN). The CNN will be trained on an image database containing known coloured objects. 
The system will show the colour of the object in the image with confidence in the prediction.The system can be used in many applications 
such as fruit and vegetable sorting, crop tracking and medical imaging.


