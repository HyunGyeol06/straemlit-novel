from openai import OpenAI
import streamlit as st
import tiktoken


def create_novel(
        era="현대",
        genre="로맨스",
        main_character_name="앨리스",
        key_word="사랑",
        country="프랑스",
        option="줄거리"
):
    global messages
    client = OpenAI(
        api_key=st.secrets["openai_key"]
    )

    message_content = ""
    if option == "줄거리":
        message_content = "줄거리만 말해주세요."
    elif option == "간단한 묘사":
        message_content = "간단하게 묘사해주세요"
    else:
        message_content = "자세하게 묘사해주세요."

    messages = [
        {"role": "system", "content": "You are the world's best novelist."},
        {"role": "user","content": f"소설을 써 주세요. 시대는 {era}이고, 장르는 {genre}이고, 주인공의 이름은 {main_character_name}이고, 주요 키워드는 {key_word}이고, 나라는 {country}입니다. {message_content}"}
    ]

    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        max_tokens=5000,
        temperature=1,
    )
    summary = response.choices[0].message.content
    return summary


# def summarize_text_final(text_list, lang="en"):
#     joined_summary = " ".join(text_list)
#
#     enc = tiktoken.encoding_for_model("gpt-4")
#     token_num = len(enc.encode(joined_summary))
#
#     req_max_token = 5000
#     final_summary = ""
#     if token_num < req_max_token:
#         final_summary = create_novel(joined_summary, lang)
#
#     return token_num, final_summary
