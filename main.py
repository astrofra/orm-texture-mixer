from PIL import Image
import os

def combine_to_orm(ambient_occlusion_path, roughness_path, metalness_path=None, output_name="orm_combined.png"):
    ao_img = Image.open(ambient_occlusion_path).convert("L")
    roughness_img = Image.open(roughness_path).convert("L")

    if metalness_path:
        metalness_img = Image.open(metalness_path).convert("L")
    else:
        metalness_img = Image.new("L", ao_img.size, color=int(5/255 * 255))

    assert ao_img.size == roughness_img.size == metalness_img.size, "All images must have the same dimensions."

    orm_img = Image.new("RGB", ao_img.size)

    for y in range(orm_img.height):
        for x in range(orm_img.width):
            r = ao_img.getpixel((x, y))
            g = roughness_img.getpixel((x, y))
            b = metalness_img.getpixel((x, y))
            orm_img.putpixel((x, y), (r, g, b))

    orm_img.save(output_name)

def process_directory(input_dir="in", output_dir="out"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List files in the input directory
    files = os.listdir(input_dir)
    base_names = set()

    for file in files:
        base_name = file.split('_AmbientOcclusion.png')[0]
        if base_name and base_name not in base_names:
            base_names.add(base_name)

    for base_name in base_names:
        ambient_occlusion_path = os.path.join(input_dir, base_name + "_AmbientOcclusion.png")
        roughness_path = os.path.join(input_dir, base_name + "_Roughness.png")
        metalness_path = os.path.join(input_dir, base_name + "_Metalness.png")

        if os.path.exists(ambient_occlusion_path) and os.path.exists(roughness_path):
            if not os.path.exists(metalness_path):
                metalness_path = None

            output_name = os.path.join(output_dir, base_name + "_ORM.png")
            combine_to_orm(ambient_occlusion_path, roughness_path, metalness_path, output_name)

if __name__ == "__main__":
    process_directory()
