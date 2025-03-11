# Telomere Circular Permutations Tool

## 📌 Overview
This tool generates **circular permutations** of a given DNA or RNA sequence, identifies its **complementary strand**, and performs circular permutations on it. If an **ancestral/known repeat** sequence is provided, it highlights the occurrences in red.

## 📥 Download & Install
To download the latest release, run:
```bash
wget https://github.com/GihanKau/telomere_circular_permutations/releases/download/v1.0/telomere_circular_permutations
```

Make it executable:
```bash
chmod +x telomere_circular_permutations
```

## 🛠 Run the Tool
Execute the program by running:
```bash
./telomere_circular_permutations
```

### 📌 Input:
1. **Ancestral/Known Repeat** (e.g., `ACCTA`)
2. **DNA or RNA Sequence** (e.g., `TTAGG`)

### 📤 Expected Output:
```
Enter the Ancestral/Known repeat: ACCTA
Enter the DNA or RNA sequence: TTAGG

Ancestral/Known repeat: ACCTA

Input sequence (positive strand) in 5' to 3' direction: TTAGG
Circular permutations of the positive strand:
TTAGG
TAGGT
AGGTT
GGTTA
GTTA

Complementary sequence (negative strand) in 5' to 3' direction: CCTAA

Circular permutations of the negative strand:
CCTAA
CTAAC
TAACC
AACCT
ACCTA  <-- Highlighted in Red
```

## 📝 Features
✅ Validates DNA/RNA sequences  
✅ Generates circular permutations  
✅ Computes complementary sequences  
✅ Highlights known repeats in **red**  
✅ Works in Linux environments  

## ⚠️ Notes
- Ensure your Linux system supports **64-bit x86_64 architecture**.
- If running on Mac, you must recompile it using **PyInstaller** for Mac architectures.

## 📜 License
This project is open-source and available under the **MIT License**.

## 🤝 Contributing
Feel free to submit **issues** or **pull requests** in the [GitHub repository](https://github.com/GihanKau/telomere_circular_permutations).

---
🚀 *Developed by GihanKau*

