### 常用的Python模块以及主要作用

**1 json**

json.dump()：把Python对象编码为json对象字符串，并写入文件

    with open('json-dump.json','w') as fp:
    json.dump(data,fp)

json.dumps()：把Python对象编码为json对象字符串（s可以理解为string）
json.load()：将json对象字符串文件解码为Python可以识别的对象

    with open('output.json') as fp:
        loaded_json = json.load(fp)
json.loads()：将json对象字符串解码为Python可以识别的对象
有没有s的区别主要在于源或者目的是字符串还是文件

还可以对比查看：

    base64

    标准库，提供 Base16、Base32、Base64 格式的编码和解码。

    binhex

    标准库，提供 binhex4 格式的编码和解码。

    uu

    标准库，提供 uuencode 格式的编码和解码。

    Protocol Buffers（protobuf）

    这是 Google 开发的一个跨语言的库，用于网络传输的编码和解码。

**2 sys**

sys.argv 在外部向程序传递参数

    sys.argv[number]
    一般情况下，number为0是这个脚本的名字，1，2…则为命令行下传递的参数
sys.platform平台查看

sys.path 查看python路径

**3 pickle模块(和json模块作对比)**

    dumps(object) 返回一个字符串，它包含一个 pickle 格式的对象； loads(string) 返回包含在 pickle 字符串中的对象； dump(object, file) 将对象写到文件，这个文件可以是实际的物理文件，但也可以是任何类似于文件的对象，这个对象具有 write() 方法，可以接受单个的字符串参数； load(file) 返回包含在 pickle 文件中的对象。

**4 shutil**

高级的 文件、文件夹、压缩包 处理模块

文件复制: shutil.copy(source, destination);copy2()工作类似copy()，不过复制到新文件的元数据会包含访问和修改时间。

copyfile()将源的内容复制给目标，如果没有权限写目标文件则产生IoError

shutil包含三个函数处理目录树。要把一个目录从一个位置复制到另一个位置，使用copytree()。这会递归遍历源目录树，将文件复制到目标。

要删除一个目录及其内容，可以使用rmtree()。

将一个文件或目录从一个位置移动到另一个位置，可以使用move()。

**5 random**

random.random()：返回[0.0,1)之间的浮点数

random.uniform(a, b):返回[a,b]之间的浮点数

random.randint(a, b):返回[a,b]之间的整数

random.randrange([start], stop[, step]):从指定范围内，按指定基数递增的

random.choice(sequence)从序列中选择元素

random.shuffle(x[, random])，用于将一个列表中的元素打乱

random.sample(sequence, k)，从指定序列中随机获取指定长度的片断

**6  numpy**
是Python进行科学计算的基础模块/包/库

import numpy as np

http://blog.csdn.net/lockey23/article/details/77888331

**7 difflib**

difflib模块提供的类和方法用来进行序列的差异化比较，它能够比对文件并生成差异结果文本或者html格式的差异化比较页面，如果需要比较目录的不同，可以使用filecmp模块。

http://blog.csdn.net/lockey23/article/details/77913855

**8 re**

match(regular,str)  从字符串第一个开始找,开头找到就返回结果，没有就返回None；后面即使有匹配的结果也不会返回。

search(regular,str) 从开头开始找，找整个string，开头找到就返回，没有就一直找，直到找到返回结果，整个串都没有就返回None

对于以上两个方法match、search返回的结果为一个正则的对象(_sre.SRE_Match object),要获取匹配的字符串结果，必须调用group()方法来获取, 但如果匹配不到时,调用group()会返回 AttributeError 错误

group()  返回被 RE 匹配的字符串

start() 返回匹配开始的位置

end() 返回匹配结束的位置

span() 返回一个元组包含匹配 (开始,结束) 的位置

