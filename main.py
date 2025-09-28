from functions import processing,sentiment,vector,similar,describe_similarity,describe_sentiment,describe_sentiment2,extract_text,sidebar_feat,home_feat,how_feat,og_feat
from imports import st
#sidebar
sidebar_feat()
input1=""
input2=""

if "page" not in st.session_state:
    st.session_state.page = "Home"
st.sidebar.title("Options")
if st.sidebar.button("Home"):
    st.session_state.page = "Home"

if st.sidebar.button("How to use"):
    st.session_state.page = "How"

if st.sidebar.button("Plagiarism Detector"):
    st.session_state.page = "og"



if st.session_state.page == "Home":
    home_feat()
elif st.session_state.page == "How":
    how_feat()
elif st.session_state.page == "og":
    og_feat()
    upload=st.radio("Enter format of input :",["Text","pdf"])
    
    if upload=="Text":
        input1=st.text_input("Enter the first text :")
        input2=st.text_input("Enter the second text :")
    elif upload=="pdf" :
        col1,col2=st.columns(2)
        with col1:
            temp_input1=st.file_uploader("Upload the first file :")
            if temp_input1:
                input1=extract_text(temp_input1)
                st.success(f"Uploaded Doc 1")
                with st.expander("Preview of First Input"):
                    st.text_area("Preview",input1,height=500)
        with col2:
            temp_input2=st.file_uploader("Upload second file :")
            if temp_input2:
                input2=extract_text(temp_input2)
                st.success("Uploaded Doc 2")
                with st.expander("Preview of Second Input"):
                    st.text_area("Preview",input2,height=500)
        
    if input1 and input2:
        run=st.button("Detect")
        if run:
            clean_input1=processing(input1)
            clean_input2=processing(input2)  

            text_matrix=vector([clean_input1,clean_input2])
            similarity=similar(text_matrix)
            sentiment_score=sentiment(input1)
            sentiment_score2=sentiment(input2)
            st.markdown("---")
            st.subheader("🔍 Results")
            st.markdown("<h4 background-color: #0000FF; color: white; padding: 5px 10px; border-radius: 5px;>Similarity Score<h4>",unsafe_allow_html=True)
            st.write(f"Similarity detected : {int(similarity*100)}% ")
            st.write(describe_similarity(similarity))
            st.markdown("<h4 background-color: #0000FF; color: white; padding: 5px 10px; border-radius: 5px;>Sentiment Analysis<h4>",unsafe_allow_html=True)
            st.write(f"Sentiment in First/Original input : {sentiment_score['compound']}")
            st.write(describe_sentiment(input1,sentiment_score))
            st.write(f"Sentiment in Second input : {sentiment_score2['compound']}")
            st.write(describe_sentiment2(input2,sentiment_score2))



