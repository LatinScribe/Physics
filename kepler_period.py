"""
Author: Henry "TJ" Chen
Last Modified: July 9. 2023

Function to calculate the orbital period and the speed of a satellite
in orbit around a massive object of mass M at a distance r from the centre of
Mass M
"""
# Some constants
PI = 3.14159
G = 6.67300e-11  # m3 kg-1 s-2


def calc_kepler_period():
    """prompts the user to input the nesscary variable values. Then
    calculates and returns the kepler period
    """
    r = input('Enter radius r in metres and press return/enter. ')
    r = float(r)
    # get M and convert to float
    m_big = input('Enter mass M in kilograms and press return/enter. ')
    m_big = float(m_big)
    # This is the period in seconds
    t = ((4 * PI ** 2) * r ** 3 / (G * m_big)) ** 0.5
    # The period in years is T divided by the number of seconds in a year.
    t_years = t / (365.0 * 24.0 * 60.0 * 60.0)
    # The speed for a circular orbit of radius r
    v = 2 * PI * r / t
    print('Set M = ', m_big, 'kg and r = ', r, 'metres.')
    print('The period is ', t_years, 'years and the speed is', v, 'm/s.')


if __name__ == '__main__':
    calc_kepler_period()
