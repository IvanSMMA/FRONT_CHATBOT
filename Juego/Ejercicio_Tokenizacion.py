import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

nltk.download('punkt')
nltk.download('stopwords')

# Cargar df
df = pd.read_csv('df_total.csv', encoding='UTF-8')

# Función para tokenización y stemming
stemmer = SnowballStemmer('spanish')
def tokenize_and_stem(text):
    tokens = word_tokenize(text.lower())
    stems = [stemmer.stem(token) for token in tokens if token.isalpha()]
    return ' '.join(stems)

# Aplicar el stemming a las noticias
df['news_stemmer'] = df['news'].apply(tokenize_and_stem)

# Separar los datos
x_df = df['news_stemmer']
y_df = df['Type']

# Dividir los datos
x_train, x_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.2)

# Vectorización
vectorizer = CountVectorizer()
x_train_transformed = vectorizer.fit_transform(x_train)
x_test_transformed = vectorizer.transform(x_test)

# Modelo
model = MultinomialNB()
model.fit(x_train_transformed, y_train)

# Predicción y evaluación
y_pred = model.predict(x_test_transformed)
print(metrics.accuracy_score(y_test, y_pred))
