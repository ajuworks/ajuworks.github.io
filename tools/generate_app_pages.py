# -*- coding: utf-8 -*-
"""Aju Works 公式サイト: ホーム / アプリ一覧 / アプリ別詳細ページの生成。

掲載内容は各アプリの AndroidManifest / build.gradle / app.json / strings.xml /
README / リリース資料で確認できた事実のみ。確認できないものは掲載しない。
"""
import os

SITE = "https://ajuworks.github.io"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIL = "ajuworks.official@gmail.com"

# ---------------------------------------------------------------------------
# アプリ台帳（棚卸し結果）
# ---------------------------------------------------------------------------
APPS = [
  dict(
    slug="gym-record",
    name="筋トレ記録＆ベンチコーチ",
    short="筋トレ記録＆ベンチコーチ",
    app_id="com.atushi.benchcoach",
    tagline="重量・回数・セット数を記録して、ベンチプレス100kgへ。",
    category="健康・フィットネス",
    status="live",
    play="https://play.google.com/store/apps/details?id=com.atushi.benchcoach",
    icon="gym-record.png",
    card="重量・回数・セット数の記録と次回メニュー提案で、筋トレの継続を支えるアプリ。Wear OS対応。",
    overview=[
      "筋トレの記録・管理とメニュー提案を1つにまとめたアプリです。重量・回数・セット数をシンプルに記録し、推定1RMや目標までの進捗を自動で計算します。",
      "ベンチプレス100kgを目標に取り組む方を中心に、まず記録から始めたい初心者の方やマシン中心でトレーニングしている方にも使いやすい設計です。記録データは端末内に保存されるため、インターネット接続がなくても記録を続けられます。",
      "Wear OS版を同梱しており、スマートウォッチ側でセット記録・休憩タイマー・進捗確認・ランニング計測を行えます。",
    ],
    features=[
      "トレーニング記録（重量・回数・セット数）",
      "推定1RMの自動計算と目標達成率の表示",
      "次回メニューの自動提案",
      "身体データ・食事データの記録",
      "Wear OS版（セット記録・休憩タイマー・タイル・ランニング計測）",
      "記録は端末内に保存。オフラインで利用可能",
    ],
    facts=[
      ("データ保存場所", "トレーニング記録・身体データ・食事データは端末内のデータベースに保存します。"),
      ("広告", "Google AdMob による広告を表示します（広告識別子を使用）。"),
      ("アプリ内課金", "Google Play インアプリ課金に対応しています。"),
      ("Health Connect", "ユーザーが許可した場合に限り、アプリ内で記録した筋力トレーニングの運動セッションを Health Connect へ書き込みます。現在の版では Health Connect からの読み取りは行いません。"),
      ("主要な権限", "インターネット / バイブレーション / 課金 / 広告ID / Health Connect への運動記録の書き込み"),
    ],
    privacy=("https://gym-record-bench-coach-policy.vercel.app/privacy", "専用プライバシーポリシーを見る", True),
    badges=[("badge-android", "Android"), ("badge-free", "基本無料"), ("badge-free", "Wear OS対応")],
    note="提案メニューは、ベンチプレス100kgを目指す方向けの内容を中心にしつつ、マシン中心でトレーニングする方にも使いやすい構成を想定しています。",
  ),
  dict(
    slug="fanvolt",
    name="FANVOLT｜推し活記録・支出管理",
    short="FANVOLT",

    app_id="com.ajuworks.fanvolt",
    tagline="推し活の記録・予定・支出を、貼るだけで残す。",
    category="ライフスタイル",
    status="live",
    play="https://play.google.com/store/apps/details?id=com.ajuworks.fanvolt",
    icon="fanvolt.svg",
    card="推し活の記録・予定・支出・メモを一元管理。画像を貼るだけで日付や金額を読み取ります。",
    overview=[
      "推し活の記録・予定・支出・メモを一元管理できるアプリです。スクリーンショットや画像を投げ込むだけで、端末内の文字認識機能が日付・金額・カテゴリを読み取り、入力の手間を減らします。",
      "カレンダー・推し活年表・熱量メーターで、これまでの活動をふり返れます。記録した内容は端末内に保存され、Aju Works のサーバーへ送信することはありません。",
    ],
    features=[
      "推しの登録・推し画像登録、スクショ投げ込みBOX",
      "貼り付けた画像・テキストからの日付・金額・カテゴリ自動抽出（端末内OCR）",
      "カレンダー表示・推し活年表・推し熱量メーター",
      "共有カード作成（共有範囲設定・履歴付き）",
      "記録に応じた称号・バッジ判定",
      "予定・記念日・支払期限のリマインド通知",
    ],
    facts=[
      ("データ保存場所", "推し情報・記録・予定・支出・メモ・画像は端末内に保存します。"),
      ("文字認識（OCR）", "端末上の文字認識機能のみを使用します。読み取り対象の画像や認識結果を外部へ送信しません。"),
      ("広告", "Google AdMob による広告を表示します（広告識別子を使用）。EU/UK等では UMP による同意取得画面を表示します。"),
      ("アプリ内課金", "Google Play インアプリ課金による買い切りの追加機能があります。"),
      ("主要な権限", "インターネット / ネットワーク状態 / 通知 / 広告ID"),
    ],
    privacy=("../privacy.html#fanvolt", "プライバシーポリシーを見る", False),
    badges=[("badge-android", "Android"), ("badge-free", "基本無料")],
    note=None,
  ),
  dict(
    slug="subscription-manager",
    name="サブスク整理｜解約ナビ",
    short="サブスク整理",
    app_id="com.atush.cancelnav",
    tagline="契約経路から、解約ページへ最短で。",
    category="家計・ツール",
    status="prep",
    play=None,
    icon="subscription-manager.png",
    card="サブスクの金額と更新日を管理し、契約経路に応じた公式の解約手続きへ案内します。",
    overview=[
      "契約中のサブスクリプションを一覧で管理し、解約手続きへの最短経路を案内するアプリです。契約経路（Apple・Google Play・Web・電話・メールなど）に応じて、公式の解約ページや管理画面へ直接誘導します。",
      "自動ログインや代理解約は行いません。ID・パスワードを保存・取得することもなく、最終的な解約操作はご自身で各サービス上で行っていただく設計です。",
    ],
    features=[
      "人気サービスの1タップ登録プリセット",
      "金額・更新日・契約経路・ステータスの管理",
      "ホーム画面での月額・年額合計表示",
      "契約経路別「最短解約」導線（公式ページ誘導・電話・メール文面自動生成）",
      "更新日前のリマインド通知",
      "解約記録（解約日・申請状況）の保存",
    ],
    facts=[
      ("データ保存場所", "サービス名・金額・支払い周期・更新日・メモ・解約記録は端末内にのみ保存します。"),
      ("認証情報", "各サービスの ID・パスワードを保存・取得しません。自動ログイン・代理解約も行いません。"),
      ("広告", "無料版では Google AdMob によるバナー広告を表示します。有料版へのアップグレードで広告は非表示になります。"),
      ("アプリ内課金", "有料版（買い切り）の購入に Google Play インアプリ課金を利用します。決済情報は Google が処理します。"),
      ("通知", "更新日前のリマインドを端末内のローカル通知で行います。"),
    ],
    privacy=("../privacy.html#cancel-nav", "プライバシーポリシーを見る", False),
    badges=[("badge-android", "Android"), ("badge-coming-soon", "公開準備中")],
    note=None,
  ),
  dict(
    slug="focus-gate",
    name="Focus Gate｜スマホ使いすぎ防止",
    short="Focus Gate",
    app_id="com.ajuworks.focusgate",
    tagline="開く前に、理由と少しの待ち時間を。",
    category="生産性・自己管理",
    status="prep",
    play=None,
    icon="focus-gate.png",
    card="選んだアプリを開くとき、理由の入力と待機を求めて無意識な利用に気づきを促します。",
    overview=[
      "あらかじめ選んだアプリ（SNS・動画・ブラウザ・ゲームなど）を開こうとした際に、使用理由の入力と一定時間の待機を求めることで、無意識な利用に気づきを促す自己管理アプリです。",
      "使用後には簡単なふり返りを行い、自分の利用習慣を見つめ直すきっかけを作ります。記録は端末内に保存され、外部のAI APIやクラウド同期へ送信することはありません。ログインも不要です。",
    ],
    features=[
      "制限対象アプリの検知と全画面ゲート表示",
      "理由入力＋段階的な待機時間による利用抑制",
      "1時間あたりの解除回数上限、緊急解除（1日1回）",
      "使用後のふり返りレビュー（必要だったか等）",
      "集中時間の記録",
      "データは端末内保存のみ、ログイン不要",
    ],
    facts=[
      ("データ保存場所", "対象アプリ一覧・使用理由・ゲート発動記録・ふり返り回答・集中時間は端末内にのみ保存します。"),
      ("使用状況へのアクセス", "前面のアプリを判定するため UsageStatsManager を利用します。ユーザー補助機能（Accessibility Service）は使用しません。"),
      ("他のアプリの上への表示", "ゲート画面を重ねて表示するために使用します。この権限で取得する情報はありません。"),
      ("広告", "Google AdMob によるバナー広告をホーム画面にのみ表示します。ゲート画面とふり返り画面には広告を表示しません。"),
      ("主要な権限", "使用状況へのアクセス / 他のアプリの上に重ねて表示 / フォアグラウンドサービス / 通知 / インターネット"),
    ],
    privacy=("../privacy.html#focus-gate", "プライバシーポリシーを見る", False),
    badges=[("badge-android", "Android"), ("badge-coming-soon", "公開準備中")],
    note=None,
  ),
  dict(
    slug="step-bp-diary",
    name="歩数・血圧手帳",
    short="歩数・血圧手帳",
    app_id="com.ajuworks.stepbpdiary",
    tagline="歩数・血圧・体重・食事を、広告なしで記録する。",
    category="健康・フィットネス",
    status="prep",
    play=None,
    icon="step-bp-diary.png",
    card="歩数・血圧・体重・食事を一元管理する非医療用の健康記録手帳。広告・外部送信なし。",
    overview=[
      "歩数・血圧・体重・食事を一元管理できる、非医療用の健康記録手帳アプリです。Health Connect 連携による歩数の取得と、血圧・食事・体重の手動記録を組み合わせ、週間・月間のグラフ分析やカロリー収支の可視化、PDFレポート出力までを1つのアプリで行えます。",
      "このアプリはインターネット通信を行わない構成で、広告配信SDKやアクセス解析も使用していません。記録はすべて端末内に保存されます。",
    ],
    features=[
      "歩数記録（Health Connect 連携・任意）",
      "血圧・脈拍・体重の手動記録",
      "食事記録（食品117種＋検索）とカロリー収支の可視化",
      "週間・月間の分析グラフ、30日間の達成カレンダー",
      "週間・月間レポートのPDF出力、リマインダー通知",
      "全データのローカルJSONバックアップ",
    ],
    shots=[
      ("01_home.jpg", "歩数・血圧手帳のホーム画面"),
      ("02_steps.jpg", "歩数の記録画面"),
      ("03_blood_pressure.jpg", "血圧の記録画面"),
      ("05_analytics.jpg", "分析グラフ画面"),
      ("04_settings.jpg", "設定画面"),
    ],
    facts=[
      ("データ保存場所", "歩数・血圧・体重・食事記録・プロフィール・設定値は端末内のデータベースにのみ保存します。"),
      ("外部送信", "インターネット権限を持たない構成のため、記録が外部へ送信されることはありません。"),
      ("広告・解析", "広告配信SDK・アクセス解析・トラッキングは一切使用していません。"),
      ("Health Connect", "ユーザーが連携をONにした場合に限り、歩数（Steps）のみを読み取ります。書き込みは行いません。"),
      ("主要な権限", "身体活動（歩数計測）/ 通知 / Health Connect の歩数読み取り"),
    ],
    privacy=("../privacy.html#step-bp-diary", "プライバシーポリシーを見る", False),
    badges=[("badge-android", "Android"), ("badge-coming-soon", "公開準備中")],
    note="本アプリは医療機器ではありません。血圧を測定する機能はなく、数値は手動入力のみです。表示される数値は入力値から算出した概算の参考値であり、診断・治療を目的としたものではありません。健康上の問題や治療方針については、必ず医師・専門家にご相談ください。",
  ),
  dict(
    slug="yomioku",
    name="ヨミオク｜読書を記憶に残す",
    short="ヨミオク",
    app_id="com.ajuworks.readrecall",
    tagline="読んだものを、自分の中に残す。",
    category="教育・読書",
    status="prep",
    play=None,
    icon="yomioku.svg",
    card="本から得たことを軽く残し、後日思い出し、別の本とつなぐ。要点づくりは端末内AIで行います。",
    overview=[
      "本から得たことを軽く残し、後日思い出し、別の本とつなぎ、他の読者の異なる視点を自分の理解へ取り込む——という流れを1つのアプリにしたものです。開発時の名称は ReadRecall（読書記憶）です。",
      "メモの要点づくり・本同士のつながり判定・視点の統合は、すべて端末内のAIで行います。メモの内容が外部のAIサービスへ送られることはありません。端末が端末内AIに対応していない場合は、AIを使わず、書いた言葉をそのまま要点として扱います。",
      "文章の取り込みは、撮影したあとで残したい範囲を囲む方式です。撮るときにページを枠へきっちり合わせる必要はありません。図・表・グラフは文字に直さず、画像のまま残せます。",
      "現在は公開準備中です。Google Play への提出前の確認作業を進めています。",
    ],
    features=[
      "本の登録（ISBNバーコード読み取り・書誌情報の検索）",
      "文章の取り込み（撮影 → 残したい範囲を囲む → 端末内で文字に → その場で修正）",
      "縦書き・横書きの読み順の切り替え",
      "図・表・グラフを画像のまま残す",
      "話した内容を端末内で文字にする音声入力（対応端末のみ）",
      "キーボード入力と、コピーした文章の貼り付け",
      "端末内AIによる要点づくり（非対応端末では入力文をそのまま要点として扱う）",
      "復習（1／3／7／14／30／60／120日の間隔で出題）",
      "本同士のつながりの提示",
      "「みんなの視点」の閲覧と、選んだ視点を自分の理解へ取り込む機能",
      "本・メモ・要点・つながり・復習のJSON書き出し",
    ],
    facts=[
      ("会員登録", "会員登録はありません。メールアドレス・パスワード・電話番号による登録や、外部アカウントでのログインは行いません。"),
      ("データ保存場所", "本の情報・メモ・読み取った文字・要点・つながり・復習カード・取り込んだ視点は端末内のデータベースに保存します。図表として残すことを選んだ画像は、アプリ専用の領域に保存し、外部へ送信しません。文章の読み取りに使った撮影画像は保存しません。"),
      ("音声入力", "端末内の音声認識だけを使います。音声も認識結果も外部へ送信せず、録音データも保存しません。端末内認識に対応していない端末では機能を表示しません。"),
      ("端末内AI", "要点の作成・視点の集約・統合は端末内のAIで行います。メモの内容を外部のAIサービスへ送信しません。"),
      ("「みんなの視点」", "この機能を使うときだけ Firebase（Cloud Firestore / Authentication / App Check）へ接続し、本を特定する識別子を送信して投稿を取得します。現在の版は閲覧のみで、投稿機能は無効です。"),
      ("識別子", "閲覧には Firebase の匿名認証による識別子（UID）を使います。アカウントではなく、氏名やメールアドレスとは結び付いていません。"),
      ("外部サービス", "Firebase（Authentication / Cloud Firestore / App Check）、Google Books API・openBD（書誌情報の検索。検索語のみを送信）"),
      ("広告", "広告配信SDKは使用していません。"),
      ("データの削除", "アプリ内の「設定 → データとプライバシー」から、端末内に保存されたデータをまとめて削除できます。アンインストールでも端末内のデータは削除されます。"),
      ("主要な権限", "カメラ（バーコード読み取り・紙面の文字読み取り・図表の撮影）/ マイク（音声入力を選んだときのみ）/ インターネット / ネットワーク状態"),
    ],
    privacy=("../privacy.html#yomioku", "プライバシーポリシーを見る", False),
    extra_links=[("../privacy.html#yomioku-data-deletion", "データ削除について", False)],
    badges=[("badge-android", "Android"), ("badge-coming-soon", "公開準備中")],
    note="カメラを許可しなくても、本の登録とメモの作成はできます。",
  ),
  dict(
    slug="kokoshare",
    name="ここシェア",
    short="ここシェア",
    app_id="com.ajuworks.kokoshare",
    tagline="いざというときの連絡先と備えを、手元にまとめる。",
    category="安全・防災",
    status="prep",
    play=None,
    icon="kokoshare.png",
    card="家族の連絡先・防災メモ・備蓄・安否の共有文を端末内にまとめる防災アプリ。",
    overview=[
      "災害時に必要な家族の連絡先、防災メモ、備蓄、安否の共有文をひとまとめにしておくためのアプリです。必要なときに、LINE やメールなどの共有機能で自分から安否を送れます。",
      "初回公開版はクラウド機能を停止した構成です。ログイン・アカウント登録・アプリ内の安否同期・プッシュ通知は行わず、登録した情報はすべて端末内に保存されます。位置情報は、ご自身がONにしたときだけ前景で取得します。",
      "現在は公開準備中です。",
    ],
    features=[
      "家族・連絡先の登録",
      "防災メモと備蓄の管理",
      "安否記録と共有文テンプレートの作成",
      "位置情報をONにしたときの地図プレビュー（OpenStreetMap）",
      "「Googleマップで開く」を選んだときの地図連携",
      "LINE・メール等への共有（本人の操作時のみ）",
    ],
    facts=[
      ("データ保存場所", "家族・連絡先・防災メモ・備蓄・安否記録・共有文テンプレートは端末内に保存します。"),
      ("クラウド機能", "初回公開版では Firebase Authentication / Cloud Firestore / Cloud Messaging を停止しています。ログイン・招待・アプリ内の安否同期・プッシュ通知・クラウドバックアップは行いません。"),
      ("位置情報", "ユーザーがONにしたときだけ前景で取得し、地図プレビューに使用します。"),
      ("広告", "広告配信SDKは使用していません。"),
      ("主要な権限", "位置情報（おおよそ／正確）/ インターネット"),
    ],
    privacy=("../privacy.html#kokoshare", "プライバシーポリシーを見る", False),
    badges=[("badge-android", "Android"), ("badge-coming-soon", "公開準備中")],
    note=None,
  ),
  dict(
    slug="night-fade",
    name="Night Fade",
    short="Night Fade",
    app_id="com.ajuworks.nightfade",
    tagline="就寝時刻に向けて、画面をゆっくり暗く・暖色へ。",
    category="生産性・自己管理",
    status="prep",
    play=None,
    icon="night-fade.svg",
    card="夜の時間経過に合わせて画面を暗く暖色寄りに変え、朝は徐々に戻す完全オフラインのアプリ。",
    overview=[
      "夜の時間経過に合わせて画面を暗く・暖色寄りに変化させるアプリです。半透明のオーバーレイ方式で、就寝時刻に向けて滑らかに変化し、朝は徐々に通常表示へ戻します。",
      "完全オフラインで動作します。インターネット権限を持たず、広告もユーザー補助サービスも使用していません。設定は端末内にのみ保存されます。",
      "現在は公開準備中です。",
    ],
    features=[
      "就寝時刻に向けた明るさ・色温度の段階的な変化",
      "朝に向けた通常表示への復帰",
      "半透明オーバーレイ方式（表示中も操作可能）",
      "常駐通知からの状態確認",
      "端末の再起動後にスケジュールを再評価",
      "アプリ別設定（有効にした場合のみ、前面アプリを判定）",
    ],
    facts=[
      ("データ保存場所", "設定は端末内の DataStore にのみ保存します。"),
      ("外部送信", "インターネット権限を持たないため、外部への送信は行いません。"),
      ("広告", "広告配信SDKは使用していません。"),
      ("使用状況へのアクセス", "「アプリ別設定」を有効にした場合のみ、前面アプリの判定に使用します。ユーザーが設定画面で明示的に許可するまで機能せず、自動では要求しません。"),
      ("主要な権限", "他のアプリの上に重ねて表示 / フォアグラウンドサービス / 通知 / 再起動後の起動 / 使用状況へのアクセス（任意）"),
    ],
    privacy=("../privacy.html#night-fade", "プライバシーポリシーを見る", False),
    badges=[("badge-android", "Android"), ("badge-coming-soon", "公開準備中")],
    note=None,
  ),
  dict(
    slug="watchit",
    name="WatchIt",
    short="WatchIt",
    app_id="com.ajuworks.watchit",
    tagline="変わったら教えて。ページの更新を端末自身が見張る。",
    category="ツール",
    status="prep",
    play=None,
    icon="watchit.svg",
    card="登録したWebページを端末自身が定期確認し、意味のある変化だけをローカル通知します。",
    overview=[
      "登録した Web ページを Android 端末自身が定期的に確認し、意味のある変化があったときにローカル通知でお知らせするアプリです。アカウント登録は不要です。",
      "運営側のサーバーやクラウドDBを持たない構成です。URL・監視条件・取得内容・変更履歴は端末内のデータベースだけに保存され、確認のための通信は端末から対象サイトへ直接行われます。",
      "現在は公開準備中です。",
    ],
    features=[
      "監視するWebページの登録（最大50件）",
      "約1／3／6／12／24時間の確認間隔",
      "取得したHTMLをテキスト化して比較し、意味のある変化を判定",
      "変化を検知したときのローカル通知",
      "変更履歴の保存と確認",
      "通信可能なときだけ確認を実行（端末の省電力設定に従う）",
    ],
    facts=[
      ("データ保存場所", "URL・監視条件・取得内容・変更履歴は端末内の SQLite にのみ保存します。"),
      ("サーバー", "運営側のサーバー・Firebase・FCM・クラウドDB・外部APIを使用していません。"),
      ("通信", "登録した URL へ端末から直接接続します。http/https と 80/443 のみを許可し、localhost や内部ネットワーク宛のアドレスは拒否します。取得したHTMLはテキスト化して保存・表示し、WebView で実行しません。"),
      ("広告", "広告配信SDKは使用していません。"),
      ("主要な権限", "インターネット / 通知"),
    ],
    privacy=("../privacy.html#watchit", "プライバシーポリシーを見る", False),
    badges=[("badge-android", "Android"), ("badge-coming-soon", "公開準備中")],
    note="確認間隔は最短の実行間隔です。端末の省電力機能や通信状態により遅れることがあり、定刻での実行は保証されません。",
  ),
  dict(
    slug="linkpocket",
    name="リンクポケット",
    short="リンクポケット",
    app_id="com.ajuworks.linkpocket",
    tagline="Chromeに残さないリンク管理。",
    category="ツール",
    status="prep",
    play=None,
    icon="linkpocket.svg",
    card="共有メニューからURLを端末内に保存。Chromeのブックマークを使わずにリンクを整理します。",
    overview=[
      "Chrome の共有メニューから URL をアプリ内のデータベースへ保存し、ブックマークとは別の場所でリンクを管理するアプリです。ブックマークに残さないことで、ブックマーク由来の予測候補が表示されにくくなります。",
      "保存したリンクは端末内にのみ置かれ、外部への送信は行いません。任意で生体認証によるロックをかけられます。",
      "現在は公開準備中です。",
    ],
    features=[
      "Chrome等の共有メニューからのURL保存",
      "保存したリンクの一覧・整理",
      "Custom Tabs によるリンクの表示",
      "生体認証によるアプリロック（任意）",
      "データは端末内のみ。外部送信なし",
    ],
    facts=[
      ("データ保存場所", "保存した URL とその情報は端末内の SQLite にのみ保存します。"),
      ("外部送信", "保存したリンクを外部へ送信しません。"),
      ("広告", "広告配信SDKは使用していません。"),
      ("主要な権限", "インターネット（リンクの表示）/ 生体認証（任意のアプリロック）"),
    ],
    privacy=("../privacy.html#linkpocket", "プライバシーポリシーを見る", False),
    badges=[("badge-android", "Android"), ("badge-coming-soon", "公開準備中")],
    note="Chrome や Google の予測候補そのものを制御する機能ではありません。",
  ),
  dict(
    slug="midnight-hotel",
    name="深夜ホテル",
    short="深夜ホテル",
    app_id="com.ajuworks.midnighthotel",
    tagline="昼はホテル経営。夜は、何かがおかしい。",
    category="ゲーム",
    status="prep",
    play=None,
    icon="midnight-hotel.svg",
    card="昼の経営判断が夜の出来事に返ってくる、客室8室のホテル経営ゲーム。完全オフライン。",
    overview=[
      "小さなビジネスホテル（客室8室）のオーナーとして、昼に価格・人員・投資を決め、夜はフロントに立って起きたことに対応するゲームです。夜の判断は翌朝の数字に返ってきます。",
      "価格を上げれば予約は減るが利益は増えることがあり、防音工事をすれば騒音の苦情が減り、防犯カメラを上げれば夜に得られる手がかりが増えます。自分で夜勤に入れば人件費はゼロですが、疲労で夜の持ち時間が減ります。",
      "権限の要求はなく、完全にオフラインで動作します。現在は公開準備中です。",
    ],
    features=[
      "昼の経営判断（価格・人員・投資）",
      "夜のフロント対応と監視カメラの確認",
      "経営判断が夜の事件に影響し、夜の判断が翌朝の数字に返る構造",
      "資金・評判・人員・疲労の管理",
      "権限要求なし・完全オフライン",
    ],
    facts=[
      ("データ保存場所", "ゲームの進行状況は端末内にのみ保存します。"),
      ("外部送信", "ネットワーク通信を行いません。"),
      ("広告", "広告配信SDKは使用していません。"),
      ("権限", "要求する権限はありません。"),
    ],
    privacy=("../privacy.html#midnight-hotel", "プライバシーポリシーを見る", False),
    badges=[("badge-android", "Android"), ("badge-coming-soon", "公開準備中")],
    note=None,
  ),
]

