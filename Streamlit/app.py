import streamlit as st

weight = st.number_input('Weight (kg)', 0, 200)

height_format = st.radio('Height format', ('cms', 'meters', 'feet'))

height_value = st.number_input('Height', 0.0, 300.0)

button = st.button('Calculate BMI')

bmi = None

if button:
    if height_format == 'cms':
        height_in_meters = height_value / 100 
        bmi = weight / height_in_meters**2
    elif height_format == 'meters':
        bmi = weight / height_value**2
    elif height_format == 'feet':
        height_in_meters = height_value * 0.3048  
        bmi = weight / height_in_meters**2

    st.write(f'Your BMI is {bmi:.2f}')

if bmi is not None:
    if bmi < 16:
        st.write('Extremely Underweight')
        st.image("https://www.planetayurveda.com/pa-wp-images/underweight.jpg")
    elif bmi >= 16 and bmi < 18.5:
        st.write('Underweight')
        st.image("https://st3.depositphotos.com/6436316/12529/v/450/depositphotos_125297812-stock-illustration-young-man-in-white-shirt.jpg")
    elif bmi < 18.5 and bmi < 25:
        st.write('Healthy')
        st.image("https://www.foodsforbetterhealth.com/wp-content/uploads/2013/05/underweight.jpg")
    elif bmi < 25 and bmi < 30:
        st.write('Overweight')
        st.image("https://th.bing.com/th/id/OIP.EBUMGaZLfMhN6R8hS3iX7gHaE8?rs=1&pid=ImgDetMain")
    else:
        st.write('Moti')
        st.image("https://th.bing.com/th/id/OIP.FicFWLAkXrcSO35CPP7PtAHaEc?rs=1&pid=ImgDetMain")
        
        

