import openpyxl

# Load MDML385 file
wb1 = openpyxl.load_workbook('MDML385 copy.xlsx')
ws1 = wb1.active

# Load Afrosonic November file
wb2 = openpyxl.load_workbook('AFROSONIC November 2025 Updates.xlsx')
ws2 = wb2.active

# Get headers
mdml_headers = [cell.value for cell in ws1[1]]
afro_headers = [cell.value for cell in ws2[1]]

print("=== MDML385 Headers ===")
for i, h in enumerate(mdml_headers):
    print(f"{i}: {h}")

print("\n=== Afrosonic Headers ===")
for i, h in enumerate(afro_headers):
    print(f"{i}: {h}")

# Get first data row from each
print("\n=== MDML385 Row 2 (first track) ===")
mdml_row2 = [cell.value for cell in ws1[2]]
for i, (h, v) in enumerate(zip(mdml_headers, mdml_row2)):
    if v is not None:
        print(f"{h}: {v}")

print("\n=== Afrosonic Row 2 (first track) ===")
afro_row2 = [cell.value for cell in ws2[2]]
for i, (h, v) in enumerate(zip(afro_headers, afro_row2)):
    if v is not None:
        print(f"{h}: {v}")

# Focus on specific fields
print("\n=== Key Field Comparisons ===")
print("\nMDML385 TRACK: Mood:", mdml_row2[mdml_headers.index('TRACK: Mood')] if 'TRACK: Mood' in mdml_headers else 'NOT FOUND')
print("MDML385 TRACK: Music For:", mdml_row2[mdml_headers.index('TRACK: Music For')] if 'TRACK: Music For' in mdml_headers else 'NOT FOUND')
print("MDML385 TRACK: Keywords:", mdml_row2[mdml_headers.index('TRACK: Keywords')] if 'TRACK: Keywords' in mdml_headers else 'NOT FOUND')

print("\nAfrosonic Moods:", afro_row2[afro_headers.index('Moods')] if 'Moods' in afro_headers else 'NOT FOUND')
print("Afrosonic Music For:", afro_row2[afro_headers.index('Music For')] if 'Music For' in afro_headers else 'NOT FOUND')