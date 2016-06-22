#here we will identify whether the numbers in two series are in same directions or not
#so we identify
#       1. whether each number is above the mean or not. this will return a series of booleans. We do this for both the series
#       2. then we compare both the series to generate another series which help us identify if data moves in same direction
#       3. finally sum the booleans. True = 1 False = 0
import pandas as pd

countries = ['Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
             'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
             'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
             'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia']

life_expectancy_values =  [74.7,  75. ,  83.4,  57.6,  74.6,  75.4,  72.3,  81.5,  80.2,
                          70.3,  72.1,  76.4,  68.1,  75.2,  69.8,  79.4,  70.8,  62.7,
                          67.3,  70.6]

gdp_values = [ 1681.61390973,   2155.48523109,  21495.80508273,    562.98768478,
              13495.1274663 ,   9388.68852258,   1424.19056199,  24765.54890176,
              27036.48733192,   1945.63754911,  21721.61840978,  13373.21993972,
                483.97086804,   9783.98417323,   2253.46411147,  25034.66692293,
               3680.91642923,    366.04496652,   1175.92638695,   1132.21387981]
               
life_expectancy_series = pd.Series(life_expectancy_values)
gdp_series = pd.Series(gdp_values)

def variable_correlation(variable1, variable2):
    comp_var1 = variable1>=variable1.mean()
    comp_var2 = variable2>=variable2.mean()
    direction = comp_var1 == comp_var2
    print(direction.sum(),len(direction)-direction.sum())
    return(direction.sum(),len(direction)-direction.sum())
    
print(variable_correlation(life_expectancy_series, gdp_series))
