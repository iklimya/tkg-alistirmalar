# Hafta 3: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest -v

import pytest

from alistirma import kargo_ucreti, bilet_fiyat, ortalama


def test_kargo_buyuk_sipariste_ucretsiz():
    assert kargo_ucreti(800) == 0
# kargo_ucreti
def test_kargo_kucuk_siparis():
    assert kargo_ucreti(100) == 50

def test_kargo_tam_sinir():
    assert kargo_ucreti(500) == 0

def test_kargo_sinirin_bir_alti():
    assert kargo_ucreti(499) == 50

def test_kargo_sinirin_bir_ustu():
    assert kargo_ucreti(501) == 0

def test_kargo_sifir_tutar():
    assert kargo_ucreti(0) == 50

def test_kargo_negatif_hata():
    with pytest.raises(ValueError):
        kargo_ucreti(-1)


# bilet_fiyati
def test_bilet_sifir_yas():
    assert bilet_fiyati(0) == 0

def test_bilet_6_yas():
    assert bilet_fiyati(6) == 0

def test_bilet_7_yas():
    assert bilet_fiyati(7) == 50

def test_bilet_17_yas():
    assert bilet_fiyati(17) == 50

def test_bilet_18_yas():
    assert bilet_fiyati(18) == 100

def test_bilet_64_yas():
    assert bilet_fiyati(64) == 100

def test_bilet_65_yas():
    assert bilet_fiyati(65) == 60

def test_bilet_yasli():
    assert bilet_fiyati(90) == 60

def test_bilet_negatif_hata():
    with pytest.raises(ValueError):
        bilet_fiyati(-1)


# ortalama
def test_ortalama_normal():
    assert ortalama([70, 85]) == 77.5

def test_ortalama_tek_eleman():
    assert ortalama([100]) == 100

def test_ortalama_sifirlar():
    assert ortalama([0, 0, 0]) == 0

def test_ortalama_bos_liste_hata():
    with pytest.raises(ValueError):
        ortalama([])
