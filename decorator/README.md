
# Decorator Pattern
https://www.techscore.com/tech/DesignPattern/Decorator.html/

# Builderとの違い
 - あるオブジェクトにオプションを選択して実装できるものならbuilderでもできる？
 - サブクラス化は、is-a関係をモデル化するために使用されます。デコレータは、機能を拡張するためのサブクラス化に対する柔軟な代替手段を提供します
 - 「カシューナッツアイスクリーム」クラスを作るのがDecorator、「カシューナッツ」フィールドに値をつけるアプローチがBuilder
 - Decoratorはすでにあるオブジェクトを修正することなく拡張するパターン
 - Decoratorは機能拡張に利用する。今回の例だとgetNameメソッドを継承している。
 - Builderは継承関係はない。ただのトッピングならBuilderを使うべきだが、トッピングによる振る舞いの変化によってはDecoratorパターンを使う選択肢もある。
 - 順序制約？
