import numpy as np
import csv
import random
#Load data from a .txt file
def load_data(filename):
data = []
with open(filename, 'r') as file:
reader
csv.DictReader (file)
for row in reader:
#Ensure we handle various expected keys
if name in row and "brand" in row and 'price' in row:
# Convert numeric fields to integers or floats where applicable
try:
row['price'] = int(row['price'])
except ValueError:
row['price'] = None
# For laptops, handle storage differently
if 'storage in row:
if 'GB in row['storage']:
| row['storage'] = int(row['storage'].replace('GB', '').strip())
elif TB in row['storage']:
else:
row['storage'] = int(float (row['storage'].replace('TB', '').strip()) 1024) # Convert TB to GB
row['storage'] int(row['storage']) # Fallback to integer if no units
# For cameras and other types, handle fields as needed
if 'ram in row:
row['ram']
int(row['ram'])
if 'battery in row:
row["battery'] = int(row['battery'].replace('hours', '').strip())
if 'megapixels in row:
try: # Attempt to convert to integer
row['megapixels'] = int(row['megapixels'])
except (ValueError, TypeError): # Handle cases where conversion fails
return data
row['megapixels'] = None
if 'driver size in row:
row["driver_size'] = int(row['driver_size'])
data.append(row)
#Function to get unique options from a given data field
def get_unique_options (data, field):
T return sorted(set (item[field] for item in data if field in item)) #Function to choose laptops
def choose laptops (laptops):
print("Let's find the perfect laptop for you!")
#Gather options for user selection
brands get_unique_options (laptops, "brand") price_options= [30000, 60000] # Example fixed range ram_options= get_unique_options (laptops, 'ram') storage_options= get_unique_options (laptops, storage') processors = get_unique_options (laptops, 'processor')
# Display options with numbers print("Available Brands:")
for i, brand in enumerate(brands, 1):
print (f" (i). (brand)")
print("Price Range: (price_options[0]) to (price_options[1]}")
print("Available RAM options (GB):",, .join(map(str, ram_options)))
print("Available Storage options (GB):",, .join(map(str, storage_options))) print("Available Processors: ")
for i, processor in enumerate(processors, 1):
print("(i). (processor)")
# User selections using numbers
brand index= int(input("Choose a brand number: ")) - 1
price range input(f"Choose a price range (e.g., (price_options[0])-(price_options[1])):").split('-') ram = int(input("Choose minimum RAM (e.g., (min(ram_options)}):"))
storage int(input(f"Choose minimum Storage (e.g., (min(storage_options)}): "))
processor_index= int(input("Choose a processor number: ")) - 1
selected_brand brands [brand_index]
selected processor = processors [processor_index]
print("Awesome choice on your preferences!")
filtered laptops = [
laptop for laptop in laptops
if (selected brand. lower() in laptop["brand"].lower() and
price_options[0] <= laptop['price'] <= price_options[1] and ram < laptop['ram'] and
storage <= laptop['storage'] and
selected processor.lower() in laptop['processor'].lower())
if filtered laptops:
else:
print("Found (len(filtered laptops)) laptops that match your criteria!")
return filtered laptops
print("Sorry, no laptops found that match your criteria. Here are some alternative choices:") return random.sample (laptops, min(3, len(laptops)))
#Function to display laptop details
def display laptop_details(laptop):
print("\nHere are the details of the chosen laptop:") print("-
print("Name: (laptop['name']}")
print("Brand: (laptop["brand"]}")
print("Price: *{laptop['price']}")
print("RAM: (laptop['ram']} GB")
print("Storage: (laptop['storage']} GB")
print("Processor: {laptop['processor']}") print(f"Display: {laptop['display']}")
print(f"Battery: {laptop['battery']} hours")
print(f"Category: {laptop['category']}")
print(f"other Features: {laptop['other_features']}") print("=
# Function to choose phones
def choose_phones (phones):
print("Let's find the perfect phone for you!")
# Gather options for user selection
brands = get_unique_options(phones, 'brand')
price_options
=
=")
[10000, 50000] # Example fixed range
ram_options get_unique_options(phones, 'ram')
storage_options get_unique_options(phones, 'storage') processors = get_unique_options(phones, 'processor') displays = get_unique_options (phones, 'display')
# Display options with numbers
print("Available Brands:")
for i, brand in enumerate(brands, 1):
print(f"{i}. {brand}")
print("Price Range: ${price_options[0]} to $3{price_options[1]}")
print("Available RAM options (GB):",
.join(map(str, ram_options)))
J
print("Available Storage options (GB):", '.join(map(str, storage_options))) print("Available Processors:")
for i, processor in enumerate(processors, 1):
print(f"{i}. {processor}")
print("Available Display Types:")
for i, display in enumerate(displays, 1):
print(f"{i}. {display}")
# User selections using numbers
brand_index int(input("Choose a brand number: ")) - 1
price_range= input(f"Choose a price range (e.g., (price_options[0])-(price_options[1]}): ").split('-') ram = int(input("Choose minimum RAM (e.g., (min(ram_options)}): "))
storage int(input(f"Choose minimum Storage (e.g., (min(storage_options)}): "))
processor_index= int(input("Choose a processor number: ")) 1
display_index int(input("Choose a display type number: ")) 1
selected brand brands[brand_index]
selected_processor = processors [processor_index]
selected display displays [display_index]
print("Awesome choice on your preferences!")
filtered phones = [
phone for phone in phones.
if (selected brand. lower() in phone["brand"].lower() and price_options[0] <= phone['price'] <price_options[1] and ram <= phone['ram'] and
storage < phone['storage'] and
selected_processor.lower() in phone['processor'].lower() and selected_display.lower() in phone['display'].lower())
if filtered_phones:
else:
print("Found (len(filtered_phones)) phones that match your criteria!")
return filtered phones
print("Sorry, no phones found that match your criteria. Here are some alternative choices:") return random.sample (phones, min(3, len(phones)))
#Function to display phone details
def display_phone_details(phone):
print("\nHere are the details of the chosen phone:") 
print(f"Name: (phone['name']}") print("Brand: (phone["brand"]}") print("Price: ${phone['price']}") print("RAM: (phone['ram']) GB")
print("storage: (phone['storage']} GB") print("Processor: (phone['processor']}")
print("Display: (phone['display']}")
print("Battery: (phone['battery']} hours")
print(f"Category: (phone['category']}")
print("other Features: (phone['other_features']}") print("
#Function to choose tablets
def choose tablets (tablets):
print("Let's find the perfect tablet for you!")
#Gather options for user selection
brands= get_unique_options (tablets, 'brand') price_options[15000, 30000] # Example fixed range ram_options= get_unique_options (tablets, 'ram') storage_options= get_unique_options (tablets, 'storage') processors = get_unique_options (tablets, 'processor') displays get_unique_options (tablets, 'display')
# Display options with numbers print("Available Brands:")
for i, brand in enumerate(brands, 1):
print (f"(i). (brand)")
print("Price Range: ${price_options[0]} to ${price_options[1]}")
print("Available RAM options (GB):",
.join(map(str, ram_options)))
print("Available Storage options (GB):", .join(map(str, storage_options)))
print("Available Processors: ")
for i, processor in enumerate(processors, 1):
print("(i). (processor}")
print("Available Display Types: ")
for i, display in enumerate(displays, 1): print (f" (i). (display}")
#User selections using numbers
brand_index= int(input("Choose a brand number: ")) - 1
price range input (f"Choose a price range (e.g., (price_options[0])-(price_options[1]}): ").split('-') ram = int(input("Choose minimum RAM (e.g., (min(ram_options)}): "))
storage int(input(f"Choose minimum Storage (e.g., (min(storage_options)}): "))
processor_index= int(input("Choose a processor number: ")) - 1
display_index= int(input("Choose a display type number: ")) 1
selected brand brands[brand_index]
selected_processor = processors [processor_index]
selected display displays[display_index]
print("Awesome choice on your preferences!")
filtered tablets = [
tablet for tablet in tablets
if (selected_brand. lower() in tablet["brand"].lower() and price_options[0] <= tablet['price'] <price_options[1] and ram <= tablet['ram'] and
storage <tablet['storage'] and
selected_processor.lower() in tablet['processor'].lower() and selected_display.lower() in tablet['display'].lower())
if filtered tablets:
else:
print("Found (len(filtered tablets)} tablets that match your criterial") return filtered_tablets
print("Sorry, no tablets found that match your criteria. Here are some alternative choices:") return random.sample(tablets, min(3, len(tablets)))
#Function to display tablet details
def display tablet_details(tablet):
print("\nHere are the details of the chosen tablet:") print("
print("Name: (tablet['name']}")
print("Brand: (tablet["brand"]}")
print("Price: $(tablet['price']}")
print("RAM: (tablet['ram']} GB")
print("Storage: (tablet['storage']} GB")
print("Processor: (tablet['processor']}")
print("Display: (tablet['display']}")
print(f"Battery: (tablet['battery']} hours")
print(f"Category: (tablet['category']}")
print("Other Features: (tablet['other_features"]}") print("*******---------
#Function to choose cameras
def choose_cameras (cameras):
print("Let's find the perfect camera for you!")
#Gather options for user selection
brands = get_unique_options(cameras, "brand")
price_options= [5000, 30000] # Example fixed range
megapixel_options= get_unique_options (cameras, megapixels')
battery options get_unique_options (cameras, 'battery')
# Display options with numbers print("Available Brands:")
for i, brand in enumerate(brands, 1):
print("(i). (brand)")
print("Price Range: ${price_options[0]) to $(price_options[1]}")
print("Available Megapixel options:",, .join(map(str, megapixel_options)))
print("Available Battery options (hours):",, .join(map(str, battery options)))
# User selections using numbers
brand_index
price range
int(input("Choose a brand number: ")) - 1
input("Choose a price range (e.g., (price_options[0]}-{price_options[1])): ").split('-')
megapixels = int(input(f"Choose minimum Megapixels (e.g., (min(megapixel_options)}): ")) battery int(input(f"Choose minimum Battery Life (e.g., (min(battery_options)}): "))
selected_brand brands [brand_index]
print("Awesome choice on your preferences!")
filtered cameras = [
camera for camera in cameras
if (selected_brand.lower() in camera["brand"].lower() and price_options[0] <= camera['price'] <= price_options[1] and megapixels <= camera['megapixels'] and
battery <= camera['battery'])
if filtered_cameras:
else:
print("Found (len(filtered_cameras)) cameras that match your criteria!")
return filtered_cameras
print("Sorry, no cameras found that match your criteria. Here are some alternative choices:") return random.sample(cameras, min(3, len(cameras)))
#Function to display camera details
def display_camera_details(camera):
print("\nHere are the details of the chosen camera:") print("
print("Name: (camera['name']}")
print(f"Brand: (camera["brand"]}")
print("Price: $(camera['price']}")
print("Megapixels: (camera['megapixels']}")
print(f"Battery Life: (camera['battery']} hours")
print(f"Category: (camera['category']}")
print(f"Other Features: (camera['other_features]") 
#Function to choose headphones
def choose headphones (headphones):
print("Let's find the perfect headphones for you!")
# Gather options for user selection
brands get_unique_options (headphones, 'brand') price_options= [500, 10000] # Example fixed range
driver_options= get_unique_options (headphones, 'driver_size") battery options = get_unique_options (headphones, 'battery")
# Display options with numbers
print("Available Brands:")
for i, brand in enumerate(brands, 1):
print(f" (i). (brand)")
print("Price Range: ${price_options[0]} to ${price_options[1]}")
print("Available Driver Sizes (mm):",
'.join(map(str, driver_options)))
print("Available Battery Life (hours):",, .join(map(str, battery options)))
#User selections using numbers
brand_index= int(input("Choose a brand number: ")) 1
price_range= input("Choose a price range (e.g., (price_options[0]}-{price_options[1]}): ").split('-') battery int(input(f"Choose minimum Battery Life (e.g., (min(battery options)}): "))
selected_brand= brands[brand_index]
print("Awesome choice on your preferences!")
filtered_headphones = [
headphone for headphone in headphones
if (selected_brand. lower() in headphone[ 'brand'].lower() and
price_options[0] <= headphone['price'] <= price options[1] and battery <= headphone['battery'])
if filtered_headphones:
print("Found (len(filtered_headphones)} headphones that match your criteria!")
return filtered_headphones
else:
print("Sorry, no headphones found that match your criteria. Here are some alternative choices:") return random.sample(headphones, min(3, len(headphones)))
#Function to display headphone details
def display_headphone_details(headphone):
print("\nHere are the details of the chosen headphone:") print("
print("Name: (headphone['name']}")
print("Brand: (headphone["brand"]}")
print("Price: $(headphone['price']}")
print("Battery Life: (headphone['battery']} hours")
print("Category: (headphone['category']}")
print("other Features: (headphone['other_features']}")
print("
def get_feedback():
feedback
input("How would you rate your experience on a scale of 1 to 5?")
comments input("Any additional comments or suggestions?") print("Thank you for your feedback! It helps us improve.")
#Main function to run the gadget recommendation system
def main():
user_name = input("Welcome! Please enter your name: ")
print("Hello, (user_name)! Welcome to the Smart Choice gadget recommendation system!")
print("Before we start, I'd love to know more about what you're looking for.")
category= input("what type of device are you interested in? (Laptop, Phone, Tablet, Camera, Headphones): ").strip().lower()
budget = input("What is your budget range? (e.g., 20000-50000): ")
usage input("what will you primarily use the device for? (e.g., Gaming, Work, Entertainment, Photography): ").strip().lower() brand preference input("Do you have a preferred brand? (e.g., Dell, Apple, Samsung, etc., or type 'Any' for no preference): ").stri feature_importance input("which feature is most important to you? (e.g., Battery life, Performance, Camera quality): ").strip().low print("Great! You are looking for a (category) within the budget of (budget), primarily for (usage), with a preference for {brand_pr
laptops
load_data('laptops.txt')
phones
load_data('phones.txt')
tablets
load_data('tablets.txt')
cameras
load_data('cameras.txt')
headphones load_data('headphones.txt')
while True:
print("Please choose a category:")
print("1. Laptops")
print("2. Phones")
print("3. Tablets")
print("4. Cameras")
print("5. Headphones")
print("6. Exit")
choice = input("Enter your choice (1-6): ")
if choice == '1':
filtered laptops choose_laptops (laptops) for laptop in filtered_laptops: display_laptop_details(laptop)
elif choice == '2':
filtered phones choose_phones (phones) for phone in filtered phones: display_phone_details(phone)
elif choice = '3':
filtered_tablets choose_tablets (tablets) for tablet in filtered_tablets:
display_tablet_details(tablet)
elif choice "4":
filtered_cameras choose_cameras (cameras) for camera in filtered_cameras:
display_camera_details(camera)
elif choice '5':
filtered_headphones choose_headphones (headphones)
for headphone in filtered_headphones:
display_headphone_details(headphone)
elif choice "6":
print("Thank you for using the Smart Choice gadget recommendation system!")
else:
break
print("Invalid choice. Please select a valid option.")
get_feedback()
# Run the main function
if
name
main()