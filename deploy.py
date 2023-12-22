import numpy as np
import streamlit as st
import pickle

loaded_model = pickle.load(open('C:/Users/arunk/Desktop/Final Mini/best_model_cb_pred.sav','rb'))


def prediction(new_entry):
    Predict_lr = loaded_model.predict(new_entry)
    outp = float(Predict_lr)
    return (outp)
   
def main():
    st.title("Calories burn prediction")
    gender = st.number_input("Enter Your Gender as (Female:0,Male:1) ",step=0,min_value=0, max_value=1)
    age = st.number_input("Enter Your Age: ",step=0,min_value=15, max_value=100)
    height = st.number_input("Enter Your Height (in cm) : ",step=0,min_value=100, max_value=200)
    weight = st.number_input("Enter Your Weight (in kg) : ",step=0,min_value=40, max_value=200)
    duration = st.number_input("Enter Your duration (in mins) : ",step=0,min_value=1, max_value=180)
    heart_rate = st.number_input("Enter Your Heart Rate from 60 to 130 : ",step=0,min_value=60, max_value=130 )
    body_temp = st.number_input("Enter Your Body temp from 36 to 42 (in celsius ) : ",step=0,min_value=36, max_value=42 )
    
    
    new_entry = [[gender,age,height,weight,duration,heart_rate,body_temp]]
    # ctreating a button for prediction
    if st.button('Calories burned'):
        predicted_lr = prediction(new_entry)
        st.write("Calories burned:")
        st.success(predicted_lr)
    
if __name__=='__main__':
    main()



