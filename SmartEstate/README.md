# Smart Estate

**Description:** This project creates Decision Tree and Random Forest Machine Learning models to predict the sale price of the homes in the `test.csv` dataset. 

**Tools & Techniques:** Python(numpy, Jax, pandas, seaborn, matplotlib, fast_ml), Decision Trees, Random Forest

**Dataset:** 

`train.csv`
+ 81 Features
+ 1461 Records

`test.csv`
+ 80 Features (Excluding Sale Price)
+ 1461 Records

<ins>**High Level Steps:**<ins>

**1. Load the data** from the training and testing datasets and read into a pandas dataframe

**2. Clean the data**

+ Remove features with all `NULL` values

+ Remove features where 95% or more of the values are identical

+ Fill N/A values and encode categorical values

**3. Create a DecisionTree class** that takes `x` features, `y` outputs, current tree depth and a max tree depth as arguments

**4. Create a RandomForest class** that generates `n` DecisionTrees objects to tune the attributes to make accurate predictions
   
**5. Test the model** accuracy by splitting the training dataset
 
+ 75% of the dataset will be used the train the model

+ 25% of the dataset will be used to test the model
   
**6. Utilize the model** to predict the Sale Price for each of the homes in the `test.csv` dataset



