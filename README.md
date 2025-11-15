# Onlayn Do‘kon – Polimorfizm Misoli (Python)

## Tavsif
Ushbu loyiha onlayn do‘kondagi mahsulotlarni OOP orqali modellashtiradi. Quyidagi sinflar mavjud:

- **Mahsulot** (bazaviy sinf)
- **Elektronika**
- **Kiyim**
- **Kitob**

Har bir sinf quyidagi metodlarga ega:

- `yetkazib_berish_narxi(shahar)` – shahar bo‘yicha yetkazib berish narxini qaytaradi  
- `chegirma_qollash(foydalanuvchi)` – foydalanuvchi turiga ko‘ra chegirma hisoblash  
- `kafolat_muddati()` – faqat Elektronika sinfida qiymat qaytaradi, boshqalari `None`

---

## Funksionallik

- Mahsulotlar savatga joylanadi.
- Polimorfizm orqali ro‘yxatdagi barcha mahsulotlar uchun:
  - umumiy yetkazib berish narxi  
  - chegirma qo‘llangan nomaosh  
  hisoblanadi.
- Elektronika sinfi kafolat muddatiga ega, boshqalar `None`.

---

## Ishga tushirish

```bash
python main.py
