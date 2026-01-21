import matplotlib.pyplot as plt
import numpy as np

# Overview of Common Chart Types

def main():
    # Bar Chart
    def bar_chart():
        categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
        values = [100, 120, 90, 140, 130]

        plt.figure(figsize=(10, 5))
        plt.bar(categories, values, color='skyblue')
        plt.title('Sales by Month (Bar Chart)')
        plt.xlabel('Months')
        plt.ylabel('Sales')
        plt.show()

    # Pie Chart
    def pie_chart():
        categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
        values = [100, 120, 90, 140, 130]

        plt.figure(figsize=(8, 8))
        plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.title('Monthly Sales Distribution (Pie Chart)')
        plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
        plt.show()

    # Trend Chart (Line Chart)
    def trend_chart():
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
        sales = [100, 120, 90, 140, 130]

        plt.figure(figsize=(10, 5))
        plt.plot(months, sales, marker='o', color='orange')
        plt.title('Sales Trend Over Months (Line Chart)')
        plt.xlabel('Months')
        plt.ylabel('Sales')
        plt.grid()
        plt.show()

    # Scatter Plot
    def scatter_plot():
        ages = [5, 6, 7, 8, 9, 10, 11, 12]
        heights = [110, 115, 120, 125, 130, 135, 140, 145]

        plt.figure(figsize=(10, 5))
        plt.scatter(ages, heights, color='green')
        plt.title('Height vs. Age (Scatter Plot)')
        plt.xlabel('Age')
        plt.ylabel('Height')
        plt.grid()

        # Adding a trendline (linear regression)
        z = np.polyfit(ages, heights, 1)
        p = np.poly1d(z)
        plt.plot(ages, p(ages), color='red', linestyle='--')
        
        plt.show()

    # Call the functions to generate the charts
    bar_chart()
    pie_chart()
    trend_chart()
    scatter_plot()

# Run the main function
if __name__ == '__main__':
    main()
