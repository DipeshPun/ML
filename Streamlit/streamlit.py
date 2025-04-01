import streamlit as st

#Title 
st.title("Hello World")

st.header("Header")

st.subheader("Subheader")

st.text("Dipesh text")

st.markdown("This is one markdown")

#Success, info, warning, error and value error
st.success("This is success message")
st.info("This is info message")
st.warning("This is warning message")
st.error("This is error message")
st.exception("This is value error")

#exception for division by zero
exp = ZeroDivisionError("Tring to divide by zero")
st.exception(exp)

st.write("This is write")
st.code("This is a code")

st.image("https://i0.wp.com/abtc.ng/wp-content/uploads/2022/04/RKO.webp?fit=624%2C390&ssl=1")

st.checkbox("Show/hide")
st.text("Show is showing")

#Radio button
status = st.radio("Select Gender:",("Male", "Female"))
if status=='Male':
    st.text("This is male ")
else:
    st.text("This female")
    

#add selectbox to select ml models
meta = st.selectbox("Select Model",("Dipesh","Pun","Magar"))
st.write("This is running",meta)

#multiple select box
models=st.multiselect("This is multibox",("Dipesh","Pun","Magar","Dell"))
st.write("This is running",models)

button= st.button("Submit")
if button:
    st.success("We are success")

#input
input = st.text_input("Enter the name", "")
if st.button("submit"):
    result = "Hello" + input
    st.write( result)


#slider
slide=st.slider("Select a level", 0, 10, 100)
st.progress(slide)
