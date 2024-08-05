# Old Image Restorer App

A Python application utilizing OpenCV's inpainting and filtering techniques to restore old and damaged images. Developed as a Streamlit app, users can upload photos, paint over imperfections on a drawable canvas, and choose from advanced inpainting algorithms—Navier Stokes (NS) and Fast Marching Method (Telea)—to seamlessly blend repairs. The final restored image can be previewed and downloaded directly, simplifying photo restoration and making it accessible without the need for complex software. Features include removing scratches, blemishes, and other imperfections, with options to enhance and preserve the original quality of historical photographs.


## Live Application
Check out the live app here: [Old Image Restorer App](https://old-image-restorer.streamlit.app/)


![image](https://github.com/user-attachments/assets/43000e4b-4018-4f2c-ae71-13bf7883e51b)

![image](https://github.com/user-attachments/assets/a9b8f2dc-4e7f-4a92-8ae8-5a4966614feb)

- **Image Upload**: Users can upload old or damaged images for restoration.
- **Interactive Canvas**: Draw directly on the image to mark areas that need restoration using a customizable stroke width.
- **Inpainting Techniques**: Choose between Telea and Navier-Stokes (NS) inpainting algorithms to restore the marked areas.
- **Comparison View**: Compare the results of Telea and NS inpainting side by side.
- **Download Restored Images**: Download the restored image in JPEG format.

![image](https://github.com/user-attachments/assets/a970fcf7-0e05-46cc-b8f2-1e3e05777f53)

![image](https://github.com/user-attachments/assets/6ba73c44-e78f-46d9-8d54-c0362efd5a10)

![image](https://github.com/user-attachments/assets/d868e63e-2db8-43ca-b58a-9bdc1e4bc420)

![image](https://github.com/user-attachments/assets/d2a910ef-af6a-4395-add8-b70776b8f7a9)

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

## Watch the Demo

<p align="center">
  <a href="https://vimeo.com/977449604" target="_blank">
    <img width="634" src="https://github.com/user-attachments/assets/bed5dee8-c035-44cf-abd5-f59202e043ca" alt="Watch the video" />
  </a>
</p>

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

Enjoy restoring your old images!

![image](https://github.com/user-attachments/assets/5bee23cf-3ba4-43d3-8372-31869c5c4822)



