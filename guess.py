import streamlit as st
import numpy as np 
import random

st.header("SAMMY GUESSS GAME")
st.image("dice.gif")
st.subheader("lets have some fun,guess the right number")

x = st.number_input("choose a number from 1 - 10",step=1)
x = int(x)
y = np.random.randint(1,10)

def gg (x,y):
        if x > 9:
            return("invalid number,choose numberfrom 1 - 6")
        else:
          st.write(f"random number is {y} ")
          st.write(f"chosen number is {x} ")

          if x == y:
               st.balloons()
               return("correct")
          else:
               return("Try again")

        
c1,c2 = st.columns(2)
with c1:
     if st.button("Guess"):
          st.write(gg(x,y))
with c2:
     if st.button("Retry"):
          st.experimental_return()
     
   
          


