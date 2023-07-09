"""
Name: Henry "TJ" Chen
Last updated: July 9, 2023

Run this file to generate a model of a beat pattern
"""
from numpy import sin, arange
import matplotlib.pyplot as plt
import plotly.graph_objects as go


def sine_wave_zero(amplitude, ang_freq, time):
    """ This function returns the result of the expression: Asin(−ωt)"""
    return amplitude * sin(-1 * ang_freq * time)


def plot_wave_plotly():
    """Plots a beat pattern using plotly"""
    # create an independant variable list
    dt = 0.1
    t = arange(0, 100, dt)

    # create two dependent variable lists
    x1 = sine_wave_zero(5, 0.5, t)
    x2 = sine_wave_zero(5, 0.7, t)

    # create plot figure variable
    fig = go.Figure()

    # making a subplot that takes up entire figure window
    fig.add_trace(go.Scatter(x=t, y=x1, mode='lines', name='lines'))
    fig.add_trace(go.Scatter(x=t, y=x2, mode='lines', name='lines'))
    fig.add_trace(go.Scatter(x=t, y=x1 + x2, mode='lines', name='lines'))

    # Display the plot to the user
    fig.show()


def plot_wave_plotlib():
    """Plot beat pattern using matplotlib"""
    # create an independant variable list
    dt = 0.1
    t = arange(0, 100, dt)

    # create two dependent variable lists
    x1 = sine_wave_zero(5, 0.5, t)
    x2 = sine_wave_zero(5, 0.7, t)

    # create plot figure variable
    fig = plt.figure()

    # making a subplot that takes up entire figure window
    subplot1 = fig.add_subplot(111)

    # plot all three waves (on the same plot)
    subplot1.plot(t, x1)
    subplot1.plot(t, x2)
    subplot1.plot(t, x1 + x2)

    # Display the plot to the user
    plt.show()


if __name__ == '__main__':
    plot_wave_plotly()
    # plot_wave_plotlib()
