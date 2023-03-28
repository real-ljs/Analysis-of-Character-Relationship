# Analysis-of-Character-Relationship
金庸小说人物关系分析
##  代码结构说明
```
|——jinyong
    |——data
	|——bangs.txt  #  帮派词库
	|——kungfu.txt #  功夫词库
	|——names.txt  #  小说人物名词库
|——result # 保存结果
|——model  # 模型参数
|—— counts.py # 数据读取、数据转换等预处理逻辑
|—— train.py # word2vec训练代码
|—— use.py # word2vec使用代码
```

## 说明

数据已经爬好放在jinyong/data文件夹里

couts.py目前可以实现的功能：

1. 给定小说名称（需要为金庸笔下的十五部小说之一），绘制出小说中出现频率最高的五位人物，五个帮派，五项武功（top k，其中k可调）

2. 绘制金庸小说宇宙人物关系图
3. 绘制金庸小说宇宙帮派关系图

train.py为word2vec的处理及训练函数，训练后的模型参数可保存在model文件夹下

use.py目前可实现的功能：

1. 给定人物/武功/帮派名称，输出金庸小说宇宙中与其最相似的人物/武功/帮派
2. 给定人物/武功/帮派关系对（A，B），及询问人物/武功/帮派C，输出与C有如（A，B）关系的人物/武功/帮派D
