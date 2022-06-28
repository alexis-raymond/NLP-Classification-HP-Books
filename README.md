# NLP Project - Harry Potter Books

## Context
In 2022, I challenged myself with deepening my understanding of NLP techniques. Part of my strategy was completing the [DeepLearning.AI Natural Language Processing Specialization](https://www.deeplearning.ai/program/natural-language-processing-specialization/). On June 16th, I [completed](https://www.coursera.org/account/accomplishments/verify/PCDXA6F7GFLX) the first of the four courses which was about *Natural Language Processing with Classification and Vector Spaces*. This course covered:
1. Sentiment Analysis with Logistic Regression
2. Sentiment Analysis with Naive Bayes
3. Vector Space Models
4. Machine Translation and Document Search

Now, I will test my understanding of the concepts covered by working with the Harry Potter Books - my all-time favourite series - on two *fun* use cases. Following this project, I will take my learnings to a more *serious* use case about financial news sentiment analysis.

## Use Cases
I will explore two use cases as part of this learning project:
1. **Text Classification**: Given a sentence from any of the seven books, the model should return the book in which it appeared. This will practice text classification, a similar process to sentiment analysis.
2. **Document Search**: ~~Given any sentence, the model should return a similar, but different sentence. This will practice vector space models and K-Nearest Neighbors.~~ Given any sentence, the model should return the following sentence in the book. This will practice vector space models and K-Nearest Neighbors. The initial intent was to return a similar sentence, but after consideration this was not practical as I do not have labeled data for this type of operation. I don't expect this use case to return a strong accuracy, but it will help me put in practice vector searches, which is the goal of this project.

## Dataset
The dataset used for this project comes the [Kaggle Dataset: Harry Potter Books Corpora (Part 1 - 7)](https://www.kaggle.com/datasets/balabaskar/harry-potter-books-corpora-part-1-7) published by BALA BASKAR. The dataset is structured as seven text files, containing the full text corpus for each of the seven books.

### About the Novel
>Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling. The novels chronicle the lives of a young wizard, Harry Potter, and his friends Hermione Granger and Ron Weasley, all of whom are students at Hogwarts School of Witchcraft and Wizardry.The popularity of the Harry Potter series has translated into substantial financial success for Rowling, her publishers, and other Harry Potter related license holders. The books have sold more than 500 million copies worldwide and have also given rise to the popular film adaptations produced by Warner Bros., all of which have been highly successful in their own right. The total revenue from the book sales is estimated to be around $7.7 billion.

### Content
>This dataset contains the text corpus of all 7 books in Harry Potter series. There are 7 text files, each contains the data from each book of the series.

### Inspiration
>This data can be used to do text mining, various NLP models like sentiment analysis, word embedding, even chatbot to answer the Harry Potter fans.

## Repository
* [create-full-df.ipynb](create-full-df.ipynb): Notebook used to consolidate the text from all seven books into one usable DataFrame.
* [train_test_split.ipynb](train_test_split.ipynb): Notebook used to split the full set of sentences into training, validation and testing datasets.
* [model1-custom-naive.ipynb](model1-custom-naive.ipynb): Notebook used to create the first model to compare - a custom naive bayes algorithm.
* [utils.py](utils.py): Python file with common functions used across notebooks.
* [img/EDA](/img/EDA/): Screenshots and relevant images used when performing Exploratory Data Analysis (EDA).
* [data/processed](/data/processed): Datasets produced by me that are ready to be used for modelling.
* [data/raw](/data/raw): Raw datasets that need to be transformed before being used for modelling.