# ホームに出す代表6本
HOME_SLUGS = ["fanvolt", "gym-record", "focus-gate", "step-bp-diary", "yomioku", "watchit"]

BY_SLUG = {a["slug"]: a for a in APPS}

STATUS_LABEL = {"live": ("status-live", "公開中"), "testing": ("status-testing", "テスト中"), "prep": ("status-prep", "公開準備中")}

ARROW = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<path d="M5 12h14M12 5l7 7-7 7"/></svg>')


def icon_markup(app, prefix, cls):
    """アプリアイコン。実プロジェクトのアイコン資産から生成したファイルを使う。"""
    return ('<span class="%s"><img src="%sassets/img/apps/%s" width="192" height="192" '
            'alt="%s のアプリアイコン" loading="lazy" decoding="async"></span>'
            % (cls, prefix, app["icon"], app["name"]))


def head(prefix, title, desc, canonical, og_title=None):
    return """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>%(title)s</title>
  <meta name="description" content="%(desc)s">
  <link rel="canonical" href="%(canonical)s">

  <!-- OGP -->
  <meta property="og:type"        content="website">
  <meta property="og:title"       content="%(og)s">
  <meta property="og:description" content="%(desc)s">
  <meta property="og:url"         content="%(canonical)s">
  <meta property="og:site_name"   content="Aju Works">
  <meta property="og:locale"      content="ja_JP">
  <meta name="twitter:card"       content="summary">
  <meta name="twitter:title"      content="%(og)s">
  <meta name="twitter:description" content="%(desc)s">

  <!-- ファビコン（インラインSVG: 紺背景に白の「A」） -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='6' fill='%%231e3a5f'/><text x='50%%25' y='50%%25' dominant-baseline='central' text-anchor='middle' font-family='sans-serif' font-size='20' font-weight='900' fill='white'>A</text></svg>">

  <link rel="stylesheet" href="%(prefix)sassets/css/style.css">
</head>
<body>
""" % dict(title=title, desc=desc, canonical=canonical, og=og_title or title, prefix=prefix)


