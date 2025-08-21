# Define constants
total_land = 80
segments = 5
segment_area = total_land / segments  # 16 acres each

#Tomato
tomato_area_1 = 0.3 * segment_area  # 30%
tomato_area_2 = 0.7 * segment_area  # 70%
tomato_yield_1 = tomato_area_1 * 10  # in tonnes
tomato_yield_2 = tomato_area_2 * 12  # in tonnes
tomato_total_yield = tomato_yield_1 + tomato_yield_2
tomato_price_per_kg = 7
tomato_sales = tomato_total_yield * 1000 * tomato_price_per_kg  # tonnes to kg

# Potato 
potato_yield = segment_area * 10
potato_price_per_kg = 20
potato_sales = potato_yield * 1000 * potato_price_per_kg

# Cabbage
cabbage_yield = segment_area * 14
cabbage_price_per_kg = 24
cabbage_sales = cabbage_yield * 1000 * cabbage_price_per_kg

# Sunflower
sunflower_yield = segment_area * 0.7
sunflower_price_per_kg = 200
sunflower_sales = sunflower_yield * 1000 * sunflower_price_per_kg

# Sugarcane 
sugarcane_yield = segment_area * 45
sugarcane_price_per_tonne = 4000
sugarcane_sales = sugarcane_yield * sugarcane_price_per_tonne

# Total sales
total_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales

# Chemical-free sales after 11 months (Tomato, Potato, Cabbage, Sunflower)
chemical_free_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales

# Print results
print(f"a. Total sales from all 80 acres is: Rs. {total_sales:,.2f}")
print(f"b. Sales from chemical-free farming after 11 months is: Rs. {chemical_free_sales:,.2f}")