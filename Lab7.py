import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('tourism.csv', delimiter=',')

#Task 1 - Aggregate the data based on the ’State’ column and plot the results for each state
# and the aggregated data on the country level (see T07 Lecture slides).

states = list(data['State'].unique()) #unique states from the 'State' column in the dataset

new_df = pd.DataFrame()
T = 8 #numbers of quarters for forecasting

for state in states:
    stat_data = data[data['State'] == state].groupby('Quarter').mean()
    #Groups the data by 'State' and 'Quarter', calculating the mean visits for each quarter for each state
    if state == states[0]:
        new_df = stat_data.copy()
        new_df.columns = [state]
    else:
        new_df[state] = stat_data


# BOTTOM - UP
# A = B + C

#Task 2 - Forecast the total number of visits for Australia using the bottom-up approach
country = new_df.sum(axis=1)
fore = new_df.shift(4) # naive forecast
fore_country = country.shift(4) #Shifts the country-level visits by four quarters
fore['bottom_up'] = fore.iloc[-T:,:-1].sum(axis=1) #Calculates the bottom-up forecast by summing the last 8 quarters of state-level forecasts to estimate the country-level forecast

australia_bottom_up_forecast = fore['bottom_up'].iloc[-1]
print(f"Forecasted total visits for Australia using bottom-up approach: {australia_bottom_up_forecast}")

plt.plot(new_df.index, country, label='Country Level', linestyle='--')
plt.xlabel('Quarter')
plt.ylabel('Number of Visits')
plt.title('Visits by State and Country Level')
plt.legend()
plt.show()


# TOP-DOWN
# B = A*p1, C = A*p2

#Task 4 - Forecast the total number of visits for each Australian state using the top-down approach
# (compare both cases of proportion calculation)
#for each state

prop1 = {}
prop2 = {}
prop3 = {}

for state in states:
    # Calculate average state value divided by country value
    prop1[state] = new_df[state].div(country).mean() #avg(state/country) - averagge historical proportions

    # Calculate ratio of average state value to overall average country value
    prop2[state] = new_df[state].mean() / country.mean() #avg(state)/avg(country) - proportions of the historical average

    # Calculate proportion of forecasted state value to total forecasted values - coś innego to jest, nie używać!
    prop3[state] = fore[state] / fore.sum(axis=1)

for state in states:
    fore[state+'top_down_1'] = prop1[state]*fore_country.loc[new_df.index[-T:]]
    
for state in states:
    fore[state+'top_down_2'] = prop2[state]*fore_country.loc[new_df.index[-T:]]

for state in states:
    fore[state+'top_down_3'] = prop3[state]*fore_country.loc[new_df.index[-T:]]

for state in states:
    top_down_1_state_forecast = fore[state+'top_down_1'].iloc[-1]
    top_down_2_state_forecast = fore[state+'top_down_2'].iloc[-1]
    top_down_3_state_forecast = fore[state + 'top_down_3'].iloc[-1]

    # print(f"Forecasted visits for {state} using top-down approach with prop1: {top_down_1_state_forecast}")
    # print(f"Forecasted visits for {state} using top-down approach with prop2: {top_down_2_state_forecast}")
    # print(f"Forecasted visits for {state} using top-down approach with prop3: {top_down_3_state_forecast}")


#Task 3 - Forecast the total number of visits for Australia using the top-down approach with proportions based
# on forecasts (see page 10 of T07 Lecture slides)
#for all country

australia_top_down_1 = fore.filter(like='top_down_1').iloc[-1].sum()
australia_top_down_2 = fore.filter(like='top_down_2').iloc[-1].sum()
australia_top_down_3 = fore.filter(like='top_down_3').iloc[-1].sum()

print(f"Forecasted total visits for Australia using top-down approach with prop1: {australia_top_down_1}")
print(f"Forecasted total visits for Australia using top-down approach with prop2: {australia_top_down_2}")
print(f"Forecasted total visits for Australia using top-down approach with prop3: {australia_top_down_3}")