def header(prefix):
    nav = "".join(
        '\n        <a href="%s%s">%s</a>' % (prefix, h, t)
        for h, t in (("index.html", "ホーム"), ("apps.html", "アプリ"), ("support.html", "サポート"), ("about.html", "事業者情報"))
    )
    mnav = "".join(
        '\n    <a href="%s%s">%s</a>' % (prefix, h, t)
        for h, t in (("index.html", "ホーム"), ("apps.html", "アプリ"), ("support.html", "サポート"), ("about.html", "事業者情報"))
    )
    return """
  <!-- ===== ヘッダー ===== -->
  <header class="site-header">
    <div class="container">
      <a href="%(prefix)sindex.html" class="site-logo">
        <span class="logo-mark">A</span>
        Aju Works
      </a>

      <!-- PCナビ -->
      <nav class="site-nav" aria-label="メインナビゲーション">%(nav)s
      </nav>

      <!-- ハンバーガーボタン（スマホ用） -->
      <button class="hamburger" aria-label="メニューを開く" aria-expanded="false">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </header>

  <!-- モバイルメニュー -->
  <nav class="mobile-menu" aria-label="モバイルナビゲーション">%(mnav)s
  </nav>
""" % dict(prefix=prefix, nav=nav, mnav=mnav)


def footer(prefix):
    return """
  <!-- ===== フッター ===== -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-inner">
        <!-- ブランド -->
        <div class="footer-brand">
          <a href="%(p)sindex.html" class="footer-logo">Aju Works</a>
          <p>日々の実務と暮らしを少し便利にする<br>デジタル制作スタジオ</p>
        </div>

        <!-- ナビ: サービス -->
        <div class="footer-nav-group">
          <h4>サービス</h4>
          <ul>
            <li><a href="%(p)sapps.html">アプリ一覧</a></li>
            <li><a href="%(p)ssupport.html">サポート</a></li>
            <li><a href="%(p)sabout.html">事業者情報</a></li>
          </ul>
        </div>

        <!-- ナビ: ポリシー -->
        <div class="footer-nav-group">
          <h4>ポリシー</h4>
          <ul>
            <li><a href="%(p)sprivacy.html">プライバシーポリシー</a></li>
            <li><a href="%(p)sterms.html">利用規約</a></li>
          </ul>
        </div>

        <!-- ナビ: お問い合わせ -->
        <div class="footer-nav-group">
          <h4>お問い合わせ</h4>
          <ul>
            <li><a href="mailto:%(mail)s">%(mail)s</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2026 Aju Works. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <script src="%(p)sassets/js/main.js"></script>
</body>
</html>
""" % dict(p=prefix, mail=MAIL)


