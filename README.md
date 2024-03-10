# DKE
I have developed a new NLP method for feature extraction that outperforms traditional Bag of Words and Tf-idf methods. Now I will explain How it's actually works. So Let's get Started!

The model consists of two functions: the `extractor function` and the `counter function`.

**Extractor Function:**

The extractor function initially divides the dataframe based on the classes in the target variable. It then extracts unique words from the first class and stores them as a list. This process is repeated for all classes. Next, it eliminates common words shared among all classes using the inverse set operation. For instance, if the unique words lists for three classes are as follows:

Class A: [a, b, c, d, e]

Class B: [a, f, g, h]

Class C: [a, b, c, l, m]

The resulting output will be:

Class A: [d, e]

Class B: [f, g, h]

Class C: [l, m]

**Counter Function:**

The counter function first creates columns (features) corresponding to the number of classes in the target variable. If the target variable has, for example, 5 classes, then 5 features are created. It then counts the frequency of words extracted by the extractor function for all indices in the dataframe and records these counts in the respective features.
