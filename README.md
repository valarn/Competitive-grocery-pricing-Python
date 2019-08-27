## Market evaluation of the grocery products

Vala Rahmani August 2019


## Table of contents


- [Overview](#Overview)

- [Approach](#Approach)

- [Scraper](#Scraper)

- [Cleaning](#Cleaning)

- [How to use](#How_to_use)

- [Suggested Work](#Suggested_Work)

- [Additional Resources](#Additional_Resources)



<a id='Overview'></a>
# Overview
---

How should you position your products to stay competitive?

With the rise of online grocery shopping, it has become more important than ever for brands to choose the right pricing and seo strategies to stay competitive. Unlike Brick and mortar grocery stores, where brands can rent out better shelf spaces to position their products in the best locations, online stores are all about seo optimization, and competitive pricing. Even though it is cheaper to sell products online, the winning brands are the ones who utilize data efficiently to show up on the top of the search ahead of their competitors. Consumer Packaged Goods companies spend a lot of money buying data from third party institutions such as IRI and Nielson when a lot of the data collected are already publicly available. The goal of this website is to help small business owners who are trying to enter the highly saturated CPG market, research the top keywords and the best pricing practices to stay competitive and grow their brands outreach. This website has used the Target, Whole Foods, Amazon and Bristol Farms' websites to scrape thru their products, and gather all of the information available about every single item. The total number of rows for the dataset is 13615 and the prices are for the 90048 zipcode in Los Angeles, CA. 

Dairy|Produce|Snacks & Sweets|Pantry|Bread & Bakery|
Frozen Foods|Meat & Seafood|Breakfast & Cereals|Specialty Diets|Nutrition & Weight Loss|
Beverages|Coffee & Tea|Sports & Energy Drink|Deli|

<a id='Approach'></a>
### Approach
---
This application will use NLTK TFidf in order to look into the description of each individual product, and find the most similar products to the one chosen in the first place. Then a recommender system is build up that gives out the top 10 similar products.

<a id='Scraper'></a>
### Scraping
---
The most important part, and most time consuming part is the scraping. For the sake of comprehensiveness of data, product information from Target, Whole Foods, Bristol Farms and Amazon Website were collected. Targest Same Day Delivery website makes it very hard for the scraper to capture all of the products and by using solely BeautifulSoup or Selenium it is almost impossible to capture the necessary data. Therefore, a combination of both is used so every part of each product page would get scraped. Moreover, Target provides its customers with text data of the nutritional facts. However, Amazon Prime Now platform does not provide comprehensive nutritional values and in most cases only a photo of the Nutritional Facts label is available which reading it goes beyond the scope of this web app. Amazon_Prime_Now_on_Demand_Scraper notebook contains the 'amazon_beast' function which would allow users to scrape desired categories by inputting a list of the categories, zipcode and the desired filename for the csv outcome. 
The Target Scraper notebook on the other hand needs more hands on approach since Target's html requires the mouse be on the Chrome Driver while the scraping is in progress. Otherwise many products will be missed since the 'lazy load' prevents BeatifulSoup from capturing all of the product links.

<a id='Cleaning'></a>
### Cleaning
---
After the Scraping is done regex is used to find the common patterns in the name and the description to clean up the special characters and the unnecessary information in the data. English Stopwords and some common words such as important, calorie,etc. were removed as well since they repeated in more than 90 percent of the data. Since the scraper was designed ground up by me, not much cleaning was needed and the amount of the missing data was very limited. The price column for 255 products was missing which meant that these items were either out of stock or not produced by the manufacturer. Therefore, they were dropped from the dataset. After data is put into the same clean format the Prime Now dataframe and Target were joined together so preprocessing for modeling could be started.

<a id='Modeling'></a>
### Modeling 
---
Recommender systems are unsupervised models where there is no one prediction. The model provides user with the most similar items in the row. In order to get the numeric columns for the description the Tf-idf was used with ngram_range of 1-3 and a score based on the frequency words were assigned to each word. Then these scores were put in a sparse matrix to find the pairwise distances between the products. Now we have a working recommender system that uses 'cosine' similarities between product descriptions to predict the best alternatives to a product. 

<a id='Future enhancements'></a>
### Future tweaks
Even though Tf-idf does a decent job predicting the alternative product, using the Doc2Vec from Gensim seems like a better approach to find the best alternatives to a product since it scans thru the sentences and models over the context of the document. In the notebooks you can find the 'Recommender-doc2vec-incomplete notebook' where most parts of the modeling has been done, however building_vocab has been giving some trouble.


