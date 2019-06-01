import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.patches import Arc

pd.set_option ( "display.max_columns", 5)
fig, ax = plt.subplots()
 
df = pd.read_pickle(r"C:\Users\Admin\Desktop\Abhishek\STATS Data\test_data_2.pkl")
#print(df)

df2 = pd.DataFrame.from_dict(df,orient = 'index')
df2.columns = ['Sequences']

lists = df2.iloc[1,0]
##for list in lists:
##    print(list)

dff = pd.DataFrame.from_records(lists[1:])
#print(dff)
e = 50
e = [e]*22
e.append(25)
##############################################

def _update_plot(i, fig, scat):
    scat.set_offsets(([dff.iloc[i,0], dff.iloc[i,1]], [dff.iloc[i,2],dff.iloc[i,3]], [dff.iloc[i,4],dff.iloc[i,5]], [dff.iloc[i,6],dff.iloc[i,7]], [dff.iloc[i,8],dff.iloc[i,9]], [dff.iloc[i,10],dff.iloc[i,11]], [dff.iloc[i,12],dff.iloc[i,13]], [dff.iloc[i,14],dff.iloc[i,15]], [dff.iloc[i,16],dff.iloc[i,17]], [dff.iloc[i,18],dff.iloc[i,19]], [dff.iloc[i,20],dff.iloc[i,21]],[dff.iloc[i,22],dff.iloc[i,23]]
                      ,[dff.iloc[i,24],dff.iloc[i,25]],[dff.iloc[i,26],dff.iloc[i,27]],[dff.iloc[i,28],dff.iloc[i,29]],[dff.iloc[i,30],dff.iloc[i,31]],[dff.iloc[i,32],dff.iloc[i,33]],[dff.iloc[i,34],dff.iloc[i,35]],[dff.iloc[i,36],dff.iloc[i,37]],[dff.iloc[i,38],dff.iloc[i,39]],[dff.iloc[i,40],dff.iloc[i,41]]
                      ,[dff.iloc[i,42],dff.iloc[i,43]],[dff.iloc[i,44],dff.iloc[i,45]]))
    scat.set_color(np.array(["yellow","red","red","red","red","red","red","red","red","red","red","yellow", "blue","blue","blue","blue","blue","blue","blue","blue","blue","blue", "grey"]))
    scat.set_sizes(np.array(e))
    #print("Frames: %d"%i)

    return scat,

x = [0]
y = [0]

ax = fig.add_subplot(111)
ax.grid(True, linestyle ='-', color = '0.75')
ax.set_xlim([-52.5,52.5])
ax.set_ylim([-34,34])

scat = plt.scatter(x, y, c = x)
scat.set_alpha(0.8)

anim = animation.FuncAnimation(fig, _update_plot, fargs = (fig, scat),
                               frames = len(dff.index)-1, interval = 100)


plt.plot([-52.5,52.5],[-34,-34], color = "k")
plt.plot([-52.5,-52.5],[-34,34], color = "k")
plt.plot([-52.5,52.5],[34,34], color = "k")
plt.plot([52.5,52.5],[-34,34], color = "k")

plt.plot([0,0],[-34,34], color = "k")

plt.plot([47,47],[-5.5,5.5], color = "k")
plt.plot([-47,-52.5],[-5.5,-5.5], color = "k")
plt.plot([-47,-52.5],[5.5,5.5], color = "k")

plt.plot([-47,-47],[-5.5,5.5], color = "k")
plt.plot([47,52.5],[-5.5,-5.5], color = "k")
plt.plot([47,52.5],[5.5,5.5], color = "k")

plt.plot([36,36],[-16.5,16.5], color = "k")
plt.plot([36,52.5],[-16.5,-16.5], color = "k")
plt.plot([36,52.5],[16.5,16.5], color = "k")

plt.plot([-36,-36],[-16.5,16.5], color = "k")
plt.plot([-36,-52.5],[-16.5,-16.5], color = "k")
plt.plot([-36,-52.5],[16.5,16.5], color = "k")

leftArc = Arc((-41.5,0),height=18.3,width=18.3,angle=0,theta1=306,theta2=54,color="black")
rightArc = Arc((41.5,0),height=18.3,width=18.3,angle=0,theta1=126,theta2=234,color="black")
centreCircle = plt.Circle((0,0),9.15,color="black",fill=False)

    #Draw Arcs
ax.add_patch(leftArc)
ax.add_patch(rightArc)
ax.add_patch(centreCircle)

plt.scatter([-41.5,0,41.5],[0,0,0], color = "k")
plt.fill([-52.5,-52.5,52.5,52.5],[-36,36,36,-36], color = "green", alpha = 0.25)


##
##FFWriter = animation.FFMpegWriter()
##anim.save('STATS1.mp4',  writer = FFWriter)

plt.show()


