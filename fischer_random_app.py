import streamlit as st
import random
from collections import OrderedDict

def fischer_random():
    base_array=['R','R','R','Q','N','N']
    random.shuffle(base_array)
    white_spaces=base_array[0:3]
    black_spaces=base_array[3:6]
    white_spaces.append('B')
    black_spaces.append('B')
    random.shuffle(white_spaces)
    random.shuffle(black_spaces)
    white_coord=['b','d','f','h']
    black_coord=['a','c','e','g']
    white_dick={}
    black_dick={}
    for x in range(4):
        white_dick[white_coord[x]]=white_spaces[x]
    for x in range(4):
        black_dick[black_coord[x]]=black_spaces[x]
    black_dick.update(white_dick)
    final={}
    for i in sorted(black_dick):
        final[i]=black_dick[i]
    r_counter=0
    for key in final.keys():
        if r_counter==0:
            if final[key]=='R':
                r_counter+=1
        elif r_counter==1:
            if final[key]=='R':
                final.update(
                    {key: 'K'}
                )
                r_counter+=1 
    return final

st.title("Hey chess nerd, this is B's Fischer Randomizer", anchor="title")

if st.button("Randomize"):
    st.markdown("Set up the pieces like this:")
    st.markdown(fischer_random())
