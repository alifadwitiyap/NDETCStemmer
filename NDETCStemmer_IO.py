from NDETCStemmer import NDETCStemmer

stemmer=NDETCStemmer()


# From text test

# import NDETCStemmer library
from NDETCStemmer import NDETCStemmer

#init stemmer
stemmer=NDETCStemmer()

# stemming process
output=stemmer.stem('boleh saya memerah lembu ini')

print(output)
#boleh saya perah lembu ini

print(stemmer.stem('bibirnya memerah tangannya jadi selengket madu'))
# #bibir merah tangan jadi lengket madu





# # from file test

# import time
# from NDETCStemmer.Utility import normalizer

# input_dir='test/lp/input_lp.txt'
# corr_dir='test/lp/correct_output_lp.txt'

# t = time.process_time()
# best_word=stemmer.stem(input_dir,from_file=True)
# elapsed_time = time.process_time() - t
# print(f'runtime : {elapsed_time}ms')


# correct_output = normalizer.normalize(corr_dir,from_file=True)
# input_words = normalizer.normalize(input_dir,from_file=True)

# ambiguous_word = list()
# unique_ambiguous_word = set()
# for keys in best_word:
#     if len(best_word[keys]) > 1:
#         ambiguous_word.append([input_words[keys], best_word[keys]])
#         unique_ambiguous_word.add(input_words[keys])

# num_correct_stem = 0

# num_correct_stem = 0




# incorrect_stem = dict()

# unique_incorrect_stem = list()

# correct_stem = dict()

# print(len(best_word), len(correct_output))

# for keys in range(len(best_word)):
#     if best_word[keys][0] == correct_output[keys]:
#         num_correct_stem += 1
#         correct_stem[keys] = [input_words[keys], best_word[keys][0], correct_output[keys]]
#     else:
#         incorrect_stem.update({keys: [input_words[keys], best_word[keys][0], correct_output[keys]]})
#         if [input_words[keys], best_word[keys][0], correct_output[keys]] not in unique_incorrect_stem:
#             unique_incorrect_stem.append([input_words[keys], best_word[keys][0], correct_output[keys]])

# num_unique = list()
# for idx in range(len(unique_incorrect_stem)):
#     num = 0
#     for keys in incorrect_stem:
#         if unique_incorrect_stem[idx][0] == incorrect_stem[keys][0] \
#                 and unique_incorrect_stem[idx][1] == incorrect_stem[keys][1] and \
#                 unique_incorrect_stem[idx][2] == incorrect_stem[keys][2]:
#             num += 1
#     num_unique.append(num)

# print(len(ambiguous_word), len(unique_ambiguous_word))
# print('\nTotal word:', len(best_word))

# print('Total correct:', num_correct_stem)
# print('Total incorrect:', len(incorrect_stem))
# print('Total incorrect Unique:', len(unique_incorrect_stem))
# print('Incorrect Stem:', len(incorrect_stem))
# print('Unique Incorrect Stem:', len(unique_incorrect_stem))
# for idx in range(len(unique_incorrect_stem)):
#     print(idx+1, unique_incorrect_stem[idx][0], unique_incorrect_stem[idx][1],
#         unique_incorrect_stem[idx][2], num_unique[idx])

# print('\nAccuracy:', round(num_correct_stem / len(best_word), 4))

# print(len(incorrect_stem), len(unique_incorrect_stem), round(num_correct_stem / len(best_word), 4))

# print(round(num_correct_stem / len(best_word), 4))
