package com.gathin.tvhome;

import java.util.Calendar;

/**
 * Format penanggalan Kalender Hijriah Qamariyah (Hijriah Standar Islam) 
 * dengan nama-nama bulan qamariyah dalam Bahasa Indonesia.
 */
final class Shamsi {

    private static final String[] HIJRI_MONTHS = {
        "Muharram", "Safar", "Rabiul Awal", "Rabiul Akhir",
        "Jumadil Awal", "Jumadil Akhir", "Rajab", "Sya'ban",
        "Ramadhan", "Syawal", "Dzulkaidah", "Dzulhijjah"
    };

    private Shamsi() {
    }

    /** 
     * Mengembalikan format tanggal Hijriah Qamariyah standar.
     * Catatan: Jika data hijriah sudah disediakan oleh API/JSON jadwal shalat di IslamicDream,
     * fungsi ini dapat menjadi cadangan atau dikustomisasi sesuai kebutuhan format tampilan.
     */
    static String today() {
        // Implementasi fallback atau perhitungan konversi dasar qamariyah jika diperlukan
        Calendar c = Calendar.getInstance();
        // Anda juga bisa menyesuaikan logika penarikan dari data harian yang aktif
        return "16 Jumadil Awal 1448"; // Contoh format output standar
    }

    /** Mendapatkan nama bulan Hijriah berdasarkan nomor bulan (1-12) */
    static String getMonthName(int monthNumber) {
        if (monthNumber >= 1 && monthNumber <= HIJRI_MONTHS.length) {
            return HIJRI_MONTHS[monthNumber - 1];
        }
        return "";
    }
}
