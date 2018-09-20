import numpy as np

from deeppavlov.dataset_iterators.sqlite_iterator import SQLiteDataIterator
from deeppavlov.skills.odqa.basic_neural_context_encoder import BasicNeuralContextEncoder

iterator = SQLiteDataIterator(load_path='/media/olga/Data/projects/DeepPavlov/download/odqa/enwiki_full_chunk.db')
encoder = BasicNeuralContextEncoder(load_path='/media/olga/Data/projects/DeepPavlov/download/bnr/model')
SAVE_PATH = '/media/olga/Data/projects/DeepPavlov/download/odqa/chunk_vectors'

all_vectors = np.empty(shape=(512,))

# i = 0
for docs, _ in iterator.gen_batches(batch_size=100):
    # if i == 2:
    #     break
    batch_vectors = encoder(docs)
    all_vectors = np.vstack((all_vectors, batch_vectors))
    # i += 1


all_vectors = np.delete(all_vectors, 0, axis=0)
print(type(all_vectors))
print(all_vectors.shape)
np.save(SAVE_PATH, all_vectors)
# a = np.load('/media/olga/Data/projects/DeepPavlov/download/odqa/chunk_vectors.npy')
# print(a)
