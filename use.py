import gensim

def find_relationship(a, b, c):
    d, _ = model.wv.most_similar(positive=[b, c], negative=[a])[0]
    print(f"{a}-{b} is similar to {c}-{d}")

model = gensim.models.Word2Vec.load("model/louis_cha.model")
char=model.wv.most_similar(positive=["降龙十八掌"]) 
print(char)
find_relationship ("郭靖","黄蓉","杨过")
find_relationship("郭靖", "降龙十八掌", "小龙女")
# find_relationship("段誉", "段公子", "乔峰")