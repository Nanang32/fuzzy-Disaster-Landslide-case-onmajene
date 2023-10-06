# ! pip install -U scikit-fuzzy
# -- coding: utf-8 --
import numpy as np
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt


# Import pandas
import pandas as pd
df=pd.read_excel('/content/drive/MyDrive/tesisku/Datatraining.xlsx')
print(df.head())



# Variabel Longsor

curahHujan = np.arange(1500, 2301, 1)
ketinggian = np.arange(250, 1001, 1)
kemiringan = np.arange(0, 41, 1)
jarakJalan = np.arange(0, 401, 1)
penggunaanLahan = np.arange(0, 51, 1)
jenisTanah = np.arange(25, 101, 1)
kerawanan = np.arange(0, 51, 1)


print("\n\n-----------------------------------------------------------------------------\n\n")
print("Enter Landslide Parameter Data ... \n\n")

input_curahHujan = float(input("Rainfall: "))
input_ketinggian = float(input("Slope Elevation: "))
input_kemiringan = float(input("Slope: "))
input_jarakJalan = float(input("Distance To Road: "))
input_penggunaanLahan = float(input("Land Use: "))
input_jenisTanah = float(input("Soil Type: "))


print("\n\nThank you. Your data has been entered.")
print("\n\nFuzzy Algorithm Process ... \n\n")

# Fungsi Keanggotaan


curahHujanRendah = mf.trapmf(curahHujan, [-2000, -1500, 1501, 1700])
curahHujanSedang = mf.trapmf(curahHujan, [1501, 1700, 1800, 1900])
curahHujanTinggi = mf.trapmf(curahHujan, [1900, 2100, 2101, 2300])

ketinggianSangatRendah = mf.trapmf(ketinggian, [0,0, 0, 250])
ketinggianRendah = mf.trapmf(ketinggian, [0,0, 250, 500])
ketinggianSedang = mf.trapmf(ketinggian, [0,0, 500, 750])
ketinggianTinggi = mf.trapmf(ketinggian, [0,0, 750, 1000])
ketinggianSangatTinggi = mf.trapmf(ketinggian, [0,0,  1000, 1001])

# kemiringanRendah = mf.trapmf(kemiringan, [0, 8, 13, 15])
# kemiringanSedang = mf.trapmf(kemiringan, [13, 15, 23, 25])
# kemiringanTinggi = mf.trapmf(kemiringan, [23, 25, 30, 40])

kemiringanDatar = mf.trapmf(kemiringan, [0, 0, 0, 8])
kemiringanLandai = mf.trapmf(kemiringan, [0, 0, 8, 15])
kemiringanAgakCuram = mf.trapmf(kemiringan, [0, 0, 15, 25])
kemiringanCuram = mf.trapmf(kemiringan, [0, 0, 25, 40])
kemiringanTerjal = mf.trapmf(kemiringan, [0, 0, 40, 41])

jarakJalanSangatJauh = mf.trimf(jarakJalan, [0, 300, 401])
jarakJalanJauh = mf.trimf(jarakJalan, [0, 300, 400])
jarakJalansedang = mf.trimf(jarakJalan, [0, 200, 300])
jarakJalandekat = mf.trimf(jarakJalan, [0, 100, 200])
jarakJalanSangatdekat = mf.trimf(jarakJalan, [0, 0, 100])

pl_kurangPeka= mf.trimf(penggunaanLahan, [0, 0, 10,])
pl_agakPeka= mf.trimf(penggunaanLahan, [10, 20, 30,])
pl_peka= mf.trimf(penggunaanLahan, [30, 40, 50,])
pl_sangatPeka= mf.trapmf(penggunaanLahan, [50, 51, 52, 53])

jt_tidakPeka= mf.trapmf(jenisTanah, [0, 0, 20, 25])
jt_kurangPeka= mf.trapmf(jenisTanah, [0, 0, 20, 50])
jt_peka= mf.trapmf(jenisTanah, [0, 0, 50, 75])
jt_sangatpeka= mf.trapmf(jenisTanah, [0, 0, 70, 100])


