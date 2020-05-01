1.ブログを　登録、修正、削除する画面を追加した
2.同上の機能をログイン者のみに限定した
　→いきなりURLを入力してもログイン画面にいくようにした。
3.最初の表示画面（base.html)に表示されているカテゴリリストが
登録順なのでカテゴリの名前順に表示したい。
 views.pyの中のCategoryViewsの　get_queryset(self):
 のqueryset = Post.objects.order_by('created_at').filter(category=category)
をCategory.objects.order_by('name').filter(category=category)
と変更したが、変わらず（前のまま、Categoryの登録順）
→　Postモデルとカテゴリの関係をどう、したらいいのかわからず
 挫折

４．ブログを削除したときに、戻る画面を最初の全部一覧
ではなくて、カテゴリ一覧→詳細画面→削除→元のカテゴリ一覧
としたいが、これもどうしたらいいかわからず。
当然のことながら
DeleteViewの success_url = reverse_lazy('category:index')
としたらerrorになった。ここでいっているindexはcategorのIDじゃなくて
POSTのIDだからだと思うし、カテゴリ一覧から詳細画面に移るとは
限らない。初期表示の全部一覧から詳細にいって削除したときには
全部一覧に戻るべき・・・これは難しい。挫折。
5.写真をアップロードしたい。（views.pyに書くのがCLASSじゃなくて関数にしたほうがいいのかも？悩む）
ということで、
まだまだ直したいところはいろいろあるけれど、やはり、１つ１つの
意味がきちんと理解できていないのです。







IMAGE_ROOT = OS.path.join(BASE_DIR,'images')
IMAGE_URL = '/images/'