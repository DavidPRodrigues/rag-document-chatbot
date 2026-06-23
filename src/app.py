import streamlit as st
from generate_answer import generate_answer

st.set_page_config(
    page_title="RAG Document Search",
    page_icon = "📄",
    layout = "wide"
)

st.title('RAG Document Search')
st.write('Ask a question and retrieve the most relevant document chunks :)')

query = st.text_input('ask a question about your document:')

k = st.slider('Number of chunks to retrieve', 
              min_value=1, 
              max_value=5, 
              value=3
              )

if st.button('Generate Answer'):
    if not query.strip():
        st.warning('please enter a question.')
    else:
        with st.spinner('searching document and generating answer...'):
            answer, docs = generate_answer(query, k=k)


            st.subheader('answer')
            st.write(answer)

            with st.expander('show retrived source chunks:'):
                for i, doc in enumerate(docs, start=1):
                    st.markdown(f"### Source {i}")
                    st.write(doc.page_content)
                    st.caption(f"Metadata: {doc.metadata}")