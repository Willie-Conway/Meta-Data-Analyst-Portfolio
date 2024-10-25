import pandas as pd
import matplotlib.pyplot as plt

# Your original data
data = {
    "Invoice": [489434, 489435, 489436, 489437, 489438, 489439, 489440, 
                489441, 489442, 489443, 489445, 489446, 489448, 489449, 
                489450, 489459, 489460, 489461, 489462, 489465, 489545, 
                489476, 489488, 489503, 489504, 489505, 489514, 489517, 
                489518, 489519, 489520, 489522, 489523, 489525, 489526, 
                489527, 489528, 489529, 489530, 489531, 489532, 489533, 
                489534, 489537],
    "StockCode": [22041, 22195, 48173, 22143, 21252, 22138, 22350, 
                  22138, 22111, 82580, 35916, 21733, 20823, 21871, 
                  21896, 90200, 21977, 21248, 90200, 90185, 21707, 
                  22113, 22149, 84032, 21540, 85083, 48185, 47591, 
                  16207, 20892, 35751, 72760, 84879, 85226, 
                  85049, 85048, 22300, 72803, 85231, 84970, 
                  35832, 20967],
    "Description": ["RECORD FRAME 7\" SINGLE SIZE", "HEART MEASURING SPOONS LARGE", 
                    "DOOR MAT BLACK FLOCK", "CHRISTMAS CRAFT HEART DECORATIONS", 
                    "SET OF MEADOW FLOWER STICKERS", "BAKING SET 9 PIECE RETROSPOT", 
                    "CAT BOWL", "BAKING SET 9 PIECE RETROSPOT", 
                    "SCOTTIE DOG HOT WATER BOTTLE", "BATHROOM METAL SIGN", 
                    "BLUE FELT HANGING HEART W FLOWER", "RED HANGING HEART T-LIGHT HOLDER", 
                    "GOLD WINE GOBLET", "SAVE THE PLANET MUG", 
                    "POTTING SHED TWINE", "GREEN SWEETHEART BRACELET", 
                    "PACK OF 60 PINK PAISLEY CAKE CASES", 
                    "DOOR HANGER MUM + DADS ROOM", "GREEN SWEETHEART BRACELET", 
                    "BLACK DIAMANTE EXPANDABLE RING", "FOLDING UMBRELLA , BLACK/BLUE SPOT", 
                    "GREY HEART HOT WATER BOTTLE", "FELTCRAFT 6 FLOWER FRIENDS", 
                    "CHARLIE+LOLA PINK HOT WATER BOTTLE", "DAIRY MAID CERAMIC BUTTER DISH", 
                    "KISS REINDEER SCANDINAVIAN STOCKING", "DOOR MAT FAIRY CAKE", 
                    "PINK FAIRY CAKE CHILD'S APRON", "PINK STRAWBERRY HANDBAG", 
                    "SET/3 TALL GLASS CANDLE HOLDER PINK", "WASH BAG VINTAGE ROSE PAISLEY", 
                    "PURPLE CURRENT CANDLE RING", "VINTAGE CREAM 3 BASKET CAKE STAND", 
                    "ASSORTED COLOUR BIRD ORNAMENT", "BLUE PULL BACK RACING CAR", 
                    "SCANDINAVIAN REDS RIBBONS", "LOO ROLL METAL SIGN", 
                    "15CM CHRISTMAS GLASS BALL 20 LIGHTS", "COFFEE MUG DOG + BALL DESIGN", 
                    "ROSE SCENT CANDLE JEWELLED DRAWER", "REX CASH+CARRY JUMBO SHOPPER", 
                    "STRAWBERRY SCENTED SET/9 T-LIGHTS", "HANGING HEART ZINC T-LIGHT HOLDER", 
                    "WOOLLY HAT SOCK GLOVE ADVENT STRING", "GREY FLORAL FELTCRAFT SHOULDER BAG"],
    "Quantity": [48, 24, 10, 6, 30, 9, 8, 6, 3, 12, 12, 32, 48, 12, 
                 6, 3, 24, 12, 3, 3, 12, 1, 6, 2, 6, 50, 2, 2, 6, 
                 12, 1, 800, 1, 12, 1, 1, 12, 12, 1, 1, 12, 12, 1, 
                 2],
    "InvoiceDate": pd.to_datetime(["12/1/09 7:45", "12/1/09 7:46", "12/1/09 9:06",
                                    "12/1/09 9:08", "12/1/09 9:24", "12/1/09 9:28", 
                                    "12/1/09 9:43", "12/1/09 9:44", "12/1/09 9:46", 
                                    "12/1/09 9:50", "12/1/09 9:57", "12/1/09 10:06", 
                                    "12/1/09 10:18", "12/1/09 10:33", "12/1/09 10:36", 
                                    "12/1/09 10:44", "12/1/09 10:46", "12/1/09 10:49", 
                                    "12/1/09 10:49", "12/1/09 10:49", "12/1/09 10:52", 
                                    "12/1/09 12:22", "12/1/09 10:55", "12/1/09 10:59", 
                                    "12/1/09 11:04", "12/1/09 11:10", "12/1/09 11:17", 
                                    "12/1/09 11:21", "12/1/09 11:34", "12/1/09 11:35", 
                                    "12/1/09 11:37", "12/1/09 11:41", "12/1/09 11:45", 
                                    "12/1/09 11:46", "12/1/09 11:49", "12/1/09 11:50", 
                                    "12/1/09 11:50", "12/1/09 11:50", "12/1/09 11:51", 
                                    "12/1/09 11:56", "12/1/09 11:57", "12/1/09 11:58", 
                                    "12/1/09 12:02", "12/1/09 12:09", "12/1/09 12:14"]),
    "Price": [2.10, 1.65, 5.95, 2.10, 1.69, 4.95, 2.55, 4.25, 4.95, 
              0.55, 0.85, 2.55, 4.25, 1.25, 2.10, 4.25, 0.55, 1.45, 
              4.25, 4.25, 4.95, 3.45, 2.10, 2.95, 4.25, 2.55, 1.65, 
              5.95, 1.65, 2.95, 12.75, 2.55, 0.75, 9.95, 1.45, 0.55, 
              1.25, 1.65, 7.95, 1.25, 2.55, 0.99],
    "Customer ID": [12748, 12345, 12345, 12346, 12347, 12348, 12349, 
                    12350, 12351, 12352, 12353, 12354, 12355, 12356, 
                    12357, 12358, 12359, 12360, 12361, 12362, 12363, 
                    12364, 12365, 12366, 12367, 12368, 12369, 12370, 
                    12371, 12372, 12373, 12374, 12375, 12376, 12377, 
                    12378, 12379, 12380, 12381, 12382, 12383, 12384],
    "Country": ["United Kingdom"] * 45  # Changed to ensure it matches the data
}

