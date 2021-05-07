import math
from collections import Counter
# 定义计算tfidf公式的函数
# count[word]可以得到每个单词的词频， sum(count.values())得到整个句子的单词总数
def tf(word, count):
    return count[word] / sum(count.values())
# 统计的是含有该单词的句子数
def n_containing(word, count_list):
    return sum(1 for count in count_list if word in count)
# len(count_list)是指句子的总数，n_containing(word, count_list)是指含有该单词的句子的总数，加1是为了防止分母为0
def idf(word, count_list):
    return math.log(len(count_list) / (1 + n_containing(word, count_list)))
# 将tf和idf相乘
def tfidf(word, count, count_list):
    return tf(word, count) * idf(word, count_list)
# 1.语料库
train = load_data(filename, separation='\t')
corpus = train['packagename']
# 2.对语料进行分词
word_list = []
for i in range(len(corpus)):
    word_list.append(corpus[i].split(','))
# 3.统计词频
countlist = []
for i in range(len(word_list)):
    count = Counter(word_list[i])
    countlist.append(count)
all_dict = {}
for counte in countlist:
    counter = dict(counte)
    for k, v in counter.items():
        try:
            all_dict[k] += v
        except:
            all_dict[k] = v
# all_dict = sorted(all_dict.items(), key=lambda kv: (kv[1], kv[0]))
print('merge-->')
with open('user_appCount.txt', 'w+') as ucin, open('idf.txt', 'w+') as idfin:
    for k in all_dict.keys():
        # k_tf = tf(k, countlist)
        ucin.write(k + '\t' + str(all_dict[k]) + '\n')
        k_idf = idf(k, countlist)
        idfin.write(k + '\t' + str(k_idf) + '\n')
with open('user_appNum.txt', 'w+') as tfin:
    sum_apps = 0
    for i, arr in enumerate(countlist):
        tf_vec = len(arr)  # 计算每个人app数量
        # tf_vec = np.zeros(len(all_dict)) # 计算tf-vector
        # for k, word in enumerate(all_dict.keys()):
        #     k_tf = tf(word, arr)
        #     tf_vec[k] = k_tf
        tfin.write(str(train['uid'][i]) + '\t' + str(tf_vec) + '\n')
        sum_apps += tf_vec
    print(sum_apps, '\t', sum_apps / len(countlist))
print('All program are OJBK!')
