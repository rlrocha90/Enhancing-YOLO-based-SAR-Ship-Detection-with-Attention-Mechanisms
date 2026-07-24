import os
from collections import Counter
from PIL import Image

# Caminhos
labels_root = "datasets/MSAR/"
label_folders = ["train/labels", "test/labels", "valid/labels"]
image_folders = ["train/images", "test/images", "valid/images"]

# Função para classificar com normalização proporcional
def classify_bbox(w, h, img_w, img_h):
    max_dim = max(w, h)
    
    # fator proporcional em relação à dimensão de referência COCO (640)
    scale = (img_w + img_h) / 2 / 640  # média das dimensões
    
    small_thr = 32 * scale
    medium_thr = 96 * scale
    
    if max_dim < small_thr:
        return "small"
    elif max_dim <= medium_thr:
        return "medium"
    else:
        return "large"

# Contador
counts = Counter()
total = 0

# Percorre todas as pastas
for lbl_folder, img_folder in zip(label_folders, image_folders):
    labels_path = os.path.join(labels_root, lbl_folder)
    images_path = os.path.join(labels_root, img_folder)

    for fname in os.listdir(labels_path):
        if fname.endswith(".txt"):
            label_file = os.path.join(labels_path, fname)
            image_file = os.path.join(images_path, os.path.splitext(fname)[0] + ".jpg")

            if not os.path.exists(image_file):
                continue

            with Image.open(image_file) as img:
                img_w, img_h = img.size

            with open(label_file, "r") as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) < 5:
                        continue
                    _, x, y, w, h = parts
                    w = float(w) * img_w
                    h = float(h) * img_h

                    categoria = classify_bbox(w, h, img_w, img_h)
                    counts[categoria] += 1
                    total += 1

# Resultado
if total > 0:
    print("Distribuição de bounding boxes (normalizada pelo tamanho da imagem):")
    for categoria in ["small", "medium", "large"]:
        pct = (counts[categoria] / total) * 100
        print(f"{categoria}: {pct:.2f}% ({counts[categoria]} bboxes)")
else:
    print("Nenhum bounding box encontrado.")

