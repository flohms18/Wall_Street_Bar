import numpy as np

Menu_WS = {
    "Draft Bear": {
        'Goose IPA': 9.9,
        'Ginette Blanche': 7,
        'Kwak fruit rouge': 10,
        'Triple Karmeliet': 9.9,
    },
    "Bottles Beer": {
        "Chouffe": 6.6,
        "Parisis Ambre": 5,
        "Chouf Cherry": 4,
    },
}

for category in Menu_WS:
    for item in Menu_WS[category]:
        Menu_WS[category][item] = np.random.rand()

# Now print the updated Menu_WS nicely
for category, items in Menu_WS.items():
    print(f"Category: {category}")
    for item, price in items.items():
        print(f"  {item}: {price:.2f}")