def status_badge(app):
    cls, label = STATUS_LABEL[app["status"]]
    return '<span class="status-badge %s">%s</span>' % (cls, label)


def app_tile(app, prefix, with_actions=False):
    """一覧用カード。機能の長文は載せず、詳細ページへ送る。"""
    out = ['      <article class="app-tile">']
    out.append('        <div class="app-tile-head">')
    out.append('          ' + icon_markup(app, prefix, "app-tile-icon"))
    out.append('          <div class="app-tile-heading">')
    out.append('            <h3 class="app-tile-name">%s</h3>' % app["name"])
    out.append('            <span class="app-tile-category">%s</span>' % app["category"])
    out.append('          </div>')
    out.append('        </div>')
    out.append('        <p class="app-tile-desc">%s</p>' % app["card"])
    if with_actions:
        acts = ['          <a href="%sapps/%s.html" class="btn btn-primary btn-sm">詳細を見る</a>' % (prefix, app["slug"])]
        if app["play"]:
            acts.append('          <a href="%s" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">Google Play</a>' % app["play"])
        out.append('        <div class="app-tile-actions">')
        out.extend(acts)
        out.append('        </div>')
        out.append('        <div class="app-tile-foot">')
        out.append('          %s' % status_badge(app))
        out.append('        </div>')
    else:
        out.append('        <div class="app-tile-foot">')
        out.append('          %s' % status_badge(app))
        out.append('          <a href="%sapps/%s.html" class="app-tile-link">詳しく見る %s</a>' % (prefix, app["slug"], ARROW))
        out.append('        </div>')
    out.append('      </article>')
    return "\n".join(out)


