# AI Audio Analysis: "Widziałem dzisiaj Twój głos"

Analiza i badanie sygnałów audio z datasetu **LJ Speech** przy użyciu Pythona (`librosa`, `matplotlib`, `numpy`).

---

# Analiza spektrogramu sygnału mowy

## 1. Co można wywnioskować z dźwięku na podstawie spektrogramu?

Spektrogram pokazuje, jak energia sygnału rozkłada się w czasie i w różnych zakresach częstotliwości.

Na jego podstawie można zaobserwować między innymi:

- **Strukturę harmoniczną** – charakterystyczną dla dźwięków dźwięcznych, takich jak samogłoski.
- **Formanty (F1, F2, F3)** – pasma częstotliwości związane z artykulacją samogłosek.
- **Spółgłoski bezdźwięczne** – często widoczne jako szum o szerokim zakresie częstotliwości.
- **Zwarcia i wybuchy spółgłosek zwarto-wybuchowych** – mogą być widoczne jako krótkie, pionowe struktury o dużej energii.
- **Intonację i rytm wypowiedzi** – można obserwować zmiany wysokości tonu podstawowego oraz przerwy między fragmentami mowy.

## 2. Jakie informacje są widoczne, a jakich nie można wiarygodnie odczytać?

Spektrogram pozwala zaobserwować:

- rozkład energii w czasie i częstotliwości,
- strukturę i długość poszczególnych fragmentów wypowiedzi,
- obecność przerw i zmian energii,
- część cech artykulacyjnych, np. formanty i charakterystyczne pasma szumowe,
- zmiany wysokości tonu podstawowego w dźwiękach dźwięcznych.

Nie pozwala jednak bezpośrednio i wiarygodnie odczytać:

- dokładnej treści wypowiedzi,
- fazy sygnału na podstawie samego wykresu amplitudy spektrogramu,
- wszystkich szczegółów artykulacyjnych,
- emocji i intencji mówiącego,
- dokładnych warunków nagrania, takich jak rodzaj mikrofonu czy pomieszczenie.

Spektrogram jest więc użytecznym narzędziem analizy, ale nie przedstawia wszystkich informacji zawartych w oryginalnym sygnale.

## 3. Które cechy sygnału są najważniejsze dla rozpoznawania i odtwarzania mowy?

Istotne są przede wszystkim:

- **Formanty (F1, F2, F3)** – dostarczają informacji o artykulacji samogłosek.
- **Ton podstawowy (F0)** – odpowiada za wysokość głosu i jest ważny dla intonacji oraz naturalności mowy.
- **Struktura czasowa** – długość głosek, sylab i przerw wpływa na zrozumiałość wypowiedzi.
- **Charakterystyka widmowa spółgłosek** – szczególnie ważna dla rozróżniania głosek szczelinowych i syczących.
- **Energia sygnału** – pomaga rozróżniać fragmenty wypowiedzi i ciszę.

Znaczenie poszczególnych cech zależy od analizowanego dźwięku i rodzaju zadania. Inne informacje mogą być najważniejsze dla rozpoznawania słów, a inne dla wiernego odtwarzania głosu.

## 4. Co można usuwać ze spektrogramu, a jakie informacje powinny pozostać najdłużej?

Informacje można usuwać stopniowo, obserwując wpływ zmian na zrozumiałość i jakość odtwarzanego dźwięku.

W pierwszej kolejności można sprawdzić wpływ ograniczenia bardzo wysokich częstotliwości oraz szczegółów, które mają mniejsze znaczenie dla danego fragmentu sygnału.

Nie należy jednak zakładać, że pasmo powyżej 7–8 kHz jest całkowicie zbędne. Zawiera ono między innymi energię niektórych spółgłosek szczelinowych i syczących, która może być istotna dla rozróżniania fonemów.

Informacje, których utrata może być szczególnie zauważalna, to:

- formanty, ważne dla rozpoznawania samogłosek,
- charakterystyczne składowe widmowe spółgłosek,
- struktura czasowa i długość poszczególnych dźwięków,
- ton podstawowy, ważny dla zachowania intonacji i naturalności głosu.

Nie oznacza to, że utrata jednej z tych cech zawsze uniemożliwi rozpoznanie mowy. Wpływ usunięcia poszczególnych informacji należy oceniać eksperymentalnie.

## 5. Jak sprawdzić, czy postawione hipotezy są poprawne?

Można przygotować kilka zmodyfikowanych wersji tego samego nagrania, stopniowo ograniczając wybrane zakresy częstotliwości lub usuwając określone informacje ze spektrogramu.

Następnie można:

1. Odsłuchać oryginalne i zmodyfikowane nagrania.
2. Porównać ich zrozumiałość i jakość.
3. Sprawdzić, czy system rozpoznawania mowy poprawnie rozpoznaje wypowiedziane słowa.
4. Porównać wyniki dla różnych wariantów sygnału.

Do oceny można wykorzystać między innymi:

- **WER (Word Error Rate)** – do porównania błędów rozpoznawania słów,
- **STOI** – do oceny zrozumiałości mowy,
- **PESQ** – do oceny jakości sygnału mowy.

Takie porównanie pozwoli sprawdzić, które informacje można ograniczyć przy niewielkiej utracie jakości, a które są istotne dla rozpoznawania i odtwarzania mowy.
