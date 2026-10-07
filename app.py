import streamlit as st
from coach_agent import generate_drill, generate_session

# Page configuration
st.set_page_config(
    page_title="U8 Football Coach AI",
    page_icon="⚽",
    layout="wide"
)

# ============================================================
# TRANSLATIONS FOR THE INTERFACE
# ============================================================

TRANSLATIONS = {
    "English": {
        "title": "⚽ U8 Football Coach",
        "subtitle": "Generate fun, safe, and age-appropriate training drills and session plans for children aged 6 to 8.",
        "settings": "Settings",
        "language_label": "Output Language:",
        "mode_label": "What would you like to create?",
        "mode_drill": "Single Drill",
        "mode_session": "Full Session Plan",
        "drill_header": "🎯 Create a Single Drill",
        "drill_instruction": "Describe the drill you want to create. The AI will generate a complete, age-appropriate drill for U8 children.",
        "drill_label": "Describe your drill idea:",
        "drill_placeholder": "e.g., A fun dribbling game where children pretend to be pirates protecting their treasure",
        "drill_button": "Generate Drill",
        "drill_spinner": "Creating your drill...",
        "drill_success": "Drill created!",
        "drill_warning": "Please describe your drill idea.",
        "session_header": "📋 Create a Full Session Plan",
        "session_instruction": "Enter a theme for your session. The AI will generate a complete, structured session plan.",
        "session_label": "Session theme:",
        "session_placeholder": "e.g., Dribbling and turning",
        "session_duration": "Session duration (minutes):",
        "session_button": "Generate Session Plan",
        "session_spinner": "Creating your session plan...",
        "session_success": "Session plan created!",
        "session_warning": "Please enter a session theme.",
        "about_title": "About This Tool",
        "about_text": "This tool is designed for U8 football coaches who want fun, safe, and age-appropriate training ideas.",
        "principles_title": "Principles:",
        "principle_1": "Fun is the priority",
        "principle_2": "Every child is active",
        "principle_3": "Small-sided games",
        "principle_4": "Simple language",
        "principle_5": "Safety first",
        "built_with": "Built with the Claude API",
    },
    "French": {
        "title": "⚽ Assistant Entraîneur U8",
        "subtitle": "Générez des exercices et des plans de séance amusants, sûrs et adaptés à l'âge des enfants de 6 à 8 ans.",
        "settings": "Paramètres",
        "language_label": "Langue de sortie :",
        "mode_label": "Que souhaitez-vous créer ?",
        "mode_drill": "Exercice Simple",
        "mode_session": "Plan de Séance Complet",
        "drill_header": "🎯 Créer un Exercice Simple",
        "drill_instruction": "Décrivez l'exercice que vous souhaitez créer. L'IA générera un exercice complet et adapté à l'âge des enfants U8.",
        "drill_label": "Décrivez votre idée d'exercice :",
        "drill_placeholder": "ex. : Un jeu de dribble amusant où les enfants jouent aux pirates protégeant leur trésor",
        "drill_button": "Générer l'Exercice",
        "drill_spinner": "Création de votre exercice...",
        "drill_success": "Exercice créé !",
        "drill_warning": "Veuillez décrire votre idée d'exercice.",
        "session_header": "📋 Créer un Plan de Séance Complet",
        "session_instruction": "Entrez un thème pour votre séance. L'IA générera un plan de séance complet et structuré.",
        "session_label": "Thème de la séance :",
        "session_placeholder": "ex. : Dribble et changement de direction",
        "session_duration": "Durée de la séance (minutes) :",
        "session_button": "Générer le Plan de Séance",
        "session_spinner": "Création de votre plan de séance...",
        "session_success": "Plan de séance créé !",
        "session_warning": "Veuillez entrer un thème de séance.",
        "about_title": "À Propos de Cet Outil",
        "about_text": "Cet outil est conçu pour les entraîneurs de football U8 qui recherchent des idées d'entraînement amusantes, sûres et adaptées à l'âge.",
        "principles_title": "Principes :",
        "principle_1": "Le plaisir est la priorité",
        "principle_2": "Chaque enfant est actif",
        "principle_3": "Jeux à effectif réduit",
        "principle_4": "Langage simple",
        "principle_5": "La sécurité avant tout",
        "built_with": "Construit avec l'API Claude",
    },
    "Arabic": {
        "title": "⚽ مساعد مدرب كرة القدم تحت 8 سنوات",
        "subtitle": "أنشئ تمارين وخطط تدريبية ممتعة وآمنة ومناسبة للأطفال من عمر 6 إلى 8 سنوات.",
        "settings": "الإعدادات",
        "language_label": "لغة الإخراج:",
        "mode_label": "ماذا تريد أن تنشئ؟",
        "mode_drill": "تمرين واحد",
        "mode_session": "خطة تدريب كاملة",
        "drill_header": "🎯 إنشاء تمرين واحد",
        "drill_instruction": "صف التمرين الذي تريد إنشاءه. سيقوم الذكاء الاصطناعي بإنشاء تمرين كامل ومناسب للأطفال تحت 8 سنوات.",
        "drill_label": "صف فكرة التمرين:",
        "drill_placeholder": "مثال: لعبة مراوغة ممتعة حيث يتظاهر الأطفال بأنهم قراصنة يحمون كنزهم",
        "drill_button": "إنشاء التمرين",
        "drill_spinner": "جاري إنشاء التمرين...",
        "drill_success": "تم إنشاء التمرين!",
        "drill_warning": "الرجاء وصف فكرة التمرين.",
        "session_header": "📋 إنشاء خطة تدريب كاملة",
        "session_instruction": "أدخل موضوعًا لجلستك التدريبية. سيقوم الذكاء الاصطناعي بإنشاء خطة تدريب كاملة ومنظمة.",
        "session_label": "موضوع الجلسة:",
        "session_placeholder": "مثال: المراوغة والالتفاف",
        "session_duration": "مدة الجلسة (بالدقائق):",
        "session_button": "إنشاء خطة التدريب",
        "session_spinner": "جاري إنشاء خطة التدريب...",
        "session_success": "تم إنشاء خطة التدريب!",
        "session_warning": "الرجاء إدخال موضوع الجلسة.",
        "about_title": "حول هذه الأداة",
        "about_text": "هذه الأداة مصممة لمدربي كرة القدم تحت 8 سنوات الذين يبحثون عن أفكار تدريبية ممتعة وآمنة ومناسبة للعمر.",
        "principles_title": "المبادئ:",
        "principle_1": "المرح هو الأولوية",
        "principle_2": "كل طفل يشارك بنشاط",
        "principle_3": "ألعاب بعدد لاعبين قليل",
        "principle_4": "لغة بسيطة",
        "principle_5": "السلامة أولاً",
        "built_with": "مبني باستخدام واجهة Claude API",
    }
}

