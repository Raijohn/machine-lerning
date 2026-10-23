sizes = [500,1000,1500,2000]
prices = [100000, 200000, 300000, 400000]



def predict_price(size):

    price_per_sqft = prices[0]/sizes[0]
    return size * price_per_sqft

new_size = 1750

    

print("Predicted House Price: $", predict_price(new_size))