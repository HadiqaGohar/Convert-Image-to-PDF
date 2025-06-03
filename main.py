# # # from fpdf import FPDF

# # # pdf = FPDF()

# # # for image in imagelist:
# # #     pdf.add_page()
# # #     pdf.image(image,x,y,w,h)
# # #     pdf("yourfile.pdf", "F")


# # import streamlit as st
# # from fpdf import FPDF
# # from PIL import Image # Used to get image dimensions
# # import io

# # def create_pdf_from_images(image_files, output_filename="output.pdf"):
# #     """
# #     Creates a PDF from a list of uploaded image files.
# #     Each image gets its own page.
# #     """
# #     pdf = FPDF()

# #     for img_file in image_files:
# #         try:
# #             # Read the image bytes from the uploaded file
# #             image_bytes = img_file.read()
            
# #             # Open image with PIL to get dimensions and convert if necessary
# #             img = Image.open(io.BytesIO(image_bytes))
            
# #             # Determine image format for FPDF
# #             if img.format == 'JPEG':
# #                 img_format = 'JPEG'
# #             elif img.format == 'PNG':
# #                 img_format = 'PNG'
# #             else:
# #                 # Convert to RGB if not JPEG/PNG (e.g., TIFF, WEBP, etc.)
# #                 # and save to a new BytesIO object for FPDF
# #                 st.warning(f"Converting {img_file.name} to JPEG for PDF compatibility.")
# #                 img = img.convert('RGB')
# #                 temp_img_buffer = io.BytesIO()
# #                 img.save(temp_img_buffer, format="JPEG")
# #                 image_bytes = temp_img_buffer.getvalue()
# #                 img_format = 'JPEG'

# #             # Add a page to the PDF. Default page size is A4 (210x297 mm)
# #             pdf.add_page()
            
# #             # Calculate aspect ratio to fit image on page
# #             img_width, img_height = img.size
# #             page_width = pdf.w - 2 * pdf.l_margin
# #             page_height = pdf.h - 2 * pdf.t_margin

# #             # Calculate scaling factor to fit image, preserving aspect ratio
# #             # Scale based on whichever dimension is larger relative to page
# #             width_ratio = page_width / img_width
# #             height_ratio = page_height / img_height
            
# #             scale = min(width_ratio, height_ratio)
            
# #             new_width = img_width * scale
# #             new_height = img_height * scale

# #             # Center the image on the page
# #             x_pos = (pdf.w - new_width) / 2
# #             y_pos = (pdf.h - new_height) / 2

# #             # Add the image to the PDF
# #             # FPDF expects image path or an opened file object (which BytesIO acts as)
# #             pdf.image(io.BytesIO(image_bytes), x=x_pos, y=y_pos, w=new_width, h=new_height, type=img_format)

# #         except Exception as e:
# #             st.error(f"Could not process image {img_file.name}: {e}")
# #             continue
    
# #     # Save the PDF to an in-memory bytes buffer
# #     pdf_output_bytes = pdf.output(dest='S').encode('latin1') # 'S' returns as string, then encode to bytes
# #     return pdf_output_bytes

# # st.set_page_config(
# #     page_title="Image to PDF Converter",
# #     layout="centered",
# #     icon="📄"
# # )

# # st.title("📸 Image to PDF Converter")
# # st.write("Upload your images, and I'll combine them into a single PDF document. Each image will be placed on its own page.")

# # # File uploader allows multiple image files
# # uploaded_files = st.file_uploader(
# #     "Choose image files (JPEG, PNG)", 
# #     type=["jpg", "jpeg", "png", "webp", "tiff", "bmp"], 
# #     accept_multiple_files=True
# # )

# # if uploaded_files:
# #     st.subheader("Uploaded Images:")
# #     for uploaded_file in uploaded_files:
# #         st.image(uploaded_file, caption=uploaded_file.name, width=150)
    
# #     output_pdf_name = st.text_input("Enter desired PDF filename (e.g., my_document.pdf):", "my_images.pdf")
# #     if not output_pdf_name.lower().endswith(".pdf"):
# #         output_pdf_name += ".pdf"

# #     if st.button("Generate PDF"):
# #         with st.spinner("Generating PDF... This might take a moment for large files."):
# #             pdf_bytes = create_pdf_from_images(uploaded_files, output_pdf_name)
            
