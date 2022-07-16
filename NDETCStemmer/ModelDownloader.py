import wget
import shutil
import os

class ModelDownloader:
	def __init__(self):
		self.model_1_url = "https://github.com/alifadwitiyap/NDETCStemmer/raw/master/NDETCStemmer/Model/w2vec_wiki_id_case"
		self.model_2_url = "https://github.com/alifadwitiyap/NDETCStemmer/raw/master/NDETCStemmer/Model/w2vec_wiki_id_case.trainables.syn1neg.npy"
		self.model_3_url = "https://github.com/alifadwitiyap/NDETCStemmer/raw/master/NDETCStemmer/Model/w2vec_wiki_id_case.wv.vectors.npy"


		self.path=os.path.dirname(__file__) 
		self.path = os.path.join(self.path,'Model')
		self.validateModel()
		self.downloadModel()



	def checkFolderSize(self):
		total = 0
		for entry in os.scandir(self.path):
			if entry.is_file():
				total += entry.stat().st_size
			elif entry.is_dir():
				total += self.checkFolderSize(entry.path)
		return total

	def validateModel(self):
		if os.path.exists(self.path) and self.checkFolderSize()<681817300:
			print('Model have wrong size, delete model....')
			shutil.rmtree(self.path)

	def downloadModel(self):
		if  not os.path.exists(self.path):
			print('Model missing, downloading new model....')
			os.mkdir(self.path)
			print("\nDownloading Model 1/3")
			wget.download(self.model_1_url, self.path)
			print("\nDownloading Model 2/3")
			wget.download(self.model_2_url, self.path)
			print("\nDownloading Model 3/3")
			wget.download(self.model_3_url, self.path)
			print("\nDownload Complete")