#aman = mf.trapmf(kerawanan, [0 ,0 ,5 ,10])
rendah = mf.trapmf(kerawanan, [0 , 0 ,15 ,20])
sedang = mf.trapmf(kerawanan, [15 ,20 ,25 ,30])
tinggi = mf.trapmf(kerawanan, [25 ,30 ,35 ,40])
sangatTinggi = mf.trapmf(kerawanan, [35, 40, 45, 50])

# Grafik

fig, (ax0, ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(nrows = 7, figsize =(10, 25))

ax0.plot(curahHujan, curahHujanRendah, 'r', linewidth = 2, label = 'Rainfall Low')
ax0.plot(curahHujan, curahHujanSedang, 'g', linewidth = 2, label = 'Rainfall Moderate')
ax0.plot(curahHujan, curahHujanTinggi, 'b', linewidth = 2, label = 'Rainfall High')
ax0.set_title('Rainfall')
ax0.legend()
# ketinggianSangatRendah
ax1.plot(ketinggian, ketinggianSangatRendah, 'c', linewidth = 2, label = 'SlopeElevation very Low')
ax1.plot(ketinggian, ketinggianRendah, 'r', linewidth = 2, label = 'SlopeElevation Low')
ax1.plot(ketinggian, ketinggianSedang, 'g', linewidth = 2, label = 'SlopeElevation Moderate')
ax1.plot(ketinggian, ketinggianTinggi, 'b', linewidth = 2, label = 'SlopeElevation high')
ax1.plot(ketinggian, ketinggianSangatTinggi, 'y', linewidth = 2, label = 'SlopeElevation Very High')
ax1.set_title('SlopeElevation')
ax1.legend()

ax2.plot(kemiringan, kemiringanDatar, 'r', linewidth = 2, label = 'Slope Flat')
ax2.plot(kemiringan, kemiringanLandai, 'g', linewidth = 2, label = 'Slope Smooth')
ax2.plot(kemiringan, kemiringanAgakCuram, 'b', linewidth = 2, label = 'Slope modarate steep')
ax2.plot(kemiringan, kemiringanCuram, 'b', linewidth = 2, label = 'Sloping')
ax2.plot(kemiringan, kemiringanTerjal, 'c', linewidth = 2, label = 'Steep Slope')

# kemiringanDatar = mf.trapmf(kemiringan, [0, 0, 0, 8])
# kemiringanLandai = mf.trapmf(kemiringan, [0, 0, 8, 15])
# kemiringanAgakCuram = mf.trapmf(kemiringan, [0, 0, 15, 25])
# kemiringanCuram = mf.trapmf(kemiringan, [0, 0, 25, 40])
# kemiringanTerjal = mf.trapmf(kemiringan, [0, 0, 40, 41])

ax2.set_title('Slope')
ax2.legend()

ax3.plot(jarakJalan, jarakJalanSangatJauh, 'r', linewidth = 2, label = 'Distance To Road Very Far ')
ax3.plot(jarakJalan, jarakJalanJauh, 'g', linewidth = 2, label = 'Distance To Road Far ')
ax3.plot(jarakJalan, jarakJalansedang, 'b', linewidth = 2, label = 'Distance To Road moderate ')
ax3.plot(jarakJalan, jarakJalandekat, 'y', linewidth = 2, label = 'Distance To Road  Close ')
ax3.plot(jarakJalan, jarakJalanSangatdekat, 'c', linewidth = 2, label = 'Distance To Road Very Close ')
ax3.set_title('Distance To Road')
ax3.legend()

ax4.plot(jenisTanah, jt_tidakPeka, 'r', linewidth = 2, label = 'SoilType Less Sensitive')
ax4.plot(jenisTanah, jt_kurangPeka, 'g', linewidth = 2, label = 'SoilType Moderately Sensitive')
ax4.plot(jenisTanah, jt_peka, 'b', linewidth = 2, label = 'SoilType Sensitive')
ax4.plot(jenisTanah, jt_sangatpeka, 'c', linewidth = 2, label = 'SoilType very Sensitive')

# jt_sangatpeka
ax4.set_title('Soil Type')
ax4.legend()

ax5.plot(penggunaanLahan, pl_kurangPeka, 'r', linewidth = 2, label = 'landUse_Less Sensitive')
ax5.plot(penggunaanLahan, pl_agakPeka, 'g', linewidth = 2, label = 'LandUse Moderately Sensitive')
ax5.plot(penggunaanLahan, pl_peka, 'b', linewidth = 2, label = 'LandUse Sensitive')
ax5.plot(penggunaanLahan, pl_sangatPeka, 'y', linewidth = 2, label = 'LandUse Very Sensitive')
ax5.set_title('LandUse')
ax5.legend()

#ax6.plot(kerawanan, aman, 'r', linewidth = 2, label = 'aman')
ax6.plot(kerawanan, rendah, 'g', linewidth = 2, label = 'Low')
ax6.plot(kerawanan, sedang, 'b', linewidth = 2, label = 'Moderate')
ax6.plot(kerawanan, tinggi, 'y', linewidth = 2, label = 'High')
ax6.plot(kerawanan, sangatTinggi, 'm', linewidth = 2, label = 'Very High')
ax6.set_title('Landslide Susceptibility Level')
ax6.legend()

plt.tight_layout()

# Üyelik dereceleri > BULANDIRMA

curahHujan_fit_rendah = fuzz.interp_membership(curahHujan, curahHujanRendah, input_curahHujan)
curahHujan_fit_sedang = fuzz.interp_membership(curahHujan, curahHujanSedang, input_curahHujan)
curahHujan_fit_tinggi = fuzz.interp_membership(curahHujan, curahHujanTinggi, input_curahHujan)


ketinggian_fit_sangatrendah = fuzz.interp_membership(ketinggian, ketinggianSangatRendah, input_ketinggian)
ketinggian_fit_rendah = fuzz.interp_membership(ketinggian, ketinggianRendah, input_ketinggian)
ketinggian_fit_sedang = fuzz.interp_membership(ketinggian, ketinggianSedang, input_ketinggian)
ketinggian_fit_tinggi = fuzz.interp_membership(ketinggian,ketinggianTinggi , input_ketinggian)
ketinggian_fit_sangattinggi = fuzz.interp_membership(ketinggian, ketinggianSangatTinggi, input_ketinggian)

kemiringan_fit_rendah = fuzz.interp_membership(kemiringan, kemiringanRendah, input_kemiringan)
kemiringan_fit_sedang = fuzz.interp_membership(kemiringan, kemiringanSedang, input_kemiringan)
kemiringan_fit_tinggi = fuzz.interp_membership(kemiringan, kemiringanTinggi, input_kemiringan)

jarakjalan_fit_sangatjauh = fuzz.interp_membership(jarakJalan, jarakJalanSangatJauh, input_jarakJalan)

pl_fit_kurangPeka = fuzz.interp_membership(penggunaanLahan, pl_kurangPeka, input_penggunaanLahan)
pl_fit_agakPeka = fuzz.interp_membership(penggunaanLahan, pl_agakPeka, input_penggunaanLahan)
pl_fit_peka = fuzz.interp_membership(penggunaanLahan,pl_peka , input_penggunaanLahan)
pl_fit_sangatPeka = fuzz.interp_membership(penggunaanLahan, pl_sangatPeka, input_penggunaanLahan)

jt_fit_tidakPeka = fuzz.interp_membership(jenisTanah, jt_tidakPeka, input_jenisTanah)
jt_fit_kurangPeka = fuzz.interp_membership(jenisTanah, jt_kurangPeka, input_jenisTanah)
jt_fit_peka = fuzz.interp_membership(jenisTanah, jt_peka, input_jenisTanah)

# Kurallar

rule1 = np.fmin(np.fmin(np.fmin(np.fmin(ketinggian_fit_rendah ,kemiringan_fit_rendah),pl_fit_kurangPeka), jt_fit_peka), rendah)
rule2 = np.fmin(np.fmin(np.fmin(np.fmin(ketinggian_fit_rendah ,kemiringan_fit_rendah),pl_fit_agakPeka), jt_fit_peka), rendah)
rule3 = np.fmin(np.fmin(np.fmin(np.fmin(ketinggian_fit_rendah ,kemiringan_fit_rendah),pl_fit_peka), jt_fit_peka), sedang)
rule4 = np.fmin(np.fmin(np.fmin(np.fmin(ketinggian_fit_rendah ,kemiringan_fit_rendah),pl_fit_sangatPeka), jt_fit_peka), tinggi)
rule5 = np.fmin(np.fmin(np.fmin(ketinggian_fit_sedang ,kemiringan_fit_rendah), jt_fit_peka), rendah)

rule6 = np.fmin(np.fmin(np.fmin(curahHujan_fit_rendah, ketinggian_fit_sedang), kemiringan_fit_sedang), rendah)
rule7 = np.fmin(np.fmin(np.fmin(curahHujan_fit_sedang, ketinggian_fit_sedang), kemiringan_fit_sedang), rendah)
rule8 = np.fmin(np.fmin(np.fmin(curahHujan_fit_tinggi, ketinggian_fit_sedang), kemiringan_fit_sedang), rendah)
rule9 = np.fmin(np.fmin(np.fmin(curahHujan_fit_rendah, ketinggian_fit_tinggi), kemiringan_fit_tinggi), sedang)
rule10 = np.fmin(np.fmin(np.fmin(curahHujan_fit_sedang, ketinggian_fit_tinggi), kemiringan_fit_tinggi), tinggi)
rule11 = np.fmin(np.fmin(np.fmin(curahHujan_fit_tinggi, ketinggian_fit_tinggi), kemiringan_fit_tinggi), sangatTinggi)
rule12 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(curahHujan_fit_rendah, ketinggian_fit_sedang), kemiringan_fit_rendah), pl_fit_kurangPeka), jt_fit_tidakPeka), rendah)

