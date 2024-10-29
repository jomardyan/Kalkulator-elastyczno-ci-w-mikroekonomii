Oczywiście, oto wersja README.md w języku polskim:

# Kalkulator Wartości Ekonomicznych

Kalkulator Wartości Ekonomicznych to aplikacja desktopowa zbudowana przy użyciu Pythona i biblioteki GUI Tkinter. Oferuje ona narzędzia do obliczania różnych rodzajów elastyczności ekonomicznej, w tym:

- Elastyczność cenowa popytu
- Elastyczność dochodowa popytu
- Elastyczność cenowa krzyżowa popytu

Aplikacja zawiera również funkcję monitorowania bieżącego kursu wymiany, umożliwiając użytkownikom śledzenie aktualnego kursu USD/PLN.

## Funkcje

1. **Kalkulator elastyczności cenowej popytu**: Oblicza elastyczność cenową popytu na podstawie danych wejściowych dotyczących początkowej i końcowej ceny oraz ilości.
2. **Kalkulator elastyczności dochodowej popytu**: Oblicza elastyczność dochodową popytu na podstawie danych wejściowych dotyczących początkowego i końcowego dochodu oraz ilości.
3. **Kalkulator elastyczności cenowej krzyżowej popytu**: Oblicza elastyczność cenową krzyżową popytu na podstawie danych wejściowych dotyczących początkowej i końcowej ceny jednego produktu oraz ilości innego powiązanego produktu.
4. **Monitorowanie kursu wymiany**: Wyświetla bieżący kurs USD/PLN i udostępnia przycisk do ręcznego odświeżenia kursu.
5. **Śledzenie historii**: Prowadzi historię poprzednich obliczeń, umożliwiając użytkownikom przeglądanie poprzednich wyników.

![alt text](https://github.com/jomardyan/Kalkulator-elastyczno-ci-w-mikroekonomii/blob/main/mainwindow.png?raw=true)


## Instalacja

Aby korzystać z Kalkulatora Wartości Ekonomicznych, musisz mieć zainstalowanego Pythona 3 na swoim systemie. Następnie możesz zainstalować wymagane zależności, uruchamiając następujące polecenie w terminalu:

```
pip install -r requirements.txt
```

## Użytkowanie

1. Uruchom skrypt `kalkulator_wartosci_ekonomicznych.py`, aby uruchomić aplikację.
2. Wprowadź niezbędne dane wejściowe w odpowiednich polach.
3. Kliknij odpowiedni przycisk, aby obliczyć żądaną miarę elastyczności.
4. Wynik zostanie wyświetlony, a obliczenie zostanie dodane do historii.
5. Możesz odświeżyć kurs USD/PLN, klikając przycisk "Odśwież kurs".

## Współpraca

Jeśli znajdziesz jakiekolwiek problemy lub masz sugestie dotyczące ulepszeń, możesz przesłać żądanie ściągnięcia lub otworzyć zgłoszenie na [repozytorium GitHub](https://github.com/jomardyan/Kalkulator-elastyczno-ci-w-mikroekonomii/).

## Licencja

Ten projekt jest objęty licencją [MIT License](LICENSE).