# #             if pdf_bytes:
# #                 st.success("PDF generated successfully!")
# #                 st.download_button(
# #                     label="Download PDF",
# #                     data=pdf_bytes,
# #                     file_name=output_pdf_name,
# #                     mime="application/pdf"
# #                 )
# #             else:
# #                 st.error("Failed to generate PDF. Please check the uploaded images.")

# # st.markdown("---")
# # st.markdown("Made with ❤️ using Streamlit and FPDF2.")


# import streamlit as st
# from fpdf import FPDF
# from PIL import Image # Used to get image dimensions
# import io

# def create_pdf_from_images(image_files):
#     """
#     Creates a PDF from a list of uploaded image files.
#     Each image gets its own page, scaled to fit within A4 dimensions.
#     Returns the PDF as bytes.
#     """
#     # A4 dimensions in mm: 210 x 297
#     pdf = FPDF(unit="mm", format="A4")

#     for img_file in image_files:
#         try:
#             # Read the image bytes from the uploaded file
#             image_bytes = img_file.read()

#             # Use PIL to open the image and determine its properties
#             img = Image.open(io.BytesIO(image_bytes))

#             # FPDF typically handles JPEG and PNG well. For other formats,
#             # it's safer to convert them to JPEG.
#             img_format = img.format.upper()
#             if img_format not in ['JPEG', 'PNG']:
#                 st.warning(f"Converting '{img_file.name}' from {img_format} to JPEG for PDF compatibility.")
#                 img = img.convert('RGB') # Ensure it's in RGB mode for JPEG conversion
                
#                 # Save the converted image to a new BytesIO buffer
#                 temp_img_buffer = io.BytesIO()
#                 img.save(temp_img_buffer, format="JPEG")
#                 image_bytes = temp_img_buffer.getvalue()
#                 img_format = 'JPEG'
            
#             # Add a page. FPDF.add_page() adds a new page with default orientation (portrait)
#             # and dimensions (A4 if format="A4" was set).
#             pdf.add_page()

#             # Calculate image dimensions and position to fit on the page while maintaining aspect ratio
#             # and centering the image.
            
#             # Get available page width and height, considering margins (default 10mm each side)
#             # FPDF's default margins are 10mm left, right, top, bottom.
#             # pdf.w is page width, pdf.h is page height
#             page_width_mm = pdf.w - 2 * pdf.l_margin
#             page_height_mm = pdf.h - 2 * pdf.t_margin

#             # Get image pixel dimensions
#             img_pixel_width, img_pixel_height = img.size

#             # Calculate aspect ratios
#             img_aspect_ratio = img_pixel_width / img_pixel_height

#             # Calculate the dimensions the image will take on the PDF page
#             # based on fitting it within the available page area.
            
#             # If the image is wider than the page aspect ratio (meaning it's 'more horizontal')
#             if img_aspect_ratio > (page_width_mm / page_height_mm):
#                 # Scale primarily by width
#                 new_img_width_mm = page_width_mm
#                 new_img_height_mm = page_width_mm / img_aspect_ratio
#             else:
#                 # Scale primarily by height (or if aspect ratios are similar)
#                 new_img_height_mm = page_height_mm
#                 new_img_width_mm = page_height_mm * img_aspect_ratio
            
#             # Calculate x and y coordinates to center the image on the page
#             x_pos_mm = (pdf.w - new_img_width_mm) / 2
#             y_pos_mm = (pdf.h - new_img_height_mm) / 2

#             # Add the image to the PDF
#             # We pass the BytesIO object directly as FPDF can read from it.
#             pdf.image(io.BytesIO(image_bytes), x=x_pos_mm, y=y_pos_mm, 
#                       w=new_img_width_mm, h=new_img_height_mm, type=img_format)

#         except Exception as e:
#             st.error(f"⚠️ Could not process image '{img_file.name}': {e}")
#             # Optionally, you could skip this image or raise the error further
#             continue
    
#     # Save the PDF to an in-memory bytes buffer
#     # 'S' destination returns the document as a string. We then encode it to bytes.
#     # 'latin1' is a common encoding for FPDF output and safe for byte conversion.
#     pdf_output_bytes = pdf.output(dest='S').encode('latin1') 
#     return pdf_output_bytes

# # --- Streamlit UI ---

# # st.set_page_config(
# #     page_title="Image to PDF Converter",
# #     layout="centered",
# #     icon="📄" # This requires Streamlit 1.10.0+
# # )
# st.set_page_config(
#     page_title="Image to PDF Converter",
#     layout="centered",
#     # icon="📄" # Comment this line out if your Streamlit version is stubbornly old
# )

