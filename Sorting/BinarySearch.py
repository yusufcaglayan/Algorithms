arr = [1, 2, 3, 4, 5, 6, 7, 8]

def binarySearch(arr, hedef):
    ilk = 0
    son = len(arr) - 1

    while ilk <= son:
        orta = (ilk + son) // 2  # Orta indeks tam sayı bölme ile bulunur
        tahmin = arr[orta]

        if tahmin == hedef:  # Hedef bulundu
            return orta
        elif tahmin < hedef:  # Hedef sağ yarıda
            ilk = orta + 1
        else:  # Hedef sol yarıda
            son = orta - 1

    return -1  # Hedef bulunamadı

# Örnek Kullanım
result = binarySearch(arr, 7)
if result != -1:
    print(f"Hedef 7, indeks {result} konumunda bulundu.")
else:
    print("Hedef 7 listede bulunamadı.")
