import streamlit as st

st.header('BMI Calculator')

try:
    weight = st.number_input('Enter your weight (in kgs)')
    height = st.number_input('Enter your height (in cm)')
    height = float(height)
    if st.button('Calculate BMI'):
        bmi = weight / ((height/100)**2)
        st.write(f'Your BMI is {bmi}')
        if bmi < 18.5:
            st.write('You are underweight')
        elif bmi >= 18.5 and bmi < 25:
            st.write('You are normal')
        elif bmi >= 25 and bmi < 30:
            st.write('You are overweight')
        elif bmi >= 30:
            st.write('You are obese')

except ZeroDivisionError:
    st.write('Height cannot be zero')

except Exception as e:
    st.write(e)
