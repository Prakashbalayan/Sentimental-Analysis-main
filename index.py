import streamlit as st
import pandas as pd

# Title of the app
st.title("ChatGPT Review Sentiment Analyzer")

# Upload CSV file
uploaded_file = st.file_uploader("Upload ChatGPT Reviews CSV", type=["csv"])

if uploaded_file:
    # Load the dataset
    df = pd.read_csv(uploaded_file)

    # Function to classify sentiment based on rating
    def classify_sentiment(rating):
        try:
            rating = float(rating)
            if rating >= 4:
                return 'positive'
            elif rating == 3:
                return 'neutral'
            else:
                return 'negative'
        except:
            return 'unknown'

    # Apply sentiment classification
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    df['sentiment'] = df['rating'].apply(classify_sentiment)

    # Display the data
    st.subheader("Sample Data with Sentiment")
    st.dataframe(df[['review', 'rating', 'sentiment']].head())

    # Sentiment Distribution
    st.subheader("Sentiment Distribution")
    sentiment_counts = df['sentiment'].value_counts()
    st.bar_chart(sentiment_counts)

    # Downloadable CSV
    st.subheader("Download Updated CSV")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV with Sentiment",
        data=csv,
        file_name='chatgpt_reviews_with_sentiment.csv',
        mime='text/csv',
    )
