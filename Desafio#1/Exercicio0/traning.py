"""
Universidade Tecnológica Federal do Paraná
Departamento de Informática
Mineração de Dados
Thiago H Silva
#---------------------------------------------------------------------------------------------------------------------------#
Exercício 0:
    1. Fazer o download dos dados do desafio https://www.kaggle.com/c/mindados2021/
    2. Carregar os dados na linguagem que você está seguindo nos treinamentos recomendados (Python ou R).
    3. Usar esses dados para praticar os comandos básicos aprendidos no treinamento seguido.
"""
import pandas as pd

def main ():
    """
        In the cell below, create a DataFrame fruits that looks like this:
            Apples	Bananas
        0	30	    21
    """
    fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})
    #print(fruits)
    """
        Create a dataframe fruit_sales that matches the diagram below:
                    Apples	Bananas
        2017 Sales	35	    21
        2018 Sales	41	    34
    """
    fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])
    #print(fruit_sales)
    """
        Create a variable ingredients with a Series that looks like:
        Flour     4 cups
        Milk       1 cup
        Eggs     2 large
        Spam       1 can
        Name: Dinner, dtype: object
    """
    ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')
    #print(ingredients)
    """
        Read the following csv dataset of wine reviews into a DataFrame called reviews:
    """
    reviews = pd.read_csv("../Data/reviewsTrainCharlotte.csv", index_col=0) 
    #print(reviews)
    """
        Run the cell below to create and display a DataFrame called animals:
        In the cell below, write code to save this DataFrame to disk as a csv file with the name cows_and_goats.csv
    """
    animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
    #animals.to_csv('cows_and_goats.csv')

    #---------------------------------------------------------------------------------------------------------------------------#
    
    """
        Select the description column from reviews and assign the result to the variable desc.
    """
    desc = reviews.text
    #print(desc)
    """
        Select the first value from the description column of reviews, assigning it to variable first_description.
    """
    first_description = reviews.text.iloc[0]
    #print(first_description)
    """
        Select the first row of data (the first record) from reviews, assigning it to the variable first_row.
    """
    first_row = reviews.iloc[0]
    #print(first_row)
    """
        Select the first 10 values from the description column in reviews, assigning the result to variable first_descriptions.
    """
    first_descriptions = reviews.text.iloc[0:10]
    #print(first_descriptions)
    """
        Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.
    """
    sample_reviews = reviews.iloc[[1, 2, 3, 5, 8]]
    #print(sample_reviews)
    """
        Create a variable df containing the country, province, region_1, and region_2 columns of the records with the index labels 0, 1, 10, and 100.
    """
    df = reviews.iloc[[0, 1, 10, 100], [1, 2, 3, 5]]
    #print(df)
    """
        Create a variable df containing the country and variety columns of the first 100 records.
    """
    df = reviews.iloc[0:100,[0, 5]]
    #print(df)
    """
        Create a DataFrame italian_wines containing reviews of wines made in Italy.
    """
    italian_wines = reviews.loc[reviews.funny == 5]
    #print(italian_wines)

    #---------------------------------------------------------------------------------------------------------------------------#

    """
        What is the median of the points column in the reviews DataFrame?
    """
    median_points = reviews.useful.median()
    #print(median_points)
    """
        What countries are represented in the dataset? (Your answer should not include any duplicates.)
    """
    countries = reviews.business_id.unique()
    #print(countries)
    """
        How often does each country appear in the dataset? Create a Series reviews_per_country mapping countries to the count of reviews of wines from that country.
    """
    reviews_per_country = reviews.business_id.value_counts()
    #print(reviews_per_country)
    """
        Create variable centered_price containing a version of the price column with the mean price subtracted.
    """
    centered_price = reviews.useful.map(lambda p: p - reviews.useful.mean())
    #print(centered_price)
    """
        I'm an economical wine buyer. Which wine is the "best bargain"? Create a variable bargain_wine with the title of the wine with the highest points-to-price ratio in the dataset.
    """
    bargain_list = reviews.useful / reviews.funny
    bargain_index = bargain_list.index[bargain_list == bargain_list.max()]
    bargain_wine = reviews.business_id[bargain_index[0]]
    #print(bargain_wine)

if __name__ == '__main__':
    main ()