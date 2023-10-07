# apkDecompiler

fork from https://github.com/luckyandyzhang/easy-android-decompiler 
just test mac os

```
# 首次自己重新编译一次dex2jar
./init_dev_env.sh

python decompile.py apk/test.apk
./dejar.sh apk/classes.jar apk/src
```

### Deps
[http://sourceforge.net/projects/dex2jar/](http://sourceforge.net/projects/dex2jar/)

[http://ibotpeaches.github.io/Apktool/](http://ibotpeaches.github.io/Apktool/)

[http://varaneckas.com/jad/](http://varaneckas.com/jad/)

License
-----------

The MIT License (MIT)

Copyright (c) 2021 haoxiqiang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
