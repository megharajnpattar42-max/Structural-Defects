import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# Configure The Model

genai.configure(api_key='AIzaSyBoeSXdufkVkNp4YlQEFmlDoWXLJ9PQWu4')
model=genai.GenerativeModel('gemini-2.5-flash-lite')


# Upload Image in Sidebar
st.sidebar.title(':red[UPLOAD YOUR IMAGE HERE]')
upload_image=st.sidebar.file_uploader("Upload your PDF file here",type=["pdf",'png','jpg','jpeg'])
if upload_image:
    image=Image.open(upload_image)
    st.sidebar.subheader(":blue[UPLOADED IMAGE]")
    st.sidebar.image(image)


# Create the main page

st.title(':orange[STRUCTURAL DEFECTS] : :green[AI Assisted Structural Defect Identifier in construction business]')
tips='''To use the application follow the steps below:

 * Upload the image of the structural defect in the sidebar.
 * Click on the button to generate the summary of the defect.
 * Click download to save the report generated.'''
st.write(tips)

prompt='''Assume you are a structural engineer. the user has provided an image of a structure. you need 
to identify the structural defect in the image and provide a detailed report on the defect.
The report should contain the following:
* it should start with title, prepared by and prepared for details. provided by the user
* Identify and classify the defect for eg: crack,spalling,corrosion,leakage etc.
* Explain the possible reasons for the defect.
* there could be more than one defect in the image. identify all the defects.
* for each defect identified provide the possible reasons.
* for each measure the severity of the defect as low, medium, high. also mention if the defect is in a critical location.
* also mention the time before this defect leads to permanent damage to the structure.
* provide short term and long term solutions for the defect.
* along with there estimated cost(in INR) and time required to implement the solution.
* what precuations to be taken to avoid this defect in future.
* suggest raw material with cost effective and long lasting.
* the report should be in the word format 
* use tables if required.
* show data in tabular format if required.
* use bullet points if required.
* make sure the the report should not exceed 3 pages.
* repport should professionally formatted. include all the sections mentioned above.as per project
report format.'''

if st.button('Generate report'):
    if upload_image is None:
        st.error('Please upload an image to procceed')
    else:
        with st.spinner('Generating Report...'):
            response= model.generate_content([prompt,image])
            st.write(response.text)
            st.download_button(
                label="Download Report",
                data=response.text,
                file_name="structural_defect_report.txt",
                mime="text/plain",
                )

       