# Check lengths of each list
lengths = {key: len(value) for key, value in data.items()}
print("Lengths of each list in the data dictionary:", lengths)

# Determine the minimum length
min_length = min(len(value) for value in data.values())

# Trim all lists to the minimum length
for key in data:
    data[key] = data[key][:min_length]

# Verify all lengths are the same after trimming
lengths_after_trimming = {key: len(value) for key, value in data.items()}
print("Lengths of each list after trimming:", lengths_after_trimming)

# Step 1: Create DataFrame
df = pd.DataFrame(data)

# Optional: Display the DataFrame
print(df)

# Step 2: Visualize or analyze the data

# Example 1: Count of items sold by country (Bar Chart)
country_counts = df['Country'].value_counts()
country_counts.plot(kind='bar')
plt.title('Count of Items Sold by Country')  # Bar chart title
plt.xlabel('Country')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()

# Example 2: Total sales amount per country (Line Chart)
df['Total Sales'] = df['Quantity'] * df['Price']
sales_by_country = df.groupby('Country')['Total Sales'].sum()
sales_by_country.plot(kind='line', marker='o', color='skyblue')
plt.title('Total Sales Amount by Country (Line Chart)')  # Line chart title
plt.xlabel('Country')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()

# Example 3: Scatter plot of Quantity vs Price
plt.scatter(df['Quantity'], df['Price'], alpha=0.5)
plt.title('Scatter Plot of Quantity vs Price')  # Scatter chart title
plt.xlabel('Quantity')
plt.ylabel('Price')
plt.grid(True)
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()

# Example 4: Pie Chart of Items Sold by Country
country_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
plt.title('Distribution of Items Sold by Country')  # Pie chart title
plt.ylabel('')  # Hide y-label
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()
