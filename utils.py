# import text manipulation libraries

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string

# define sentence processing function
def process_sentence (txt):
    """
    Returns the processed version of the sentence in a list.
    
        Parameters:
            sentence (str): A sentence in the form of a string
            
        Returns:
            processed_sentence (list of str): A list of the processed tokens that make up the sentence
    """
    
    # lowercase every word
    txt_lower = txt.lower()
    
    # remove punctuation and digits
    txt_punc_digit = ""
    for char in txt_lower:
        if (char not in string.punctuation + "“’”—") and (char.isdigit() == False):
            txt_punc_digit += char
            
    # tokenize the sentence
    txt_token = word_tokenize(txt_punc_digit)
    
    # remove stop words and stem each word
    stemmer = PorterStemmer()
    txt_processed = []
    for token in txt_token:
        if (token not in stopwords.words('english')):
            txt_processed.append(stemmer.stem(token))
            
    return txt_processed

# define accuracy calculation function
def calc_accuracy (real, prediction):
    """
    Calculates the accuracy of the model in predicting the book in which the sentence appeared.
    
    Parameters:
        real (series): numpy series that holds the real book in which each sentence appears
        prediction (series): numpy series that holds the predicted book in which each sentence appears
        
    Returns:
        accuracy (float): accuracy metric of the classification model
    """
    
    # initiate the count of accurate predictions
    count_right = 0
    
    # iterate over the real and predicted book values
    for real_book, predicted_book in zip(real, prediction):
        
        # if the prediction was accurate, add 1 to the count
        if real_book == predicted_book:
            count_right += 1
    
    # return the accuracy (# of accurate predictions / number of predictions)
    return count_right / len(prediction)