import streamlit as st
import random, base64, io, os
from PIL import Image
from datetime import date

st.set_page_config(page_title="猫のタロットカード", page_icon="🐱", layout="centered")

# ===== 画像をBase64に変換 =====
def load_image_base64(path):
    if not os.path.exists(path):
        return ""
    img = Image.open(path)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()



# ===== カードデータ =====
cards = [
    {"id": 0, "name": "The Fool", "image": "images/0_the_fool.png",
     "meaning_upright": "新しい旅立ち、自由な魂、未知への好奇心。猫のように気ままに一歩を踏み出す時です。",
     "meaning_reversed": "衝動的、無計画、現実逃避。足元を見ずに飛び出すと危険です。"},
    {"id": 1, "name": "The Magician", "image": "images/1_the_magician.png",
     "meaning_upright": "創造力、意志、行動力。あなたの中の魔法が現実を動かします。",
     "meaning_reversed": "力の乱用、自己欺瞞、焦り。自分の力を信じすぎないよう注意。"},
    {"id": 2, "name": "The High Priestess", "image": "images/2_the_high_priestess.png",
     "meaning_upright": "直感、神秘、内なる知恵。心の静寂に答えがあります。",
     "meaning_reversed": "混乱、秘密、誤解。感情に流されて真実を見失わないで。"},
    {"id": 3, "name": "The Empress", "image": "images/3_the_empress.png",
     "meaning_upright": "豊かさ、愛、美しさ、母性。あなたの優しさが実りをもたらします。",
     "meaning_reversed": "過保護、怠惰、嫉妬。愛を与えすぎて疲れていませんか？"},
    {"id": 4, "name": "The Emperor", "image": "images/4_the_emperor.png",
     "meaning_upright": "安定、秩序、責任、リーダーシップ。信頼と自信が周囲を導きます。",
     "meaning_reversed": "支配的、頑固、抑圧。自分の意見を押しつけすぎていませんか？"},
    {"id": 5, "name": "The Hierophant", "image": "images/5_the_hierophant.png",
     "meaning_upright": "伝統、導き、信頼、教育。知識を共有することで絆が深まります。",
     "meaning_reversed": "盲信、形式主義、閉鎖的。古い考えに縛られすぎていませんか？"},
    {"id": 6, "name": "The Lovers", "image": "images/6_the_lovers.png",
     "meaning_upright": "愛、調和、選択、運命の出会い。心で選んだものが正解です。",
     "meaning_reversed": "迷い、不一致、誘惑。心と現実のズレを見つめ直すとき。"},
    {"id": 7, "name": "The Chariot", "image": "images/7_the_chariot.png",
     "meaning_upright": "勝利、意志、行動力。強い意志が未来を切り開きます。",
     "meaning_reversed": "暴走、焦り、迷走。進む前に心の手綱を握り直して。"},
    {"id": 8, "name": "Strength", "image": "images/8_strength.png",
     "meaning_upright": "勇気、忍耐、優しさ。静かな強さがあなたを導きます。",
     "meaning_reversed": "弱気、自己不信、怠惰。力は外ではなく内にあります。"},
    {"id": 9, "name": "The Hermit", "image": "images/9_the_hermit.png",
     "meaning_upright": "探求、内省、孤独。静かな時間の中で答えを見つけましょう。",
     "meaning_reversed": "孤立、閉鎖、迷い。人の温もりを拒んでいませんか？"},
    {"id": 10, "name": "Wheel of Fortune", "image": "images/10_wheel_of_fortune.png",
     "meaning_upright": "運命の転換、チャンス、流れの変化。幸運の風が吹いています。",
     "meaning_reversed": "停滞、タイミングのずれ、運命の試練。焦らず流れを待って。"},
    {"id": 11, "name": "Justice", "image": "images/11_justice.png",
     "meaning_upright": "公平、真実、正義。冷静な判断が幸運を引き寄せます。",
     "meaning_reversed": "偏り、不正、誤審。感情が判断を曇らせています。"},
    {"id": 12, "name": "The Hanged Man", "image": "images/12_the_hanged_man.png",
     "meaning_upright": "受容、献身、新しい視点。苦しみの中に光があります。",
     "meaning_reversed": "無駄な犠牲、停滞、無力感。何のために我慢しているのか見直して。"},
    {"id": 13, "name": "Death", "image": "images/13_death.png",
     "meaning_upright": "終わりと再生、変化、再出発。古いものを手放して新しい扉を開く時。",
     "meaning_reversed": "拒絶、停滞、執着。変化を恐れると新しい道が閉ざされます。"},
    {"id": 14, "name": "Temperance", "image": "images/14_temperance.png",
     "meaning_upright": "調和、節制、バランス、癒し。異なるものを融合させる力。",
     "meaning_reversed": "不均衡、過剰、焦り。心と体の調和を取り戻して。"},
    {"id": 15, "name": "The Devil", "image": "images/15_the_devil.png",
     "meaning_upright": "誘惑、快楽、執着。心の影を見つめる勇気を。",
     "meaning_reversed": "解放、克服、自由。あなたはもう鎖を外せます。"},
    {"id": 16, "name": "The Tower", "image": "images/16_the_tower.png",
     "meaning_upright": "崩壊、衝撃、覚醒。壊れることで新しい未来が始まります。",
     "meaning_reversed": "恐怖、回避、限界。変化を恐れすぎていませんか？"},
    {"id": 17, "name": "The Star", "image": "images/17_the_star.png",
     "meaning_upright": "希望、癒し、信頼。願いは静かに叶いつつあります。",
     "meaning_reversed": "失望、不信、自己否定。希望を見失わないで。"},
    {"id": 18, "name": "The Moon", "image": "images/18_the_moon.png",
     "meaning_upright": "直感、夢、潜在意識。不安の中にも真実があります。",
     "meaning_reversed": "幻惑、誤解、不安定。現実と幻想の区別をつけましょう。"},
    {"id": 19, "name": "The Sun", "image": "images/19_the_sun.png",
     "meaning_upright": "成功、喜び、生命力。光がすべてを照らします。",
     "meaning_reversed": "空回り、傲慢、疲労。少し休んで心を整えて。"},
    {"id": 20, "name": "Judgement", "image": "images/20_judgement.png",
     "meaning_upright": "再生、赦し、目覚め。新しい可能性に心を開きましょう。",
     "meaning_reversed": "自己否定、迷い、後悔。過去を責めず未来を見つめて。"},
    {"id": 21, "name": "The World", "image": "images/21_the_world.png",
     "meaning_upright": "完成、達成、調和。すべてが一つに結ばれる瞬間です。",
     "meaning_reversed": "未完、迷い、喪失。まだ終わっていない課題があります。"}
]

