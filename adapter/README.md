# adapter

https://www.techscore.com/tech/DesignPattern/Adapter/Adapter1.html/

TaroをChairparsonにしたいが、インターフェースが合っていない。

すなわち、Chairpersonの持つメソッドをTaroが持っていない。

そのため、Taroを継承したAdapterクラスを作成して問題を解決する。

Javaの場合はインスタンス化するする際に型チェックが発生するため継承なり移譲なりが必須

Pythonの場合はダックタイピング的に特定のメソッドが実装されていれば良い。

```
$ python teacher.py
Traceback (most recent call last):
  File "teacher.py", line 5, in <module>
    chairperson.organizeClass()
AttributeError: 'Taro' object has no attribute 'organizeClass'
``` 
