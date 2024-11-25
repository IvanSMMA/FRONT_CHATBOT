#La similitud coseno mide la semejanza entre dos vectores, comparando el ángulo entre ellos, en lugar de su magnitud.
#La similitud coseno es una métrica utilizada para medir la semejanza entre dos vectores en un espacio multidimensional,
# calculando el coseno del ángulo entre ellos. Su valor varía entre -1 y 1, donde 1 indica que los vectores son
# idénticos, 0 significa que son ortogonales (sin relación) y -1 indica que son completamente opuestos.
# Es muy utilizada en procesamiento de texto, como en modelos de bolsa de palabras y TF-IDF, y en visión por computadora
# para comparar descriptores de imágenes.
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


A = np.array([[0.9, 0.7, 0.5]])
B = np.array([[0.1, 0.2, 0.6]])


similarity = cosine_similarity(A, B)

print(similarity)
