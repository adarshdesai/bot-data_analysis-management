sudo pip install -r requirements.txt
sudo apt-get install python-pyaudio jackd2
sudo tar -xvf /home/bot-data_analysis-management/data/trans.csv.tar.gz
py_script="
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
"
python -c "$py_script"
