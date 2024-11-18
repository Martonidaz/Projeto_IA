# Pacote de implementação de máquina preditiva
import streamlit as st

# NLTK - Natural Language Tool Kit
import nltk

# Fase 1
# Título do sistema
st.write("# Análise de satisfação do cliente")

# Entrada de dados do usuário - manisfestação do cliente
user_input = st.text_input("Por favor avalie nosso atendimento : ")

# Fase 2 
# Criação da Máquina Preditiva de satisfação do cliente

# Metodologia Vader utilizada e com isso baixar o vocabulário
nltk.download('vader_lexicon')

# Para usar o analisador de sentimento
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# MP
satisfacao = SentimentIntensityAnalyzer()

# Predição ou resultado da satisfação função para avaliar o tipo do sentimento do usuário
score = satisfacao.polarity_scores(user_input)

# Refinamento

if score == 0:
    st.write('Análise neutra')
elif score['neg'] != 0:
    st.write("Análise Negativa")
elif score['pos'] != 0:
    st.write('Análise Posiitiva')

    

