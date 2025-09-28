from imports import TfidfVectorizer,cosine_similarity,nltk,word_tokenize,stopwords,SentimentIntensityAnalyzer,WordNetLemmatizer,fitz,st
def processing(text):#filter the text 
    lemment=WordNetLemmatizer()
    token=word_tokenize(text.lower())
    stopword=set(stopwords.words('english')) # set of stop words in english language
    filter=[lemment.lemmatize(word) for word in token if word.isalnum() and word not in stopword]
    return ' '.join(filter) #return the filtered output


def sentiment(inp):
    sen=SentimentIntensityAnalyzer()
    score=sen.polarity_scores(inp)
    return score


def vector(txt):
    vector=TfidfVectorizer()
    cleaned=vector.fit_transform(txt)
    return cleaned


def similar(input):
    sim=cosine_similarity(input)
    similarity_score=sim[0][1]
    return similarity_score


def describe_similarity(sim):
    if sim>0.7:
        st.markdown('<span style="background-color:red; color:white; padding:3px; border-radius:5px;">HIGH SIMILARITY DETECTED !!!</span>', unsafe_allow_html=True)
    elif sim<0.3:
        st.markdown(f'<span style="background-color:green; color:white; padding:3px; border-radius:5px;">SAFE !! NO COPY DETECTED</span>', unsafe_allow_html=True)
    else:
        st.markdown(f'<span style="background-color:orange; color:black; padding:3px; border-radius:5px;">MODERATE SIMILARITY DETECTED!!!</span>', unsafe_allow_html=True)


def describe_sentiment(text,score):
    if len(text.split())<=3 and -0.1<score['compound']<0.1:
        st.markdown(f'<span style="background-color:gray; color:white; padding:5px 10px; border-radius:10px;">Overall sentiment of First Input:😐 Neutral</span>', unsafe_allow_html=True)
    elif score['compound']>=0.05:
        st.markdown(f'<span style="background-color:green; color:white; padding:5px 10px; border-radius:10px;">Overall sentiment of First Input:😀 Positive</span>', unsafe_allow_html=True)
    elif score['compound']<0.05:
        st.markdown(f'<span style="background-color:red; color:white; padding:5px 10px; border-radius:10px;">Overall sentiment of First Input:😡 Negative</span>', unsafe_allow_html=True)
    else:
        st.markdown(f'<span style="background-color:gray; color:white; padding:5px 10px; border-radius:10px;">Overall sentiment of First Input:😐 Neutral</span>', unsafe_allow_html=True)


def describe_sentiment2(text,score):
    if len(text.split())<=3 and -0.1<score['compound']<0.1:
        st.markdown(f'<span style="background-color:gray; color:white; padding:5px 10px; border-radius:10px;">Overall sentiment of Second Input:😐 Neutral</span>', unsafe_allow_html=True)
    elif score['compound']>=0.05:
        st.markdown(f'<span style="background-color:green; color:white; padding:5px 10px; border-radius:10px;">Overall sentiment of Second Input:😀 Positive</span>', unsafe_allow_html=True)
    elif score['compound']<0.05:
        st.markdown(f'<span style="background-color:red; color:white; padding:5px 10px; border-radius:10px;">Overall sentiment of Second Input:😡 Negative</span>', unsafe_allow_html=True)
    else:
        st.markdown(f'<span style="background-color:gray; color:white; padding:5px 10px; border-radius:10px;">Overall sentiment of Second Input:😐 Neutral</span>', unsafe_allow_html=True)


def extract_text(temp_input):
    text=""
    pdf=fitz.open(stream=temp_input.read(),filetype="pdf")
    for page in pdf:
        text+=page.get_text()+" "
    pdf.close()
    return text.strip()


def sidebar_feat():
    st.sidebar.markdown(
    """
    <style>
    [data-testid="stSidebar"] button:hover {
        background-color: #00ffcc !important;
        color: black !important;
        transform: scale(1.05);
        transition: all 0.2s ease-in-out;
    }
    </style>
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1f1f2e, #2e2e3e);
        color: white;
        border-right: 2px solid #00ffcc;
    }
    </style>
    """,
    
    unsafe_allow_html=True
)
    
def home_feat():
    st.markdown("<h1 style='text-align: center; color: #00ffcc;'>📄 Plagiarism Detector</h1>", unsafe_allow_html=True)
    
    st.markdown("---")  
    
    st.markdown("""
    <div style='background-color:#2e2e3e; padding: 15px; border-radius: 10px;'>
    <h3 style='color:#ffffff;'>Welcome!</h3>
    <p style='color:#cccccc;'>This tool allows you to compare two documents — either <b>text</b> or <b>PDF</b> — to check for similarity.</p>
    
    <h4 style='color:#00ffcc;'>Features:</h4>
    <ul style='color:#cccccc;'>
        <li>Compare text or PDF files for plagiarism.</li>
        <li>Get a similarity score (%) between the two documents.</li>
        <li>Basic sentiment analysis of your inputs.</li>
        <li>Easy-to-use interface — just upload or type your documents.</li>
        <li>Perfect for academic projects and learning purposes.</li>
    </ul>
    
    <p style='color:#ffcc00;'>Use the sidebar to navigate and get started! Select <b>Plagiarism Detector</b> to compare documents, or <b>How to Use</b> for instructions.</p>
    </div>
    """, unsafe_allow_html=True)


def how_feat():
    st.markdown("<h1 style='text-align:center; color:#00ffcc;'>📖 How to Use</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    steps = [
        "1️⃣ Select **Plagiarism Detector** from the sidebar.",
        "2️⃣ Choose input format: **Text** or **PDF**.",
        "3️⃣ Enter or upload the documents you want to compare.",
        "4️⃣ Click to process and view similarity score.",
        "5️⃣ Optional: Check sentiment analysis of each document."
    ]
    
    for step in steps:
        st.markdown(f"<div style='background-color:#1f1f2e; padding:10px; border-radius:10px; margin-bottom:10px; color:#ffffff;'>{step}</div>", unsafe_allow_html=True)


def og_feat():
    st.markdown("<h1 style='text-align:center; color:#00ffcc;'>📝 Plagiarism Detection</h1>", unsafe_allow_html=True)
    st.markdown("---")