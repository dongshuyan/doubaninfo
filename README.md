## DoubanInfo

抓取豆瓣信息并生成简介文本, 目前支持电影类（电影/剧集/动漫/综艺）和书籍类。  
  
Get douabn information to a summary text.

## Useage(使用方法)

```bash
doubaninfo -u douban-url -c douban-cookie(不强制)
```

示例1:  

```bash
doubaninfo -u https://movie.douban.com/subject/26353671/
```

示例2:  

```bash
doubaninfo -u https://movie.douban.com/subject/26353671/ -c 'your cookie'
```

示例3:  

```bash
di -u https://movie.douban.com/subject/26353671/ -c 'your cookie'
```


## Install 安装方法


1.安装Python环境  
  
2.在PowerShell（Windows）/ Terminal.app（MacOS）/ command-line interface（Linux）下输入  
```bash
pip3 install doubaninfo
```
Or    
```bash
pip install doubaninfo
```
## Upgrade 更新方法
```shell
pip3 install --upgrade auto_upload
```
Or  
```shell
pip install --upgrade auto_upload
```

## Reference
[DouBan-Spider](https://github.com/weizhixiaoyi/DouBan-Spider)  
[电影信息查询脚本](https://greasyfork.org/zh-CN/scripts/38878-%E7%94%B5%E5%BD%B1%E4%BF%A1%E6%81%AF%E6%9F%A5%E8%AF%A2%E8%84%9A%E6%9C%AC)  