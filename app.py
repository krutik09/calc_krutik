# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:25:24 2021

@author: Krutik Shah
"""


# -*- coding: utf-8 -*-
"""	
Created on Mon Mar 22 07:51:47 2021

@author: Krutik Shah
"""


import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import math
import win10toast
from win10toast import ToastNotifier
notif = ToastNotifier()


html_code = """
        <div style="background-color: #1abc9c; padding:  10px; border-radius: 10px">
          <h1 style="color:white; text-align: center">SIMPLE CALCULATOR AND OTHER PYTHON OPERATIONS</h1>
        </div>
        """
components.html(html_code) 
#image
img = Image.open("calc.png")
st.image(img)
#SELECT FUNACTION
fun = st.radio("SELECT FUNCTIONS", ['ARITHMETIC','TRIGNOMETRIC','RELATIONAL','LOGICAL'])

#ARITHMETIC
if(fun == 'ARITHMETIC'):
    op = st.selectbox("SELECT OPERATION",['+','-','*','/','%','root'])
    a = st.number_input("ENTER NUMBER 1")
    b = st.number_input("ENTER NUMBER 2")
    st.text("CLICK BELOW GIVEN BUTTON TO SUBMIT")
    #calculation
    if(st.button("LETS GO!")):
        if(op == '+'):
            c = a+b
            c = round(c, 3)
            st.write(c)
            st.success("EXCELLENT!")
            st.balloons()
            notif.show_toast('SUCCESS','ADDITION DONE SUCCESSFULLY',duration = 10)
        elif(op == '-'):
            c = a-b
            c = round(c, 3)
            st.write(c)
            st.success("EXCELLENT!")
            st.balloons()
            notif.show_toast('SUCCESS','SUBTRACTION DONE SUCCESSFULLY',duration = 10)
        elif(op == '*'):
            c = a*b
            c = round(c, 3)
            st.write(c)
            st.success("EXCELLENT!")
            st.balloons()
            notif.show_toast('SUCCESS','MULTIPLICATION DONE SUCCESSFULLY',duration = 10)
        elif(op == '/'):
            c = a/b
            c = round(c, 3)
            st.write(c)
            st.success("EXCELLENT!")
            st.balloons()
            notif.show_toast('SUCCESS','DIVISION DONE SUCCESSFULLY',duration = 10)
        elif(op == '%'):
            c = a%b
            st.write(c)
            st.success("EXCELLENT!")
            st.balloons()
            notif.show_toast('SUCCESS','MODULO DONE SUCCESSFULLY',duration = 10)
        elif(op == 'root'):
            c = math.sqrt(a)
            st.write(round(c,3))
            st.success("EXCELLENT!")
            st.balloons()
            notif.show_toast('SUCCESS','ROOT DONE SUCCESSFULLY',duration = 10)
            
        else:
            st.error("NO SELECTED OPERATION")
#trignometirc 
if(fun == 'TRIGNOMETRIC'):
    op = st.selectbox("SELECT OPERATION",['sin','cos','tan'])
    a1 = st.number_input("ENTER THE ANGLE IN DEGREE")
    a2 = (a1*3.14)/180
    st.text("CLICK BELOW GIVEN BUTTON TO SUBMIT")
    if(st.button("LETS GO!")):
        if(op == 'sin'):
            st.write(round(math.sin(a2),2))
            st.success("EXCELLENT!")
            st.balloons()
            notif.show_toast('SUCCESS','SIN DONE SUCCESSFULLY',duration = 10)
        elif(op=='cos'):
            st.write(round(math.cos(a2),2))
            st.success("EXCELLENT!")
            st.balloons()
            notif.show_toast('SUCCESS','COS DONE SUCCESSFULLY',duration = 10)
        elif(op=='tan'):
            st.write(round(math.tan(a2),2))
            st.success("EXCELLENT!")
            st.balloons()
            notif.show_toast('SUCCESS','TAN DONE SUCCESSFULLY',duration = 10)
        else:
            st.error("NO SELECTED OPERATION")
        
#relationl
if(fun == 'RELATIONAL'):
        op = st.selectbox("SELECT OPERATION",['>','<','>=','<=','==','!='])
        a = st.number_input("ENTER NUMBER 1")
        b = st.number_input("ENTER NUMBER 2")
        st.text("CLICK BELOW GIVEN BUTTON TO SUBMIT")
        if(st.button("LETS GO!")):
            if(op == '>'):
                c = a>b
                st.write(bool(c))
                st.success("EXCELLENT!")
                st.balloons()
                notif.show_toast('SUCCESS','OPERATION SUCCESSFULLY',duration = 10)
            elif(op == '<'):
                c = a<b
                st.write(bool(c))
                st.success("EXCELLENT!")
                st.balloons()
                notif.show_toast('SUCCESS','OPERATION SUCCESSFULLY',duration = 10)
            elif(op == '>='):
                c = a>=b
                st.write(bool(c))
                st.success("EXCELLENT!")
                st.balloons()
                notif.show_toast('SUCCESS','OPERATION SUCCESSFULLY',duration = 10)
            elif(op == '<='):
               c = a<=b
               st.write(bool(c))
               st.success("EXCELLENT!")
               st.balloons()
               notif.show_toast('SUCCESS','OPERATION SUCCESSFULLY',duration = 10)
            elif(op == '=='):
                c = a==b
                st.write(bool(c))
                st.success("EXCELLENT!")
                st.balloons()
            elif(op == '!='):
                c = a!=b
                st.write(bool(c))
                st.success("EXCELLENT!")
                st.balloons()
                notif.show_toast('SUCCESS','OPERATION SUCCESSFULLY',duration = 10)
            else:
                st.error("NO SELECTED OPERATION")
#logical
if(fun == 'LOGICAL'):
    op = st.selectbox("SELECT OPERATION",['OR','AND','NOT'])
    a = st.number_input("ENTER NUMBER 1")
    b = st.number_input("ENTER NUMBER 2")
    st.text("CLICK BELOW GIVEN BUTTON TO SUBMIT")
    if(st.button("LETS GO!")):
        if(op == 'OR'):
            c = a or b
            st.write(int(c))
            st.success("EXCELLENT!")
            st.balloons()
            notif.show_toast('SUCCESS','OPERATION SUCCESSFULLY',duration = 10)
        elif(op == 'AND'):
            c = a and b
            st.write(int(c))
            st.success("EXCELLENT!")
            st.balloons()
            notif.show_toast('SUCCESS','OPERATION SUCCESSFULLY',duration = 10)
        elif(op == 'NOT'):
            st.info(" HERE NOT IS CONSIDERED AS UNARY FOR UNARY OPERATIONS SO OPERATION WILL BE PERFORMED AS [NOT {YOUR NUMBER 1}]") 
            c = not a
            st.write(int(c))
            st.success("EXCELLENT!")
            st.balloons()
            notif.show_toast('SUCCESS','OPERATION SUCCESSFULLY',duration = 10)
        else:
            st.error("NO SELECTED OPERATION")
                         
                     
            
    
    
            
                                          
    
     
            
        
     
    
       
                  
                  
