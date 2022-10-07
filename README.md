## DoubanInfo

抓取豆瓣信息并生成简介文本, 目前支持电影类（电影/剧集/动漫/综艺）和书籍类。

Get douabn information to a summary text.

## Functions（功能介绍）

- 输出简介文本
- 输出Json格式信息
- 自动将输出信息复制到前剪切板
- 支持适用cookie抓取部分只有登录豆瓣才能看到的资源信息
- 支持Python调用

## Usage Scenario（适用场景）

- 抓取到只有登录豆瓣才能看到的资源信息
- 在Python等脚本中获取豆瓣简介/Json格式豆瓣信息
- 在命令行/Shell中获取豆瓣简介/Json格式豆瓣信息

## 更新日志  
- 20221007 去掉无法识别的字符  
- 20221007 修复豆瓣链接中id后必须有/的bug  


## Useage(使用方法)

### 1.命令行直接使用

#### 参数说明

-h, --help            show this help message and exit
-u URL, --url URL     Input your douban-url（豆瓣链接）
-c COOKIE, --cookie COOKIE
    Input your douban-cookie（豆瓣cookie，用于抓取部分只有登录才能看到的资源）
-j, --json            Output as json format（输出json格式的结果）
-cp, --copy        Copy the output to the clipboard(将结果添加到剪切板)

#### 示例

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

### 2.Python接口使用

```python
from doubaninfo.doubaninfo import getdoubaninfo
res_douban=getdoubaninfo(url=url,cookie=cookie,ret_val=True)
douban_dict=res_douban.parse() # get the douban information dict
douban_text=res_douban.info() # get the douban information str
```

## Install 安装方法

1.安装Python环境

2.在PowerShell（Windows）/ Terminal.app（MacOS）/ command-line interface（Linux）下输入

```shell
pip3 install doubaninfo
```

Or

```shell
pip install doubaninfo
```

## Upgrade 更新方法

```shell
pip3 install --upgrade doubaninfo
```

Or

```shell
pip install --upgrade doubaninfo
```

## Reference

[1] [DouBan-Spider](https://github.com/weizhixiaoyi/DouBan-Spider)

[2] [电影信息查询脚本](https://greasyfork.org/zh-CN/scripts/38878-%E7%94%B5%E5%BD%B1%E4%BF%A1%E6%81%AF%E6%9F%A5%E8%AF%A2%E8%84%9A%E6%9C%AC)
