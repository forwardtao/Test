import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#执行API调用并存储响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'#存储API调用的URL
r=requests.get(url) #获得URL对象
print("Status code:",r.status_code) #判断请求是否成功（状态码200时表示请求成功）
response_dict=r.json() #API返回json格式的信息（将响应存储到变量中）
print("Total repositories:",response_dict['total_count'])
#探索有关仓库的信息
repo_dicts=response_dict['items']
'''
print("Repositories returned:",len(repo_dicts))  #获得了多少个仓库
#研究第一个仓库
repo_dict=repo_dicts[0]
print('\nKeys:',len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
'''
names,stars=[],[]     #获得项目的名称和星数
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
#可视化
my_style=LS('#333366',base_style=LCS)
chart=pygal.Bar(style=my_style,x_lable_rotation=45,show_legend=False)#创建一条简单的条形图
chart._title='Most-Starred Python Projects on GitHub'
chart.x_labels=names
chart.add('',stars)
chart.render_to_file('python_repos.svg')
