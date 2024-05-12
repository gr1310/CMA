e(len(h_list)):
    y_pts= x_list[i]
    x_pts= t_list[i]
    y_actual= [5*math.exp(-2*i) for i in x_pts]
    plt.scatter(x_pts,y_pts)
    plt.plot(x_pts, y_actual)
    plt.show()