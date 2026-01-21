# Import necessary libraries
import webbrowser

# Define a list of data sources with names and links
data_sources = [
    {
        "name": "Google Public Dataset Search",
        "link": "https://datasetsearch.research.google.com"
    },
    {
        "name": "United States Census Bureau",
        "link": "https://www.census.gov"
    },
    {
        "name": "Pew Research Center",
        "link": "https://www.pewresearch.org/tools-and-resources/"
    },
    {
        "name": "Eurostat",
        "link": "https://ec.europa.eu/eurostat"
    },
    {
        "name": "OECD",
        "link": "https://data.oecd.org/united-states.htm"
    },
    {
        "name": "Kaggle Datasets",
        "link": "https://www.kaggle.com/datasets"
    },
    {
        "name": "National Centers for Environmental Information (NCEI)",
        "link": "https://www.ncei.noaa.gov"
    },
    {
        "name": "World Bank Open Data",
        "link": "https://data.worldbank.org"
    }
]

# Function to display data sources
def display_data_sources(sources):
    print("Helpful Free Data Sources:\n")
    for source in sources:
        print(f"{source['name']}: {source['link']}")

# Function to open a data source in a web browser
def open_data_source(source):
    webbrowser.open(source)

# Main function to run the script
def main():
    # Display the data sources
    display_data_sources(data_sources)
    
    # Prompt user to open a specific data source
    choice = input("\nEnter the name of the data source you want to open (or 'exit' to quit): ")
    for source in data_sources:
        if source['name'].lower() == choice.lower():
            open_data_source(source['link'])
            break
    else:
        if choice.lower() != 'exit':
            print("Data source not found. Please try again.")

# Check if the script is run directly
if __name__ == "__main__":
    main()
