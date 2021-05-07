import math
from collections import Counter
# �������tfidf��ʽ�ĺ���
# count[word]���Եõ�ÿ�����ʵĴ�Ƶ�� sum(count.values())�õ��������ӵĵ�������
def tf(word, count):
    return count[word] / sum(count.values())
# ͳ�Ƶ��Ǻ��иõ��ʵľ�����
def n_containing(word, count_list):
    return sum(1 for count in count_list if word in count)
# len(count_list)��ָ���ӵ�������n_containing(word, count_list)��ָ���иõ��ʵľ��ӵ���������1��Ϊ�˷�ֹ��ĸΪ0
def idf(word, count_list):
    return math.log(len(count_list) / (1 + n_containing(word, count_list)))
# ��tf��idf���
def tfidf(word, count, count_list):
    return tf(word, count) * idf(word, count_list)
# 1.���Ͽ�
train = load_data(filename, separation='\t')
corpus = train['packagename']
# 2.�����Ͻ��зִ�
word_list = []
for i in range(len(corpus)):
    word_list.append(corpus[i].split(','))
# 3.ͳ�ƴ�Ƶ
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
        tf_vec = len(arr)  # ����ÿ����app����
        # tf_vec = np.zeros(len(all_dict)) # ����tf-vector
        # for k, word in enumerate(all_dict.keys()):
        #     k_tf = tf(word, arr)
        #     tf_vec[k] = k_tf
        tfin.write(str(train['uid'][i]) + '\t' + str(tf_vec) + '\n')
        sum_apps += tf_vec
    print(sum_apps, '\t', sum_apps / len(countlist))
print('All program are OJBK!')
