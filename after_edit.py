import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib as mpl

def one(x,y):
    result = "Parabola"
    print("the conic section is = ",result)
    Option = int(input("enter your option from 1 or 2 (1:on X axis , 2: on Y axis) : "))
    if Option == 1:
        plt.axhline(color='black', lw=0)
        plt.axvline(color='black', lw=0)
        x, y = np.meshgrid(x, y)
        def axes():
            plt.axhline(0, alpha=.1)
            plt.axvline(0, alpha=.1)
        mpl.rcParams['lines.color'] = 'k'
        mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])
        print('Equation is : (x-k)**2 - 4*a*(y-h)')
        a = float(input("a = "))
        h = float(input("h = "))
        k = float(input("k = "))
        print('Vertex = (',h,',',k,')')
        print('Focus = (',h,',',k+a,')')
        print('Directrix : y =',k-a)
        axes()
        plt.contour(x, y,(x-k)**2 - 4*a*(y-h), [1], colors='k')
        plt.title('Parabola')
        plt.show()
    elif Option == 2:
        x, y = np.meshgrid(x, y)
        def axes():
            plt.axhline(0, alpha=.1)
            plt.axvline(0, alpha=.1)
        mpl.rcParams['lines.color'] = 'k'
        mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])
        print('Equation is : (y-k)**2 - 4*a*(x-h)')
        a = float(input("a = "))
        h = float(input("h = "))
        k = float(input("k = "))
        print('Vertex = (',h,',',k,')')
        print('Focus = (',h+a,',',k,')')
        print('Directrix : x =',h-a)
        axes()
        plt.contour(x, y,(y-k)**2 - 4*a*(x-h), [1], colors='k')
        plt.title('Parabola')
        plt.show()

def two(x,y):
    result =  "Ellipse"
    print("the conic section is ", result)
    Option = int(input("enter your option from 1 or 2 (1: a > b , 2: b > a) : "))
    if Option == 1:
        print('Equation is : ((x-h)**2/a**2+(y-k)**2/b**2)')
        h = float(input("h = "))
        k = float(input("k = "))
        fig, ax = plt.subplots()
        a = float(input("a = "))
        b = float(input("b = "))
        c = (a**2 - b**2)**0.5
        print('c =', c)
        print('Vertices = (',h+a,',',k,') & (',h-a,',',k,')')
        print('Co-Vertices = (',h,',',k+b,') & (',h,',',k-b,')')
        print('Foci = (',h+c,',',k,') & (',h-c,',',k,')')
        print('Major axis = ', 2*a)
        print('Minor axis = ', 2*b)
        ax.axis('equal')
        ell = Ellipse(xy=[h,k], width=2*a, height=2*b, angle=0,edgecolor='k', lw=1, facecolor='none')

        ax.add_artist(ell)
        ax.set(xlim=[start, end], ylim=[start, end])
        plt.axvline(x=0, c="grey")
        plt.axhline(y=0, c="grey")
        plt.title('Ellipse')
        plt.show()
    elif Option == 2:
        print('Equation is : ((x-h)**2/a**2+(y-k)**2/b**2)')
        h = float(input("h = "))
        k = float(input("k = "))
        fig, ax = plt.subplots()
        a = float(input("a = "))
        b = float(input("b = "))
        c = (a**2 - b**2)**0.5
        print('c =', c)
        print('Vertices = (',h,',',k+b,') & (',h,',',k-b,')')
        print('Co-Vertices = (',h+a,',',k,') & (',h-a,',',k,')')
        print('Foci = (',h,',',k+c,') & (',h,',',k-c,')')
        print('Major axis = ', 2*b)
        print('Minor axis = ', 2*a)
        ax.axis('equal')
        ell = Ellipse(xy=[h,k], width=2*a, height=2*b, angle=0,edgecolor='k', lw=1, facecolor='none')

        ax.add_artist(ell)
        ax.set(xlim=[start, end], ylim=[start, end])
        plt.axvline(x=0, c="grey")
        plt.axhline(y=0, c="grey")
        plt.title('Ellipse')
        plt.show()

def three(x,y):
    result = "Circle"
    print("the conic section is ", result)
    print('Equation is :((x-h)**2 + (y-k)**2 = r**2)')
    h = float(input("h = "))
    k = float(input("k = "))
    fig, ax = plt.subplots()
    r = float(input("Radius = "))
    print('Center = (',h,',',k ,')')
    ax.axis('equal')
    ell = Ellipse(xy=[h,k], width=2*r, height=2*r, angle=0,edgecolor='k', lw=1, facecolor='none')

    ax.add_artist(ell)
    ax.set(xlim=[start, end], ylim=[start, end])
    plt.axvline(x=0, c="grey")
    plt.axhline(y=0, c="grey")
    plt.title('Circle')
    plt.show()

def four(x,y):
    result = "hyperabola"
    print("the conic section is ", result)
    Option = int(input("enter your option from 1 or 2 (1:on X axis , 2: on Y axis) : "))
    if Option == 1:
        plt.axhline(color='black', lw=0)
        plt.axvline(color='black', lw=0)
        x, y = np.meshgrid(x, y)
        def axes():
            plt.axhline(0, alpha=.1)
            plt.axvline(0, alpha=.1)
        mpl.rcParams['lines.color'] = 'k'
        mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])
        print('((x-h)**2/a**2 - (y-k)**2/b**2)')
        a = float(input("a = "))
        b = float(input("b = "))
        h = float(input("h = "))
        k = float(input("k = "))
        c = (a**2 + b**2)**0.5
        print('Vertices = (',h+a,',',k,') & (',h-a,',',k,')')
        print('Foci = (',h+c,',',k,') & (',h-c,',',k,')')
        print('asmptotes = +',b/a,'& -',b/a)
        axes()
        plt.contour(x, y,(x-h)**2/a**2 - (y-k)**2/b**2, [1], colors='k')
        plt.title('Hyperbola')
        plt.show()
    elif Option == 2:
        plt.axhline(color='black', lw=0)
        plt.axvline(color='black', lw=0)
        x, y = np.meshgrid(x, y)
        def axes():
            plt.axhline(0, alpha=.1)
            plt.axvline(0, alpha=.1)
        mpl.rcParams['lines.color'] = 'k'
        mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])
        print('((x-h)**2/a**2 - (y-k)**2/b**2)')
        a = float(input("a = "))
        b = float(input("b = "))
        h = float(input("h = "))
        k = float(input("k = "))
        c = (a**2 + b**2)**0.5
        print('Vertices = (',h,',',k+b,') & (',h,',',k-b,')')
        print('Foci = (',h,',',k+c,') & (',h,',',k-c,')')
        print('asmptotes = +',b/a,'& -',b/a)
        axes()
        plt.contour(x, y,(y-k)**2/a**2 - (x-h)**2/b**2, [1], colors='k')
        plt.title('Hyperbola')
        plt.show()

def start():
    start = int(input("Axis Start from = "))
    end = int(input("Axis End To = "))
    x = np.linspace(start,end,100)
    y = np.linspace(start,end,100)
    option = int(input("Enter your option from 1-4 (1:Parabola , 2: Ellipse , 3:Circle , 4:Hyparabola) : "))
    if option == 1:
        one(x, y)
    elif option == 2:
        two(x, y)
    elif option == 3:
        three(x, y)
    elif option == 4:
        four(x, y)
    else:
        print("This option is not correct..:(")
        print("="*20)
        start()
    
while True:
    start()
    print("="*20,"\n")
