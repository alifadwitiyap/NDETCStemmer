import gdown
from checksumdir import dirhash
import shutil
import os
import requests
from tqdm import tqdm

class ModelDownloader:
	def __init__(self):
		self._model_1_id = "1DJ_u_xKSXmgS_CsM0xlB5rIznnDVfz-w"
		self._model_2_id = "1DQhPp-D3o0e-x3PfJd2Il3vf7wVgZu4J"
		self._model_3_id = "1zCn5YINEC82cZ1SH-nB4WXUvuELCzKu-"
		self._md5="f94b050f583fd7fedbf53c88d2ec8698"

		self._path=os.path.dirname(__file__) 
		self._path = os.path.join(self._path,'Model')
  
	def run(self):
		while not self._isValidModel() or not self._isModelExist():
			self._downloadModel()

	def _isModelExist(self):
		return os.path.exists(self._path)

	def _isValidModel(self):
		if self._isModelExist() and dirhash(self._path)!=self._md5:
			print('Broken model, delete model....')
			shutil.rmtree(self._path)
			return False
		return True

	def _downloadModel(self):
		if  not os.path.exists(self._path):
			print('Model missing, downloading new model....')
			os.mkdir(self._path)
			print("\nDownloading Model 1/3")
			gdown.download(id=self._model_1_id,output=os.path.join(self._path,'w2vec_wiki_id_case'))

			print("\nDownloading Model 2/3")
			gdown.download(id=self._model_2_id,output=os.path.join(self._path,'w2vec_wiki_id_case.trainables.syn1neg.npy'))

			print("\nDownloading Model 3/3")
			gdown.download(id=self._model_3_id,output=os.path.join(self._path,'w2vec_wiki_id_case.wv.vectors.npy'))

			print("\nDownload Complete")
   
class CustomModelDownloader:
	"""
	
	# CustomModelDownloader
 
	This class is used to create a downloader instance using custom external links. 
 	It will download all data needed and check the hash if its a matching with the original models.
  
	### Params
	model_1: str: Link to download with original file name `w2vec_wiki_id_case`
 
	model_2: str: Link to download with original file name `w2vec_wiki_id_case.trainables.syn1neg.npy`  
 
	model_3: str: Link to download with original file name `w2vec_wiki_id_case.wv.vectors.npy`
 	"""

	def __init__(self, model_1: str, model_2: str, model_3: str):
		self._md5="f94b050f583fd7fedbf53c88d2ec8698"
  
		self.model_1 = model_1
		self.model_2 = model_2
		self.model_3 = model_3

		self._path=os.path.dirname(__file__) 
		self._path = os.path.join(self._path,'Model')

		while not self._isValidModel() or not self._isModelExist():
			self._downloadModel()

	def run(self):
		while not self._isValidModel() or not self._isModelExist():
			self._downloadModel()
   
	def _isModelExist(self):
		return os.path.exists(self._path)

	def _isValidModel(self):
		if self._isModelExist() and dirhash(self._path)!=self._md5:
			print('Broken model, delete model....')
			shutil.rmtree(self._path)
			return False
		return True

	def _downloadFile(self, url: str, fname: str):
		CHUNK_SIZE = 1024
		resp = requests.get(url, stream=True)
		total = int(resp.headers.get('content-length', 0))
		with open(fname, 'wb') as file, tqdm(
			desc=fname,
			total=total,
			unit='iB',
			unit_scale=True,
			unit_divisor=1024,
		) as bar:
			for data in resp.iter_content(chunk_size=CHUNK_SIZE):
				size = file.write(data)
				bar.update(size)

	def _downloadModel(self):
		if  not os.path.exists(self._path):
			print('Model missing, downloading new model....')
			os.mkdir(self._path)
			print("\nDownloading Model 1/3")
			fname=os.path.join(self._path,'w2vec_wiki_id_case')
			self._downloadFile(self.model_1, fname)

			print("\nDownloading Model 2/3")
			fname=os.path.join(self._path,'w2vec_wiki_id_case.trainables.syn1neg.npy')
			self._downloadFile(self.model_2, fname)

			print("\nDownloading Model 3/3")
			fname=os.path.join(self._path,'w2vec_wiki_id_case.wv.vectors.npy')
			self._downloadFile(self.model_3, fname)

			print("\nDownload Complete")