card_back = "images/back.png"

# Base64化
for c in cards:
    c["b64"] = load_image_base64(c["image"])
back_b64 = load_image_base64(card_back)

# ===== セッション管理 =====
if "drawn" not in st.session_state:
    st.session_state.drawn = False
    st.session_state.results = []
if "mode" not in st.session_state:
    st.session_state.mode = "3枚引き（過去・現在・未来）"

# ===== タイトル＆モード選択 =====
st.title("🐱✨猫のタロットカード✨🐱")
st.session_state.mode = st.selectbox("モードを選んでください：", ["3枚引き（過去・現在・未来）", "1枚引き"])

# 🧩モード変更でリセット
if "prev_mode" not in st.session_state:
    st.session_state.prev_mode = st.session_state.mode
elif st.session_state.mode != st.session_state.prev_mode:
    st.session_state.drawn = False
    st.session_state.results = []
    st.session_state.prev_mode = st.session_state.mode

# ===== カードを引くボタン =====
if st.button("カードを引く 🎴"):
    num = 1 if "1枚" in st.session_state.mode else 3
    st.session_state.results = [
        {"card": c, "reversed": random.choice([True, False])}
        for c in random.sample(cards, num)
    ]
    st.session_state.drawn = True

# ===== カードレイアウト =====
positions = ["過去", "現在", "未来"]

