from dotenv import load_dotenv
import streamlit as st
from langchain.schema import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

# 環境変数の読み込み
load_dotenv()

# ChatOpenAIの初期化
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# Streamlitアプリのタイトル
st.title("スペシャリストの回答コーナー")

st.write("##### 専門家A: 人事部スペシャリストAI")
st.write("入力フォームに人事や社内教育に関する質問にスペシャリストとして回答をします。")
st.write("##### 専門家B: マーケティング部スペシャリストAI")
st.write("入力フォームにマーケティングや広告に関する質問にスペシャリストとして回答をします。")

# 動作モードの選択
selected_item = st.radio(
    "動作モードを選択してください。",
    ["人事部スペシャリスト", "マーケティング部スペシャリスト"]
)

st.divider()

# モードごとのプロンプト設定
prompts = {
    "人事部スペシャリスト": """あなたは経験豊富な人事部のスペシャリストです。
労務管理、採用、人材育成、給与・福利厚生、退職手続きなど人事全般に関する専門知識を持っています。
従業員の立場に立って、実務的で具体的なアドバイスを提供してください。
社内制度や手続きについて詳しく説明し、必要に応じて関連する法律や規則も含めて回答してください。

重要：もし質問が人事・労務以外の専門分野（マーケティング、法務、技術、営業など）に関するものであれば、
「申し訳ございませんが、その質問は人事部の専門領域外です。マーケティング部や該当する専門部署にお問い合わせいただくことをお勧めします。
人事・労務に関するご質問でしたら、喜んでお答えいたします。」
と回答してください。""",
    
    "マーケティング部スペシャリスト": """あなたは経験豊富なマーケティング部のスペシャリストです。
市場調査、広告戦略、ブランディング、デジタルマーケティング、SNS活用、コンテンツマーケティングなどマーケティング全般に関する専門知識を持っています。
顧客のニーズに基づいた効果的なマーケティング施策を提案し、実行可能なアドバイスを提供してください。

重要：もし質問がマーケティング以外の専門分野（人事、法務、技術など）に関するものであれば、
「申し訳ございませんが、その質問はマーケティング部の専門領域外です。人事部や該当する専門部署にお問い合わせいただくことをお勧めします。
マーケティングに関するご質問でしたら、喜んでお答えいたします。」
と回答してください。"""
}

# 入力フォーム
input_message = st.text_input(label="質問を入力して実行ボタンを押してください。")

# 実行ボタン
if st.button("実行"):
    if input_message:
        try:
            # メッセージの構築
            messages = [
                SystemMessage(content=prompts[selected_item]),
                HumanMessage(content=input_message)
            ]
            # LLMへの問い合わせ
            response = llm.invoke(messages)
            st.write(f"{selected_item}の回答: {response.content}")
            
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
    else:
        st.error("質問を入力してから「実行」ボタンを押してください。")
