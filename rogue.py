from rouge_score import rouge_scorer

def calcular_rouge_promedio(referencia, candidato):
    # Inicializar el calculador de ROUGE
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

    # Calcular las métricas
    scores = scorer.score(referencia, candidato)

    # Extraer las métricas de precisión, recall y F1 para ROUGE-1, ROUGE-2 y ROUGE-L
    metrics = {
        'ROUGE-1': scores['rouge1'],
        'ROUGE-2': scores['rouge2'],
        'ROUGE-L': scores['rougeL']
    }

    # Promediar precisión, recall y F1
    avg_precision = sum(metric.precision for metric in metrics.values()) / 3
    avg_recall = sum(metric.recall for metric in metrics.values()) / 3
    avg_f1 = sum(metric.fmeasure for metric in metrics.values()) / 3

    # Construir resultados
    resultados = {
        'ROUGE-1 Precision': metrics['ROUGE-1'].precision,
        'ROUGE-1 Recall': metrics['ROUGE-1'].recall,
        'ROUGE-1 F1': metrics['ROUGE-1'].fmeasure,
        'ROUGE-2 Precision': metrics['ROUGE-2'].precision,
        'ROUGE-2 Recall': metrics['ROUGE-2'].recall,
        'ROUGE-2 F1': metrics['ROUGE-2'].fmeasure,
        'ROUGE-L Precision': metrics['ROUGE-L'].precision,
        'ROUGE-L Recall': metrics['ROUGE-L'].recall,
        'ROUGE-L F1': metrics['ROUGE-L'].fmeasure,
        'Promedio Precision': avg_precision,
        'Promedio Recall': avg_recall,
        'Promedio F1': avg_f1
    }

    return resultados

if __name__ == "__main__":
    # Rutas a los archivos
    candidato_archivo = "candidato.txt"
    referencia_archivo = "referencia.txt"

    # Leer el contenido de los archivos
    with open(referencia_archivo, 'r', encoding='utf-8') as ref_file:
        referencia = ref_file.read().strip()

    with open(candidato_archivo, 'r', encoding='utf-8') as cand_file:
        candidato = cand_file.read().strip()

    # Calcular métricas ROUGE
    resultados = calcular_rouge_promedio(referencia, candidato)

    # Mostrar los resultados
    for key, value in resultados.items():
        print(f"{key}: {value:.4f}")
