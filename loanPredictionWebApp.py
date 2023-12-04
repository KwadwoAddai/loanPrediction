# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 13:48 2023

@author: ADDAI POKU
"""

import numpy as np
import pickle 
import streamlit as st

#loading the saved model
#rb read binary file
loaded_model=pickle.load(open('d:/Code/AI Assignment/Assignment II/diabetes/Model.sav','rb'))

#creating a function for Prediction

def LoanPrediction(input_data):
    #changing the input data to numpy array
    input_data_as_numpy_array=np.asarray(input_data)
    #reshape the array as we are predicting for one instance
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped) 
    print(prediction)
    if(prediction[0]==0):
        return 'You are denied loan'
    else:
        return 'You are granted loan'


def main():
    
    #give the page a title
    st.title('Intelligent Loan Prediction System')
    
    #getting the input data of the user
    Gender=st.text_input("Gender")
    Married=st.text_input("Married")
    Dependents =st.text_input("Number of dependents")
    Education =st.text_input("Are you a graduate or not")
    Self_Employed=st.text_input("Employed or not")
    ApplicantIncome=st.text_input("What is your income")
    CoapplicantIncome=st.text_input("what is your coapplicant income")
    LoanAmount=st.text_input("How much loan do you want")
    Loan_Amount_Term =st.text_input("Loan amount term")
    Credit_History=st.text_input("Credit history")
    Property_Area=st.text_input("Property area")
    
    
    #code for prediction
    loan=''
    
    #creating a button for prediction
    if st.button('Loan Prediction Result'):
        loan=LoanPrediction([Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, 
                             LoanAmount, Loan_Amount_Term, Credit_History,Property_Area])
    
    st.success(loan)
        

if __name__== '__main__':
    main()
