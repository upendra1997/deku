
# coding: utf-8

# In[11]:


import nltk
from nltk.corpus import stopwords


# In[28]:

class classifier_mine:

	def __init__(self,message):

		self.count = 0

		#message = "Help me!! There are people after me."
		tokenized_words = nltk.word_tokenize(message)
		#print(tokenized_words)
		stop = set(stopwords.words('english'))

		self.sentence_word = [i for i in message.lower().split() if i not in stop]
		#print(self.sentence_word)


		# In[9]:

		file_reader = open('word_dict.txt','r')
		self.content = file_reader.read()

	# In[30]:
	def counter(self):

		self.count = 0
		for ix in self.sentence_word:
			if ix in self.content:
				#print(ix)
				self.count += 1
		return self.count

	def get_count(self):

		return self.count

obj = classifier_mine("Help me!! There are people after me.")
print(obj.counter())


