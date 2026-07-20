import streamlit as st

mbti_pokemon = {
    "INTJ": {"name": "메타그로스", "dex": 376, "reason": "전략적 사고와 강한 목표 지향성을 지닌 포켓몬입니다."},
    "INTP": {"name": "슬로우킹", "dex": 199, "reason": "깊은 사고와 분석을 즐기는 지적인 포켓몬입니다."},
    "ENTJ": {"name": "리자몽", "dex": 6, "reason": "강한 리더십과 추진력을 상징하는 포켓몬입니다."},
    "ENTP": {"name": "딱구리", "dex": 84, "reason": "재치 있고 임기응변에 강한 포켓몬입니다."},
    "INFJ": {"name": "뮤", "dex": 151, "reason": "신비롭고 통찰력 있는 이상주의 포켓몬입니다."},
    "INFP": {"name": "라프라스", "dex": 131, "reason": "따뜻한 마음과 이상을 소중히 여기는 포켓몬입니다."},
    "ENFJ": {"name": "루카리오", "dex": 448, "reason": "타인을 이끌고 돕는 데 능한 포켓몬입니다."},
    "ENFP": {"name": "피카츄", "dex": 25, "reason": "밝고 에너지 넘치는 친화력의 상징입니다."},
    "ISTJ": {"name": "개굴닌자", "dex": 658, "reason": "원칙과 책임감을 중시하는 포켓몬입니다."},
    "ISFJ": {"name": "잠만보", "dex": 143, "reason": "안정적이고 헌신적인 성향의 포켓몬입니다."},
    "ESTJ": {"name": "삼지주", "dex": 45, "reason": "체계적이고 관리 능력이 뛰어난 포켓몬입니다."},
    "ESFJ": {"name": "픽시", "dex": 36, "reason": "사교적이고 배려심 많은 포켓몬입니다."},
    "ISTP": {"name": "이상해씨", "dex": 1, "reason": "실용적이고 적응력이 뛰어난 포켓몬입니다."},
    "ISFP": {"name": "이브이", "dex": 133, "reason": "다재다능하고 개성이 뚜렷한 포켓몬입니다."},
    "ESTP": {"name": "부스터", "dex": 136, "reason": "즉흥적이고 행동력이 강한 포켓몬입니다."},
    "ESFP": {"name": "고라파덕", "dex": 97, "reason": "즉흥적이고 유쾌한 매력의 포켓몬입니다."},
}

def pokemon_image_url(dex_number):
    return f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{dex_number}.png"

st.title("📝 MBTI 간이 테스트")
st.write("아래 4개 질문에 답하면 간단히 MBTI 유형을 추정해드립니다.")
st.caption("※ 질문 1개당 하나의 축(E/I, S/N, T/F, J/P)을 판단하는 단순화된 테스트입니다. 정식 심리검사가 아니니 참고용으로만 봐주세요.")

q1 = st.radio(
    "1. 주말에 에너지를 얻는 방법은?",
    ["친구들을 만나 어울리며 활력을 얻는다 (E)", "혼자만의 시간을 보내며 재충전한다 (I)"]
)

q2 = st.radio(
    "2. 새로운 정보를 받아들일 때 더 편한 방식은?",
    ["구체적인 사실과 경험을 중시한다 (S)", "가능성과 아이디어, 큰 그림을 중시한다 (N)"]
)

q3 = st.radio(
    "3. 결정을 내릴 때 더 중요하게 생각하는 것은?",
    ["논리와 원칙에 따라 객관적으로 판단한다 (T)", "사람들의 감정과 관계를 고려해서 판단한다 (F)"]
)

q4 = st.radio(
    "4. 일상을 살아가는 스타일은?",
    ["계획을 세우고 정해진 대로 진행하는 게 편하다 (J)", "상황에 따라 유연하게 대처하는 게 편하다 (P)"]
)

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