rule13 = np.fmin(np.fmin(curahHujan_fit_rendah, jarakjalan_fit_sangatjauh), rendah)
rule14 = np.fmin(np.fmin(curahHujan_fit_sedang, jarakjalan_fit_sangatjauh), tinggi)
rule15 = np.fmin(np.fmin(curahHujan_fit_tinggi, jarakjalan_fit_sangatjauh), sangatTinggi)

rule16 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(curahHujan_fit_rendah, ketinggian_fit_rendah), kemiringan_fit_rendah), jarakjalan_fit_sangatjauh), pl_fit_kurangPeka), jt_fit_peka), rendah)
rule17 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(curahHujan_fit_sedang, ketinggian_fit_rendah), kemiringan_fit_rendah), jarakjalan_fit_sangatjauh), pl_fit_kurangPeka), jt_fit_peka), tinggi)
rule18 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(curahHujan_fit_tinggi, ketinggian_fit_rendah), kemiringan_fit_rendah), jarakjalan_fit_sangatjauh), pl_fit_kurangPeka), jt_fit_peka), sangatTinggi)
rule19 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(curahHujan_fit_sedang, ketinggian_fit_rendah), kemiringan_fit_rendah), jarakjalan_fit_sangatjauh), pl_fit_sangatPeka), jt_fit_peka), sangatTinggi)