# ---------------------------------------------------------------------------
# index.html
# ---------------------------------------------------------------------------
def build_index():
    cards = "\n".join(app_tile(BY_SLUG[s], "") for s in HOME_SLUGS)
    body = """
  <main>

    <!-- ===== ヒーローセクション ===== -->
    <section class="hero">
      <div class="container">
        <div class="hero-content">
          <span class="hero-badge">Digital Creative Studio</span>
          <h1 class="hero-title">
            日々の実務と暮らしを、<br>
            少し便利にする<br>
            デジタル制作スタジオ
          </h1>
          <p class="hero-subtitle">
            Androidアプリ・デジタルコンテンツを企画・開発しています。
          </p>
          <div class="hero-actions">
            <a href="apps.html" class="btn btn-white btn-lg">アプリを見る</a>
            <a href="support.html" class="btn btn-outline-white btn-lg">お問い合わせ</a>
          </div>
        </div>
      </div>
    </section>

    <!-- ===== アプリ一覧（代表作） ===== -->
    <section class="section section-alt">
      <div class="container">
        <div class="section-header">
          <span class="section-label">Apps</span>
          <h2>Aju Worksのアプリ</h2>
          <p>記録・習慣・暮らしの小さな困りごとを解くAndroidアプリをつくっています。</p>
        </div>

        <div class="app-grid app-grid-3">
%(cards)s
        </div>

        <div class="section-actions">
          <a href="apps.html" class="btn btn-primary btn-lg">すべてのアプリを見る</a>
        </div>
      </div>
    </section>

    <!-- ===== 事業内容セクション ===== -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-label">Our Services</span>
          <h2>3つの事業領域</h2>
          <p>利用者の課題解決にフォーカスした、実用的なデジタルコンテンツを制作・提供しています。</p>
        </div>

        <div class="card-grid card-grid-3">
          <!-- カード1: アプリ開発 -->
          <div class="card">
            <span class="card-icon" aria-hidden="true">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2"/><line x1="9" y1="18" x2="15" y2="18"/></svg>
            </span>
            <h3>アプリ開発</h3>
            <p>
              日常の習慣づくりや記録を助けるスマートフォンアプリを企画・開発しています。
              使い続けたくなるシンプルな設計を心がけています。
            </p>
          </div>

          <!-- カード2: デジタルコンテンツ -->
          <div class="card">
            <span class="card-icon" aria-hidden="true">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
            </span>
            <h3>デジタルコンテンツ</h3>
            <p>
              電子書籍をはじめとするデジタルコンテンツの企画・執筆・編集・販売を行っています。
              実体験に基づく実用的なコンテンツを提供します。
            </p>
          </div>

          <!-- カード3: Webサービス -->
          <div class="card">
            <span class="card-icon" aria-hidden="true">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            </span>
            <h3>Webサービス</h3>
            <p>
              アプリや書籍に付随するWebコンテンツ・ツールの企画・開発も行っています。
              必要な人に、必要な情報を届けることを優先します。
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ===== CTAセクション ===== -->
    <section class="cta-section">
      <div class="container">
        <h2>まずはお気軽にご相談ください</h2>
        <p>アプリのご要望・お問い合わせはメールにて受け付けています。</p>
        <a href="support.html" class="btn btn-white btn-lg">お問い合わせページへ</a>
      </div>
    </section>

  </main>
""" % dict(cards=cards)

    html = (
        head("", "Aju Works — Androidアプリ開発・デジタル制作スタジオ",
             "日々の実務と暮らしを少し便利にするデジタル制作スタジオ。FANVOLT、筋トレ記録＆ベンチコーチ、Focus Gate、歩数・血圧手帳、ヨミオクなど、記録と習慣づくりのAndroidアプリを企画・開発しています。",
             SITE + "/", "Aju Works — Androidアプリ開発・デジタル制作スタジオ")
        + header("") + body + footer("")
    )
    write(os.path.join(ROOT, "index.html"), html)


