import streamlit as st 
import requests

st.set_page_config(
page_title="Our Streamlit App"
    
)
st.write("Hello World")


st.markdown("<h1>Hello<h1>", unsafe_allow_html=True)

st.markdown("""

<style>
button{
    color:white;
    background:red;
    border: 1px solid #ccc;
    border-radius:12px;
    padding:10px;
    width:100px;
}
</style>

<button>Click </button>
""",unsafe_allow_html=True)


name=st.text_input("Enter your name")
st.number_input("Enter your age",min_value=0,max_value=100,value=25)
# <label>Enter you age</label>
# <input type="number" min="0" max="100" value="25"/>

st.markdown("---")
# <hr/>

if st.button("Submit"):
    st.error("Error")
    # st.success("Success")
    # st.write("normal print")


r = requests.get("http://localhost:8001/items")

for item in r.json():
    st.write(item["name"])