# ============================================================
# SIDEBAR
# ============================================================

language = st.sidebar.selectbox(
    "Output Language / Langue de sortie / لغة الإخراج:",
    ["English", "French", "Arabic"]
)

# Get the translation dictionary for the selected language
t = TRANSLATIONS[language]

# Set page direction for Arabic (right-to-left)
if language == "Arabic":
    st.markdown("""
    <style>
    .stApp {
        direction: rtl;
        text-align: right;
    }
    .stSidebar {
        direction: rtl;
        text-align: right;
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.header(t["settings"])

mode = st.sidebar.radio(
    t["mode_label"],
    [t["mode_drill"], t["mode_session"]]
)

# ============================================================
# MAIN CONTENT
# ============================================================

st.title(t["title"])
st.write(t["subtitle"])

# --- SINGLE DRILL MODE ---
if mode == t["mode_drill"]:
    st.subheader(t["drill_header"])
    st.write(t["drill_instruction"])
    
    drill_description = st.text_area(
        t["drill_label"],
        placeholder=t["drill_placeholder"],
        height=150
    )
    
    if st.button(t["drill_button"]):
        if drill_description:
            with st.spinner(t["drill_spinner"]):
                result = generate_drill(drill_description, language)
            st.success(t["drill_success"])
            st.markdown(result)
        else:
            st.warning(t["drill_warning"])

# --- FULL SESSION MODE ---
elif mode == t["mode_session"]:
    st.subheader(t["session_header"])
    st.write(t["session_instruction"])
    
    session_theme = st.text_input(
        t["session_label"],
        placeholder=t["session_placeholder"]
    )
    
    duration = st.slider(
        t["session_duration"],
        min_value=30,
        max_value=90,
        value=60,
        step=5
    )
    
    if st.button(t["session_button"]):
        if session_theme:
            with st.spinner(t["session_spinner"]):
                result = generate_session(session_theme, duration, language)
            st.success(t["session_success"])
            st.markdown(result)
        else:
            st.warning(t["session_warning"])

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")
st.markdown(f"""
### {t["about_title"]}
{t["about_text"]}

**{t["principles_title"]}**
- {t["principle_1"]}
- {t["principle_2"]}
- {t["principle_3"]}
- {t["principle_4"]}
- {t["principle_5"]}

*{t["built_with"]}*
""")