# python-wenku8-api

一个wenku8 (轻小说文库) 的python API!

官网: https://www.wenku8.net/index.php

# 支持

* 获取总排行榜,总推荐榜,月排行榜,月推荐榜,周排行榜,周推荐榜,日排行榜,日推荐榜,最新入库,最近更新,总收藏榜,字数排行,完结全本;

* 获取用户书架;

* 获取用户信息;

* 获取书评吐槽;

* ...(未完待续)

# 介绍

`get_bookcase`: 获取`我的书架` (https://www.wenku8.net/modules/article/bookcase.php)

返回结果如下:

```json
[
    {
        "name": "最喜欢的前辈小巧又可爱，所以想每天让她害羞三次",
        "author": "五十岚雄策",
        "status": "新",
        "aid": "3120"
    },
    {
        "name": "无职转生～到了异世界就拿出真本事～(无职转生~在异世界认真地活下去~)",
        "author": "理不尽な孙の手",
        "status": "[完结]",
        "aid": "1587"
    },
    {
        "name": "文学少女",
        "author": "野村美月",
        "status": "[完结]",
        "aid": "1"
    }
]
```

> 实际为字典`而非`json.

无需传入参数.

---

`get_userdetail`: 获取`用户信息` (https://www.wenku8.net/userdetail.php)

返回结果如下:

```json
[
    {
        "用户ID：": "11"
    },
    {
        "推广链接：": "http://www.wenku8.com/index.php?fromuid=890089"
    },
    //......
    {
        "昵称：": "wzk0(留空则用户名做昵称)"
    },
    {
        "个人简介：": "圣条学院值日生"
    }
]
```

无需传入参数.

---

`get_toplist`: 获取排行榜信息

返回结果如下:

```json
[
    {
        "name": "文学少女",
        "author": "作者:野村美月/分类:Fami通文库",
        "info": "更新:2022-02-27/字数:2223K/已完结/已动画化",
        "tag": "校园 悬疑 青春 恋爱",
        "note": "简介:一所高中的文艺社只有两位成员──擅长写作的男主角社员井上心叶和爱吃书纸的怪物文学…" //简介
    },
    //......
    {
        "name": "魔弹之王与战姬",
        "author": "作者:川口士/分类:MF文库J",
        "info": "更新:2021-04-07/字数:2324K/已完结/已动画化",
        "tag": "校园 奇幻 战争 后宫 青梅竹马",
        "note": "简介:挥舞着龙赐与的超常武器，驰骋在战场上的美丽少女们——战姬。"
    }
]
```

需要传入`list_type`和`page`两个参数.(`page`是页码数)

```
总排行榜-allvisit
总推荐榜-allvote
月排行榜-monthvisit
月推荐榜-monthvote
周排行榜-weekvisit
周推荐榜-weekvote
日排行榜-dayvisit
日推荐榜-dayvote
最新入库-postdate
最近更新-lastupdate
总收藏榜-goodnum
字数排行-size
完结全本-done
```

---

`get_review`: 获取`书评吐槽` (https://www.wenku8.net/modules/article/reviewslist.php)

返回结果如下:

```json
[
    {
        "theme": "[顶]小说资源交流专贴（好书齐分享）",
        "source": "文学少女",
        "num": "40/62052", //回复/查看
        "user": "wenku8",
        "time": "2022-07-19 11:31:50",
        "rid": "249526",
        "uid": "2"
    },
    {
        "theme": "借楼(关于本书作者是女性，女性作家写的关于恋爱的作品，懂得...",
        "source": "我当备胎女友也没关系(我，当备胎女友就可以。)",
        "num": "0/2",
        "user": "shengzehan",
        "time": "2023-05-14 13:44:46",
        "rid": "267567",
        "uid": "529509"
    },
    {
        "theme": "俗话讲的形散神不散",
        "source": "夜行观览车",
        "num": "0/1",
        "user": "#003221",
        "time": "2023-05-14 11:45:55",
        "rid": "267549",
        "uid": "680631"
    }
]
```

需要传入`page`参数.

# 注意

登陆需改`cookies`变量的值为`jieqiUserInfo`.

> 浏览器F12 > 网络 > 第一个加载的东西可看到.