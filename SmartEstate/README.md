# Smart Estate

**Description:** This project creates Decision Tree and Random Forest Machine Learning models to predict the sale price of a home given a dataset with ~80 features.

**Tools & Techniques:** Python(numpy, Jax, pandas, seaborn, matplotlib, fast_ml), Decision Trees, Random Forest

**Dataset:** 

`train.csv`
+ 81 Features
+ 1461 Records

`test.csv`
+ 81 Features
+ 1461 Records

**High Level Steps**

1. Load the data from the training and testing datasets and read into a pandas dataframe
2. Clean the data

   2a. Remove features with all `NULL` values

   2b. Remove features where 95% or more of the values are identical

   2c. Fill N/A values and encode categorical values

3. Create a DecisionTree class that takes `x` features, `y` outputs, current tree depth and a max tree depth as arguments
4. Create a RandomForest class that generates `n` DecisionTrees objects to tune the attributes to make accurate predictions
5. Test the model accuracy against using the test 
