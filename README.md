# Hierarchical Forecasting

This project focuses on hierarchical forecasting using the Tourism dataset to predict the total number of visits to Australia and its states. The Holt-Winters model is employed to generate forecasts, allowing for different aggregation approaches to be evaluated.

## Project Overview

The project consists of the following key tasks:

1. **Data Aggregation and Visualization**:
   - Aggregate the Tourism dataset based on the 'State' column and create visualizations that display the results for each state alongside the aggregated data at the country level.

2. **Bottom-Up Forecasting**:
   - Implement a bottom-up approach to forecast the total number of visits to Australia. This involves summing the forecasts from individual states to derive the national total.

3. **Top-Down Forecasting**:
   - Apply a top-down approach to forecast the total number of visits to Australia, using proportions based on the forecasts derived from the overall national data.

4. **State-Level Top-Down Forecasting**:
   - Forecast the total number of visits for each Australian state using the top-down approach. This task includes a comparison of different methods for calculating proportions in the forecasting process.

## Data

The project utilizes the `Tourism.csv` dataset, which contains information on tourism visits to Australia, categorized by state. This dataset serves as the basis for all forecasting tasks.

## Results

The outputs of the project will include visualizations of aggregated tourism data, forecasts for total visits at both the national and state levels, and a comparative analysis of the bottom-up and top-down forecasting approaches.

