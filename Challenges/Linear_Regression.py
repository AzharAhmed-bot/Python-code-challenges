def regression_line(x,y):
    n=len(x)

    E_x=sum(x)
    E_x2=sum([data**2 for data in x])
    E_x_squared=E_x**2
    E_y=sum(y)
    E_xy=sum(x[i]*y[i] for i in range(n))

    theta_1=(n*E_xy-(E_x*E_y))/(n*E_x2-E_x_squared)
    theta_0=(E_y-theta_1*E_x)/n
    # TO 2 decimal points

    return (round(theta_0, 4), round(theta_1, 4))

print(regression_line([25,30,35,40,45,50], [78,70,65,58,48,42]))