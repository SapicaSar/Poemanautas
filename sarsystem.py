import requests
from bs4 import BeautifulSoup
import nltk
import random
import time
import threading
import re
from colorama import Fore, Style, init

# Inicializar colorama para compatibilidad en distintos entornos
init(autoreset=True)

# Descargar recursos de NLTK
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# Configuración
BASE_URL = "https://lapoema.tumblr.com/page/"
NUM_PAGES = 113
scraped_texts = []

# Función para extraer y limpiar texto
def scrape_text(page):
    url = f"{BASE_URL}{page}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        return '\n'.join(paragraphs)
    return ""

# Multi-threading para extracción eficiente
def multi_thread_scrape():
    threads = []
    for i in range(1, NUM_PAGES + 1):
        thread = threading.Thread(target=lambda p: scraped_texts.append(scrape_text(p)), args=(i,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

# Procesamiento avanzado del texto
def process_text(text):
    text = re.sub(r'[^\w\s]', '', text)  # Eliminación de puntuación
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('spanish'))
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return filtered_tokens

# Generación de estructuras semánticas
def semantic_blockchain(texts):
    blockchain = []
    previous_hash = "0000"
    for text in texts:
        structured_text = ' '.join(text)
        block = {
            "text": structured_text,
            "hash": hash(structured_text + previous_hash)
        }
        blockchain.append(block)
        previous_hash = str(block["hash"])
    return blockchain

# Efecto máquina de escribir mejorado
def typewriter_effect(text, color=Style.RESET_ALL):
    print(color, end='')
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(0.01, 0.02))
    print(Style.RESET_ALL + "\n")

# Generador semántico recombinatorio con ensueños
def infinite_generator():
    multi_thread_scrape()
    processed_texts = [process_text(text) for text in scraped_texts if text]
    blockchain = semantic_blockchain(processed_texts)
    
    while True:
        selected = random.choice(blockchain)["text"]
        words = selected.split()
        random.shuffle(words)
        
        # Construcción de sintaxis vanguardista con ritmo literario
        paragraph = []
        sentence = []
        sentence_length = random.randint(4, 20)
        
        for word in words:
            sentence.append(word)
            if len(sentence) >= sentence_length:
                paragraph.append(' '.join(sentence).capitalize() + random.choice([".", "...", "—", "!"]))
                sentence = []
                sentence_length = random.randint(4, 20)
        
        if sentence:
            paragraph.append(' '.join(sentence).capitalize() + random.choice([".", "...", "—", "!"]))
        
        formatted_text = '\n\n'.join(paragraph)
        
        # Inserción de ensoñaciones en otro color aleatoriamente
        if random.random() < 0.2:  # 20% de probabilidades de ensoñación
            typewriter_effect(formatted_text, color=Fore.CYAN)
        else:
            typewriter_effect(formatted_text, color=Style.RESET_ALL)
        
        time.sleep(2)

if __name__ == "__main__":
    infinite_generator()