# ---------------------------------------------------------------------------
# apps.html
# ---------------------------------------------------------------------------
def grid_class(n):
    """件数に合わせたグリッドのクラス。3件以上のときだけ3列にする。"""
    return "app-grid app-grid-3" if n >= 3 else "app-grid"


def build_apps():
    live = [a for a in APPS if a["status"] == "live"]
    prep = [a for a in APPS if a["status"] != "live"]
    body = """
  <main>

    <!-- ===== ページヘッダー ===== -->
    <section class="page-header">
      <div class="container">
        <h1>アプリ</h1>
        <p>Aju Worksが企画・開発しているAndroidアプリの一覧です。各アプリの詳細ページで、機能とデータの取り扱いを確認できます。</p>
      </div>
    </section>

    <!-- ===== 公開中 ===== -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-label">Available now</span>
          <h2>公開中のアプリ</h2>
          <p>Google Playで公開しています。</p>
        </div>

        <div class="%(live_grid)s"%(live_style)s>
%(live)s
        </div>
      </div>
    </section>

    <!-- ===== 公開準備中 ===== -->
    <section class="section section-alt">
      <div class="container">
        <div class="section-header">
          <span class="section-label">Coming soon</span>
          <h2>公開準備中のアプリ</h2>
          <p>開発・確認作業を進めています。公開時期が決まりましたらこのページで案内します。</p>
        </div>

        <div class="%(prep_grid)s">
%(prep)s
        </div>
      </div>
    </section>

    <!-- ===== CTAセクション ===== -->
    <section class="cta-section">
      <div class="container">
        <h2>アプリについてのお問い合わせ</h2>
        <p>不具合のご報告・ご要望はメールにて受け付けています。</p>
        <a href="support.html" class="btn btn-white btn-lg">サポートページへ</a>
      </div>
    </section>

  </main>
""" % dict(
        live="\n".join(app_tile(a, "", with_actions=True) for a in live),
        prep="\n".join(app_tile(a, "", with_actions=True) for a in prep),
        live_grid=grid_class(len(live)),
        live_style=(' style="grid-template-columns: 1fr; max-width: 520px; margin: 0 auto;"'
                    if len(live) == 1 else ""),
        prep_grid=grid_class(len(prep)),
    )

    html = (
        head("", "アプリ一覧 — Aju Works",
             "Aju Worksが開発したAndroidアプリの一覧。FANVOLT、筋トレ記録＆ベンチコーチ、サブスク整理、Focus Gate、歩数・血圧手帳、ヨミオク、WatchIt、Night Fadeなど。",
             SITE + "/apps.html", "アプリ一覧 — Aju Works")
        + header("") + body + footer("")
    )
    write(os.path.join(ROOT, "apps.html"), html)


