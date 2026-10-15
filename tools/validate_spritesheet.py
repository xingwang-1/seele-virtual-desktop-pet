from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
IMAGE = ROOT / "assets" / "seele-pet-spritesheet-v1.png"
EXPECTED_SIZE = (1536, 1872)
CELL = (192, 208)
FRAMES = (6, 8, 8, 4, 5, 8, 6, 6, 6)

def main():
    image = Image.open(IMAGE).convert("RGBA")
    if image.size != EXPECTED_SIZE:
        raise SystemExit(f"INVALID: size {image.size}, expected {EXPECTED_SIZE}")
    alpha = image.getchannel("A")
    for row, count in enumerate(FRAMES):
        for col in range(8):
            crop = alpha.crop((col*CELL[0], row*CELL[1], (col+1)*CELL[0], (row+1)*CELL[1]))
            if col < count and crop.getbbox() is None:
                raise SystemExit(f"INVALID: missing artwork at row {row+1}, frame {col+1}")
            if col >= count and crop.getbbox() is not None:
                raise SystemExit(f"INVALID: unexpected artwork at unused cell row {row+1}, column {col+1}")
    print(f"VALID: {IMAGE.name}, {image.width}x{image.height}, RGBA")

if __name__ == "__main__":
    main()
