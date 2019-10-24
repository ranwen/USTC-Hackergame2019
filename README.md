# USTC-Hackergame2019-Writeup

## 0x00 占位符

(还没想好写啥)

## 0x01 签到题

F12改HTML 去掉disable

## 0x02 白与夜

众所周知 直接用chrome打开图片是带alpha通道黑色背景的

## 0x03 信息安全 2077

F12开Network 发现请求了一个flag.txt 服务器返回了412

请求头里面有 If-Unmodified-Since 携带了关于时间的字段

将时间改到2077年重发即可

## 0x04 宇宙终极问题

### 0b00 42

搜索引擎题 虽说这个结果是最近才被跑出来的(

### 0b01 Everything

数竞同学:这不是经典的四平方和定理吗

于是可以Google到申必计算器<https://www.alpertron.com.ar/CALTORS.HTM>

发现里面还有另外一个四立方和计算器(不过算不了9n+4和9n+5型)

### 0b10  Last question

显然有个费马xx定理是解决这个问题的

对于 4k+1 型素数 答案一定存在 并且可以找到现成程序

于是暴力试 直至遇到4n+1型质数(根据素数的分布大概需要试200多次?)

具体代码和实现方法看仓库 :[Everything/](https://github.com/ranwen/USTC-Hackergame2019-WP/tree/master/Everything)

## 0x05 网页读取器

观察源码 发现先将@前所有内容删掉 然后在删除/后所有内容 以此过滤http auth用户名绕过的方法

然而@是可以作为$uri等参数出现的 所以构造payload

```
http://web1/flag?@example.com
```

## 0x06 达拉崩吧大冒险

此题似乎只能选择设定好的内容而不能自己输入 猜测买鸡页面可以更改数字

F12改value 可以正常提交

测试后可发现 数据是以signed int64 存储的 构造一个负数payload使attack溢出即可

## 0x07 Happy LUG

显然这是一个考察对域名相关知识的题(

对于特殊符号 有一个编码方式转换 不过并不需要了解具体是啥

直接在浏览器输入	😂.hack.ustclug.org 然后再粘贴出来即可

之后用dig直接获取TXT记录得到flag

## 0x08 正则验证器

看到这题 我就想到[cloudflare的宕机事故](<https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/>)(里面有原理介绍)

复制这个regex 发现过长 考虑构造更短的 最后构造了这个

```
(.*)*x
xaaaaaaaaaaaaaaaaaaaaaaa
```

## 0x09 不同寻常的 Python 考试

说来惭愧 这个题我到最后一天凌晨才拿到了100多人过第一档分(

官方wp讲的挺好的 我作为只过了1 2 3 4 7 10 11 18 19 20的蒟蒻还是去面壁吧(

以及py好像认为 [[nan]]==[[nan]] ?

## 0x0a 小巧玲珑的 ELF

拖到ida 发现题目对flag进行了一个非常容易进行逆运算的编码

将数据dump出来后直接反着做一遍运算即可

## 0x0b Shell 骇客

### 0b00

<http://shell-storm.org/shellcode/>

### 0b01

网上搜到一个叫Alpha2.c的东西 然后找到函数入口eax 把上面的payload编码一下就行了

### 0b10

搜到一个repo <https://github.com/ecx86/shellcode_encoder> 不过我并不懂shellcode 这个半天没跑起来

然而在网上找到了原题 直接把payload复制下来就过了(

## 0x0c 三教奇妙夜

下载视频 发现这个视频巨大长 大小巨大短 于是考虑从mp4存储方式入手

于是找到了

http://download.tsi.telecom-paristech.fr/gpac/mp4box.js/filereader.html

然后发现视频帧里面 大量出现size<100和size>9000的 把这些写个脚本处理掉 发现还剩下几个在1000左右的关键帧

直接用vlc跳转到时间 然后慢放即可得到flag

最后一个部分在最后有点坑 我是用vlc的录制功能后用ffmpeg拆帧的(直接拆太卡)

## 0x0d 小 U 的加密

题目暗示了是音频文件 但是下载后发现大小只有几十K

猜测是midi文件 搜索到文件头后 异或验证了这点

解密后扔到Audacity得到flag

## 0x0e 献给最好的你

dex2jar一下 然后发现文件LoginDataSource.class有一串base64

直接decode发现不知道是什么东西 然后观察一下 发现前面对b64进行了大小写互换

之后得到字符串 hackergame2019withfun! 但是并不是flag

然后发现下面还有一个logout函数 对传的两个数组进行了异或处理

再异或一下得到flag

## 0x0f 驴啃计算器

点开计算器 发现有一个很好的1/x

考虑用连分数构造 那么只需要实现加法就行了

看到指数函数 就想到可以利用指数函数将幂变乘 乘变加

于是可以用 ln((e^x)^2)构造x*2

再利用ln(ln((e^(e^x))^2)) 构造x+ln2

由于第二种方法可能会掉精 所以我们把两个方法结合用

src :[Calc/](https://github.com/ranwen/USTC-Hackergame2019-WP/tree/master/Calc)

## 0x10 天书残篇

下载发现全是空白字符 仔细观察发现全是由tab space enter组成的

猜测是whitespace 找到一个ide <https://vii5ard.github.io/whitespace/>

由于我当时用的是手机 直接复制空白字符比较麻烦 所以用[特技](<https://loj.ac/submission/639981>)将源文件复制进去

用debug功能 找到输出failed信息的label 之后看有哪些跳转到它

发现跳转到它的label都非常规律 大概是

```c
x+=2;
x-=K;
if(!x)	goto faild;
goto next;
```

之后将这段代码复制出来 用简单地字符串处理处理出所有的K序列 做一下处理后输出flag

## 0x11 我想要个家

显然这题是想考Linux常识

前两个利用chroot可以绕过

要求同步两个文件内容 用ln软链接实现

查询时间 在后台写个bash脚本 自动输出时间到文件(可以直接用date的format或者grep处理格式化)

最后要求sleep 将/bin/sleep 复制到:/bin/sleep 即可

直接复制会出现一个fork/exec的错误 查询后发现 只要将/lib所有内容复制进去即可

## 0x12 十次方根

首先pq可以分开 之后使用crt合并

由于p-1不是5的倍数 可以直接处理乘m^2=c的问题 直接用cipolla求二次剩余即可

对于q^3 本人爆推了一个式子得到答案

代码和证明详见:[Root/](https://github.com/ranwen/USTC-Hackergame2019-WP/tree/master/Root)

## 0x13 被泄漏的姜戈

看到题目描述 找到源码 <https://github.com/openlug/django-common>

发现所有配置文件(db和secret_key)都被放到源码里了

查看配置 可以发现用cookie_session存储登录信息

可以搜到利用cookie_session搞事的不少文章 不过似乎并没有什么用(

考虑伪造cookie 不过函数调用过于复杂 手动重现比较麻烦

于是点开login函数 发现有request.session似乎是存session的 改库函数print内容 发现正好对应sqlite里面用户uid 之后再点开另外一个函数 接着print 发现hash是利用sqlite内存的password字段计算的

于是暴力修改代码 使其返回admin的cookies 然后将cookies复制到比赛环境上 得到flag

## 0x14 PowerShell 迷宫

题目有巨大长提示 不过我只用到了第一个(雾)

猜测里面真的放了一个叫PSMaze.dll的文件 于是 find / | grep PSMaze 发现在/opt下

于是用xxd将其dump到本地

开ida逆向 发现一个带flag的字符串 复制后发现failed 猜测要到比赛环境输入token后才能得到真flag

本来想直接逆向dll 奈何看不懂dotnetasm 于是作罢

然后随便走了几步 测试了一下 发现本地dll生成的迷宫和远程生成的迷宫是一样的

于是在本地 暴力走迷宫找到flag 然后在远程cd过去

文件:[Pwsh/](https://github.com/ranwen/USTC-Hackergame2019-WP/tree/master/Pwsh)

## 0x15 韭菜银行

### 0b00

只做出来了第一问

众所周知 这个secret显然是以明文存到storge的

get_flag_1函数是将数字转成hex形式

<https://kovan.etherscan.io/address/0xe575c9abd35fa94f1949f7d559056bb66fddeb51#code> 找到Constructor Arguments 发现后面32位有点不同 猜测是flag 然后就过了(

## 0x16 没有 BUG 的教务系统

### 0b00

也只做出来了第一问

直接下载源码 发现用了一个函数来验证密码 这个函数是逐位判定的 每次判定一位只和当前位和下一位有关 因此可以倒着dfs出密码串

不过由于是用的read 似乎直接输入会把\n输入进去导致无法通过验证?

记得密码是p455w0rd



## 0xff 后记

关于一些没有做出来的题目:

Python:

> 孔乙己喝过半碗酒，涨红的脸色渐渐复了原，旁人便又问道，“孔乙己，你当真会Python么？”孔乙己看着问他的人，显出不屑置辩的神气。他们便接着说道，“你怎的nan!=nan也不知道呢？”孔乙己立刻显出颓唐不安模样，脸上笼上了一层灰色，嘴里说些话；这回可是变量都是引用之类，一些不懂了。在这时候，众人也都哄笑起来：店内外充满了快活的空气。

感受到自己确实不会Python

无限猴子定理:

看到题目的提示 我一直以为这个程序真的能跑出flag(

一直尝试各种单次匹配

直到结束当天凌晨 准备睡觉前 拿手机看了下输出的所有flag文件的长度 发现是65512 想了一下 模数65531是个质数(懒得分解的后果) 然后大概做了个减法 这个长度几乎正好是flag的长度

于是我一度以为是我判断循环终止条件错了 然后就睡觉去了(

起床中午看到sol后 手动mod 19后人就自闭了

韭菜银行 2:

第二问似乎是个原题?不过没有时间修改学习 所以放弃了

大整数分解锦标赛:

前一天晚上看这道题

不过这题我一看代码就大概知道做法了(还是去做猴子题了)

之后网上搜了一个python的random cracker发现要似乎喂上千位 没时间再仔细研究 于是就放弃了(

Flag 红包:

做法和我最开始写的差不多 就是用简单的博弈技巧简单地处理下必胜必败态

如果路径中间出现了简单环什么的 这次行走可能会导致状态的改变 一个简单的解决方案是 枚举一下出边后再check 看看状态会不会改变 然后直接暴力走就行了(这似乎已经比题目的程序要优秀了)

意识到环的问题后已经没有大段时间摸电脑改代码了 所以就没搞成

(不过为什么我感觉原程序和别人写的wp一样 但是还是挂了)

关于re pwn:

不会



作为一个自诩对随机数生成器有一定了解的人没作出俩随机数题还是蛮自闭的(



关于比赛:

好评 适合我这种萌新非CTFer



特别感谢Termux(雾)