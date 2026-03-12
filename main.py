import time
import sys
import random

# ==========================================
# OYUNCU DURUMU (GLOBAL STATE)
# ==========================================
# Burası oyunun kalbidir. Takım olarak oyuncunun hangi özelliklere
# sahip olacağına siz karar verin. İsterseniz 'büyü_gücü', 'açlık'
# veya 'karma' gibi yeni değişkenler eklemekte tamamen özgürsünüz!
oyuncu = {
    "isim": "Bilinmeyen Kahraman",
    "can": 100,
    "enerji": 50,
    "envanter": [],
    "ozel_durumlar": []  # Örn: 'zehirlendi', 'görünmez' gibi durumlar için
}


# ==========================================
# ORTAK YARDIMCI FONKSİYONLAR (UTILITIES)
# ==========================================
def yavas_yazdir(metin, bekleme=0.02):
    """Metni daktilo efektiyle ekrana yazdırır. Atmosfer için kullanabilirsiniz."""
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekleme)
    print("")


def durum_goster():
    """Oyuncunun anlık istatistiklerini ve çantasını ekrana estetik bir şekilde basar."""
    # TODO: Takımınızın tarzına uygun bir durum ekranı tasarlayın.
    pass


# ==========================================
# 1. KİŞİNİN GÖREV ALANI: EVRENİN İNŞASI VE GİRİŞ
# ==========================================
def karakter_ve_evren_olustur(durum):
    """
    Oyunun evrenini tanıtın. Oyuncudan isim veya özellik alın.
    Burası bilimkurgu da olabilir, fantastik bir çağ da, modern bir gerilim de...
    """
    # TODO: Oyuncuyu atmosfere sokacak diyalogları ve başlangıç seçimlerini yazın.
    pass


def ilk_karsilasma_ve_secim(durum):
    """
    Oyuncunun karşısına çıkan İLK büyük olay veya engel.
    Bu bir karakterle konuşma, aşılması gereken fiziksel bir engel veya
    kritik bir karar anı olabilir. Seçimlere göre envanteri veya canı güncelleyin.
    """
    # TODO: Yaratıcılığınızı konuşturun. Oyuncunun kararı 2. bölümü nasıl etkileyecek?
    pass


def bolum_1_ana_akim(durum):
    """1. Bölümü yöneten ana fonksiyon. 2. bölüme geçiş durumunu döndürmelidir."""
    karakter_ve_evren_olustur(durum)
    basari_durumu = ilk_karsilasma_ve_secim(durum)

    # İsterseniz oyuncu ilk bölümde bile ölebilir/kaybedebilir.
    # Eğer devam etmeye hak kazandıysa True veya gidilecek mekanın adını döndürün.
    return True


# ==========================================
# 2. KİŞİNİN GÖREV ALANI: HİKAYENİN GELİŞMESİ VE RİSKLER
# ==========================================
def ana_macera_dongusu(durum):
    """
    Hikayenin en geniş kısmı. Oyuncu burada keşif yapmalı, kararlar almalı ve
    risklerle yüzleşmelidir. İsterseniz rastgele olaylar (random modülü ile)
    ekleyebilir, isterseniz tamamen hikaye odaklı derin diyaloglar yazabilirsiniz.
    """
    # TODO: Oyuncunun can, enerji ve envanterini sürekli kontrol ederek
    # kararlarına göre bu değerleri manipüle eden olaylar zinciri tasarlayın.
    pass


def kritik_engel(durum):
    """
    Finale geçmeden hemen önce oyuncunun aşması gereken zorlu bir eşik.
    Oyuncunun 1. bölümde veya bu bölümde çantasında topladığı eşyalar
    burada hayat kurtarabilir.
    """
    # TODO: Bu engeli geçip geçemediğine dair bir mantık kurun ve sonucu döndürün.
    pass


def bolum_2_ana_akim(durum):
    """2. Bölümü yöneten ana fonksiyon."""
    ana_macera_dongusu(durum)
    engel_asildi_mi = kritik_engel(durum)
    return engel_asildi_mi


# ==========================================
# 3. KİŞİNİN GÖREV ALANI: ZİRVE NOKTASI VE SONUÇLAR
# ==========================================
def final_yuzlesmesi(durum):
    """
    Hikayenin zirvesi. Bu bir düşmanla savaş, çözülmesi gereken devasa bir sistem
    veya duygusal bir seçim anı olabilir. Her şey oyuncunun geçmiş kararlarına bağlı!
    """
    # TODO: İhtişamlı bir final tasarlayın. Envanteri ve can durumunu son kez test edin.
    pass


def sonlari_belirle(durum, final_basarisi):
    """
    Oyunun birden fazla sonu olabilir. Sadece 'Kazanma' ve 'Kaybetme' değil,
    'Eksik Kazanma' veya 'Sırrı Çözerek Kazanma' gibi alternatif sonlar yazın.
    """
    # TODO: if/elif/else yapılarıyla farklı senaryo kapanışları kodlayın.
    pass


def bolum_3_ana_akim(durum):
    """3. Bölümü ve oyunun sonunu yöneten ana fonksiyon."""
    yavas_yazdir("\n--- FİNAL BÖLÜMÜ ---")
    final_sonucu = final_yuzlesmesi(durum)
    sonlari_belirle(durum, final_sonucu)


# ==========================================
# ANA KONTROL MERKEZİ (MAIN FLOW)
# ==========================================
def oyun_motoru():
    """Tüm bölümlerin birbirine bağlandığı ana sistem. BURAYI DİKKATLİ DÜZENLEYİN."""

    yavas_yazdir("OYUN BAŞLIYOR...\n")

    # 1. BÖLÜM
    devam_edebilir_mi = bolum_1_ana_akim(oyuncu)
    if not devam_edebilir_mi:
        yavas_yazdir("Hikayen çok erken sona erdi...")
        return

    # 2. BÖLÜM
    yavas_yazdir("\n--- YENİ BİR AŞAMA ---")
    finale_gidebilir_mi = bolum_2_ana_akim(oyuncu)

    # 2. bölüm sonunda can kontrolü (Güvenlik önlemi)
    if oyuncu["can"] <= 0:
        yavas_yazdir("Aldığın yaralar seni alt etti. Oyun Bitti.")
        return

    if not finale_gidebilir_mi:
        yavas_yazdir("Karşılaştığın engeli aşamadın. Yolculuğun burada bitiyor.")
        return

    # 3. BÖLÜM
    bolum_3_ana_akim(oyuncu)


# ==========================================
# BAŞLATICI
# ==========================================
if __name__ == "__main__":
    oyun_motoru()