# st.title("📸 Image to PDF Converter")
# st.write("Upload your image files below. Each image will be placed on its own page in the generated PDF.")
# st.markdown("---")

# # File uploader allows multiple image files
# uploaded_files = st.file_uploader(
#     "Choose image files (JPEG, PNG, etc.)",
#     type=["jpg", "jpeg", "png", "webp", "tiff", "bmp", "gif"], # Added more common image types
#     accept_multiple_files=True,
#     help="Select one or more image files to combine into a PDF."
# )

# if uploaded_files:
#     st.subheader("🖼️ Images to be included:")
#     # Display uploaded images with a cleaner layout
#     cols = st.columns(5) # Create 5 columns for image previews
#     for i, uploaded_file in enumerate(uploaded_files):
#         with cols[i % 5]: # Place image in a column, cycling through columns
#             st.image(uploaded_file, caption=uploaded_file.name, width=100)
    
#     st.markdown("---")

#     # User input for PDF filename
#     default_filename = "my_document.pdf"
#     output_pdf_name = st.text_input(
#         "📝 Enter desired PDF filename:", 
#         value=default_filename,
#         help="The name of the PDF file when you download it."
#     )
    
#     # Ensure filename ends with .pdf
#     if not output_pdf_name.lower().endswith(".pdf"):
#         output_pdf_name += ".pdf"

#     # Button to trigger PDF generation
#     if st.button("✨ Generate PDF"):
#         if not uploaded_files:
#             st.warning("Please upload at least one image file to generate a PDF.")
#         else:
#             with st.spinner("⏳ Generating PDF... This might take a moment for many or large images."):
#                 pdf_bytes = create_pdf_from_images(uploaded_files)
                
#                 if pdf_bytes:
#                     st.success("🎉 PDF generated successfully!")
#                     st.download_button(
#                         label="⬇️ Download PDF",
#                         data=pdf_bytes,
#                         file_name=output_pdf_name,
#                         mime="application/pdf",
#                         help="Click to download your combined PDF file."
#                     )
#                 else:
#                     st.error("❌ Failed to generate PDF. Please check the uploaded images and try again.")
# else:
#     st.info("Upload images to start generating your PDF!")

# st.markdown("""
# <style>
# .footer {
#     position: fixed;
#     left: 0;
#     bottom: 0;
#     width: 100%;
#     background-color: #f0f2f6; /* Streamlit default background */
#     color: #888;
#     text-align: center;
#     padding: 10px;
#     font-size: 0.8em;
# }
# </style>
# <div class="footer">
#     Made with ❤️ using Streamlit and FPDF2.
# </div>
# """, unsafe_allow_html=True)

import streamlit as st
from fpdf import FPDF
from PIL import Image # Used to get image dimensions
import io