if st.session_state.drawn:
    if "1枚" in st.session_state.mode:
        # 一枚引きモード
        result = st.session_state.results[0]
        c = result["card"]
        rev = result["reversed"]
        st.markdown(f"""
            <div style="text-align:center;">
                <img src="data:image/png;base64,{c['b64']}" 
                     style="width:260px; border-radius:10px;
                     transform:{'rotate(180deg)' if rev else 'none'};
                     ">
                <div style="margin-top:10px; font-size:18px;">
                    <b>{c['name']}（{'逆位置' if rev else '正位置'}）</b><br>
                    {c['meaning_reversed'] if rev else c['meaning_upright']}
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        # 3枚引きモード
        cols = st.columns(3)
        for i, result in enumerate(st.session_state.results):
            c = result["card"]
            rev = result["reversed"]
            with cols[i]:
                st.markdown(f"""
                    <div style="text-align:center;">
                        <img src="data:image/png;base64,{c['b64']}" 
                             style="width:220px; border-radius:10px;
                             transform:{'rotate(180deg)' if rev else 'none'};
                             ">
                        <div style="margin-top:10px; text-align:left;">
                            <b>{positions[i]}：{c['name']}（{'逆位置' if rev else '正位置'}）</b><br>
                            {c['meaning_reversed'] if rev else c['meaning_upright']}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
else:
    # 初期表示（裏カード）
    if "1枚" in st.session_state.mode:
        st.markdown(f"""
            <div style="text-align:center;">
                <img src="data:image/png;base64,{back_b64}" style="width:260px; opacity:0.9;">
            </div>
        """, unsafe_allow_html=True)
    else:
        cols = st.columns(3)
        for i in range(3):
            with cols[i]:
                st.markdown(f"""
                    <div style="text-align:center;">
                        <img src="data:image/png;base64,{back_b64}" style="width:220px; opacity:0.9;">
                    </div>
                """, unsafe_allow_html=True)



# ===== 今日のメッセージ =====
messages = [
    "あなたの直感を信じてください。",
    "小さな一歩が未来を変えます。",
    "心を落ち着けて、自然の流れに任せましょう。",
    "焦らなくて大丈夫、あなたは順調です。",
    "猫のように気ままに、今を楽しんでください。",
    "光はすでに、あなたの中にあります。",
    "今は休むことで、次の力が生まれます。",
    "誰かの笑顔を思い出すと、運気が上がります。",
    "過去を手放せば、未来が軽くなります。",
    "あなたの優しさが、世界を少し変えています。",
    "迷いの中にも、正しい道があります。",
    "言葉よりも、静けさの中に答えがあります。",
    "今日は、自分を褒めてあげてください。",
    "思い切り笑うことが、最高の浄化です。",
    "見えない力が、あなたをそっと守っています。",
    "どんな夜も、必ず朝に続いています。",
    "あなたの願いは、すでに動き出しています。",
    "ゆっくりでも、確実に進んでいます。",
    "猫のようにマイペースでいいんです。",
    "心配ごとは、風に乗せて手放しましょう。",
    "あなたの存在そのものが、誰かの癒しです。",
    "今のあなたで、もう十分素敵です。",
    "流れに逆らわず、軽やかに生きてください。",
    "感謝の気持ちが、幸せを呼び寄せます。",
    "恐れよりも、愛を選んでください。"
]

today = str(date.today())
if "msg_date" not in st.session_state or st.session_state.msg_date != today:
    st.session_state.msg_date = today
    st.session_state.today_msg = random.choice(messages)

st.markdown("<br><h3 style='text-align:center;'>🌟 今日のメッセージ 🌟</h3>", unsafe_allow_html=True)
st.markdown(f"""
<div style='text-align:center; font-size:20px; padding:15px;
background:#fff8e7; border-radius:15px; box-shadow:0 0 10px rgba(0,0,0,0.1);
margin-top:10px;'>🐾 {st.session_state.today_msg} 🐾</div>
""", unsafe_allow_html=True)