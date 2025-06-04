import streamlit as st
import pickle
import numpy as np
file=open(r"C:\Users\archi\OneDrive\Desktop\inteernship\model.pkl",'rb') 
model=pickle.load(file)
st.title("Weather Predictor")
st.write("Enter the input features to get a prediction")
a=st.number_input("enter the value of SO2")
b=st.number_input("enter the value of CO")
c=st.number_input("enter the value of NO")
d=st.number_input("enter the value of NO2")
e=st.number_input("enter the value of NOX")
f=st.number_input("enter the value of NH3")
g=st.number_input("enter the value of O3")
h=st.number_input("enter the value of WS")
i=st.number_input("enter the value of WD")
j=st.number_input("enter the value of RH")
k=st.number_input("enter the value of SR")
l=st.number_input("enter the value of TC")
if st.button("predict"):
    input_data=np.array([[a,b,c,d,e,f,g,h,i,j,k,l]])
    result=model.predict(input_data)
    st.write("predicted value:",result[0])
    if result<=50:
        label="good"
        color="green"
    elif result<=100:
        label="moderate"
        color="orange"
        
    else:
        label="poor"
        color="red"
    st.markdown(f"### Air Quality: <span style='color:{color};font-weight:bold'>{label}</span>",unsafe_allow_html=True)
import streamlit as st

# ✅ DESIGN & INTERACTION SECTION — put this outside any buttons

# 🔥 Inject CSS for animated background & style
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Animated gradient background */
.stApp {
    background: linear-gradient(-45deg, #1d2b64, #f8cdda, #1e3c72, #2a5298);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    color: #ffffff;
}

@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Card style */
.block-container {
    background-color: rgba(0, 0, 0, 0.6);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
}

/* Headings glow */
h1, h2, h3 {
    color: #00ffff !important;
    text-shadow: 0 0 10px #00ffff;
}

/* Expander background */
details {
    background-color: rgba(255, 255, 255, 0.05) !important;
    border-radius: 10px;
    padding: 0.5rem;
}

/* Footer */
.footer {
    text-align: center;
    color: #ccc;
    font-size: 13px;
    padding: 20px;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# 🌍 Title and Intro
st.markdown("## 🌫 Air Pollution Predictor")
st.markdown("""
Welcome to the *Air Pollution Prediction System*!  
This Machine Learning model helps predict the level of pollution in the air based on environmental sensor readings.

Understanding pollution is critical in today’s world as it affects health, environment, and climate. This model is built to assist researchers, students, and city planners in making informed decisions.
""")

# 🖼 Pollution Image
st.image("https://cdn.pixabay.com/photo/2017/01/20/00/30/pollution-1990110_1280.jpg",
         caption="Air pollution in an industrial city",
         use_container_width=True)

# 🔽 Interactivity: Expandable Sections
with st.expander("📌 What is Air Pollution?"):
    st.markdown("""
Air pollution is the presence of harmful or excessive quantities of substances in the air we breathe.  
It includes gases (like carbon monoxide), particulates (like PM2.5), and biological molecules.  

Key sources include:
- Vehicle emissions  
- Industrial processes  
- Burning fossil fuels  
- Agricultural chemicals  

Health effects include asthma, heart disease, and even premature death.
""")

with st.expander("🧠 How This ML Model Works"):
    st.markdown("""
This model uses *supervised learning* to predict pollution levels based on:
- Temperature  
- Humidity  
- Wind speed  
- Smoke levels  
- Other environmental sensor data

We trained the model on historical data and optimized it to classify pollution as *Low*, **Moderate**, or **High**.
""")

# 📊 Optional pollution summary if available
try:
    if 'data' in globals() and 'Pollution Level' in data.columns:
        st.subheader("📊 Pollution Level Summary")
        counts = data["Pollution Level"].value_counts()
        cols = st.columns(len(counts))
        for i, label in enumerate(counts.index):
            cols[i].metric(label=f"{label}", value=int(counts[label]))
except:
    pass  # Skips if data not defined

# 🔚 Footer
st.markdown('<div class="footer">Built with  by Archith Rajasekharan • BCA ML Project</div>', unsafe_allow_html=True)