rule20 = np.fmin(np.fmin(np.fmin(np.fmin(ketinggian_fit_sangattinggi, kemiringan_fit_tinggi), pl_fit_sangatPeka), jt_fit_peka), sangatTinggi)
rule21 = np.fmin(np.fmin(np.fmin(np.fmin(ketinggian_fit_tinggi, kemiringan_fit_tinggi), pl_fit_peka), jt_fit_kurangPeka), sangatTinggi)
rule22 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(curahHujan_fit_rendah, ketinggian_fit_sangattinggi), kemiringan_fit_tinggi), pl_fit_sangatPeka), jt_fit_kurangPeka), sedang)
rule23 = np.fmin(np.fmin(curahHujan_fit_sedang, ketinggian_fit_sangattinggi), sangatTinggi)
rule24 = np.fmin(np.fmin(curahHujan_fit_tinggi, ketinggian_fit_sangattinggi), sangatTinggi)


# Birleşim kümeleri > ÇIKARTIM (Mamdani)

out_rendah1 = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(rule1,rule5),rule6),rule7),rule8),rule12)
out_rendah = np.fmax(np.fmax(rule2,rule13),rule16)
out_sedang = np.fmax(np.fmax(rule3, rule9),rule22)
out_tinggi = np.fmax(np.fmax(np.fmax(rule4, rule10),rule14),rule17)
out_sangatTinggi = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(rule11,rule15),rule18),rule19),rule20),rule21),rule23),rule24)


