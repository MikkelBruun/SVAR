# Uge 4

## Data

Jeg brugte `faker` til at generere personer. Den primære interesse er deres inkomst, som bliver genereret i `genIncome()`.
Udover at skrive til filer, tilføjede jeg muligheden for at behandle dataen direkte, således at man kan simulere arbitrært store datasæt. (og potentielt kan slippe for at skulle generere de store filer)

## Analyse

Jeg blev fascineret af problemstillingen: "Hvis ikke man kender længden på et dataseæt, an man så finde median?". 
Det er potentielt umuligt at få et helt præcist svar, men der findes [metoder](https://stackoverflow.com/questions/10657503/find-running-median-from-a-stream-of-integers). Jeg valgte at bruge en datastruktur bestående af to heaps (en `dualHeap` i `runningMedian.py`), som bliver "trimmet" når de vokser sig for store.

## Resultater

Kør `main.py profile=[0|1|2|3|4|5]`, (eller `main.py profile=` for at få præsenteret mulighederne) for at gennemgå et par eksempler.
Fra profiling tests fandt jeg frem til et par optimeringer på den tungeste databehandling (heapens insert og balance funktioner).
Det blev dog klart at det meste tid enten blev brugt på at læse fra disken, eller generere data. En potentiel optimering kunne være at multithreade det således at læsning og behandling foregik sideløbende.
