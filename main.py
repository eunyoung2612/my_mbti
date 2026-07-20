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

st.set_page_config(page_title="MBTI 포켓몬 추천", page_icon="🎮")

st.title("🎮 MBTI 포켓몬 추천기")
st.write("당신의 MBTI를 선택하면 어울리는 포켓몬을 추천해드립니다.")
st.caption("왼쪽 사이드바에서 다른 페이지(간이 테스트, 내향인 도감)로 이동할 수 있습니다.")

mbti_list = list(mbti_pokemon.keys())
selected_mbti = st.selectbox("MBTI를 선택하세요", mbti_list)

if st.button("포켓몬 추천 받기"):
    result = mbti_pokemon[selected_mbti]
    st.subheader(f"✨ {selected_mbti} 유형에게 추천하는 포켓몬")
    st.image(pokemon_image_url(result["dex"]), width=250)
    st.markdown(f"### {result['name']}")
    st.write(result['reason'])
