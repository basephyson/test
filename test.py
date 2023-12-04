
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

c1 = st.radio('선의 색을 선택하시오', ['red', 'green', 'blue'])
s1 = st.radio('선의 형태를 선택하시오', ['-', ':', '-.', '--'])
# st.sidebar

# fig, ax = plt.subplots()

x = [] 
y = []
for i in range(-20, 21, 1):
    x.append(i)
    y.append(3*i*i - 2*i + 5)

plt.plot(x, y, color =c1, linestyle=s1, marker='h')

st.pyplot(fig)


import sys
sys.exit()








































# import matplotlib.pyplot as plt

# fig, ax = plt.subplots()

# x = []
# for i in range(-3, 4):
#     x.append(i/10.0)

# col = st.columns(3)
# with col[0]:
#     a = st.number_input('Insert a', step = 10)
# with col[1]:
#     b = st.number_input('Insert b', step = 10)
# with col[2]:
#     c = st.number_input('Insert c', step = 10)  

# y = []
# for i in x:
#     y.append(a*i**2 + b*i + c)

# plt.plot(x, y)

# st.pyplot(fig)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            








# import turtle

# t = turtle.Turtle()
# t.shape('turtle')
# t.speed('fastest')
# for i in range(1200):
#     t.fd(i)
#     t.right(178)


# turtle.done()

# t.forward(80)
# t.left(120)
# t.forward(80)
# t.left(120)
# t.forward(80)
# t.left(120)

#n = 200
#ang = 360/n
#for i in range(n):
 #   t.circle(80)   
  #  t.left(ang)    


#for i in range(1, 10):
 #   if 1%3 == 1:
  #      i


# s = 27
#if s >= 90:
#   st.write('귀하의 점수는 ' + str(s) + '점으로 :blue[A등급]입니다')
#elif s >= 80:
 #   '귀하의 점수는 ' + str(s) + '점으로 :green[B등급]입니다'
#elif s >= 70:
 #   '귀하의 점수는 ' + str(s) + '점으로 :orange[C등급]입니다'
#elif s >= 60:
 #   '귀하의 점수는 ' + str(s) + '점으로 :blue[D등급]입니다'
#else:
 #   '귀하의 점수는 ' + str(s) + '점으로 :red[F등급]입니다'



 
 
# st.image('im.jpg')
