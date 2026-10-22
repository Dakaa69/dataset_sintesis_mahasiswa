from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT/'data'/'dataset_sintesis_mahasiswa_1000.csv'
OUT = ROOT/'output'
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)

# Statistik deskriptif
summary = df[['Semester','IPK','Usia']].describe().T
summary.to_csv(OUT/'statistik_deskriptif.csv', encoding='utf-8-sig')

# Ringkasan jurusan
major = df.groupby('Jurusan').agg(
    mahasiswa=('ID_Mahasiswa','count'),
    semester_rata2=('Semester','mean'),
    ipk_rata2=('IPK','mean'),
    usia_rata2=('Usia','mean'),
).reset_index()
major.to_csv(OUT/'ringkasan_jurusan.csv', index=False, encoding='utf-8-sig')

# Ringkasan semester
semester = df.groupby('Semester').agg(
    mahasiswa=('ID_Mahasiswa','count'),
    ipk_rata2=('IPK','mean'),
    usia_rata2=('Usia','mean'),
).reset_index()
semester.to_csv(OUT/'ringkasan_semester.csv', index=False, encoding='utf-8-sig')

# Korelasi
corr = df[['Semester','IPK','Usia']].corr()
corr.to_csv(OUT/'korelasi.csv', encoding='utf-8-sig')

# Distribusi silang
pd.crosstab(df['Semester'], df['Jurusan']).to_csv(OUT/'distribusi_jurusan_semester.csv', encoding='utf-8-sig')

# Visualisasi
plt.figure(figsize=(9,5))
plt.bar(major['Jurusan'], major['mahasiswa'])
plt.title('Jumlah Mahasiswa menurut Jurusan')
plt.xlabel('Jurusan'); plt.ylabel('Jumlah Mahasiswa')
plt.tight_layout(); plt.savefig(OUT/'01_jumlah_mahasiswa_jurusan.png', dpi=160); plt.close()

plt.figure(figsize=(9,5))
plt.bar(semester['Semester'].astype(str), semester['mahasiswa'])
plt.title('Distribusi Mahasiswa menurut Semester')
plt.xlabel('Semester'); plt.ylabel('Jumlah Mahasiswa')
plt.tight_layout(); plt.savefig(OUT/'02_distribusi_semester.png', dpi=160); plt.close()

plt.figure(figsize=(9,5))
plt.hist(df['IPK'], bins=24)
plt.title('Distribusi IPK'); plt.xlabel('IPK'); plt.ylabel('Frekuensi')
plt.tight_layout(); plt.savefig(OUT/'03_distribusi_ipk.png', dpi=160); plt.close()

plt.figure(figsize=(9,5))
plt.hist(df['Usia'], bins=range(int(df['Usia'].min()), int(df['Usia'].max())+2))
plt.title('Distribusi Usia'); plt.xlabel('Usia'); plt.ylabel('Frekuensi')
plt.tight_layout(); plt.savefig(OUT/'04_distribusi_usia.png', dpi=160); plt.close()

plt.figure(figsize=(9,5))
for major_name, g in df.groupby('Jurusan'):
    plt.scatter(g['Semester'], g['IPK'], alpha=0.35, s=16, label=major_name)
plt.title('Semester vs IPK'); plt.xlabel('Semester'); plt.ylabel('IPK'); plt.legend()
plt.tight_layout(); plt.savefig(OUT/'05_semester_vs_ipk.png', dpi=160); plt.close()

plt.figure(figsize=(9,5))
for major_name, g in df.groupby('Jurusan'):
    plt.scatter(g['Usia'], g['IPK'], alpha=0.35, s=16, label=major_name)
plt.title('Usia vs IPK'); plt.xlabel('Usia'); plt.ylabel('IPK'); plt.legend()
plt.tight_layout(); plt.savefig(OUT/'06_usia_vs_ipk.png', dpi=160); plt.close()

print('Analisis selesai.')
