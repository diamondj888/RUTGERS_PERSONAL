# Segmenting with PCA

In this activity, you will use your knowledge of PCA in order to reduce the dimensionality of a dataset. Then, you'll compare that result to the segmentation of the data using all of the factors.

## Instructions

One of the world's biggest banks launched a machine learning competition in Kaggle, an online community of data scientists and machine learning practitioners. They want to improve their marketing campaigns by identifying the optimal number of customer segments for their clients. They offer a reward of $5,000 that gained your interest, so you decided to put your unsupervised learning skills into practice to participate in the competition.

The bank provided a dataset that consists of customer data that includes ten different features. The data columns were anonymized using generic names to protect customers' privacy, and data values were already normalized.

The PCA technique for dimensional reduction has just come to your attention. At this point, you have already segmented the data based on all of the factors, but are wondering if PCA would alter the segmentation results.

Using the starter code and the customer data provided, reduce the factors to only two dimensions using PCA, determine the optimal value for k using the PCA DataFrame, and then segment the data by using the K-Means algorithm and the optimal value for k. Once these steps are complete, segment the preprocessed customer DataFrame by using the K-means algorithm and that same value for k, and then compare the segmentation results.

This task will involve five parts. Follow the instructions below to accomplish each step.

1. Use PCA to reduce the dimensionality of the `customers_transformed_df` DataFrame to two principal components.

   - Import the PCA module from scikit-learn.

   - Instantiate the instance of the PCA model declaring the number of principal components as two.

   - Using the `fit_transform` function from PCA, fit the PCA model to the `customers_transformed_df` DataFrame. Review the first five rows of list data.

   - Using the `explained_variance_ratio_` function from PCA, calculate the percentage of the total variance that is captured by the two PCA variables. What is the explained variance ratio captured by the two PCA variables?

   - Using the `customer_pca` data, create a Pandas DataFrame called `customers_pca_df`. The columns of the DataFrame should be called "PCA1" and "PCA2".

2. Using the `customers_pca_df` DataFrame, use the elbow method to determine the optimal value of k.

3. Segment the `customers_pca_df` DataFrame using the K-means algorithm and the optimal value for k defined in Step 2.

4. Segment the `customers_transformed_df` DataFrame with all factors by using the K-means algorithm.

5. Compare the segmentation results between the PCA DataFrame and the full-factored DataFrame.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