# ---------------------------------------------------------------------------
# apps/<slug>.html
# ---------------------------------------------------------------------------
def related_for(app):
    order = [a for a in APPS if a["slug"] != app["slug"]]
    same = [a for a in order if a["category"] == app["category"]]
    others = [a for a in order if a["category"] != app["category"] and a["status"] == "live"]
    picks, seen = [], set()
    for a in same + others + order:
        if a["slug"] in seen:
            continue
        seen.add(a["slug"])
        picks.append(a)
        if len(picks) == 3:
            break
    return picks


def fact_rows(app):
    """事実行。ストア掲載名がサイト掲載名と違う場合は先頭に出す。"""
    rows = []
    if app["status"] == "live" and app.get("store_name") and app["store_name"] != app["name"]:
        rows.append(("Google Playでの表示名", app["store_name"]))
    rows.append(("アプリID", "<code>%s</code>" % app["app_id"]))
    rows.extend(app["facts"])
    return rows


def build_detail(app):
    p = "../"
    badges = "".join('\n            <span class="badge %s">%s</span>' % (c, t) for c, t in app["badges"])

    if app["play"]:
        cta = ('<a href="%s" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">Google Playで入手</a>'
               % app["play"])
    else:
        cta = '<span class="btn btn-secondary btn-lg" aria-disabled="true">公開準備中</span>'

    overview = "\n".join("          <p>%s</p>" % t for t in app["overview"])

    features = "\n".join(
        '          <div class="feature-item">\n'
        '            <span class="feature-item-num" aria-hidden="true">%d</span>\n'
        '            <p>%s</p>\n'
        '          </div>' % (i + 1, f)
        for i, f in enumerate(app["features"])
    )

    shots_block = ""
    if app.get("shots"):
        imgs = "\n".join(
            '          <img src="%sassets/img/screenshots/%s/%s" width="360" height="800" alt="%s" loading="lazy" decoding="async">'
            % (p, app["slug"], f, alt) for f, alt in app["shots"]
        )
        shots_block = """
    <!-- ===== スクリーンショット ===== -->
    <section class="section section-alt">
      <div class="container">
        <div class="section-header">
          <span class="section-label">Screenshots</span>
          <h2>画面</h2>
        </div>
        <div class="shot-strip">
%s
        </div>
      </div>
    </section>
""" % imgs

    facts = "\n".join(
        '          <div class="fact-row">\n            <dt>%s</dt>\n            <dd>%s</dd>\n          </div>' % (dt, dd)
        for dt, dd in fact_rows(app)
    )

    purl, plabel, pext = app["privacy"]
    if pext:
        privacy_link = ('<a href="%s" target="_blank" rel="noopener noreferrer" class="btn btn-outline">%s</a>'
                        % (purl, plabel))
    else:
        privacy_link = '<a href="%s" class="btn btn-outline">%s</a>' % (purl, plabel)

    # プライバシーポリシー以外に案内したいリンク（データ削除の説明など）
    for url, label, external in app.get("extra_links", []):
        target = ' target="_blank" rel="noopener noreferrer"' if external else ""
        privacy_link += (
            "\n          " + '<a href="%s"%s class="btn btn-outline">%s</a>' % (url, target, label)
        )

    note_block = ""
    if app.get("note"):
        note_block = ('\n        <div class="app-note-card mt-6">\n          <p>%s</p>\n        </div>' % app["note"])

    rel = "\n".join(
        '          <a href="%s.html" class="related-item">\n'
        '            %s\n'
        '            <span class="related-item-text">\n'
        '              <span class="related-item-name">%s</span>\n'
        '              <span class="related-item-note">%s</span>\n'
        '            </span>\n'
        '          </a>' % (r["slug"], icon_markup(r, p, "related-item-icon"), r["short"], r["category"])
        for r in related_for(app)
    )

    body = """
  <main>

    <!-- ===== パンくず ===== -->
    <div class="container">
      <nav class="breadcrumb" aria-label="パンくずリスト">
        <ol>
          <li><a href="%(p)sindex.html">ホーム</a></li>
          <li><a href="%(p)sapps.html">アプリ</a></li>
          <li><span class="breadcrumb-current" aria-current="page">%(name)s</span></li>
        </ol>
      </nav>
    </div>

    <!-- ===== ヒーロー ===== -->
    <section class="detail-hero">
      <div class="container">
        <div class="detail-hero-inner">
          %(icon)s
          <div>
            <div class="detail-hero-badges">%(badges)s
            </div>
            <h1>%(name)s</h1>
            <p class="detail-hero-tagline">%(tagline)s</p>
            <div class="detail-hero-actions">
              %(cta)s
              <a href="%(p)ssupport.html" class="btn btn-outline">サポート</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ===== アプリ概要 ===== -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-label">Overview</span>
          <h2>このアプリについて</h2>
        </div>
        <div class="app-description" style="max-width: 760px; margin: 0 auto;">
%(overview)s
        </div>%(note)s
      </div>
    </section>

    <!-- ===== 主な機能 ===== -->
    <section class="section section-alt">
      <div class="container">
        <div class="section-header">
          <span class="section-label">Features</span>
          <h2>主な機能</h2>
        </div>
        <div class="feature-grid">
%(features)s
        </div>
      </div>
    </section>
%(shots)s
    <!-- ===== プライバシー ===== -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-label">Privacy</span>
          <h2>データの取り扱い</h2>
          <p>実装で確認できた内容のみを記載しています。</p>
        </div>
        <dl class="fact-list">
%(facts)s
        </dl>
        <div class="section-actions">
          %(privacy)s
        </div>
      </div>
    </section>

    <!-- ===== サポート ===== -->
    <section class="section section-alt">
      <div class="container">
        <div class="section-header">
          <span class="section-label">Support</span>
          <h2>お問い合わせ</h2>
          <p>不具合のご報告・ご要望はメールにて受け付けています。</p>
        </div>
        <div class="contact-cta-box" style="max-width: 620px; margin: 0 auto; text-align: center;">
          <p><a href="mailto:%(mail)s">%(mail)s</a></p>
          <p class="mt-4"><a href="%(p)ssupport.html" class="btn btn-primary">サポートページへ</a></p>
        </div>
      </div>
    </section>

    <!-- ===== 他のアプリ ===== -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-label">Other apps</span>
          <h2>他のアプリ</h2>
        </div>
        <div class="related-grid">
%(rel)s
        </div>
        <div class="section-actions">
          <a href="%(p)sapps.html" class="btn btn-outline">アプリ一覧へ戻る</a>
        </div>
      </div>
    </section>

  </main>
""" % dict(p=p, name=app["name"], icon=icon_markup(app, p, "detail-hero-icon"), badges=badges,
           tagline=app["tagline"], cta=cta, overview=overview, note=note_block,
           features=features, shots=shots_block, facts=facts, privacy=privacy_link,
           mail=MAIL, rel=rel)

    desc = "%s %s %s" % (app["name"], "—", app["card"])
    html = (
        head(p, "%s — Aju Works" % app["name"], desc,
             "%s/apps/%s.html" % (SITE, app["slug"]), "%s — Aju Works" % app["name"])
        + header(p) + body + footer(p)
    )
    write(os.path.join(ROOT, "apps", "%s.html" % app["slug"]), html)


