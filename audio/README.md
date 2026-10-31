# AI Audio Analysis: "Widziałem dzisiaj Twój głos"

Analiza i badanie sygnałów audio z datasetu **LJ Speech** przy użyciu Pythona (`librosa`, `matplotlib`, `numpy`).

---

##  Analiza spektrogramu i odpowiedzi na pytania badawcze

### 1. Co można wywnioskować o znajdującym się tam dźwięku ze spektrogramu?
* **Źródło dźwięku:** Wyraźnie widoczna struktura harmoniczna (równoległe poziome pasma) wskazuje na obecność ludzkiego głosu (lub instrumentu muzycznego), a nie zwykłego szumu białego.
* **Typy dźwięków:**
  * **Samogłoski:** Charakteryzują się jasnymi, gęstymi pasmami formantowymi o dużej energii.
  * **Spółgłoski:** Spółgłoski bezdźwięczne (np. [s], [sh]) wyglądają jak wysokoczęstotliwościowe strefy szumowe, a zwarte/wybuchowe ([p], [t]) — jak krótkie, pionowe impulsy.
* **Intonacja i rytm:** Zmiana wysokości tonu podstawowego ($F_0$) odzwierciedla się w postaci falistego wygięcia harmonik. Pauzy między słowami widoczne są jako pionowe przerwy o zerowej lub minimalnej energii.

---

### 2. Jakie informacje są widoczne, a jakich nie da się wiarygodnie odczytać?
* **Informacje widoczne:**
  * Rozkład energii sygnału w funkcji częstotliwości i czasu.
  * Tempo mowy, czas trwania sylab oraz struktura pauz.
  * Kontur melodyczny wypowiedzi (wznoszenie lub opadanie intonacji).
* **Informacje ukryte / Trudne do odczytania:**
  * **Dokładny tekst mowy:** Prawie niemożliwe jest "przeczytanie" dokładnego tekstu bezpośrednio ze spektrogramu bez specjalistycznego przygotowania, ze względu na indywidualne cechy artykulacji.
  * **Informacja o fazie:** Klasyczny spektrogram amplitudowy całkowicie ignoruje fazę fali akustycznej.
  * **Mikrodetale barwy głosu:** Drobne odcienie emocjonalne lub subtelne cechy akustyczne otoczenia/mikrofonu są często maskowane przez ogólne spektrum.

---

### 3. Najważniejsze cechy sygnału do rozpoznania lub odtworzenia
Przy przygotowywaniu danych dla modeli **TTS** (Text-to-Speech) lub **ASR** (Automatic Speech Recognition) kluczowe znaczenie mają:
1. **Formanty ($F_1, F_2, F_3$):** Częstotliwości rezonansowe traktu głosowego, które określają konkretne fonemy.
2. **Ton podstawowy ($F_0$):** Określa wysokość głosu, melodię oraz zabarwienie intonacyjne.
3. **Spektrogram Mel-skalowy (Mel-Spectrogram):** Reprezentacja częstotliwości w skali logarytmicznej, modelująca ludzką percepcję słuchową (wysoka szczegółowość niskich częstotliwości i mniejsza wysokich).

---

### 4. Stopniowe usuwanie informacji ze spektrogramu
* **Co może zniknąć bez większej straty (pierwszy etap):**
  * Wysokie częstotliwości powyżej 7–8 kHz (ludzka mowa pozostaje w pełni zrozumiała i czytelna).
  * Informacja o fazie oraz drobny szum kwantyzacji wysokich częstotliwości.
* **Co powinno zostać jak najdłużej (krytyczne):**
  * Trajektorie pierwszych formantów ($F_1, F_2$) oraz kontur tonu podstawowego ($F_0$). Bez nich mowa zamienia się w niezrozumiały szum lub metaliczny pomruk.
  * Synchronizacja czasowa pików energetycznych (czas trwania słów i pauz).

---

### 5. Jak sprawdzić, czy hipotezy są poprawne?
1. **Synteza powrotna (Resynthesis):** Modyfikacja spektrogramu w Pythonie i rekonstrukcja audio za pomocą **algorytmu Griffina-Lima** lub wokodera neuralnego (**HiFi-GAN**) w celu oceny słuchowej.
2. **Obiektywne metryki jakości:** Wykorzystanie metryk takich jak **PESQ** (Perceptual Evaluation of Speech Quality) oraz **STOI** (Short-Time Objective Intelligibility) do pomiaru degradacji sygnału.
3. **Testowanie ASR:** Przekazanie zmodyfikowanego audio na wejście modelu rozpoznawania mowy (np. Whisper) w celu zmierzenia wskaźnika błędów w transkrypcji (**WER — Word Error Rate**).