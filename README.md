# Old Image Restorer App

A Python application utilizing OpenCV's inpainting and filtering techniques to restore old and damaged images. Developed as a Streamlit app, users can upload photos, paint over imperfections on a drawable canvas, and choose from advanced inpainting algorithms—Navier Stokes (NS) and Fast Marching Method (Telea)—to seamlessly blend repairs. The final restored image can be previewed and downloaded directly, simplifying photo restoration and making it accessible without the need for complex software. Features include removing scratches, blemishes, and other imperfections, with options to enhance and preserve the original quality of historical photographs.


## Live Application
Check out the live app here 👉 [Old Image Restorer App](https://old-image-restorer.streamlit.app/)


![image](https://github.com/Brandi-Kinard/old-image-restorer-app/blob/main/1.gif)

<br>

## Features
- **Image Upload**: Users can upload old or damaged images for restoration.
- **Interactive Canvas**: Draw directly on the image to mark areas that need restoration using a customizable stroke width.
- **Inpainting Techniques**: Choose between Telea and Navier-Stokes (NS) inpainting algorithms to restore the marked areas.
- **Comparison View**: Compare the results of Telea and NS inpainting side by side.
- **Download Restored Images**: Download the restored image in JPEG format.

<br>
<br>

![image](https://github.com/Brandi-Kinard/old-image-restorer-app/blob/main/4.gif)

<br>

## Usage

1. **Upload Image**:
   - Click on "Upload Image to restore:" in the sidebar to upload your image (PNG or JPG format).

2. **Mark Areas for Restoration**:
   - Use the canvas to draw over the areas of the image that need restoration. Adjust the stroke width using the slider in the sidebar.

3. **Select Inpainting Mode**:
   - Choose the inpainting mode from the dropdown menu in the sidebar (`None`, `Telea`, `NS`, or `Compare both`).

4. **View and Download Results**:
   - If `Telea` or `NS` mode is selected, the restored image will be displayed. You can download the result using the provided download link.
   - If `Compare both` is selected, the results of both algorithms will be displayed side by side. Download links for both results will be available.

<br>

## Watch the Demo 👇

<p align="center">
  <a href="https://vimeo.com/977449604" target="_blank">
    <img width="634" src="https://github.com/user-attachments/assets/bed5dee8-c035-44cf-abd5-f59202e043ca" alt="Watch the video" />
  </a>
</p>

<br>
<br>

## Installation

To run the app locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/old-image-restorer-app.git
   cd old-image-restorer-app
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the Streamlit app:
   ```bash
   streamlit run image_inpaint_streamlit.py

<br>

**Enjoy restoring your old images!**

<br>
<br>

![image](https://github.com/Brandi-Kinard/old-image-restorer-app/blob/main/5.gif)

![image](https://github.com/Brandi-Kinard/old-image-restorer-app/blob/main/6.gif)

![image](https://github.com/Brandi-Kinard/old-image-restorer-app/blob/main/7.gif)

## 👋 Get in Touch
[![text](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/brandi-kinard)