def build_404():
    """GitHub Pages が 404 のときに返すページ。

    ページ名を変えた場合（例: apps/readrecall.html → apps/yomioku.html）に
    古いURLを踏んだ人が行き止まりにならないよう、案内を出す。
    リンクはルート基準で書く。どの階層で 404 になっても壊れないようにするため。
    """
    body = """
  <main>
    <div class="page-header">
      <div class="container">
        <h1>ページが見つかりません</h1>
        <p>お探しのページは、移動または削除された可能性があります。</p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-label">404</span>
          <h2>次のいずれかからお探しください</h2>
        </div>
        <div class="section-actions">
          <a href="/" class="btn btn-primary">ホームへ</a>
          <a href="/apps.html" class="btn btn-outline">アプリ一覧</a>
          <a href="/support.html" class="btn btn-outline">サポート</a>
          <a href="/privacy.html" class="btn btn-outline">プライバシーポリシー</a>
        </div>
        <p style="text-align: center; margin-top: var(--space-6);">
          見つからない場合は <a href="mailto:%(mail)s">%(mail)s</a> までお知らせください。
        </p>
      </div>
    </section>
  </main>
""" % dict(mail=MAIL)

    html = (
        head("", "ページが見つかりません — Aju Works",
             "お探しのページは移動または削除された可能性があります。",
             "%s/404.html" % SITE)
        + header("") + body + footer("")
    )
    # 検索結果に載せない
    html = html.replace("</head>", '  <meta name="robots" content="noindex">\n</head>', 1)
    write(os.path.join(ROOT, "404.html"), html)


def write(path, text):
    d = os.path.dirname(path)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote", path, len(text), "bytes")


if __name__ == "__main__":
    build_index()
    build_apps()
    for a in APPS:
        build_detail(a)
    build_404()
    print("apps:", len(APPS))
