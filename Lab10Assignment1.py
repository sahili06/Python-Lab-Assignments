import pandas as pd

df = pd.read_csv("books.csv")

print("Complete Book Report:\n")
print(df.to_string(index=False))

author_name = input("\nEnter author name: ")
print("\nBooks by given author:\n")
print(df[df['author'] == author_name].to_string(index=False))

publisher_name = input("\nEnter publishing house: ")
print("\nBooks by given publishing house:\n")
print(df[df['publishing_house'] == publisher_name].to_string(index=False))

cheapest_book = df[df['price'] == df['price'].min()]
costliest_book = df[df['price'] == df['price'].max()]

print("\nCheapest Book:\n")
print(cheapest_book[['title', 'price']].to_string(index=False))

print("\nCostliest Book:\n")
print(costliest_book[['title', 'price']].to_string(index=False))

sorted_df = df.sort_values(by='publication_year')

print("\nBooks sorted by publication year:\n")
print(sorted_df.to_string(index=False))
