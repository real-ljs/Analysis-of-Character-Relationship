import jieba


def load_novel(novel):
    with open(f'./jinyong/novels/{novel}.txt', encoding="u8") as f:
        return f.read()


with open('./jinyong/data/names.txt', encoding="utf-8") as f:
    data = f.read().splitlines()
    novels = data[::2]
    names = []
    for line in data[1::2]:
        names.extend(line.split())

with open('./jinyong/data/kungfu.txt', encoding="utf-8") as f:
    data = f.read().splitlines()
    kungfus = []
    for line in data[1::2]:
        kungfus.extend(line.split())

with open('./jinyong/data/bangs.txt', encoding="utf-8") as f:
    data = f.read().splitlines()
    bangs = []
    for line in data[1::2]:
        bangs.extend(line.split())

for name in names:
    jieba.add_word(name)
for kungfu in kungfus:
    jieba.add_word(kungfu)
for bang in bangs:
    jieba.add_word(bang)
    
# 去重
names = list(set(names))
kungfus = list(set(kungfus))
bangs = list(set(bangs))
    
sentences = []
for novel in novels:
    print(f"处理：{novel}")
    for line in load_novel(novel).splitlines():
        sentences.append(jieba.lcut(line))

import gensim

model = gensim.models.Word2Vec(sentences)
model.save("model/louis_cha.model")