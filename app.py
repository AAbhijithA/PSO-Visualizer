import streamlit as st
import plotly.graph_objects as go
import numpy as np
from numpy import random
st.set_page_config(
    page_title="PSO-Visualizer",
    page_icon="💻"
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: black;'>Particle Swarm Optimization</h1>", unsafe_allow_html=True)
# st.write('''In computational science, particle swarm optimization (PSO) is a 
# computational method that optimizes a problem by iteratively trying to improve a 
# particle solution with regard to a given measure of quality''')
# st.markdown("<h4 style='text-align: center; color: black;'>Here are the equations:</h4>", unsafe_allow_html=True)
# st.markdown("<h6 style='text-align: left; color: black;'>Vi(t+1) = W x V(t)</h6>", unsafe_allow_html=True)
# st.markdown("<h6 style='text-align: left; color: black;'>Vc(t+1) = c1 x r1 x (Pbest - Pcurrent)</h6>", unsafe_allow_html=True)
# st.markdown("<h6 style='text-align: left; color: black;'>Vs(t+1) = c2 x r2 x (Gbest - Pcurrent)</h6>", unsafe_allow_html=True)
# st.markdown("<h6 style='text-align: left; color: black;'>V(t+1) = g(Vi(t+1),Vc(t+1),Vs(t+1)) = Vi(t+1) + Vc(t+1) + Vs(t+1)</h6>", unsafe_allow_html=True)
# st.markdown("<h6 style='text-align: left; color: black;'>X(t+1) = X(t) + V(t+1)</h6>", unsafe_allow_html=True)
# st.markdown("<h6 style='text-align: left; color: black;'>W is inertial weight, c1 is degree of exploration, c2 is degree of exploitation belonging to [0,1] and r1, r2 are randomized between [0,1]</h6>", unsafe_allow_html=True)
def func(x):
    y = (x*(np.sin(x))) - (x**(np.sin(x)))
    return y
x = []
add = 0
for i in range(0,101):
    x.append(add)
    add+=0.1
y = [func(i) for i in x]
vt = [-0.3,-0.6,0.2,0.5]
xp = [4.3,4.7,5.6,5.7]
yp = [func(i) for i in xp]
pbest = []
gbesty = -9999
gbestx = -9999
for i in range(0,4):
    pbest.append(xp[i])
for i in range(0,4):
    if(yp[i]>gbesty):
        gbesty = yp[i]
        gbestx = xp[i]
xchng = []
ychng = []
xt = []
yt = []
for i in range(0,4):
    xt.append(xp[i])
    yt.append(yp[i])
xchng.append(xt)
ychng.append(yt)
max_itr = 20
c1 = 0.5
c2 = 0.6
w = 0.8
for z in range(0,max_itr):
    for i in range(0,4):
        r1 = random.rand()
        r2 = random.rand()
        vi = w*vt[i]
        vc = c1*r1*(pbest[i]-xp[i])
        vs = c2*r2*(gbestx - xp[i])
        vtnext = vi + vc + vs
        vt[i] = vtnext
        if(func(xp[i]+vtnext)>func(pbest[i])):
            pbest[i] = xp[i] + vtnext
        xp[i] = xp[i] + vtnext
        yp[i] = func(xp[i])
        if(yp[i]>gbesty):
            gbesty = yp[i]
            gbestx = xp[i]
    xt = []
    yt = []
    for i in range(0,4):
        xt.append(xp[i])
        yt.append(yp[i])
    xchng.append(xt)
    ychng.append(yt)

fig = go.Figure(
    data=[go.Scatter(x=x, y=y,
                     mode="lines",
                     line=dict(width=2, color="lime"),showlegend=False),
          go.Scatter(x=x, y=y,
                     mode="lines",
                     line=dict(width=2, color="lime"),name='F(x)',showlegend=True)],
    layout=go.Layout(
        xaxis=dict(range=[0, 10], autorange=False, zeroline=False),
        yaxis=dict(range=[-11, 2], autorange=False, zeroline=False),
        title_text="Particle Swarm Optimization for finding global maximum", hovermode="closest",
        updatemenus=[dict(type="buttons",
                          buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None])])]),
    frames=[go.Frame(
        data=[go.Scatter(
            x=xchng[k],
            y=ychng[k],
            mode="markers",
            marker=dict(color="steelblue", size=7),name='Particles',showlegend=True)])

        for k in range(0,len(ychng))]
)
st.plotly_chart(fig,use_container_width=True)
st.write("The global best is found at x = "+str(gbestx)+", with a value y = "+str(gbesty))
