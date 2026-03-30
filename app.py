import streamlit as st
from transformers import pipeline
import pandas as pd
import os

def save_result(results):
    df = pd.DataFrame(results, columns=["언어", "결과", "확률"])

    if os.path.exists("results.csv"):
        df.to_csv("results.csv", mode='a', header=False, index=False)
    else:
        df.to_csv("results.csv", index=False)

classifier = pipeline("sentiment-analysis")

st.title("다국어 감정 분석 비교")

# 입력 3개
text_ko = st.text_input("한국어 입력")
text_en = st.text_input("영어 입력")
text_other = st.text_input("소수언어 입력")

if st.button("분석하기"):
    results = []

    if text_ko:
        r = classifier(text_ko)[0]
        results.append(("한국어", r['label'], r['score']))

    if text_en:
        r = classifier(text_en)[0]
        results.append(("영어", r['label'], r['score']))

    if text_other:
        r = classifier(text_other)[0]
        results.append(("소수언어", r['label'], r['score']))

    # 결과 출력
    for lang, label, score in results:
        st.write(f"{lang} → {label} ({score:.2f})")

    # 편향 감지
    labels = [r[1] for r in results]
    if len(set(labels)) > 1:
        st.error("⚠️ 언어별 결과가 다릅니다 → 편향 가능성")

    df = pd.DataFrame(results, columns=["언어", "결과", "확률"])
    st.bar_chart(df.set_index("언어")["확률"])

    save_result(results)
    st.success("결과가 저장되었습니다!")