fullmatch(str,[,start,end] 和match类似,但必须完全匹配才返回值,可以指定字符串的一段位置类匹配

findall(regular,str) 获取全部的匹配字符，返回一个所有匹配字符串的列表

findfilter(regular,str) 与findall类似，只是findfilter返回的是一个迭代器

split(regular,str[,maxsplit])  字符串分割, str.split只能按照某个分隔符分割,  正则的分割可以按照某个规则分割.

compile(regular) 对正则表达式进行编译，生成一个object对象.然后再进行匹配,而传统re方法是每次在匹配的时候编译。通过compile先编译对于需要重复进行多次匹配的时候执行效率要比每次都编译高。

sub(regular,replacestr,str[,count]) sub将根据正则表达式找到的字符串用新串替换，返回结果为字符串，countt是要替换的个数，也就是说可以实现局部替换


**9 os**

http://blog.csdn.net/lockey23/article/details/77879547

**10 time**

time()，它返回纪元开始的秒数，返回值为浮点数，具体精度依赖于平台。

ctime()浮点数一般用于存储和比较日期，但是对人类不友好，要记录和打印时间，可以使用ctime()。

clock()返回处理器时钟时间，它的返回值一般用于性能测试与基准测试。因此它们反映了程序的实际运行时间。

gmtime()用于获取UTC时间，localtime()用于获取当前时区的当前时间，UTC时间实际就是格林尼治时间，它与中国时间的时差为八个小时。locatime() = gmtime() + 8hour

strptime()用于将字符串时间转换成struct_time格式：

    now=time.strptime(time.ctime())

strftime()用于时间的格式化输出

    time.strftime("%a, %d %b %Y %H:%M:%S +0000",time.gmtime())

mktime()用于将struct_time转换成时间的浮点数表示

    time.mktime(time.gmtime())

sleep函数用于将当前线程交出，要求它等待系统将其再次唤醒，如果写程序只有一个线程，这实际上就会阻塞进程，什么也不做。

**11 socket**

In [169]: s=socket.socket()

In [170]: s.connect(("127.0.0.1",80))

In [171]: s.send("GET / HTTP/1.1\n\n")

In [172]: s.recv(200)

In [173]: s.close()

**12 math**

ceil(x) 取顶

floor(x) 取底

fabs(x) 取绝对值

factorial (x) 阶乘

hypot(x,y)  

sqrt(x*x+y*y)

pow(x,y) x的y次方

sqrt(x) 开平方

log(x)

log10(x)

trunc(x)  截断取整数部分

isnan (x)  判断是否NaN(not a number)

degree (x) 弧度转角度

radians(x) 角度转弧度

**13 安全类模块**

hashlib

它支持的哈希算法有：MD5 SHA1 SHA224 SHA256 SHA384 SHA512

sha1 = hashlib.sha1('Hello world').hexdigest()

PyCrypto

这个库包含了常见的对称加密算法（DES、AES、IDEA、等）、公钥加密算法（RSA、DSA、等）、散列算法（MD5、SHA1、RIPEMD、等）。

pyOpenSSL

OpenSSL 在加密领域可是大名鼎鼎。这个库使用 Python 对 OpenSSL 进行很薄的封装。

**14 ctypes**

ctypes 在 Python 2.5 版本加入到标准库中。

通过它，你可以很方便地调用 C/C++ 动态库导出的函数，可以在 Python 中使用各种 C/C++ 的数据类型（比如指针）。

代码示例，调用 Linux/Unix 系统的标准 C 函数，获取当前时间

    from ctypes import *
    libc = CDLL('libc.so.6')
    time = libc.time(None)

调用 Windows 系统 API，弹出消息提示框

    from ctypes import c_int, WINFUNCTYPE, windll
    from ctypes.wintypes import HWND, LPCSTR, UINT
    prototype = WINFUNCTYPE(c_int, HWND, LPCSTR, LPCSTR, UINT)
    paramflags = (1, 'hwnd', 0), (1, 'text', 'Hi'), (1, 'caption',None), (1, 'flags', 0)
    MessageBox = prototype(('MessageBoxA', windll.user32), paramflags)
    MessageBox(text='Hello world',flags=2)

**15 glob**

这个标准库用于查找文件（支持通配符）

代码示例， 获取当前目录所有 txt 文件

    import glob
    files = glob.glob('./*.txt')

**16 fnmatch**

这个标准库用于匹配文件名（支持通配符）

代码示例，列出当前目录所有 txt 文件

    import os, fnmatch
    for file in os.listdir('.') :
        if fnmatch.fnmatch(file, '*.txt') :
            print(file)

**17 tempfile**  

    使用这个标准库，可以安全地生成临时文件或临时目录。

**18 本地进程间通信（IPC）**

subprocess / multiprocessing

用于进程管理的标准库，可以启动子进程，通过标准输入输出跟子进程交互。

其中 multiprocessing 是 2.6 版本加入到标准库的。

signal

    用于进程信号处理的标准库。

mmap

    提供了内存映射文件的支持。

代码示例，利用 mmap 在父子进程间交换数据

    import os
    import mmap

    map = mmap.mmap(-1, 13)
    map.write("Hello world")

    pid = os.fork()

    if pid == 0: # 子进程
        map.seek(0)
        print map.readline()
        map.close()

**19 EasyInstall / Setuptools/ pip**

这套工具可以帮助你进行第三方库的管理（下载、编译、安装、升级、卸载）

**20 httplib / httplib2 / http.request / urllib.parse**

这几个库可以进行各种 HTTP 客户端请求（GET、POST、等）。

Python2 的模块名叫 httplib / httplib2，到 Python3 模块名改为 http.request / urllib.parse

代码示例,读取指定 URL 的网页内容

    import urllib
    handle = urllib.urlopen('http://www.google.com')
    page = handle.read()
    handle.close()

**21. SimpleHTTPServer / http.server**

提供轻量级 HTTP Server 的标准库。

Python2 的模块名叫 SimpleHTTPServer，到 Python3 模块名改为 http.server

代码示例,一个极简单的 HTTP 服务

    import SocketServer
    import SimpleHTTPServer

    PORT = 8000
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(('', PORT), Handler)
    print 'serving at port', PORT
    httpd.serve_forever()

**22. webbrowser**

操纵当前系统的默认浏览器，访问指定 URL 的页面。

代码示例,用默认浏览器打开 Google 主页

import webbrowser
webbrowser.open('http://www.google.com')

**23 针对数据库的**

MySQLdb：操作 MySQL 的第三方库。

psycopg：操作 PostgreSQL 的第三方库。

cx_Oracle：操作 Oracle 的第三方库。

pymssql：操作微软 SQL Server 的第三方库。

ibm-db：操作 DB2 的第三方库。

sqlite3

PyBSDDB：操作 Berkeley DB 的第三方库。


**24 处理压缩文件 / 打包文件**

zipfile：处理 zip 格式的标准库。

bz2：处理 bzip2 格式的标准库。

gzip：处理 gzip 格式的标准库。

zlib：处理 gzip 格式的标准库。

tarfile：处理 tar 格式的标准库。

PyLZMA：处理 7zip 格式的第三方库。

rarfile：处理 rar 格式的第三方库。

msilib：处理 msi 格式的标准库，从 Python 2.5 版本开始提供。

更多模块可以参阅： https://www.cnblogs.com/frchen/p/5709523.html
