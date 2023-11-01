def fungsi_contoh(x):
    return (x*x*x*x)-(x*x*x)+(2*x*x)-(2*x)-12# Misalnya, kita cari akar dari x^2 - 10

def metode_biseksi(func, a, b, tol=0.0001, max_iter=16):
    """
    Metode biseksi untuk menemukan akar fungsi dalam interval [a, b].

    :param func: Fungsi target.
    :param a: Ujung kiri interval.
    :param b: Ujung kanan interval.
    :param tol: Toleransi (berhenti ketika ukuran interval lebih kecil dari tol).
    :param max_iter: Jumlah maksimum iterasi.
    :return: Aproksimasi akar.
    """
    if func(a) * func(b) > 0:
        raise ValueError("Nilai fungsi pada ujung interval harus memiliki tanda yang berbeda.")

    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(func(c)) < tol:
            return c

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

    raise RuntimeError("Metode biseksi tidak konvergen dalam jumlah iterasi maksimum.")

a, b = -2.0, 0.0
akar_approx = metode_biseksi(fungsi_contoh, a, b, tol=0.0001)
print("Aproksimasi akar:", akar_approx)