def create_pdf_from_images(image_files):
    """
    Creates a PDF from a list of uploaded image files.
    Each image gets its own page, scaled to fit within A4 dimensions.
    Returns the PDF as bytes.
    """
    # A4 dimensions in mm: 210 x 297
    pdf = FPDF(unit="mm", format="A4")

    for img_file in image_files:
        try:
            # Read the image bytes from the uploaded file
            image_bytes = img_file.read()

            # Use PIL to open the image and determine its properties
            img = Image.open(io.BytesIO(image_bytes))

            # FPDF typically handles JPEG and PNG well. For other formats,
            # it's safer to convert them to JPEG.
            img_format = img.format.upper()
            if img_format not in ['JPEG', 'PNG']:
                st.warning(f"Converting '{img_file.name}' from {img_format} to JPEG for PDF compatibility.")
                img = img.convert('RGB') # Ensure it's in RGB mode for JPEG conversion
                
                # Save the converted image to a new BytesIO buffer
                temp_img_buffer = io.BytesIO()
                img.save(temp_img_buffer, format="JPEG")
                image_bytes = temp_img_buffer.getvalue()
                img_format = 'JPEG'
            
            # Add a page. FPDF.add_page() adds a new page with default orientation (portrait)
            # and dimensions (A4 if format="A4" was set).
            pdf.add_page()

            # Calculate image dimensions and position to fit on the page while maintaining aspect ratio
            # and centering the image.
            
            # Get available page width and height, considering margins (default 10mm each side)
            # FPDF's default margins are 10mm left, right, top, bottom.
            # pdf.w is page width, pdf.h is page height
            page_width_mm = pdf.w - 2 * pdf.l_margin
            page_height_mm = pdf.h - 2 * pdf.t_margin

            # Get image pixel dimensions
            img_pixel_width, img_pixel_height = img.size

            # Calculate aspect ratios
            img_aspect_ratio = img_pixel_width / img_pixel_height

            # Calculate the dimensions the image will take on the PDF page
            # based on fitting it within the available page area.
            
            # If the image is wider than the page aspect ratio (meaning it's 'more horizontal')
            if img_aspect_ratio > (page_width_mm / page_height_mm):
                # Scale primarily by width
                new_img_width_mm = page_width_mm
                new_img_height_mm = page_width_mm / img_aspect_ratio
            else:
                # Scale primarily by height (or if aspect ratios are similar)
                new_img_height_mm = page_height_mm
                new_img_width_mm = page_height_mm * img_aspect_ratio
            
            # Calculate x and y coordinates to center the image on the page
            x_pos_mm = (pdf.w - new_img_width_mm) / 2
            y_pos_mm = (pdf.h - new_img_height_mm) / 2

            # Add the image to the PDF
            # We pass the BytesIO object directly as FPDF can read from it.
            pdf.image(io.BytesIO(image_bytes), x=x_pos_mm, y=y_pos_mm, 
                      w=new_img_width_mm, h=new_img_height_mm, type=img_format)

        except Exception as e:
            st.error(f"⚠️ Could not process image '{img_file.name}': {e}")
            continue
    
    # Save the PDF to an in-memory bytes buffer
    # Explicitly convert to 'bytes' object as Streamlit's download_button expects it.
    pdf_output_bytes = bytes(pdf.output(dest='S')) 
    return pdf_output_bytes

# --- Streamlit UI ---

st.set_page_config(
    page_title="Image to PDF Converter",
    layout="centered",
    # icon="📄" # This requires Streamlit 1.10.0+. Remove if still causing error.
)
# st.set_page_config(
#     page_title="Image to PDF Converter",
#     layout="centered",
#     # icon="📄" # Comment this line out if your Streamlit version is stubbornly old
# )

st.title("📸 Image to PDF Converter")
st.write("Upload your image files below. Each image will be placed on its own page in the generated PDF.")
st.markdown("---")

# File uploader allows multiple image files
uploaded_files = st.file_uploader(
    "Choose image files (JPEG, PNG, etc.)",
    type=["jpg", "jpeg", "png", "webp", "tiff", "bmp", "gif"], # Added more common image types
    accept_multiple_files=True,
    help="Select one or more image files to combine into a PDF."
)

if uploaded_files:
    st.subheader("🖼️ Images to be included:")
    # Display uploaded images with a cleaner layout
    cols = st.columns(5) # Create 5 columns for image previews
    for i, uploaded_file in enumerate(uploaded_files):
        with cols[i % 5]: # Place image in a column, cycling through columns
            st.image(uploaded_file, caption=uploaded_file.name, width=100)
    
    st.markdown("---")

    # User input for PDF filename
    default_filename = "my_document.pdf"
    output_pdf_name = st.text_input(
        "📝 Enter desired PDF filename:", 
        value=default_filename,
        help="The name of the PDF file when you download it."
    )
    
    # Ensure filename ends with .pdf
    if not output_pdf_name.lower().endswith(".pdf"):
        output_pdf_name += ".pdf"

    # Button to trigger PDF generation
    if st.button("✨ Generate PDF"):
        if not uploaded_files:
            st.warning("Please upload at least one image file to generate a PDF.")
        else:
            with st.spinner("⏳ Generating PDF... This might take a moment for many or large images."):
                pdf_bytes = create_pdf_from_images(uploaded_files)
                
                if pdf_bytes:
                    st.success("🎉 PDF generated successfully!")
                    st.download_button(
                        label="⬇️ Download PDF",
                        data=pdf_bytes, # This is now guaranteed to be 'bytes'
                        file_name=output_pdf_name,
                        mime="application/pdf",
                        help="Click to download your combined PDF file."
                    )
                else:
                    st.error("❌ Failed to generate PDF. Please check the uploaded images and try again.")
else:
    st.info("Upload images to start generating your PDF!")

st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f0f2f6; /* Streamlit default background */
    color: #888;
    text-align: center;
    padding: 10px;
    font-size: 0.8em;
}
</style>
<div class="footer">
    Made with ❤️ created by Hadiqa Gohar.
</div>
""", unsafe_allow_html=True)