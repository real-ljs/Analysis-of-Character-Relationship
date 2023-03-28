from pyecharts import options as opts
from pyecharts.charts import Graph
import math
import itertools
from collections import Counter
import re
from pyecharts import options as opts
from pyecharts.charts import Tree
from pyecharts import options as opts
from pyecharts.charts import Bar,Page


def load_novel(novel):
    with open(f'./jinyong/novels/{novel}.txt', encoding="u8") as f:
        return f.read()


# 加载人物数据
with open('./jinyong/data/names.txt', encoding="utf-8") as f:
    data = [line.rstrip() for line in f]
novels = data[::2]
names = data[1::2]
novel_names = {k: v.split() for k, v in zip(novels, names)}
# print(",".join(novel_names['天龙八部'][:20]))
del novels, names, data

# 寻找小说主角


def find_main_charecters(novel, num=10, content=None):
    if content is None:
        content = load_novel(novel)
    count = Counter()
    for name in novel_names[novel]:
        count[name] = content.count(name)
    return count.most_common(num)


# 武功分析

with open('./jinyong/data/kungfu.txt', encoding="utf-8") as f:
    data = [line.rstrip() for line in f]
novels = data[::2]
kungfus = data[1::2]
novel_kungfus = {k: v.split() for k, v in zip(novels, kungfus)}
del novels, kungfus, data


def find_main_kungfus(novel, num=10, content=None):
    if content is None:
        # print(novel)
        content = load_novel(novel)
    count = Counter()
    for name in novel_kungfus[novel]:
        count[name] = content.count(name)
    return count.most_common(num)

    
# 门派分析
with open('./jinyong/data/bangs.txt', encoding="utf-8") as f:
    data = [line.rstrip() for line in f]
novels = data[::2]
bangs = data[1::2]
novel_bangs = {k: v.split() for k, v in zip(novels, bangs) if k != "未知"}
del novels, bangs, data


def find_main_bangs(novel, num=10, content=None):
    if content is None:
        content = load_novel(novel)
    count = Counter()
    for name in novel_bangs[novel]:
        count[name] = content.count(name)
    return count.most_common(num)


def show_top10(novel):
    content = load_novel(novel)
    charecters = find_main_charecters(novel, 10, content)[::-1]
    k_c, v_c = map(list, zip(*charecters))

    kungfus = find_main_kungfus(novel, 10, content)[::-1]
    k_k, v_k = map(list, zip(*kungfus))

    bangs = find_main_bangs(novel, 10, content)[::-1]
    k_b, v_b = map(list, zip(*bangs))
    page = Page(layout=Page.DraggablePageLayout)

    bar1 = Bar(init_opts=opts.InitOpts("720px", "320px"))
    bar1.add_xaxis(k_c)
    bar1.add_yaxis("", v_c)
    bar1.reversal_axis()
    bar1.set_series_opts(label_opts=opts.LabelOpts(position="right"))
    bar1.set_global_opts(title_opts=opts.TitleOpts(title=f"{novel}主角"))

    bar2 = Bar(init_opts=opts.InitOpts("720px", "320px"))
    bar2.add_xaxis(k_k)
    bar2.add_yaxis("", v_k)
    bar2.reversal_axis()
    bar2.set_series_opts(label_opts=opts.LabelOpts(position="right"))
    bar2.set_global_opts(title_opts=opts.TitleOpts(title=f"{novel}功夫"))

    bar3 = Bar(init_opts=opts.InitOpts("720px", "320px"))
    bar3.add_xaxis(k_b)
    bar3.add_yaxis("", v_b)
    bar3.reversal_axis()
    bar3.set_series_opts(label_opts=opts.LabelOpts(position="right"))
    bar3.set_global_opts(title_opts=opts.TitleOpts(title=f"{novel}门派"))
    page.add(bar1,bar2,bar3)
    page.render('result/'+str(novel)+".html")

name=input("请输入小说名称:")
show_top10(name)
# show_top10("笑傲江湖")

# 人物关系分析
count = Counter()
for novel in novel_names:
    names = novel_names[novel]
    re_rule = f"({'|'.join(names)})"
    for line in load_novel(novel).splitlines():
        names = list(set(re.findall(re_rule, line)))
        if names and len(names) >= 2:
            names.sort()
            for s, t in itertools.combinations(names, 2):
                count[(s, t)] += 1
count = count.most_common(2000)
node_count, nodes, links = Counter(), [], []
for (n1, n2), v in count:
    node_count[n1] += 1
    node_count[n2] += 1
    links.append({"source": n1, "target": n2})
for node, count in node_count.items():
    nodes.append({"name": node, "symbolSize": int(math.log(count)*5)+5})
c = (
    Graph(init_opts=opts.InitOpts("1280px", "960px"))
    .add("", nodes, links, repulsion=30)
)
c.render("result/characters_analysis.html")

# 帮派分析
count = Counter()
for novel in novel_bangs:
    bangs = novel_bangs[novel]
    re_rule = f"({'|'.join(bangs)})"
    for line in load_novel(novel).splitlines():
        names = list(set(re.findall(re_rule, line)))
        if names and len(names) >= 2:
            names.sort()
            for s, t in itertools.combinations(names, 2):
                count[(s, t)] += 1
count = count.most_common(1000)
node_count, nodes, links = Counter(), [], []
for (n1, n2), v in count:
    node_count[n1] += 1
    node_count[n2] += 1
    links.append({"source": n1, "target": n2})
for node, count in node_count.items():
    nodes.append({"name": node, "symbolSize": int(math.log(count)*5)+5})
c = (
    Graph(init_opts=opts.InitOpts("1280px","960px"))
    .add("", nodes, links, repulsion=50)
)
c.render("result/bang_analysis.html")