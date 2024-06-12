import novel
import streamlit as st
import textwrap


def write_novel(
        era1,
        genre1,
        main_character_name1,
        key_word1,
        country1
):
    st.write("새게챼고의 소설가 채찍피티가 소설을 쓰고있어요.")

    final_novel = novel.create_novel(
        era1,
        genre1,
        main_character_name1,
        key_word1,
        country1
    )
    print(final_novel)

    if final_novel != "":
        st.write("매우 엄청나고 으메이징한 소설:", final_novel)


# -------- main page ---------

st.set_page_config(page_title="pdf_sum")

st.title("소설 생성")

era = st.selectbox("시대", ["현대", "고대", "중세", "근현대", "미래"])
genre = st.selectbox("장르", ["로맨스", "스릴러", "판타지", "SF", "추리", "액션", "학원물", "무협"])
main_character_name = st.text_input("주인공 이름")
key_word = st.text_input("주요 키워드")
country = st.text_input("국가")

clicked = st.button("채찍피티의 소설쓰기")

if clicked:
    write_novel(
        era,
        genre,
        main_character_name,
        key_word,
        country
    )
