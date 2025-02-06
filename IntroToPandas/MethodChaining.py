import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    Heavy_animals = animals[animals['weight']>100]
    Sorted_ha = Heavy_animals.sort_values(by='weight',ascending=False)
    return Sorted_ha.columns[['name']]
