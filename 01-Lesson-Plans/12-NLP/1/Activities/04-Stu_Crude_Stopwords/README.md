
# Crude Stopwords

In this activity, you will practice creating a function that strips non-letter characters from a document and then applies stopwording.

## Instructions

1. Run the provided code to process necessary imports and store an article from NLTK's `reuters` module to use in the activity.

2. Complete the function called `clean_text`. This function will take in the `article` and return a list of words that does not include stopwords or any non-letter characters:
    * Inside the `clean_text` function, create a `set` of stopwords using `set(stopwords.words())`, storing them in a variable. 
    * Next, define the regex parameters using `regex = re.compile("[^a-zA-Z ]")`.
    * Run the inputted document through the regex parameters and store the result in a new variable using `regex.sub('', article)`.
    * Pass this new list of words through the `word_tokenize()` function and store the result in a new variable.
    * Create a final list of all lower-case words that does not include stop words. To do this, use a list comprehension that keeps only those words that are not in the stopword list: `output = [word.lower() for word in words if word.lower() not in sw]`
    * Finally, have the function return this `output`.

3. Pass an article into this function, and store the results in a new variable. Using the `set` function, print the unique words from the result, keeping track of words that are uninformative. 

4. Using these results, reimplement `clean_test`, but this time with a set of custom stopwords to apply.
    * Create custom stopwords by defining a set and adding your words. For example: `sw_addons = {'said', 'today', 'week'}`.
    * These custom words can be added to the existing set of stopwords using the `union` method. For example: `output = [word.lower() for word in words if word.lower() not in sw.union(sw_addons)]`.

5. Finally, pass your article into this updated function and example new results.


© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.

