import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                                layout='wide',
                                page_icon='🧑‍⚕️')
diabetes_model = pickle.load(open("saved+models/diabetes_model3.sav", "rb"))
heart_model = pickle.load(open("saved+models/heart_model.sav", "rb"))
parkinsons_model = pickle.load(open("saved+models/parkinsons_model.sav", "rb"))

with st.sidebar:
    selected=option_menu("Prediction of Disease Outbreak System",['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                        menu_icon='hospital-fill', icons = ['activity','heart','person'],default_index=0)

if selected=='Diabetes Prediction':
    st.title('Diabetes Prediction Using ML')
    col1,col2,col3= st.columns(3)
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
        SkinThickness=st.text_input('Skin Thickness Value')
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Glucose=st.text_input('Glucose Level')
        Insulin=st.text_input('Insulin Level')
        Age=st.text_input('Age of the person')
    with col3:
        Bloodpressure=st.text_input('Blood Pressure Value')
        BMI=st.text_input('BMI Value')

    diab_diagnosis=''
    if st.button('Diabetes Test Result'):
        user_input=[Pregnancies,Glucose,Bloodpressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        user_input=[float(x) for x in user_input]
        diab_prediction= diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
            diab_diagnosis='The person is diabetic'
        else:
            diab_diagnosis='The person is not diabetic'
    st.success(diab_diagnosis)

if selected=='Heart Disease Prediction':
    st.title('Heart Disease Prediction Using ML')
    col1,col2,col3= st.columns(3)
    with col1:
        age=st.text_input('Age')
        trestbps=st.text_input('Resting Blood Pressure')
        restecg=st.text_input('Resting Electrocardiographic Results')
        oldspeak=st.text_input('ST depression induced by exercise')
        thal=st.text_input('tha:0 = normal, 1 = fixed defect, 2 = reversable defect')
    with col2:
        sex=st.text_input('Sex')
        chol=st.text_input('Serum Cholestrol in mg/dl')
        thalach=st.text_input('Maximum Heart Rate achieved')
        slope=st.text_input('Slope of the peak exercise ST segment')
    with col3:
        cp=st.text_input('Chest Pain Types')
        fbs=st.text_input('Fasting Blood Sugar > 120 mg/dl')
        exang=st.text_input('Exercise Induced Angina')
        ca=st.text_input('Major vessels coloured by fluorosopy')

        heart_diagnosis=''
    if st.button('Heart Disease Test Result'):
        user_input=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldspeak,slope,ca,thal]
        user_input=[float(x) for x in user_input]
        heart_prediction= heart_model.predict([user_input])
        if heart_prediction[0]==1:
            heart_diagnosis='The person has a heart disease'
        else:
          heart_diagnosis='The person do not have a heart disease'
    st.success(heart_diagnosis)

if selected=='Parkinsons Prediction':
    st.title('Parkinsons Disease Prediction Using ML')
    col1,col2,col3,col4,col5= st.columns(5)
    #MDVP:Fo(Hz),MDVP:Fhi(Hz),MDVP:Flo(Hz),MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP,MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA,NHR,HNR,status,RPDE,DFA,spread1,spread2,D2,PPE
    with col1:
        fo=st.text_input('MDVP:Fo(Hz)')
        RAP=st.text_input('MDVP:RAP')
        APQ3=st.text_input('Shimmer:APQ3')
        HNR=st.text_input('HNR')
        D2=st.text_input('D2')
    with col2:
        fhi=st.text_input('MDVP:Fhi(Hz)')
        PPQ=st.text_input('MDVP:PPQ')
        APQ5=st.text_input('Shimmer:APQ5')
        RPDE=st.text_input('RPDE')
        PPE=st.text_input('PPE')
    with col3:
        flo=st.text_input('MDVP:Flo(Hz)')
        DDP=st.text_input('Jitter:DDP')
        APQ=st.text_input('MDVP:APQ')
        DFA=st.text_input('DFA')
        
    with col4:
        Jitter_percent=st.text_input('MDVP:Jitter(%)')
        Shimmer=st.text_input('MDVP:Shimmer')
        DDA=st.text_input('Shimmer:DDA')
        spread1=st.text_input('spread1')
    with col5:
        Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')
        Shimmer_dB=st.text_input('MDVP:Shimmer(dB)')
        NHR=st.text_input('NHR')
        spread2=st.text_input('spread2')

        parkinsons_diagnosis=''
    if st.button('Parkinsons Test Result'):
        user_input=[fo,fhi,flo,Jitter_percent,Jitter_Abs,RAP,PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
        user_input=[float(x) for x in user_input]
        parkinsons_prediction= parkinsons_model.predict([user_input])
        if parkinsons[0]==1:
            parkinsons_diagnosis='The person has parkinsons disease'
        else:
          parkinsons_diagnosis='The person do not have parkinsons disease'
    st.success(parkinsons_diagnosis)