# Grafik

risk0 = np.zeros_like(kerawanan)

fig, ax0 = plt.subplots(figsize = (7, 4))
ax0.fill_between(kerawanan, risk0, out_rendah1, facecolor = 'r', alpha = 0.7)
ax0.plot(kerawanan, out_rendah1, 'r', linestyle = '--')
ax0.fill_between(kerawanan, risk0, out_rendah, facecolor = 'g', alpha = 0.7)
ax0.plot(kerawanan, rendah, 'g', linestyle = '--')
ax0.fill_between(kerawanan, risk0, out_sedang, facecolor = 'b', alpha = 0.7)
ax0.plot(kerawanan, sedang, 'b', linestyle = '--')
ax0.fill_between(kerawanan, risk0, out_tinggi, facecolor = 'y', alpha = 0.7)
ax0.plot(kerawanan, tinggi, 'y', linestyle = '--')
ax0.fill_between(kerawanan, risk0, out_sangatTinggi, facecolor = 'm', alpha = 0.7)
ax0.plot(kerawanan, sangatTinggi, 'm', linestyle = '--')
ax0.set_title('Landslide Susceptibility Level')

plt.tight_layout()

# DURULAMA - CoA

out_kerawanan = np.fmax(np.fmax(np.fmax(np.fmax(out_rendah1, out_rendah), out_sedang), out_tinggi), out_sangatTinggi)

defuzzified  = fuzz.defuzz(kerawanan, out_kerawanan, 'centroid')

result = fuzz.interp_membership(kerawanan, out_kerawanan, defuzzified)

print("Diagnosis of Landslide Susceptibility level:", defuzzified)

# Contoh nilai suhu
nilai = defuzzified

# Logika if untuk rentang nilai
if nilai >= 75 and nilai <= 100:
    print("Sangat Tinggi")
elif nilai >= 50 and nilai < 75:
    print("Tinggi")
elif nilai >= 25 and nilai < 50:
    print("Sedang")
elif nilai >= 0 and nilai < 25:
    print("Rendah")
else:
    print("Aman")



# Grafik

fig, ax0 = plt.subplots(figsize=(7, 4))

#ax0.plot(kerawanan, aman, 'r', linewidth = 0.5, linestyle = '--')
ax0.plot(kerawanan, rendah, 'g', linewidth = 0.5, linestyle = '--')
ax0.plot(kerawanan, sedang, 'b', linewidth = 0.5, linestyle = '--')
ax0.plot(kerawanan, tinggi, 'y', linewidth = 0.5, linestyle = '--')
ax0.plot(kerawanan, sangatTinggi, 'm', linewidth = 0.5, linestyle = '--')

ax0.fill_between(kerawanan, risk0, out_kerawanan, facecolor = 'Orange', alpha = 0.7)
ax0.plot([defuzzified , defuzzified], [0, result], 'k', linewidth = 1.5, alpha = 0.9)
ax0.set_title('Defuzzyfikasi')

plt.tight_layout()