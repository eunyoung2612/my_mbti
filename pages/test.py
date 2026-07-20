if st.button("내 MBTI 결과 보기"):
    e_or_i = "E" if q1.endswith("(E)") else "I"
    s_or_n = "S" if q2.endswith("(S)") else "N"
    t_or_f = "T" if q3.endswith("(T)") else "F"
    j_or_p = "J" if q4.endswith("(J)") else "P"

    result_mbti = e_or_i + s_or_n + t_or_f + j_or_p

    st.success(f"당신의 예상 MBTI는 **{result_mbti}** 입니다.")
    result = mbti_pokemon[result_mbti]
    st.subheader(f"✨ {result_mbti} 유형에게 추천하는 포켓몬")
    st.image(pokemon_image_url(result["dex"]), width=250)
    st.markdown(f"### {result['name']}")
    st.write(result['reason'])
